# Conversational Agent with Empathy for women in Afghanistan

## Background
From the 2008, 87.2% women in Afghanistan have reported at least one form of DV, which might have increased with the government takeover in 2021 by Taliban.

## Access Services
By [link](http://52.193.135.127:8000/)

## Get start in local

1. Clone the repo in your local
```shell
git clone https://github.com/xiaogeamadeus/EmpathyConversationalAgent.git
```

2. Install the dependency
```shell
pip3 install -r requirements.txt
```

3. Import the environment parameters 
    please copy the `envsample` file in your local, change the name to `.env` and add your own api-key into .env file.

#### Start frontend

```shell
# Go to frontend folder
cd frontend

python3 -m http.server 8000 --bind 0.0.0.0
```

Go to the [website](http://localhost:8000/)

#### Make backend and frontend still work

Start Frontend
```shell
cd frontend/
nohup python3 -m http.server 8000 --bind 0.0.0.0 > /home/ec2-user/output_front.log 2>&1 &
```

Start Backend
```shell
nohup python3 app.py > /home/ec2-user/output_backend.log 2>&1 &
```

Check current process
```shell
ps -ef
```

Kill process
```shell
kill [processId]
```



#### Test agent in local

Contact with fully conversational agent
```shell
python3 main.py
```

Only talk with listener agent
```shell
python3 onlyListener.py
```

Only talk with chatGPT4.0
```shell
python3 onlyGPT.py
```

#### Test in flask
Start server in local
```shell
python3 app.py
```

Send request to local server

1. Talk with empathy agent
URL: http://{localhost}/empathyConverse
body
```json
{
  "id": "{user id}",
  "message": "{user input}"
}
```

2. Talk with listener agent
   URL: http://{localhost}/listenerConverse
   body
```json
{
  "id": "{user id}",
  "message": "{user input}"
}
```

3. Talk with chatGPT4.0 agent
   URL: http://{localhost}/gptConverse
   body
```json
{
  "id": "{user id}",
  "message": "{user input}"
}
```

## Logs handling
Backend will automatedly store logs in a folder named `logs`. The logs will be stored as a json file with name of date. E.g. `log_2024-01-01.json`

Every logs will be generated when backend accepted a request from frontend. 

A case of logs seems like below:
```json
{
  "userId": "12345", 
  "currentAgent": "Listener", 
  "currentTime": "05:20:00", 
  "userInput": "I'm Wang, I feel not so good today... I need your help.", 
  "userOutput": "Hello Wang, I'm here to listen and support you. It's okay to have tough days, and I'm glad you reached out. Would you like to share a bit about what's making you feel not so good, or would you prefer to talk about something else to help take your mind off things? Remember, this is a safe space for you."
  }
```

#### Get logs from remote server
Our server run in Amazon EC2, so if we hope to get the logs file, we need to use `scp` command to safety copy the logs file to your local.

```shell
scp -i /directory/to/abc.pem user@ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com:path/to/file /your/local/directory/files/to/download
```

Use logsHandler.py function can handle logs file as below:
1. group by logs with user id with time order
2. stored logs to some new json file "{userId}.json"
   
Please remember to update the original logs file.
```shell
python3 logsHandler.py
```