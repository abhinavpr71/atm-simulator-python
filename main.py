print("ATM")

user_pin = int(input("enter your pin(4 number) : "))

def menu():
    print("1. Check balance")
    print("2. Deposti money")
    print("3. withdraw money")
    print("4. Exit")
    print("5. Change pin")

balance = 5000

stored_pin = 6695

while True:
    if user_pin == stored_pin:
        menu()
        user_option = int(input("Select option (1, 2 , 3 , 4) :"))

        if user_option == 4:
            break
        elif user_option == 1:
            print(f"Balance : ₹{balance}")
        elif user_option == 2:
            deposit_amount = int(input("Enter amount :"))
            if deposit_amount < 100:
                print("Minimum deposit amount is ₹100")
            else:
                balance += deposit_amount
                print(f"₹{deposit_amount} is credited to your account.Your account balance : ₹{balance}")
        elif user_option == 3:
            withdraw_amount = int(input("Enter withdraw amount :"))
            if withdraw_amount > balance :
                print("Not enough balance. click 1 to check balance")
            else:
                balance = balance - withdraw_amount
                print(f"₹{withdraw_amount} has been debited from your account . Your account balance : ₹{balance} ")
        elif user_option == 5:
            correct_pin =  int(input("Enter old pin :"))
            if correct_pin == stored_pin:
                new_pin = int(input("Enter New pin :"))
                stored_pin = new_pin
                print("PIN changed successfully")
            else:
                print("Incorrect pin")
        else:
            print("Invalid option. please chooe 1,2,3,4 or 5")
            user_option = int(input("Select option (1, 2 , 3 , 4 or 5) :"))   
    else:
        print("Your pin is wrong!! Enter pin again")
        user_pin = int(input("enter your pin(4 number) : "))
print("Thanks for using ATM")   
