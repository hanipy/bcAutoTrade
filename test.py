import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2499428039858-2532803133058-DB3ehVDYf0x0X2yCj27xgnO1"
 
post_message(myToken,"#coin","Everything will be alright")
