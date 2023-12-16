const originBotName = 'ChatBot';

let curBot = 0;
let curStatus = 0;

const bots = [
    {1:"gptConverse"},
    {2:"listenerConverse"},
    {3:"empathyConverse"}];


document.addEventListener('DOMContentLoaded', function() {
    displayInitialMessages();
});

function displayInitialMessages() {
    const messages = [
        { text: originBotName + ": Thank you so much for your time and courage to talk with me. I am really sorry that it was the situation that brought you here today. But it takes great strength to walk through those doors and say: 'I need help'.", delay: 5000 },
        { text: originBotName + ": Before we start talking, please confirm that you are safe now and let yourself keep in a relaxed environment.", delay: 5000 },
        { text: originBotName + ": Are you in a safe environment without anyone else who will give you pressure? Please type 'yes' or 'no'", delay: 5000 },
    ];

    messages.forEach((message, index) => {
        setTimeout(() => {
            displayMessage(message.text, 'server-message');
        }, messages.slice(0, index).reduce((total, msg) => total + msg.delay, 0));
    });
}

document.getElementById('send-button').addEventListener('click', function() {
    var userInput = document.getElementById('user-input').value;
    if (userInput.trim() !== '') {
        displayMessage(userInput, 'user-message');
        document.getElementById('user-input').value = ''; // clear input
        if (curStatus === 3) {
            const botObj = bots.find(obj => obj.hasOwnProperty(curBot));
            const address = botObj[curBot];
            // Backend
            fetch(`http://127.0.0.1:5000/${address}`, {
                method: 'POST',
                mode: "cors",
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ "message": userInput })
            })
            .then(response => response.json())
            .then(data => {
                displayMessage(data.agentName + ": " + data.message, 'server-message');
            })
            .catch(error => {
                console.error('Error:', error);
                displayMessage('Error: Having some connection error, please refresh the page.', 'server-message');
            });
        } else if (curStatus === 2) {
            if (userInput !== "1" && userInput !== "2" && userInput !== "3") {
                displayMessage('Error: Please input 1, 2 or 3.', 'server-message');
            } else {
                curStatus = 3
                curBot = parseInt(userInput, 10);
                const messages = [
                    { text: originBotName + ": Thank you so much! It seems like you have chose bot " + userInput + ".", delay: 3000 },
                    { text: originBotName + ": Please enjoy the conversation with your bot!", delay: 6000 },
                ];
            
                messages.forEach((message, index) => {
                    setTimeout(() => {
                        displayMessage(message.text, 'server-message');
                    }, messages.slice(0, index).reduce((total, msg) => total + msg.delay, 0));
                });
            }
        } else if (curStatus === 0) {
            if (userInput !== "yes" && userInput !== "no") {
                displayMessage('Error: Please input yes or no.', 'server-message');
            } else {
                curStatus = 1
                const messages = [
                    { text: originBotName + ": I'm really happy to hear that you are safe now!", delay: 5000 },
                    { text: originBotName + ": Please feel free to talk anything to me. All the record of conversation will be deleted in your phone or computer. Nobody will know what we have talked before after closing this website.", delay: 5000 },
                    { text: originBotName + ": By the way, please confirm that would you mind letting researchers from Kyoto University use our conversation data to make me more smart and can talk more things to you. Feel free to do the decision cause if you say 'No', you can also talk with me as well. We respect your choices.", delay: 5000 },
                    { text: originBotName + ": Would you mind if the researchers use this conversation data? (This conversation only) Please type 'yes' or 'no'", delay: 5000}
                ];
            
                messages.forEach((message, index) => {
                    setTimeout(() => {
                        displayMessage(message.text, 'server-message');
                    }, messages.slice(0, index).reduce((total, msg) => total + msg.delay, 0));
                });
            }
        } else if (curStatus === 1) {
            if (userInput !== "yes" && userInput !== "no") {
                displayMessage('Error: Please input yes or no.', 'server-message');
            } else {
                curStatus = 2
                const messages = [
                    { text: originBotName + ": Thank you so much for sharing data to us! Researchers will try them best to make me more smart and easy to talk with!", delay: 5000 },
                    { text: originBotName + ": The next step is choosing bot type you want to talk with today.", delay: 5000 },
                    { text: originBotName + ": Bot 1: a Nomal Bot; Bot 2: a Listener Bot; Bot 3: a Friendly Bot.", delay: 5000 },
                    { text: originBotName + ": Please type '1', '2' or '3' to pick one of them and open conversation! P.S. you cannot change bot in once conversation.", delay: 5000}
                ];
            
                messages.forEach((message, index) => {
                    setTimeout(() => {
                        displayMessage(message.text, 'server-message');
                    }, messages.slice(0, index).reduce((total, msg) => total + msg.delay, 0));
                });
            }
        } else {
            displayMessage('Error: Having some internal error, please refresh the page.', 'server-message');
        }
        
    }
});

function displayMessage(message, className) {
    var messageArea = document.getElementById('message-area');
    var messageDiv = document.createElement('div');
    messageDiv.classList.add('message', className);
    messageDiv.innerText = message;
    messageArea.appendChild(messageDiv);

    messageArea.scrollTop = messageArea.scrollHeight; // scroll done to the end.
}
