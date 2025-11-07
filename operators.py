"""
Module operators.py
Contient les fonctions d'opérations arithmétiques pour la calculatrice.
"""


def add(a, b):
    """
    Additionne deux nombres.
    
    Args:
        a (float): Le premier nombre à additionner
        b (float): Le deuxième nombre à additionner
    
    Returns:
        float: La somme de a et b
    """
    return a + b

def subtract(a, b):
    """
    Soustrait le premier nombre du second.
    
    Args:
        a (float): Le nombre à soustraire (second opérande dans la soustraction)
        b (float): Le nombre de base (premier opérande dans la soustraction)
    
    Returns:
        float: Le résultat de a - b
    """

    #TODO: Corriger la fonction pour que le résultat soit a - b
    
    return a - b


def multiply(a, b):
    """
    Élève le premier nombre à la puissance du second.
    
    Args:
        a (float): La base de l'exponentiation
        b (float): L'exposant
    
    Returns:
        float: Le résultat de a élevé à la puissance b
    """
    #TODO: Corriger la fonction pour que le résultat soit a * b (en ce moment, il calcule a^b)
    return a * b


def divide(a, b):
    """
    Effectue une division entière entre deux nombres.
    
    Note: Cette fonction effectue une division entière (//) et non une division décimale (/).
    Le résultat est arrondi vers le bas au nombre entier le plus proche.
    
    Args:
        a (float): Le dividende (nombre à diviser)
        b (float): Le diviseur (nombre par lequel diviser)
    
    Returns:
        float: Le quotient entier de a divisé par b
    
    Raises:
        ZeroDivisionError: Si b est égal à zéro
    """

    return a // b
