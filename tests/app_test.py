import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import re
import pytest

import re

from app import calculate, app

"""
    Fichier de tests pour app.py  
    - Les tests unitaires de la fonction calculate() verifient le bon traitement 
    des expressions mathematiques simples ainsi que la gestion des erreurs de format. 
    - Les tests d'integration valident le fonctionnement global de l'application : 
    * Chargement de la page d'acceuil avce une requete GET 
    * Traitement des formulaires POST 
    * Presence correcte des elements HTML. 
"""


def test_calculate_addition(): 
    """
    Verifie que calculate() gere correctement les expressions d'addition,
    avec ou sans espaces autour des operateurs. 
    """
    assert calculate("1+0") == 1
    assert calculate("0 + 0") == 0 
    assert calculate(" 2 + 3 ") == 5 

def test_calculate_substraction(): 
    """
    Verifie que calculate() gere correctement les soustractions simples, 
    incluant les resultats negatifs et les zeros. 
    """
    assert calculate("5 -4") == 1 
    assert calculate(" 4-5 ") == -1 
    assert calculate("0- 0") == 0 

def test_calculate_multiplication(): 
    """
    Verifie que calculate() gere les multiplications, 
    incluant les cas de produit nul et les valeurs entiere simples. 
    """
    assert calculate("1*7") == 7
    assert calculate(" 5 * 0") == 0
    assert calculate("2 * 3") == 6

def test_calculate_division(): 
    """
    Verifie que calculate() effectue une division entiere correcte
    et que le resultat est arrondi vers le bas. 
    """
    assert calculate("10 / 2") == 5
    assert calculate("9/2") == 4.5

def test_calculate_invalid_expression(): 
    """
    Verifie que calculate leve une ValueError pour des expressions invalides : 
    - chaine vide. 
    - operateurs consecutifs. 
    - operateurs manquants ou expressions incompletes. 
    """
    with pytest.raises(ValueError): 
        assert calculate("")
    with pytest.raises(ValueError): 
        assert calculate("1++1")
    with pytest.raises(ValueError): 
        assert calculate("-1")
    with pytest.raises(ValueError): 
        assert calculate("1-")
    with pytest.raises(ValueError): 
        assert calculate("2+3-5")

@pytest.fixture 

def client(): 
    """
    Initialise un client de test Flask pour simuler des requetes HTTP,
    sans lancer le serveur reel.
    """
    app.config["TESTING"] = True 
    with app.test_client() as client: 
        yield client 

def test_index_get(client): 
    """
    Verifie que la page d'acceuil est accessible via GET 
    et contient une structure HTML valide. 
    """
    response = client.get('/') 
    assert response.status_code == 200 
    assert b"<html" in response.data 

def test_index_post_valid(client): 
    """
    Verifie qu'une requete POST valide retourne
    une reponse contenant le bon resulat.
    """
    response = client.post('/', data={'display': '2+3'})
    assert response.status_code == 200 
    assert b"5" in response.data 

def test_index_post_invalid(client): 
    """
    Verifie qu'une requete POST invalide affiche 
    un message d'erreur dans la page HTML.
    """
    response = client.post('/', data={'display': '2++3'})
    assert b"Error:" in response.data 

def test_html_buttons_numbers(client): 
    """
    Verifie que les boutons des chiffres 1 a 9 sont bien presents dans le code HTML. 
    """
    response = client.get('/')
    html = response.data.decode('utf-8')

    assert '>1<' in html 
    assert '>2<' in html 
    assert '>3<' in html 
    assert '>4<' in html 
    assert '>5<' in html 
    assert '>6<' in html 
    assert '>7<' in html 
    assert '>8<' in html 
    assert '>9<' in html 

def test_html_button_addition(client): 
    """
    Verifie la presence du bouton d'addition ('+') dans le HTML. 
    Peut detecter les balises avec ou sans attributs.
    """
    response = client.get('/')
    html = response.data.decode('utf-8')

    assert re.search(r'<button[^>]*>+</button>', html) or re.search(r'value="+"', html), \
        "Division button not found in HTML"
    
def test_html_button_subtraction(client): 
    """
    Verifie la presence du bouton de soustraction ('-') dans le HTML. 
    Peut detecter les balises avec ou sans attributs.
    """
    response = client.get('/')
    html = response.data.decode('utf-8')

    assert re.search(r'<button[^>]*>-</button>', html) or re.search(r'value="-"', html), \
        "Division button not found in HTML"

def test_html_button_product(client): 
    """
    Verifie la presence du bouton multiplication ('*') dans le HTML. 
    Peut detecter les balises avec ou sans attributs.
    """
    response = client.get('/')
    html = response.data.decode('utf-8')

    assert re.search(r'<button[^>]*>\s*\*\s*</button>', html) or re.search(r'value="\*"', html), \
        "Multiplication button not found in HTML"
    

def test_html_button_division(client): 
    """
    Verifie la presence du bouton de division ('/') dans le HTML. 
    Peut detecter les balises avec ou sans attributs.
    """
    response = client.get('/')
    html = response.data.decode('utf-8')

    assert re.search(r'<button[^>]*>/</button>', html) or re.search(r'value="/"', html), \
        "Division button not found in HTML"