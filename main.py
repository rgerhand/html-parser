""" Import modules """
import re
import requests
from bs4 import BeautifulSoup

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

    print(country_list)
    print(population_list)
    dict_list = dict(zip(country_list, population_list))
    print(dict_list)


if __name__ == '__main__':
    func()
