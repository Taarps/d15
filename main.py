from menu import MENU
from resources import resources

# TODO: 1. Prompt user by asking what he like

turn_on_machine = True
enough_resources = True

while turn_on_machine:

    while enough_resources:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # TODO: 4. Check resources sufficient?
        if resources["water"] >= MENU[user_choice]["ingredients"]["water"]:
            print("water is ok")
        else:
            print("Sorry there is not enough water.")
            break

        if MENU[user_choice] == "latte" or "cappuccino":
            if resources["milk"] >= MENU[user_choice]["ingredients"]["milk"]:
                print("milk is ok")
            else:
                print("Sorry there is not enough milk.")
                break

        if resources["coffee"] >= MENU[user_choice]["ingredients"]["coffee"]:
            print("coffee is ok")
        else:
            print("Sorry there is not enough coffee.")
            break

        print("Please insert coins.")
        quarters = input("how many quarters?: ")
        # TODO: 2. Turn off the Coffee Machine
        if quarters == "off":
            break
        dimes = input("how many dimes?: ")
        if dimes == "off":
            break
        nickles = input("how many nickles?: ")
        if nickles == "off":
            break
        pennies = input("how many pennies?: ")
        if pennies == "off":
            break
        # TODO: 5. Process coins.
        total_coins = int(quarters)*0.25 + int(dimes)*0.10 + int(nickles)*0.05 + int(pennies)*0.01
        print(total_coins)
        coffee_costs = MENU[user_choice]["cost"]
        # TODO: 6. Check transaction successful?
        if total_coins > coffee_costs:
            returns = total_coins - coffee_costs
            # TODO: 7. Make Coffee.
            print(
                f"Here is ${returns} in change."
            )
            print("Here is your latte ☕️. Enjoy!")
            resources["water"] -= MENU[user_choice]["ingredients"]["water"]
            resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]
            resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
        else:
            print("Sorry that's not enough money. Money refunded.")

# TODO: 3. Print reportŗ

