# Birthday Boy
Scripting Project for MSD20

## About
### Authors/Contributors
* [David Riegler](mailto:david.riegler@fh-joanneum.at)
* [Lukas Weber](lukas.weber@fh-joanneum.at)
* [Ulrike Ozim](ulrike.ozim@fh-joanneum.at)

### Description
The idea is an application with functionalities of reading and writing names and dates to a .csv file, and sending the information via telegram bot

This "project" contains/will implement/focus on:
* Reading/Writing csv
* Requests module and telegram bot
* Cron Job able
* Command Line parameter input


## Run/Execute
> placeholder, in the future description about functionalities

## Documentation
https://web.telegram.org/#/im?p=@uuuuuiiii_bot
Use this link to start the bot. After that get use of your Browser Console.

In Google Chrome go Application -> Storage -> Local Storage -> user_auth. 
In Safari go Storage -> Local Storage -> user_auth
Under Value there is a key like {dcID":"1":0123456789}

Fill the last String of number in your config.py file under the name botID.

![Screenshot](ConsoleInput.png)
For start the Script use your command line and enter python bot.py < name > < birthday >
  
  
![Screenshot](TelegramNameDate.png)
For getting the names and dates use the command python bot.py

![Screenshot](TelegramName.png)
For only one person enter python.bot.py < name >
  
  
## Known Issues
> placeholder


## Useful links
* https://core.telegram.org/bots


