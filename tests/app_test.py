import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
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
    assert calculate("1+0") == 1
    assert calculate("0 + 0") == 0 
    assert calculate(" 2 + 3 ") == 5 

def test_calculate_substraction(): 
    assert calculate("5 -4") == 1 
    assert calculate(" 4-5 ") == -1 
    assert calculate("0- 0") == 0 

def test_calculate_multiplication(): 
    assert calculate("1*7") == 7
    assert calculate(" 5 * 0") == 0
    assert calculate("2 * 3") == 6

def test_calculate_division(): 
    assert calculate("10 / 2") == 5
    assert calculate("9/2") == 4 

def test_calculate_invalid_expression(): 
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
    app.config["TESTING"] = True 
    with app.test_client() as client: 
        yield client 

def test_index_get(client): 
    response = client.get('/') 
    assert response.status_code == 200 
    assert b"<html" in response.data 

def test_index_post_valid(client): 
    response = client.post('/', data={'display': '2+3'})
    assert response.status_code == 200 
    assert b"5" in response.data 

def test_index_post_invalid(client): 
    response = client.post('/', data={'display': '2++3'})
    assert b"Error:" in response.data 

def test_html_button_two(client): 
    response = client.get('/')
    html = response.data.decode('utf-8')

    assert '>1<' in html 
    assert '>2<' in html 

def test_html_button_eight(client): 
    response = client.get('/')
    html = response.data.decode('utf-8')

    assert '>1<' in html 
    assert '>8<' in html 

def test_html_button_product(client): 
    response = client.get('/')
    html = response.data.decode('utf-8')

    assert '>' not in html.split('*')[0]

def test_html_button_division(client):
    response = client.get('/')
    html = response.data.decode('utf-8')

    assert re.search(r'<button[^>]*>/</button>', html) or re.search(r'value="/"', html), \
        "Division button not found in HTML"