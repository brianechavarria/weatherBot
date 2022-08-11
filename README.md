# weatherBot

**Requires a "SensitiveInfo.txt" text document to function**

This script uses the openweathermap and twilio api to text a specific user
the current weather conditions in New York. For the script to work properly,
the "SensitiveInfo.txt" document needs to contain your openweather api key in the first line,
your twilio account_sid in the second line, your twilio auth_token in the third line,
your twilio phone number in the fourth line and the phone number you want to text in the fifth line.
Once you have the "SensitiveInfo.txt" document properly filled out this script can simply
be run through the terminal.

The "requirements.txt" document contains the names of the necessary python packages to run the script.
This allows for the script to be run using the heroku client along with the heroku scheduler addon to
run the script at a predetermined time daily.
