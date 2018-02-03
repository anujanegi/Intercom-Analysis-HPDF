# Intercom-Analysis-HPDF

Custom service that integrates with Intercom APIs and sends out daily emails with a list of open conversations for X days/hours  at the time specified by the user.

### Getting started
#### Get the apk
1. Get the apk of the app from [here](https://drive.google.com/file/d/1ziAM8hXKdhAVEJfi1pwRJo9UWIZfmpUg/view).
2. Install on your device.
3. Enter details as per requirement of open conversations and submit.

#### Configure Intercom
Add your extended access intercom token in `intercomconfig.py` to enable connection to intercom.
```
intercom = Client(personal_access_token='extended_access_token_here')
```
#### Add email credentials
Setup you email server in `email.py` by configuring it with valid credentials.
```
# email server
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'test@gmail.com'
    app.config['MAIL_PASSWORD'] = 'test-password'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    # administrator list
    ADMINS = ['test@gmail.com']
```

### Making the request
Make a `POST` request to the endpoint `/mailconversations` with the correct headers and body.
Find API endpoint documentation [here](https://documenter.getpostman.com/view/3487083/automate-open-conversations-email/7TT5oSF).


### Note
This is a dummy and will not work unless you have an Intercom acount with proper access and edit in your extended access token and your email credentials from which the conversations will be fetched and a daily mail to the user be automated respectively.
