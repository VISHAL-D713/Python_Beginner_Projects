print("WELCOME TO CLASSIC CAFE!!!!")
total_cost=0
items={"Pizza":50,"Burger":45,"French Fries":60,"Exit":0}

while True:
    
  for food,price in items.items():
    print(f"{food}= {price}")
  item=input("Enter your choice:")
  if(item not in items):
    print("Invalid choice!!")
    continue
  if(item=="Exit"):
        print("Exiting!!!")
        break    
  print(f"You selected {item}")
  quantity=input(f"Enter the quantity of {item}")
  if quantity.isdigit():
       quantity=int(quantity)
       cost=items[item]*quantity
       total_cost+=cost
       print(f"{quantity} x {item}={cost}")
       print("Thanks for orderingg!!")
  else:
       print("Enter a valid number")
  
print(f"The total cost is {total_cost}")      

        
# print("WELCOME TO CLASSIC CAFE!!!!")
# total_cost = 0
# items = {"Pizza": 50, "Burger": 45, "French Fries": 60, "Exit": 0}

# while True:
#     for food, price in items.items():
#         print(f"{food} = ₹{price}")

#     item = input("Enter your choice: ")
    
#     if item not in items:
#         print("Invalid choice!!")
#         continue

#     if item == "Exit":
#         print("Exiting!!!")
#         break    

#     print(f"You selected {item}")
#     quantity = input(f"Enter the quantity of {item}: ")

#     if quantity.isdigit():  # <-- fixed here (add () to isdigit)
#         quantity = int(quantity)
#         cost = items[item] * quantity
#         total_cost += cost
#         print(f"{quantity} x {item} = ₹{cost}")
#         print("Thanks for ordering!!")
#     else:
#         print("Enter a valid number")

# print(f"Current total cost: ₹{total_cost}")
