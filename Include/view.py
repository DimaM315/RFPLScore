from app import app
import controller

@app.route('/')
def lenta_page():
	#страница с лентой статей
	return controller.ViewLenta().call()

@app.route('/table/<tb_name>')
def table_page(tb_name='currency_table'):
	TB_NAMES = ('currency_table', 'kf_uefa', 'five_year')
	tb_name = 'currency_table' if tb_name not in TB_NAMES else tb_name

	return controller.ViewTables().call(tb_name)


@app.errorhandler(404)
def error_log(err):
	print(err)
	return '404 error'

@app.errorhandler(405)
def error_log(err):
	print(err)
	return '405 error'
