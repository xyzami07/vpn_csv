from flask import Flask
import requests

app = Flask(__name__)

base_url = "http://www.vpngate.net/api/iphone/"

response = requests.get(base_url)
response.encoding = "utf-8"
data = response.text


@app.route("/")
def api():
    return data
