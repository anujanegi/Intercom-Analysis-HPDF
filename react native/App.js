import React, { Component } from 'react';

import { AppRegistry, StyleSheet, TextInput, View, Alert, Button } from 'react-native';

export default class MainProject extends Component {

    constructor(props) {

        super(props)

        this.state = {

            TextInputEmail: '',
            TextInputHours: '',
            TextInputDays: '',
            TextInputMinutes: '',
            TextInputTime: ''

        }

    }

    Submit = () => {
        const { TextInputEmail } = this.state;
        const { TextInputDays } = this.state;
        const { TextInputHours } = this.state;
        const { TextInputMinutes } = this.state;
        const { TextInputTime } = this.state;
        const reg = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
		const regex=/^([0-1]?[0-9]|[2][0-3]):([0-5][0-9])/;
      
        if (regex.test(TextInputTime)=== true && reg.test(TextInputEmail) === true && !isNaN(TextInputDays) && !isNaN(TextInputHours) && !isNaN(TextInputMinutes)) {


            var url = "https://data.atonal20.hasura-app.io/v1/query";

            var requestOptions = {
                "method": "POST",
                "headers": {
                    "Content-Type": "application/json"
                }
            };

            var body = {
                "type": "insert",
                "args": {
                    "table": "automation_details",
                    "objects": [{
                        "email": TextInputEmail,
                        "days": TextInputDays,
                        "hours": TextInputHours,
                        "minutes": TextInputMinutes,
                        "time":TextInputTime
                    }]
                }
            };

            requestOptions.body = JSON.stringify(body);

            fetch(url, requestOptions)
                .then(function(response) {
                    return response.json();
                })
                .then(function(result) {
                    console.log(result);
                })
                .catch(function(error) {
                    console.log('Request Failed:' + error);
                });

         


        
		
arr = TextInputTime.split(':');
hour = parseInt(arr[0]);
min = parseInt(arr[1]);
            var url = "https://app.atonal20.hasura-app.io/mailconversations";
			var requestOptions = {
                "method": "POST",
                "headers": {
                    "Content-Type": "application/json"
                }
            };

            var body = {
                "days" : "TextInputDays",
				"hours" : "TextInputHours",
				"minutes" : "TextInputMinutes",
				"time_hour" : "hour",
				"time_minute" : "min",
				"emailid" : "TextInputEmail"
            };

            requestOptions.body = JSON.stringify(body);

            fetch(url, requestOptions)
                .then(function(response) {
					if(response.code===200){
                    return response.json();
					  Alert.alert('Email Automated Successfully');
					}
					else{
					Alert.alert('Email Not Automated');
					}
					
                })
                .then(function(result) {
                    console.log(result);
                })
                .catch(function(error) {
                    console.log('Request Failed:' + error);
                });

          } else {
            Alert.alert('Incorrect input');
        }
		


         

		
		
		
    }
    render() {
        return (
		< View style = { styles.MainContainer } >
            <TextInput
            // Adding hint in Text Input using Place holder.
            placeholder = "Enter Email"
            onChangeText = { TextInputEmail => this.setState({ TextInputEmail }) }
            // Making the Under line Transparent.
            underlineColorAndroid = 'transparent'
            style = { styles.TextInputStyleClass }
            />
             <TextInput
            // Adding hint in Text Input using Place holder.
            placeholder = "Enter Days"
            onChangeText = { TextInputDays => this.setState({ TextInputDays }) }
            // Making the Under line Transparent.
            underlineColorAndroid = 'transparent'
            style = { styles.TextInputStyleClass }
            />
             <TextInput
            // Adding hint in Text Input using Place holder.
            placeholder = "Enter Hours"
            onChangeText = { TextInputHours => this.setState({ TextInputHours }) }
            // Making the Under line Transparent.
            underlineColorAndroid = 'transparent'
            style = { styles.TextInputStyleClass }
            />
             <  TextInput
            // Adding hint in Text Input using Place holder.
            placeholder = "Enter Minutes"
            onChangeText = { TextInputMinutes => this.setState({ TextInputMinutes }) }
            // Making the Under line Transparent.
            underlineColorAndroid = 'transparent'
            style = { styles.TextInputStyleClass }
            />
             <TextInput
            // Adding hint in Text Input using Place holder.
            placeholder = "HH:MM"
            onChangeText = { TextInputTime => this.setState({ TextInputTime }) }
            // Making the Under line Transparent.
            underlineColorAndroid = 'transparent'
            style = { styles.TextInputStyleClass }
            />

            <Button title = "Submit"
            onPress = { this.Submit }
            color = "#2196F3" / >
            </View>

        );
    }
}

const styles = StyleSheet.create({

    MainContainer: {

        justifyContent: 'center',
        flex: 1,
        margin: 10
    },

    TextInputStyleClass: {

        textAlign: 'center',
        marginBottom: 7,
        height: 40,
        borderWidth: 1,

        borderColor: '#2196F3',


    }

});

AppRegistry.registerComponent('MainProject', () => MainProject);