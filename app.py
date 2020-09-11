import os
from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_USE_TLS']=1
app.config['MAIL_PORT']=587
app.config['MAIL_USERNAME']=os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD']=os.environ.get('MAIL_PASSWORD')

mail = Mail(app)

def send_mail(sender, recipients, body, **kwargs):
    msg = Message(sender=sender, recipients=recipients, **kwargs)
    msg.body=body
    mail.send(msg)
    return 'sent'

@app.route('/mail', methods=['POST'])
def email_me():
    data = request.get_json()
    message = {
            'message': 'Mail sent successfully'
        }
    if 'sender' not in data.keys() or 'recipients' not in data.keys():
        message['message'] = 'Sender or recipient not provided'
        return message
    elif 'body' not in data.keys():
        message['message'] = 'Body of mail not provided'
        return message
    else:
        pass
    send_mail(data['sender'], data['recipients'], data['body'])
    return jsonify(message)

@app.errorhandler(500)
def error(e):
    return jsonify({'message': 'something went wrong'}), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify({'message': 'Endpoint not found'}), 404

app.run()
