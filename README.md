# Conversational Agent with Empathy for women in Afghanistan

## Background
From the 2008, 87.2% women in Afghanistan have reported at least one form of DV, which might have increased with the government takeover in 2021 by Taliban.

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