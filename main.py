""" Import modules """
import re
import requests
from bs4 import BeautifulSoup
import mysql.connector

URL = 'https://www.worldometers.info/geography/alphabetical-list-of-countries/'


def func():
    """ Return a dictionary created from two lists """

    url_rsp = requests.get(URL).text
    soup = BeautifulSoup(url_rsp, 'html.parser')

    table_body = soup.find('tbody')
    rows = table_body.find_all('tr')
    country_list = []
    population_list = []
    for row in rows:
        cols = row.find_all('td')
        country_index = 1
        td_country = cols[country_index]
        country_reg = re.findall("\">(.*)</td>", str(td_country))
        country_list.append(str(country_reg).strip('[\'').strip('\']'))

    for row in rows:
        cols = row.find_all('td')
        population_index = 2
        td_population = cols[population_index]
        population_reg = re.findall("\">([1-9].*)</a>", str(td_population))
        population_list.append(str(population_reg).strip('[\'').strip('\']'))

    #print(country_list)
    #print(population_list)

    # Create dict with values
    dict_list = dict(zip(country_list, population_list))
    #print(dict_list)

    # Create tuples from lists
    country_tuple = tuple(country_list)
    population_tuple = tuple(population_list)

    # Create list with tuples
    list_with_tuple = list(zip(country_tuple, population_tuple))
    #print(list_with_tuple)

    return list_with_tuple


def sql_connection():
    """ Database creation """
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='1234Pass',
        database='pythonparser'
    )

    my_cursor = mydb.cursor()

    # Database creation
    #my_cursor.execute("CREATE DATABASE pythonparser")

    # Table creation
    #my_cursor.execute("CREATE TABLE world (name VARCHAR(255), population VARCHAR(255))")


    # Insert data to table
    #sql_formula = "INSERT INTO world (country, population) VALUES (%s, %s)"
    #my_cursor.executemany(sql_formula, func())

    # Print data
    my_cursor.execute("SELECT * FROM world")
    my_result = my_cursor.fetchall()

    for row in my_result:
        print(row)

if __name__ == '__main__':
    func()
    sql_connection()
