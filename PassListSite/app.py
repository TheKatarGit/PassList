from flask import Flask, render_template, redirect, request
from mongo_database import *
APP = Flask(__name__)


@APP.route('/', methods = ["GET"])
def show_pass_list():
    pass

@APP.route('/', methods = ["POST"])
def add_to_database():
    pass

@APP.route('/',methods = ["DELETE"])
def remove_from_database():
    pass
