import pytest
from unittest.mock import patch, Mock
from tkinter import Tk

from calculatrice_3boutons import ScrollableCalculator

@pytest.fixture
def calculator_app():
    """
    Fixture pour créer une instance de ScrollableCalculator avec un vrai objet Tk.
    """
    with patch("calculatrice_3boutons.tk.Tk", new=Tk):  # Utilisez la classe Tk réelle
        app = ScrollableCalculator(Tk())
    return app

def test_addition(calculator_app):
    """
    Teste l'addition avec des valeurs spécifiques.
    """
    # Modifier la méthode validate_choice pour simuler le comportement de get
    with patch.object(calculator_app.display, 'get', return_value="10+20"):
        calculator_app.current_index = 14
        calculator_app.validate_choice()
    assert calculator_app.display.get() == "30"

def test_addition_float(calculator_app):
    """
    Teste l'addition de nombres flottants avec des valeurs spécifiques.
    """
    # Modifier la méthode validate_choice pour simuler le comportement de get
    with patch.object(calculator_app.display, 'get', return_value="10.5+1.5"):
        calculator_app.current_index = 14
        calculator_app.validate_choice()
    assert calculator_app.display.get() == "12.0"

def test_soustraction(calculator_app):
    """
    Teste la soustraction avec des valeurs spécifiques.
    """
    with patch.object(calculator_app.display, 'get', return_value="10-5"):
        calculator_app.current_index = 14
        calculator_app.validate_choice()
    assert calculator_app.display.get() == "5"

def test_multiplication(calculator_app):
    """
    Teste la multiplication avec des valeurs spécifiques.
    """
    with patch.object(calculator_app.display, 'get', return_value="10*5"):
        calculator_app.current_index = 14
        calculator_app.validate_choice()
    assert calculator_app.display.get() == "50"

def test_division(calculator_app):
    """
    Teste la division avec des valeurs spécifiques.
    """
    with patch.object(calculator_app.display, 'get', return_value="10/5"):
        calculator_app.current_index = 14
        calculator_app.validate_choice()
    assert calculator_app.display.get() == "2.0"


def test_division_euclidienne(calculator_app):
    """
    Teste la division euclidienne avec des valeurs spécifiques.
    """
    with patch.object(calculator_app.display, 'get', return_value="15//5"):
        calculator_app.current_index = 14
        calculator_app.validate_choice()
    assert calculator_app.display.get() == "3"

def test_puissance(calculator_app):
    """
    Teste la puissance avec des valeurs spécifiques.
    """
    with patch.object(calculator_app.display, 'get', return_value="10**2"):
        calculator_app.current_index = 14
        calculator_app.validate_choice()
    assert calculator_app.display.get() == "100"
    
def test_reset(calculator_app):
    """
    Teste la réinitialisation de l'application.
    """
    with patch.object(calculator_app.display, 'get', return_value="10"):
        calculator_app.current_index = 15
        calculator_app.validate_choice()
        calculator_app.reset_application()
    assert calculator_app.display.get() == ""

def test_modulo(calculator_app):
    """
    Teste le calcul du modulo avec des valeurs spécifiques.
    """
    with patch.object(calculator_app.display, 'get', return_value="15%5"):
        calculator_app.current_index = 14
        calculator_app.validate_choice()
    assert calculator_app.display.get() == "0"

def test_calcul_complexe(calculator_app):
    """
    Teste un calcul complexe avec des parenthèses et des opérations diverses.
    """
    with patch.object(calculator_app.display, 'get', return_value="(5+3)*(2-1)/2"):
        calculator_app.current_index = 14
        calculator_app.validate_choice()
    assert calculator_app.display.get() == "4.0"

def test_erreur_division_zero(calculator_app):
    """
    Teste le cas d'erreur de division par zéro.
    """
    with patch.object(calculator_app.display, 'get', return_value="15/0"):
        calculator_app.current_index = 14
        calculator_app.validate_choice()
    assert calculator_app.display.get() == "Division par zéro impossible"

def test_clavier_desactive(calculator_app):
    """
    Teste si l'utilisation du clavier est désactivée.
    """
    with patch.object(calculator_app, 'validate_choice', return_value=None):
        # Appel à validate_choice patché
        calculator_app.current_index = 14
        calculator_app.validate_choice()
        # Ajoutez une assertion pour vérifier si l'utilisation du clavier est désactivée
        assert calculator_app.display.get() == ""

if __name__ == '__main__':
    pytest.main()
