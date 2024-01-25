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
    
    def get_fromage_names(self, database_name, table_name):
        con = sqlite3.connect(database_name)
        data_from_db = pd.read_sql_query(f"SELECT fromage_names from {table_name}", con)
        con.close()
        return data_from_db

    def get_fromage_familles(self, database_name, table_name):
        con = sqlite3.connect(database_name)
        data_from_db = pd.read_sql_query(f"SELECT fromage_familles from {table_name}", con)
        con.close()
        return data_from_db

    def get_pates(self, database_name, table_name):
        con = sqlite3.connect(database_name)
        data_from_db = pd.read_sql_query(f"SELECT pates from {table_name}", con)
        con.close()
        return data_from_db

    def connect_to_database(self, database_name):
        con = sqlite3.connect(database_name)
        return con

    def add_row(self, fromage_name, fromage_famille, pate):
        new_row = pd.DataFrame({'fromage_names': [fromage_name], 
            'fromage_familles': [fromage_famille], 'pates': [pate]})
        self.data = pd.concat([self.data, new_row], ignore_index=True)

    def sort_ascending(self):
        self.data = self.data.sort_values(by=['fromage_names'])

    def sort_descending(self):
        self.data = self.data.sort_values(by=['fromage_names'], ascending=False)

    def total_count(self):
        return len(self.data)

    def count_by_letter(self):
        return self.data['fromage_names'].str[0].value_counts()

    def update_fromage_name(self, old_name, new_name):
        self.data.loc[self.data.fromage_names == old_name, 'fromage_names'] = new_name

    def delete_row(self, fromage_name):
        self.data = self.data[self.data.fromage_names != fromage_name]

# Utilisation de la classe
fromage_etl = FromageETL('https://www.laboitedufromager.com/liste-des-fromages-par-ordre-alphabetique/')
fromage_etl.extract()
fromage_etl.transform()
fromage_etl.load('fromages_bdd.sqlite', 'fromages_table')
data_from_db = fromage_etl.read_from_database('fromages_bdd.sqlite', 'fromages_table')  # Correction ici

# Afficher le DataFrame
print(data_from_db)
