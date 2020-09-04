from flask import request, render_template, make_response, url_for
from models import *


class BaseController:
	def __init__(self):
		self.request = request

	def call(self, *args, **kwargs):
		print('in call')
		try:
			return self._call(*args, **kwargs)
		except Exception as ex:
			return make_response(str(ex), 500)

	def __call(self, *args, **kwargs):
		raise NotImplementedError('_call')


class ViewLenta(BaseController):
	def _call(self):
		articles = tuple(Articles.select())
		return render_template('lenta.html', articles = articles)


class ViewTables(BaseController):
	def _call(self, table_name):
		data = self.get_data(table_name)

		return render_template('tables.html', table_name=table_name, data=data)

	def get_data(self, table_name)->tuple:
		data = ()
		if table_name == "currency_table":
			data = tuple(Currency_Table.select().order_by(Currency_Table.score.desc()))
		elif table_name == "kf_uefa":
			data = tuple(KF_UEFA.select().order_by(KF_UEFA.total_score.desc()))
		elif table_name == "five_year":
			data = tuple(Five_Year_Table.select().order_by(Five_Year_Table.total_score.desc()))
		return data
		


class DBController:
	@classmethod
	def delete_articles(self, num):
		arts = tuple(Articles.select())
		arts[num-1].delete_instance() 

	@classmethod
	def add_articles(self, title, text):
		new_art = Articles(title=title, text=text)
		new_art.save()