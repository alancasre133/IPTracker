from flask import Blueprint, render_template, request
from utils import *


views = Blueprint(__name__,"views")

@views.route("/")
def home():
    approximately_house = ""
    collection = getCollection(getClient("alanaxelcastroresendiz","Alan7776"),'RACPIR','IP_Metadata')

    ip_address = ""
    more = ""

    return render_template("index.html",name="Alan")
