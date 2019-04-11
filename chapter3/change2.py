def main():
    print("Change Counter")
    print()
    print("Please enter the count of each coin type.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    total = .25 * quarters + .1 * dimes + .05 * nickels + .01 * pennies
    print()
    print("The total value of your change is", total)

main()