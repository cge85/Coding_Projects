const Twilio = require("twilio");
require('dotenv').config()

const client = new Twilio(process.env.API_ID, process.env.API_AUTH);

client.messages
  .list()
  .then(messages =>
    console.log(
      `The most recent message is ${messages[0].body} and the sender is ${messages[0].from}`
    )
  )
  .catch(err => console.error(err));

console.log("Gathering your message log");
