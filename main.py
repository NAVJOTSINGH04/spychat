from spy_details import spy_name, spy_salutation, spy_age, spy_rating
import sys
print "hello "
print "welcome to spychat "

question = "Do you want to continue as " + spy_salutation + " " + spy_name + " (Y/N)? "
existing = raw_input(question)

def start_chat(spy_name,spy_age, spy_rating):
    menu_choices = "What do you want to do? \n 1. Add a status update\n"
    menu_choice = raw_input(menu_choices)
    if (menu_choice == 1):
        pass
    else:
        sys.exit()



if (existing == "Y"):
  #Continue with the default user/details imported from the helper file.
    start_chat(spy_name,spy_age,spy_rating)
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











