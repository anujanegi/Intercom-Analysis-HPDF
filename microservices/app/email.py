from src import app, mail

def config_email():
    # email server
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'anuja.negi2016@vitstudent.ac.in'
    app.config['MAIL_PASSWORD'] = 'ANUJA-SANUJ'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    # administrator list
    ADMINS = ['anuja.negi2016@vitstudent.ac.in']

    mail.init_app(app)
    return ADMINS

def getattributes(conversation):
    #parse to get id and message body for each conversation
    repls = ('</p>', ''), ('<p>', '')
    msg_id = conversation['id']
    msg_body = (conversation['conversation_message'].to_dict())['body']
    msg_body = reduce(lambda a, kv: a.replace(*kv), repls, msg_body)
    body = "ID: %s\tMESSAGE: %s\n" % (msg_id,msg_body)
    return body

def getbody(conversationlist):
    # get bosy of the email from the conversations
    body = ""
    for convo in conversationlist:
        body += getattributes(convo)
    return body

def send_email(body, emailid):
    try:
        ADMINS = config_email()
        mail.connect()
    except Exception as e:
        Error(111, str(e))

    RECP = [emailid]
    msg = Message(subject="Open conversations", body=body, sender=ADMINS[0], recipients=RECP)

    try:
        mail.send(msg)
    except Exception as e:
        Error(500, str(e))
