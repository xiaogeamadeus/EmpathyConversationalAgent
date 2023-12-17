import json

from flask import Flask, request, jsonify
from flask_cors import CORS

from main import EmpathyConversationalAgent
from agents.compassionateListener import CompassionateListener
from agents.normalGPT import NormalGPT

app = Flask(__name__)
CORS(app, resources=r'/*')

empathy = EmpathyConversationalAgent()


# body: {id:"", message:""}

@app.route('/empathyConverse', methods=['post'])
def empathy_converse():
    if not request.data:
        return 'fail'
    raw_data = request.data.decode('utf-8')
    data = json.loads(raw_data)
    user_input = data["message"]
    agent_response = empathy.converse(user_input)
    return jsonify({"agentName": "Friendly Bot", "message": agent_response})


@app.route('/listenerConverse', methods=['post'])
def listener_converse():
    if not request.data:
        return 'fail'
    raw_data = request.data.decode('utf-8')
    data = json.loads(raw_data)
    user_input = data["message"]
    listener = CompassionateListener()
    agent_response = listener.run_agent(user_input)
    return jsonify({"agentName": "Listener Bot", "message": agent_response})


@app.route('/gptConverse', methods=['post'])
def gpt_converse():
    if not request.data:
        return 'fail'
    raw_data = request.data.decode('utf-8')
    data = json.loads(raw_data)
    user_input = data["message"]
    gpt = NormalGPT()
    agent_response = gpt.run_agent(user_input)
    return jsonify({"agentName": "Nomal Bot", "message": agent_response})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
