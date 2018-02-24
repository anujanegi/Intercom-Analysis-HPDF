# Intercom-Analysis-HPDF

Custom service that integrates with Intercom APIs and sends out daily emails with a list of open conversations for X days/hours  at the time specified by the user.

### Getting started

### Get the app

`hasura quickstart rishikumars/Intercom-open_conversations`.

#### Get the apk

1. Get the apk of the app from [here](https://drive.google.com/file/d/1ziAM8hXKdhAVEJfi1pwRJo9UWIZfmpUg/view).
2. Install on your device.
3. Enter details as per requirement of open conversations and submit.

### Configure

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

####  Making the request
Make a `POST` request to the endpoint `/mailconversations` with the correct headers and body.
Find API endpoint documentation [here](https://documenter.getpostman.com/view/3487083/automate-open-conversations-email/7TT5oSF).
###### Headers
**`Content-type`**                  ` application/json`
###### Body
```
{
	"days" : "days",
	"hours" : "hours",
	"minutes" : "minutes",
	"time_hour" : "time_hour",
	"time_minute" : "time_minute",
	"emailid" : "emailid"
}
```

### UI Details
This is a fully functioning native applications using react-native components for UI and Python-flask for back end.

#### Configure
The react-native code lies in Intercom-open_conversations/react-native directory.

1. Install` node_modules`. Run `npm install` from the `react-native` directory.
2. `$ cd react-native && npm install`.
3. Get your cluster name. Run `hasura cluster status`. Copy the cluster name.
4. Go to react-native/src/hasuraAPi.js. Add your cluster name to this file.

#### Emulating

1. Keep the android emulator running.
2. Run  `react-native run-android`from the react-native directory.
App will open up on your emulator.


###  Note
This is a dummy and will not work unless you have an Intercom account with proper access and edit in your extended access token and your email credentials from which the conversations will be fetched and a daily mail to the user be automated respectively.

### Authors
1. Anuja Negi - Python FLask
2. Rishi Kumar - React Native
