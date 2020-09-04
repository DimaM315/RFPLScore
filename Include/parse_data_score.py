import requests
from bs4 import BeautifulSoup
import re
import json



url = 'https://ru.wikipedia.org/wiki/%D0%A7%D0%B5%D0%BC%D0%BF%D0%B8%D0%BE%D0%BD%D0%B0%D1%82_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8_%D0%BF%D0%BE_%D1%84%D1%83%D1%82%D0%B1%D0%BE%D0%BB%D1%83_2014/2015'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}


def get_page(url, params=None):
	r = requests.get(url, headers=HEADERS, params=params)
	return r.text


def find_table(soup):
	#ищим нужную таблицу среди таблиц html-page
	tables = soup.find_all('table')
	
	for table in tables:
		th = []

		for el in table.find_all('th'):
			th.append(el.text)
			
			if 'О' in th:
			# 'О' - текст названия столбца(очки), именно той таблице которая нам нужна.
				return table

	return 'Not found'


def parse_table(table):
	#получаем в строковом виде все ряды(tr) таблицы
	tr = []
	#цикл убирает у каждого эл-та html
	for el in table.find_all('tr'):
		tr.append(el.text)
	#удаялем оглавление столбцов
	del(tr[0])

	#делаем строки читаемыми
	tr_str = []
	for r in tr:
		tr_data = r.split('\n\n')
		#удаляем значение колонки "Примечание"
		del(tr_data[len(tr_data)-1])
		tr_str.append(' '.join(tr_data[1:]).replace('\xa0', ''))
		
	#возвращается список со строк данных о каждой команде
	return tr_str

def write_data(data, season):
	#записываем данные в файл
	mod = 'w' if season == '11/2012' else 'a'
	print('Парсится сезон: '+season)
	#записываются данные в формате json
	with open('data_score.txt', mod) as of:
	#indent - говорит о том что каждая строка займёт отдельную строчку
		json.dump([season]+data, of, indent=2)

def put_data():
	with open('data_score.txt', 'r') as of:
		data = of.read()
	return data

def russin_word_decode(text):
	#декодируем кирилические символы
	return changed_text

def russin_word_encode(text):
	#кодируем кирилические символы
	return changed_text



def fill_data_score():
	seasons = ['11/2012', '12/2013', '13/2014', '14/2015', '15/2016',]# '16/2017', '17/2018', '18/2019', '19/2020'] #
	for season in seasons:
		url = ('https://ru.wikipedia.org/wiki/%D0%A7%D0%B5%D0%BC%D0%BF%D0%B8%D0%BE%D0%BD%D0%B0%D1%8'
				+'2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8_%D0%BF%D0%BE'
				+'_%D1%84%D1%83%D1%82%D0%B1%D0%BE%D0%BB%D1%83_20{}'.format(season))
		soup = BeautifulSoup(get_page(url), 'lxml')	
		table = find_table(soup)
		data = parse_table(table)
		write_data(data, season)



def main():
	#fill_data_score()
	print(put_data())




if __name__ == '__main__':
	main()

#