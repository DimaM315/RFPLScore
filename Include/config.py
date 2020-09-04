class Configuration(object):
	DEBUG = True
	SECRET_KEY = 'secret'
	
	#flack sequrity
	SECURITY_PASSWORD_SALT = 'sault'
	SECURITY_PASSWORD_HASH = 'sha512_crypt'

DB_NAME = "rpl_score.db"


HTTP_TIMEOUT = 15

IP_LIST = ['127.0.55.1']