# region ------------------ ABOUT -----------------------
"""
My Project...
"""
# endregion

# region ------------------ IMPORTS -----------------------
import sqlite3
from flask import Flask, request, g, redirect, url_for, \
    abort, render_template, flash
# endregion

# region ------------------ CONFIGURATIONS -----------------------
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
# endregion

app = Flask(__name__)
app.config.from_object(__name__)
