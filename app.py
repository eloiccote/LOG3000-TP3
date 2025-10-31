"""
Module app.py
Application Flask pour une calculatrice web permettant d'effectuer des opérations arithmétiques simples.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Dictionnaire associant chaque symbole d'opérateur à sa fonction correspondante
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Évalue une expression arithmétique simple avec un seul opérateur.
    
    Args:
        expr (str): L'expression à calculer (format: "nombre opérateur nombre")
    
    Returns:
        float: Le résultat du calcul
    
    Raises:
        ValueError: Si l'expression est vide, invalide ou contient plusieurs opérateurs
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Retirer les espaces pour faciliter le parsing
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Parcourir l'expression pour trouver l'opérateur
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Valider la position de l'opérateur (ne doit pas être au début ou à la fin)
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")

    # Extraire les opérandes de part et d'autre de l'opérateur
    left = s[:op_pos]
    right = s[op_pos+1:]

    # Convertir les opérandes en nombres
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    # Appeler la fonction d'opération appropriée
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de l'application. Gère l'affichage et le traitement des calculs.
    
    Returns:
        str: Le template HTML rendu avec le résultat du calcul
    """
    result = ""
    
    # Traiter le calcul uniquement si une expression est soumise via POST
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            # Afficher l'erreur à l'utilisateur de manière lisible
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Lancer le serveur Flask en mode debug pour faciliter le développement
    app.run(debug=True)