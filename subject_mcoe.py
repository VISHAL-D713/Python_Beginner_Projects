print("WELCOME TO R DIVISION!!!")
batches={"R-1":1,"R-2":2,"R-3":3,"E":0}
# practicals={"EGD":10,"EP":20,"BEEE":"30"}
print("Select your division:")
for batches in batches:
    batch=input("Enter your batch:")
    if(batch not in batches):
        print("Blunder ho gaya na")
        continue
    if(batches=="E"):
        print("Exiting")    
        break
    day=input("Enter the day(T,F,S)")
    # practical=input("Enter your practical")
    if(day=="T" and batch=="R-1"):
        print("You have EP Practical")
    elif(day=="F" and batch=="R-1"):
        print("You have EGD")    
    elif(day=="S" and batch=="R-1"):
        print("You have BEEE")    
    elif(day=="T" and batch=="R-2"):
        print("You have BEEE")  
    elif(day=="F" and batch=="R-2"):
        print("You have EP")   
    elif(day=="S" and batch=="R-2"):
        print("You have EGD")   

    elif(day=="T" and batch=="R-3"):
        print("You have EGD")  
    elif(day=="F" and batch=="R-3"):
        print("You have BEEE")    
    elif(day=="S" and batch=="R-3"):
        print("You have EP")
    else:
        print("Ypu have no classes!!")     





