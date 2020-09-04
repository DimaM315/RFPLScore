from peewee import (Model, IntegerField, DoubleField, CharField, 
					TextField, DateTimeField, datetime as peewee_datetime,)

from app import db 


class _Model(Model):
	class Meta:
		database = db

class Articles(_Model):
	class Meta:
		db_table = 'articles'

	title = CharField(max_length=100, null=False)
	text = TextField(null=False)
	created = DateTimeField(index=True, default=peewee_datetime.datetime.now)


class KF_UEFA(_Model):
	class Meta:
		db_table = 'koeffs_UEFA'

	country = CharField(max_length=100, index=True)
	seventeen_eighteen = DoubleField()
	eighteen_nineteen = DoubleField()
	nineteen_twenty = DoubleField()
	total_score = DoubleField()



class Currency_Table(_Model):
	class Meta:
		db_table = 'currency_table'

	team = CharField(max_length=100, index=True)
	score = IntegerField()
	games = IntegerField()
	deff_goals = IntegerField()
	xG = DoubleField()

		
class Five_Year_Table(_Model):
	class Meta:
		db_table = 'five_year_table'
		order_by = 'total_score'

	team = CharField(max_length=100, index=True)
	games = IntegerField()
	total_goals = IntegerField() #279
	deff_goals = IntegerField() #+160
	xG = IntegerField()  		#n
	total_score = IntegerField() #309
