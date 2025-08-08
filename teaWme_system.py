import datetime
import json
tea_input = 'D:\\kennguyen\\CODING\\teaWme\\teaWme\\database_teaWme_input.json'
tea_output = 'D:\\kennguyen\\CODING\\teaWme\\teaWme\\database_teaWme_output.json'

try:
    with open(tea_output, 'r') as file:
        tea_order = json.load(file)
except FileNotFoundError:
    tea_order = []

print("WELCOME TO TEAWME - READY TO ORDER YOUR DRINK?")
name = input("Please enter your name: ")
print(name)

def add_order():
    print("--------------ORDER STAGE--------------")
    tea_list = {
    1: {"name": "Tra sua truyen thong", "price": 25000},
    2: {"name": "Tra sua tran chau duong den", "price": 30000},
    3: {"name": "Tra sua Thai xanh", "price": 28000},
    4: {"name": "Tra sua socola", "price": 32000},
    5: {"name": "Tra sua matcha", "price": 32000},
    6: {"name": "Tra sua khoai mon", "price": 30000},
    7: {"name": "Tra sua caramel", "price": 32000},
    8: {"name": "Tra sua hokkaido", "price": 35000},
    9: {"name": "Tra sua bac ha", "price": 30000},
    10: {"name": "Tra sua dau", "price": 30000}
}
    topping_list = {
    1: {"name": "Tran chau trang", "price": 5000},
    2: {"name": "Tran chau den", "price": 5000},
    3: {"name": "Kem sua", "price": 7000},
    4: {"name": "Thach dua", "price": 6000},
    5: {"name": "Pudding trung", "price": 8000},
    6: {"name": "Thach pho mai", "price": 8000},
    7: {"name": "Full topping", "price": 15000}
}
    for key, value in tea_list.items():
        print(f"{key}. {value}")
    tea_choice1_num = int(input("Choose your first drink and type a number: "))
    global tea_choice1_word
    tea_choice1_word = tea_list[tea_choice1_num]["name"]
    for key, value in topping_list.items():
        print(f"{key}. {value}")
    global tea_choice1_price
    tea_choice1_price = tea_list[tea_choice1_num]["price"] 

    topping_choice1_num = int(input(f"Choose a topping for your {tea_choice1_word} and type a number: "))
    global topping_choice1_word
    topping_choice1_word = topping_list[topping_choice1_num]["name"]
    global topping_choice1_price
    topping_choice1_price = topping_list[topping_choice1_num]["price"]

    global size_choose
    size_choose = input("Choose your drink's size (M/L): ")
    quit_if = input("Press any key to continue or 'q' to quit: ")
    while True:
        if quit_if.lower() == 'q':
            print("SUCCESSFULLY CREATED ORDER!")
            break
        else:
            add_order()


add_order()

print("------------------ORDER BILL-------------------")
bill = {
        "-Name-:": name,
        "-Date-:": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "-Drink-:": tea_choice1_word,
        "-Notes-:": {
            "Topping:": topping_choice1_word,
            "Size:": size_choose
        },
        "-Total price-:": f"{tea_choice1_price + topping_choice1_price} VND",
        "-VAT-:": "5%",
        "FINAL PRICE:": f"{(tea_choice1_price + topping_choice1_price) * 1.05} VND"
}
for key, value in bill.items():
        print(f"{key}. {value}")

tea_order.append(bill)
with open(tea_output, 'w') as file:
        json.dump(tea_order, file, indent=4)
print("----------THANH YOU FOR BUYING OUR DRINKS!! HAVE A GOOD DAY!----------")