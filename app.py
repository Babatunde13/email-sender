import os
from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['MAIL_SERVER']=os.environ.get('MAIL_SERVER')
app.config['MAIL_USE_TLS']=1
app.config['MAIL_PORT']=587
app.config['MAIL_USERNAME']=os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD']=os.environ.get('MAIL_PASSWORD')

mail = Mail(app)

def send_mail(sender, recipients, body, subject=''):
    msg = Message(subject=subject, sender=sender, recipients=recipients)
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
    if data['subject']:
        send_mail(data['sender'], data['recipients'], data['body'], data['subject'])
    else:
        send_mail(data['sender'], data['recipients'], data['body'])
    return jsonify(message)

@app.errorhandler(500)
def error(e):
    return jsonify({'message': 'something went wrong'}), 500

@app.errorhandler(400)
def error1(e):
    return jsonify({'message': 'something went wrong'}), 500

@app.errorhandler(405)
def error2(e):
    return jsonify({'message': 'Method not allowed'}), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify({'message': 'Endpoint not found'}), 404

if __name__ == "__main__":
    app.run()
