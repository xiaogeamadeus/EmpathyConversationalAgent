import json

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

from main import EmpathyConversationalAgent
from agents.compassionateListener import CompassionateListener
from agents.normalGPT import NormalGPT

app = Flask(__name__)
CORS(app, resources=r'/*')

empathy = EmpathyConversationalAgent()

current_date = datetime.now().strftime("%Y-%m-%d")


# body: {id:"", message:""}

def write_json_log(user_id, cur_agent, user_input, user_output):
    current_date = datetime.now().strftime("%Y-%m-%d")
    log_entry = {
        "userId": user_id,
        "currentAgent": cur_agent,
        "userInput": user_input,
        "userOutput": user_output
    }
    with open(f"/home/ec2-user/log_{current_date}.json", "a") as log_file:
        json.dump(log_entry, log_file)
        log_file.write('\n')  # Add a newline for readability

@app.route('/empathyConverse', methods=['post'])
def empathy_converse():
    if not request.data:
        return 'fail'
    raw_data = request.data.decode('utf-8')
    data = json.loads(raw_data)
    user_input = data["message"]
    user_id = data["id"]
    agent_response = empathy.converse(user_input)
    write_json_log(user_id, "Empathy", user_input, agent_response)
    return jsonify({"agentName": "Friendly Bot", "message": agent_response})


@app.route('/listenerConverse', methods=['post'])
def listener_converse():
    if not request.data:
        return 'fail'
    raw_data = request.data.decode('utf-8')
    data = json.loads(raw_data)
    user_input = data["message"]
    user_id = data["id"]
    listener = CompassionateListener()
    agent_response = listener.run_agent(user_input)
    write_json_log(user_id, "Listener", user_input, agent_response)
    return jsonify({"agentName": "Listener Bot", "message": agent_response})


@app.route('/gptConverse', methods=['post'])
def gpt_converse():
    if not request.data:
        return 'fail'
    raw_data = request.data.decode('utf-8')
    data = json.loads(raw_data)
    user_input = data["message"]
    user_id = data["id"]
    gpt = NormalGPT()
    agent_response = gpt.run_agent(user_input)
    write_json_log(user_id, "GPT", user_input, agent_response)
    return jsonify({"agentName": "Nomal Bot", "message": agent_response})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
