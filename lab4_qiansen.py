#A FOR LOOP
ages = [17, 11, 25, 13, 9]
for age in ages:
    if age >= 13: print (str(age) + " - Access granted")
    else: print (str(age) + " - Too young")
#PREDICT: 17, 25, and 13 will get access granted and 11 & 9 will get too young 
#EXPLAIN: the variable age holds each value in the ages list
#B WHILE LOOP
#PREDICT: if the user types no then the code won't run
#EXPLAIN: Because it allows the user to keep checking ages until they want to stop 

while True: 
    keep_checking = input ("enter an age or type 'stop': ")
    if keep_checking == "stop":
        break
    age = int(keep_checking)
    if age >= 13: print ("Access granted")
    else: print ("Too young")
#PREDICT: No the loop would never end if the break wasn't there 
#EXPLAIN: This one allows the user to stop the loop
#C FUNCTIONS
def can_access(age):
    for age in ages:
        if age >= 13: return True
        else: return False
        if True: print ("Access granted")
        else: print ("Too young")
can_access(ages)
#PREDICT: The code will
signups = [22, 10, 15, 8, 19, 13]
def signup_report (age):
    approved = 0
    signup = 1
    print (" --- StreamPass Signup Report --- ")
    for age in signups:
        if age >= 13: 
            print ("Signup #" + str(signup) + " | Age " + str(age) + " - Access granted") 
            approved += 1
            signup += 1 
        else: 
            print ("Signup #" + str(signup) + " | Age " + str(age) + " - Too young") 
            signup += 1
    print ("Approved: " + str(approved) + " out of " + str(len(signups)))
signup_report (signups)