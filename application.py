from chatbot import CB
from flask import Flask, render_template, request

application = Flask(__name__)

@application.route("/chatbot")
def home():
    return render_template("index.html")

@application.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(CB.get_response(userText))
application.run(debug = True)
