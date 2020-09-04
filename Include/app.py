from flask import Flask
from config import Configuration, DB_NAME


from peewee import SqliteDatabase


app = Flask(__name__)
app.config.from_object(Configuration)

db = SqliteDatabase('db_rpl.db')

import view