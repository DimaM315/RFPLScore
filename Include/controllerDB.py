from models import *
#методы для внешней работы с таблицами

def delete_articles(num):
	arts = tuple(Articles.select())
	arts[num-1].delete_instance() 

def add_articles(title, text):
	new_art = Articles(title=title, text=text)
	new_art.save()



#cоздание таблицы УЕФА
def create_UEFA_table():
	KF_UEFA.create_table()
	
	esp = KF_UEFA(country="Испания", seventeen_eighteen=19.714, eighteen_nineteen=19.571, nineteen_twenty=18.928, total_score=80.640)
	ang = KF_UEFA(country="Англия", seventeen_eighteen=20.071, eighteen_nineteen=22.642, nineteen_twenty=18.571, total_score=78.497)
	ger = KF_UEFA(country="Германия", seventeen_eighteen=9.857, eighteen_nineteen=15.214, nineteen_twenty=18.714, total_score=60.641)
	fra = KF_UEFA(country="Франция", seventeen_eighteen=11.500, eighteen_nineteen=10.583, nineteen_twenty=11.666, total_score=50.165)

	for lig in (esp, ang, ger, fra):
		lig.save()
		
#cоздание текущей таблицы
def create_currency_table():
	Currency_Table.create_table()
	data = [['Локомотив', 7, 5, 1, 5.4],#team, score, games, deff_goals, xG
		['Рубин', 7, 5, 1, 6.2], ['Краснодар', 7, 5, 3, 7.2], ['Арсенал Тула', 5, 5, -2, 3.9],
		["Урал", 5, 5, -2, 1.2], ["Уфа", 4, 5, -6, 2.3], ["Тамбов", 3, 5, -5, 1.5],
		["Химки", 3, 5, -4, 3.1], ["Ротор", 2, 5, -6, 1.1]
	]
	
	for team in data:
		row = Currency_Table(team=team[0], score=team[1], games=team[2], deff_goals=team[3], xG=team[4])
		row.save()


def create_five_year_table():
	Five_Year_Table.create_table()
	data = [['Зенит', 300, 279, 160, 1000, 309], #team, team, total_goals, deff_goals, xG, total_score
		[],[],[],
		[],[],[],
		[],[],[],
		[],[],[],
	]
	for team in data:
		row = Five_Year_Table(team=team[0], games=team[1], total_goals=team[2], 
							  deff_goals=team[3], xG=team[4], total_score=team[5])
		row.save()


