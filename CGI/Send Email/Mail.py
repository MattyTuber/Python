from mailbox import Message
from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'matteo.broglio@studenti.fauser.edu'
app.config['MAIL_PASSWORD'] = 'FauserPompiere03,'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
    msg = Message('Hello',)
    msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
    mail.send(msg)
    return "Message sent!"

if __name__ == "__main__":
    app.run(debug=True)
