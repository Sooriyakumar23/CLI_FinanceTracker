from tracker.CustomError import ChoiceException, TransactionTypeException
from tracker.Transaction import Transaction
from tracker.utils import generate_report
from tracker.dao import write_transaction, read_transactions

try:
    print ("Start..... \n\n\n")

    choice = int(input("Enter your choice:\n 1. Add Transaction \n 2. Check Financial Report \n"))
    print ("\n")
    if (choice == 0):
        exit()
    elif (choice == 1):
        amount = float(input("Amount: "))
        type = str(input("Enter one of the type (income / expense): "))
        if (type.lower() == "income"):
            amount = +amount
        elif (type.lower() == "expense"):
            amount = -amount
        else:
            raise TransactionTypeException()
        category = str(input("Give a category(eg:- freelance, business, full-time, ...): "))
        transaction = Transaction(amount, type, category)
        write_transaction(transaction)
        print (transaction)
    elif (choice == 2):
        transactions = read_transactions()
        report = generate_report(transactions)

        print("Financial Report: \t")
        for key, value in report.items():
            print(f"{key} ---> {value}")

        print ("\n")
    else:
        raise ChoiceException()
    
    print ("\n\n\nEnd.....")
except ChoiceException as ex:
    print ("Choice must be 1 or 2")
except TransactionTypeException as ex:
    print ("Transaction Type must be income or expense")
except Exception as ex:
    print ("EXCEPTION: \t")
    print (ex)