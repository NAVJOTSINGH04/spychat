from spy_details import spy
import sys
print "hello "
print "welcome to spychat "

question = "Do you want to continue as " + spy['salutation'] + " " + spy['name'] + " (Y/N)? "
existing = raw_input(question)

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.']

friends = []

def add_status(current_status_message):
    if current_status_message != None:
        print "Your current status message is " + current_status_message + "\n"
    else:
        print 'You don\'t have any status message currently \n'

    default = input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = input("What status message do you want to set? ")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)

    elif default.upper() == 'Y':
        item_position = 1
        for message in STATUS_MESSAGES:
            print item_position + ". " + message
            item_position = item_position + 1
        message_selection = input("\nChoose from the above messages ")
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
    return updated_status_message


def add_friends():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }
    new_friend['name'] = input("Please add your friend's name: ")
    new_friend['salutation'] = input("Are they Mr. or Ms.?: ")
    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = input("Age?")
    new_friend['rating'] = input("Spy rating?")

    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['rating']:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    return len(friends)
def start_chat(spy):
    current_status_message = None

    print "What do you want to do? \n 1. Add a status update\n 2. add friends "
    menu_choice = int(raw_input("enter you choise"))

    if (menu_choice == 1):
        current_status_message= add_status(current_status_message)
    elif menu_choice == 2:
        add_friends()
    else:
        pass




if (existing == "Y"):
  #Continue with the default user/details imported from the helper file.
    start_chat(spy)
else:


    spy_name=raw_input("what is your spy_name")
    #raw_input =this will convert user input into  a string
    if len(spy_name)>0:
        # if statement to check the length of string passed is grater than 0.... just bcz there should be a name
        print "welcome"+spy_name
        spy_salutation=raw_input("should i call you Mr.or Miss. ")
        print "Alright "+ spy_salutation+spy_name+" I would like to know more about you"
    else:
        print "binna naaam k spy hai kya"


    spy_age=0
    spy_rating=0.0
    spy_is_online=False
    #to initialise them
    spy_age=input("what  is your age ?:")

    if spy_age >20 and spy_age<50:
        spy_rating=input("what is your spy rating?:")
        spy_rating=float(spy_rating)
        if spy_rating>4.5 and spy_rating<5:
            print"you are the best"

    if spy_rating>3.5 and spy_rating<=4.5:
                print"you can do it"

    if spy_rating>2.5 and spy_rating<=3.5:
                  print"work hard"
                  #sari if statement bahr rakhni hai . it should not  be in other if statement
    spy_is_online=True
    print"Authentication complete.Welcome " +spy_name+ " age: "+str(spy_age) +" rating: "+str(spy_rating)+" proud to have you back."

start_chat(spy_name,spy_age,spy_rating)











