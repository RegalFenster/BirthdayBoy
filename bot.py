import getopt
import re
import sys

import requests

import config


def telegram_bot_sendtext(bot_message):

    bot_token = config.bot_token 
    bot_chatID = config.bot_chatID 
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
 

    return response.json()



argv = sys.argv[1:] 

try: 
    opts, args = getopt.getopt(argv, "h") 
except: 
    print("For help: bot.py -h") 
    sys.exit()
  
for opt, arg in opts: 
    if opt in ['-h']: 
        print("No argument for getting all birthday boys: bot.py")
        print("Find specific birthday boy: bot.py <name>")
        print("Save new birthday: bot.py <name> <dd.mm.yyyy>")


if len(argv) == 0:
    print("All birthday boys")
  

if len(argv) == 1:
    print("Searching for birthday boy")

     
if len(argv) == 2:
    if re.match("^[a-zA-Z]+$", argv[0]):
        print(argv[0])

    if re.match("^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$", argv[1]):
        print(argv[1])
