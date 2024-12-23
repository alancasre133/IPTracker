from flask import Blueprint, render_template, request
from utils import *


views = Blueprint(__name__,"views")

@views.route("/")
def home():
    approximately_house = ""
    collection = getCollection(getClient("alanaxelcastroresendiz","Alan7776"),'RACPIR','IP_Metadata')

    ip_address = ""
    more = ""
    forwarded_for = request.headers.get('X-Forwarded-For')
    forwarded_for="189.217.111.179"
    if forwarded_for:
        for ip in forwarded_for.split(','):
            ip_address+=ip+" , "
            more += "1"
            approximately_house = requests.get(f'https://ipinfo.io/{ip}?token=9c06a926e98489').json()
            IP,city,region,country, postal, loc = getIPData(approximately_house)
            approximately_house = f'\n IP:{IP}\nCity:{city}\nRegion:{region}\nCountry:{country}\nPostal Code:{postal}\nloc:{loc}'
            insertDocuments(collection,[{"IP":IP,"loc": loc, "country": country, "region": region, "city": city, "postal":postal}])
    return render_template("index.html",name="Alan")