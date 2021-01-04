import bottle
import json

@bottle.route("/")
def index():
    return bottle.static_file("index.html", root="./Front End Files")


@bottle.route("/style.css")
def style():
    return bottle.static_file("style.css", root="./Front End Files")

bottle.run(host='127.0.0.1', port=8080, debug=True)