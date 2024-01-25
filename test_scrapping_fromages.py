import pandas as pd
import sqlite3
import pytest
from unittest.mock import patch, Mock
from scrapping_fromage import FromageETL

@pytest.fixture
def etl_instance():
    return FromageETL("https://www.laboitedufromager.com/liste-des-fromages-par-ordre-alphabetique/")

@patch('scrapping_fromage.urlopen')
def test_extract(mock_urlopen, etl_instance):
    # Configurez le comportement simulé de urlopen
    mock_urlopen.return_value.read.return_value = b"<html><body>Mocked HTML</body></html>"
    # Appelez la méthode extract
    etl_instance.extract()
    # Assurez-vous que les données ont été correctement extraites
    assert etl_instance.data == b"<html><body>Mocked HTML</body></html>"

def test_transform(etl_instance):
    # Définissez les données de test
    test_data = b"<table><tr><td>Fromage1</td><td>Famille1</td><td>Pate1</td></tr></table>"
    etl_instance.data = test_data
    # Appelez la méthode transform
    etl_instance.transform()
    # Assurez-vous que les données ont été correctement transformées
    assert etl_instance.data['fromage_names'].iloc[0] == "Fromage1"
    assert etl_instance.data['fromage_familles'].iloc[0] == "Famille1"
    assert etl_instance.data['pates'].iloc[0] == "Pate1"

def test_load_and_read_from_database(etl_instance, tmp_path):
    # Appelez extract et transform avant d'accéder à etl_instance.data
    etl_instance.extract()
    etl_instance.transform()
    # Créez un chemin de fichier temporaire pour la base de données
    database_name = tmp_path / "fromages.sqlite"
    # Chargez les données dans la base de données
    etl_instance.load(database_name, "fromages_table")
    # Lisez les données depuis la base de données
    data_from_db = etl_instance.read_from_database(database_name, "fromages_table")
    print("Données initiales:", etl_instance.data)
    print("Données depuis la base de données:", data_from_db)
    # Assurez-vous que les données dans la base de données correspondent aux données initiales
    assert len(data_from_db) == len(etl_instance.data)
    assert data_from_db['fromage_names'].tolist() == etl_instance.data['fromage_names'].tolist()
    assert data_from_db['fromage_familles'].tolist() == etl_instance.data['fromage_familles'].tolist()
    assert data_from_db['pates'].tolist() == etl_instance.data['pates'].tolist()

def test_get_fromage_names(etl_instance):
    # Appelez extract et transform avant d'accéder à etl_instance.data
    etl_instance.extract()
    etl_instance.transform()
    # Chargez les données dans la base de données
    etl_instance.load('fromages_bdd.sqlite', 'fromages_table')

    # Assurez-vous que la méthode renvoie les noms de fromages corrects
    expected_names = etl_instance.data['fromage_names'].values.tolist()
    assert etl_instance.get_fromage_names('fromages_bdd.sqlite', 'fromages_table')['fromage_names'].values.tolist() == expected_names

def test_get_fromage_familles(etl_instance):
    # Appelez extract et transform avant d'accéder à etl_instance.data
    etl_instance.extract()
    etl_instance.transform()
    # Chargez les données dans la base de données
    etl_instance.load('fromages_bdd.sqlite', 'fromages_table')

    # Assurez-vous que la méthode renvoie les familles de fromages correctes
    expected_familles = etl_instance.data['fromage_familles'].values.tolist()
    assert etl_instance.get_fromage_familles('fromages_bdd.sqlite', 'fromages_table')['fromage_familles'].values.tolist() == expected_familles

def test_get_pates(etl_instance):
    # Appelez extract et transform avant d'accéder à etl_instance.data
    etl_instance.extract()
    etl_instance.transform()
    # Chargez les données dans la base de données
    etl_instance.load('fromages_bdd.sqlite', 'fromages_table')

    # Assurez-vous que la méthode renvoie les pâtes de fromages correctes
    expected_pates = etl_instance.data['pates'].values.tolist()
    assert etl_instance.get_pates('fromages_bdd.sqlite', 'fromages_table')['pates'].values.tolist() == expected_pates

def test_connect_to_database(etl_instance):
    con = etl_instance.connect_to_database('fromages_bdd.sqlite')
    assert con is not None

def test_add_row(etl_instance):
    etl_instance.extract()
    etl_instance.transform()
    initial_len = len(etl_instance.data)
    etl_instance.add_row('Test Fromage', 'Test Famille', 'Test Pate')
    assert len(etl_instance.data) == initial_len + 1

def test_sort_ascending(etl_instance):
    etl_instance.extract()
    etl_instance.transform()
    etl_instance.sort_ascending()
    sorted_names = etl_instance.data['fromage_names'].tolist()
    assert sorted_names == sorted(sorted_names)

def test_sort_descending(etl_instance):
    etl_instance.extract()
    etl_instance.transform()
    etl_instance.sort_descending()
    sorted_names = etl_instance.data['fromage_names'].tolist()
    assert sorted_names == sorted(sorted_names, reverse=True)

def test_total_count(etl_instance):
    etl_instance.extract()
    etl_instance.transform()
    count = etl_instance.total_count()
    assert count == len(etl_instance.data)

def test_count_by_letter(etl_instance):
    etl_instance.extract()
    etl_instance.transform()
    counts = etl_instance.count_by_letter()
    assert counts is not None

def test_delete_row(etl_instance):
    etl_instance.extract()
    etl_instance.transform()
    etl_instance.add_row('Test Fromage', 'Test Famille', 'Test Pate')
    initial_len = len(etl_instance.data)
    etl_instance.delete_row('Test Fromage')
    assert len(etl_instance.data) == initial_len - 1

def test_update_fromage_name(etl_instance):
    etl_instance.extract()
    etl_instance.transform()
    etl_instance.add_row('Test Fromage', 'Test Famille', 'Test Pate')
    etl_instance.update_fromage_name('Test Fromage', 'Updated Fromage')
    assert 'Updated Fromage' in etl_instance.data['fromage_names'].values

if __name__ == '__main__':
    pytest.main()
