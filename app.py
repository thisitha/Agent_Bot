from flask import Flask, request, jsonify

from main import chatWithBot

app = Flask(__name__)


@app.route('/chat', methods=['GET', 'POST'])
def chatBot():
    chatInput = request.args.get('chatInput')
    return jsonify(chatBotReply=chatWithBot(chatInput))




if __name__ == '__main__':
    app.run()


