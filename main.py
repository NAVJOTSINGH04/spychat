print "hello "
print "welcome to spychat "
spyname=raw_input("what is your spy name")
#raw_input =this will convert user input into  a string
if len(spyname)>0:
    # if statement to check the length of string passed is grater than 0.... just bcz there should be a name
    print "welcome"+spyname
    salutation=raw_input("should i call you Mr.or Miss. ")
    print "Alright "+ salutation+spyname+" I would like to know more about you"

spyage=0
spyrating=0.0
spy_is_online=False
#to initialise them
spyage=input("what  is your age ?:")

if spyage >20 and spyage<50:
    spyrating=input("what is your spy rating?:")
    spyrating=float(spyrating)
    if spyrating>4.5 and spyrating<5:
        print"you are the best"

if spyrating>3.5 and spyrating<=4.5:
            print"you can do it"

if spyrating>2.5 and spyrating<=3.5:
              print"work hard"
              #sari if statement bahr rakhni hai . it should not  be in other if statement
spy_is_online=True
print"Authentication complete.Welcome " +spyname+ " age: "+str(spyage) +" rating: "+str(spyrating)+" proud to have you back."













