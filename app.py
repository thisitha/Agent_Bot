from flask import Flask, request, jsonify

from main import chatWithBot

app = Flask(__name__)


@app.route('/chat', methods=['GET', 'POST'])
def chatBot():
    chatInput = request.form['chatInput']
    return jsonify(chatBotReply=chatWithBot(chatInput))


@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    app.run()


