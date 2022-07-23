# import library
import argparse
from modules import Modgen as mon
from modules import sendmail as mail
# Script functions 
mon.one_monument

mon.all_monuments

# Argument parser function

def argument_parser():
    parser = argparse.ArgumentParser(description= 'Know the closest BiciMad station' )
    help_message ='You have two options. Option 1: Select one monument. Option 2: get the list for all monuments' 
    parser.add_argument('-f', '--function', help=help_message, type=str)
    args = parser.parse_args()
    return args
# Pipeline execution

if __name__ == '__main__':
    if argument_parser().function == 'all':
        useremail=str(input("To have the information enter your email: "))
        result = mon.all_monuments()
        mail.send_email(useremail, 'Test', 'MADnumentos', './monument_list.csv')
    elif argument_parser().function == 'one':
        result = mon.one_monument()
    else:
        result = 'FATAL ERROR...you need an option'
    print(f'The result is => {result}')