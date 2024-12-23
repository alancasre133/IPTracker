from flask import Blueprint, render_template, request
from utils import *


views = Blueprint(__name__,"views")

@views.route("/")
def home():
    approximately_house = ""

    return render_template("index.html",name="Alan")
