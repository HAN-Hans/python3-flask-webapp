from flask import render_template

from app import mongo
from . import mgdb


@mgdb.route("/mongo")
def home_page():
    online_users = mongo.db.users.find({'online': True})
    return render_template('online.html')
