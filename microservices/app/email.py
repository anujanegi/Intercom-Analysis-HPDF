from src import app, mail

def config_email():
    # email server
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'test-username'
    app.config['MAIL_PASSWORD'] = 'test-password'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    # administrator list
    ADMINS = ['test@gmail.com']

    mail.init_app(app)

def send_email(body, emailid):
    try:
        mail.connect()
    except Exception as e:
        Error(111, str(e))

    msg = Message(subject="Open conversations", body=body, sender=ADMINS[0], recipients=emailid)
    try:
        mail.send(msg)
    except Exception as e:
        Error(str(e))
