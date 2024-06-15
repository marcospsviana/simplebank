from formaters import currency_formater, date_formater

menu = """
********* Welcome Python Bank System *********

[d] Deposit
[w] Withdrawal
[e] Extract
[q] Quit

***********************************************
"""
extract = (
    "**************************** ACCOUNT EXTRACT ****************************\n\n\n"
)
value = 0


OPERATIONS_REPORT = {
    "deposit": "Deposit ",
    "withdrawal": "Withdrawal ",
    "account_balance": "Account Balance",
}


def record_operations(type_operation, val, time):
    global extract
    extract += f"{OPERATIONS_REPORT[type_operation]} {val} {time}\n\n"


LIMIT = 500
account_balance = 0
WITHDRAWAL_COUNT = 0
option_choice = ""
print(menu)
record_operations(
    "account_balance", currency_formater(account_balance), date_formater()
)


while True:
    option_choice = input("Choose an option from the menu\n").lower()

    if option_choice == "d":
        value = float(input("Enter with value of the deposit\n"))
        if value > 0:
            account_balance += value
            extract += "  ---------------------------------------------  \n"
            record_operations("deposit", currency_formater(value), date_formater())
            record_operations(
                "account_balance", currency_formater(account_balance), date_formater()
            )

        else:
            print("Invalid value inputted\n")

    elif option_choice == "w":
        if WITHDRAWAL_COUNT == 3:
            print(
                """************************ ATTENTION ************************
                      You exceed the daily limit withdrawal,
                       you can do 3 withdrawal per day!')
                      ***********************************************************"""
            )
        value = float(input("Enter with value of the withdrawal\n"))
        if value > 500:
            print("You exceed the maxim limit of R$ 500,00")
        if value > account_balance:
            print(
                f"""
                The value of {currency_formater(value)} exceed the limit of your balance account,
                you have {currency_formater(account_balance)} of balance!"""
            )
        else:
            account_balance -= value
            extract += "  ---------------------------------------------  \n"
            record_operations("withdrawal", currency_formater(value), date_formater())
            record_operations(
                "account_balance", currency_formater(account_balance), date_formater()
            )
            WITHDRAWAL_COUNT += 1

    elif option_choice == "e":
        print(extract)
        print(
            "****************************** END EXTRACT ******************************"
        )

    elif option_choice == "q":
        break
    else:
        print("Option or value invalid!")
