from os import system
system("cls")
client = {
    "name":             "John Doe", 
    "acc":              "0123456789012", 
    "balance_amount":   100000, 
    "balance_currency": "USD"
    }

print(client["name"])
client["card_number"] = "1111-2222-3333-4444"
client["card_pin"]    = "1234"

card_number_check = input("Enter the card number: ") #1111-2222-3333-4444
pin_check         = input("Enter the pin: ") #ex 1234


#if card_number_check == client["card_number"] and pin_check == client["card_pin"]:
   # money_enterd = float(input("Enter the money: "))*100
   # client["balance_amount"] +=money_enterd
#print(int(client["balance_amount"]))

while card_number_check == client["card_number"] and pin_check == client["card_pin"]:
    system("cls")
    print("Hello", client["name"])
    print("######### MENU #########")
    print("1. Check Balance")
    print("2. Change Pin")
    print("3. Add money")
    print("0. exit")

    option = int(input("choose> "))

    if option == 1:
        system("cls")
        print(f"Your balance is: {int(client['balance_amount'])}")
        input("hit enter to continue...")
    
    if option == 2:
        card_number_check = input("Enter new pin: ")
        client["card_pin"] = card_number_check
        print(f'Your new pin is: {client["card_pin"]}')
        
        input("Yourapdated your pin, to continue you should reenter back details")
    
    if option == 3:
        money_enterd = float(input("Enter the money: "))*100
        client["balance_amount"] +=money_enterd
        input("hit enter to continue...")
    
    if option == 0:
        quit()