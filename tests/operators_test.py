import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest 
from operators import add, subtract, multiply, divide

"""
    Fichier de tests pour operators.py 
    Ces tests verifient la validite des fonctions mathematiques : 
    * Addition : add(a, b)
    * Soustraction : substract(a, b)
    * Multiplication : multiply(a, b)
    * Divison entiere : divide(a, b)
    Chacune des fonctions est testee sur plusieurs cas.
"""


def test_add():
    """
    Verifie que la fonction add() additionne correctement deux nombres. 
    Teste plusieurs cas simples incluant des zeros et des entiers positifs.
    """
    assert add(1, 0) == 1
    assert add(0, 0) == 0
    assert add(2, 3) == 5 

def test_subtract(): 
    """
    Verifie que la fonction subtract() soustrait correctement le second operande du premier. 
    Teste des cas positifs, negatifs et nuls. 
    """
    assert subtract(5, 4) == 1
    assert subtract(4, 5) == -1
    assert subtract(0, 0) == 0 

def test_multiply(): 
    """
    Verifie que la fonction multiply() multiplie correctement deux nombres. 
    Teste des cas incluant des zeros, des nombres positifs et des produits simples. 
    """
    assert multiply(1, 7) == 7
    assert multiply(5, 0) == 0 
    assert multiply(2, 3) == 6 

def test_divide(): 
    """
    Verifie que la fonction divide() effectue une division entiere correcte. 
    Teste des cas avec un quotient exact ou coupe. 
    Teste aussi la levee d'une exception lors de la division par zero. 
    """
    assert divide(10, 2) == 5 
    assert divide(9, 2) == 4 
    with pytest.raises(ZeroDivisionError): 
        divide(5, 0)
        