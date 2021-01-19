import csv
import getopt
import os.path
import re
import sys

import requests

import config


def telegramBotSendText(botMessage):

    botToken = config.botToken 
    botChatID = config.botChatID 
    sendText = 'https://api.telegram.org/bot' + botToken + '/sendMessage?chat_id=' + botChatID + '&parse_mode=Markdown&text=' + botMessage

    response = requests.get(sendText)

    return response.json()


def checkBirthdaysFileExists():
    if os.path.isfile('birthdays.csv'):
        return True
    else:
        print("No birthday boys existent")
        return False

def main():



    #Check options and print help
    argv = sys.argv[1:] 

    try: 
        opts, argv = getopt.getopt(argv, "hd") 
    except: 
        print("For help: bot.py -h") 
        sys.exit()
    
    for opt, arg in opts: 
        if opt in ['-h']: 
            print("No argument for getting all birthday boys: bot.py")
            print("Find specific birthday boy: bot.py <name>")
            print("Save new birthday: bot.py <name> <dd.mm.yyyy>")
            print("For deleting birthday file: bot.py -d")
        if opt in ['-d']:   
            if checkBirthdaysFileExists() == True:
                os.remove('birthdays.csv')
                
        
    #Check arguments and process      
    if len(argv) == 0:
        if checkBirthdaysFileExists() == True:
            with open('birthdays.csv', 'rt') as f:
                csvReader = csv.reader(f)
                for p in csvReader:
                    telegramBotSendText(p[0] + " " + p[1])


    if len(argv) == 1:
        if checkBirthdaysFileExists() == True:
            with open('birthdays.csv', 'rt') as f:
                csvReader = csv.reader(f)
                for p in csvReader:
                    if argv[0] in p:
                        telegramBotSendText(p[1])
            
    
    if len(argv) == 2:
        if re.match("^[a-zA-Z]+$", argv[0]) and re.match("^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$", argv[1]):
            with open('birthdays.csv', 'a', newline='') as f:
                dateName = [argv[0], argv[1]]
                csvWriter = csv.writer(f)
                csvWriter.writerow(dateName)


main()