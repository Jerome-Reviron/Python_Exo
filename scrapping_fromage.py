import pandas as pd
import sqlite3
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

class FromageETL:
    def __init__(self, url):
        self.url = url
        self.data = None

    def extract(self):
        data = urlopen(self.url)
        self.data = data.read()

    def transform(self):
        soup = BeautifulSoup(self.data, 'html.parser')
        cheese_dish = soup.find('table')

        fromage_names = []
        fromage_familles = []
        pates = []

        for row in cheese_dish.find_all('tr'):
            columns = row.find_all('td')

            if columns:
                fromage_name = columns[0].text.strip()
                fromage_famille = columns[1].text.strip()
                pate = columns[2].text.strip()

                # Ignore les lignes vides
                if fromage_name != '' and fromage_famille != '' and pate != '':
                    fromage_names.append(fromage_name)
                    fromage_familles.append(fromage_famille)
                    pates.append(pate)

        self.data = pd.DataFrame({
            'fromage_names': fromage_names,
            'fromage_familles': fromage_familles,
            'pates': pates
        })

        self.data['creation_date'] = datetime.now()

    def load(self, database_name, table_name):
        con = sqlite3.connect(database_name)
        self.data.to_sql(table_name, con, if_exists="replace", index=False)
        con.close()

    def read_from_database(self, database_name, table_name):
        con = sqlite3.connect(database_name)
        data_from_db = pd.read_sql_query(f"SELECT * from {table_name}", con)
        con.close()
        return data_from_db

# Utilisation de la classe
fromage_etl = FromageETL('https://www.laboitedufromager.com/liste-des-fromages-par-ordre-alphabetique/')
fromage_etl.extract()
fromage_etl.transform()
fromage_etl.load('fromages_bdd.sqlite', 'fromages_table')
data_from_db = fromage_etl.read_from_database('fromages_bdd.sqlite', 'fromages_table')  # Correction ici

# Afficher le DataFrame
print(data_from_db)
