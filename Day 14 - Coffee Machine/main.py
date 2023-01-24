from resources import MENU, resources

still_using = True
money = 0


def print_resources(res, mon):
    for key, value in res.items():
        if key == "water" or key == "milk":
            print(f"{key.capitalize()}: {value}ml")
        else:
            print(f"{key.capitalize()}: {value}g")
    print(f"Money: ${mon}")


def check_resources(menu, res, drink):
    for key, val in res.items():
        for k, v in menu[drink]["ingredients"].items():
            if key == k:
                if val >= v:
                    res[key] = val - v
                else:
                    print(f"Sorry there is not enough {k}.")
                    return False
    return res


while still_using:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        if check_resources(MENU, resources, user_choice):
            continue
    elif user_choice == "report":
        print_resources(resources, money)
    elif user_choice == "off":
        still_using = False
        break
    else:
        print("Unknown command. Try again!")
        continue
