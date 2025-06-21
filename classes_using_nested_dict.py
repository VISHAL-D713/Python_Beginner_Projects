




schedule = {
    "R-1": {"T": "EP", "F": "EGD", "S": "BEEE"},
    "R-2": {"T": "BEEE", "F": "EP", "S": "EGD"},
    "R-3": {"T": "EGD", "F": "BEEE", "S": "EP"},
}

while True:
    print("\nAvailable Batches: R-1, R-2, R-3, E (to Exit)")
    batch = input("Enter your batch: ")

    if batch == "E":
        print("Exiting...")
        break

    day = input("Enter the day (T, F, S): ")

    if batch in schedule:
        if day in schedule[batch]:
            print(f"You have {schedule[batch][day]} Practical")
        else:
            print("You have no classes!!")
    else:
        print("Invalid batch!!")

# a="Nigger"
# reversed_a=''.join(reversed(a))
# print(reversed_a)