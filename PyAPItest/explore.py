from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()


client = Client(os.getenv("API_ID"), os.getenv("API_AUTH"))

#Abstract the Last sended message
# msg = client.messages.list()
# Last = msg[0]
# print(f"The last message is {Last.body} Send from {Last.from_}")

#Delete all the messages from the list 
# for msg in client.messages.list():
#     print(f"Deleting {msg.body}")
#     msg.delete()

#Create a new message 
msg = client.messages.create(
    to = os.getenv("My_Number"),
    from_ = os.getenv("My_Twilio_Number"),
    body = "Fixed the code to protect my API ID and API Key and also hide my phone numbers. 🚀👨‍🎓",
)

print(f"Created a new messag: {msg.body}")