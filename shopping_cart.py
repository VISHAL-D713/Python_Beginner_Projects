# list=[]
# while True:
#     data=input("Enter items to be added in list(0 to stop):")
#     if data=="0":
#         print("Exiting input loop")
#         break
#     else:
#         list.append(data)    
#     print(f"{data} has been added to list") 

    
# print("\nFinal list:")
# print(list)    
# while True:
#     print("/n Modification menu")
#     print("/n 1.Pop/n 2.Append/n 3.Print/n 4.Exit")
#     modify=int(input("Enter your choice"))
#     if modify=="1":
#         list.pop()
#         print(f"{data} has popped")
#     elif modify=="2":
#         new=input("Enter the new content")
#         list.append(new)  
#     elif modify =="3":
#         print("/n Final list")  
#         print(list) 
#     elif modify=="4":
#         print("Exiting Menu")
#         exit()       
my_list = []

# First input loop
while True:
    data = input("Enter items to be added in list (0 to stop): ")
    if data == "0":
        print("Exiting input loop.")
        break
    else:
        my_list.append(data)
        print(f"'{data}' has been added to the list.")

# Modification menu
while True:
    print("\nModification Menu:")
    print("1. Pop")
    print("2. Append")
    print("3. Print")
    print("4. Exit")

    modify = input("Enter your choice: ")

    if modify == "1":
        if my_list:
            popped = my_list.pop()
            print(f"'{popped}' has been popped from the list.")
        else:
            print("List is already empty!")

    elif modify == "2":
        new = input("Enter the new content to append: ")
        my_list.append(new)
        print(f"'{new}' has been added to the list.")

    elif modify == "3":
        print("\nCurrent List:")
        print(my_list)

    elif modify == "4":
        print("Exiting Menu.")
        break

    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")
total_cost=0      
price_list = {
    "Castor seeds": 500,
    "CD": 80,
    "Cream": 100,
    "Oil": 1000,
    "Meth":200,
    "Nitrogen":300
}  
print("\nBilling Section:")
for item in my_list:
    if item in price_list:
        total_cost += price_list[item]
        print(f"{item} - ₹{price_list[item]}")
    else:
        print(f"{item} - No price available (skipped)")

print("\nFinal Bill:")
print(f"Total cost: ₹{total_cost}")