import requests
from bs4 import BeautifulSoup


def func():
    url = 'https://www.worldometers.info/geography/' \
          'alphabetical-list-of-countries/'
    url_req = requests.get(url).text
    soup = BeautifulSoup(url_req, 'html.parser')

    table_body = soup.find('tbody')
    rows = table_body.find_all('tr')
    country_list = []
    population_list = []
    for row in rows:
        cols = row.find_all('td')
        td_country = cols[1]
        country = (str(td_country).strip('<td style="font-weight: bold; '
                                    'font-size:15px">').rstrip('</'))
        country_list.append(country)

    for row in rows:
        cols = row.find_all('td')
        td_population = cols[2]
        population = ''.join(filter(str.isdigit, str(td_population)))
        population_list.append(population)

    print(country_list)
    print(population_list)
    dict_list = {}
    for key in range(len(country_list)):
        dict_list[country_list[key]] = population_list[key]
    print(dict_list)
    #print(dict_list['Argentina'])

if __name__ == '__main__':
    func()


