# pattern 1:  repeat fixed number of times another condition is met
# print hello 5 times, but only when user says so

counter=0
while counter < 5:
    x=input("should I print?")
    if x=="y":
        print("Hello")
        counter=counter+1