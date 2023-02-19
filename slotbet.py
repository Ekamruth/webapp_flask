import random
import webbrowser

chars={'Luffy':3,
        'Zoro':2.75,
        'Sanji':2.5,
        'Robin':2.25,
        'Franky':2,
        'Brook':1.75,
        'Chopper':1.5,
        'Nami':1.35,
        'Usopp':1.2}

def balance():
    while True:
        bal = input("Add amount to your balance: ")
        if bal.isdigit():
            if int(bal)>0:
                print("Your balance is:",bal)
                bal=int(bal)
                break
            else:
                print("Enter an amount greater than 0")
        else:
            print("You did not enter a digit, please enter a digit.")
    return bal


def bet():
    while True:
        amount = input("What is your bet: ")
        if amount.isdigit():
            if 0<=int(amount):
                print("Your bet is:",amount)
                amount=int(amount)
                break
            else:
                print("Enter an amount greater than 0.")
        else:
            print("You did not enter a digit, please enter a digit.")

    bet_char = input("Enter the name of the character you want to bet on:")
    print(""*2)

    return amount,bet_char

def roll_slot():
    char_lst=[]
    slots=[]
    for name,power in chars.items():
        char_lst.append(name)
    for i in range(3):
        slot=random.choice(char_lst)
        slots.append(slot)
    for i in slots:
        print(i,end=' | ')
    print(""*2)
    return slots


def spin(deposit):
    while True:
        stake, bet_char = bet()
        if stake > deposit:
            print("You have insufficient balance. Your bet is %s but your balance is %s." % (stake, deposit))
        else:
            break
    current_balance = deposit - stake
    current_slots = roll_slot()
    count = 0
    for i in current_slots:
        if i == bet_char:
            count += 1
    winnings = count * chars[bet_char] * stake
    current_balance=current_balance+winnings
    if count>0:
        ext = "file:///C:/Users/gekam/Desktop/programing/onepiece%20chars/" + bet_char + ".html"
        webbrowser.open_new_tab(ext)

    print("" * 2)
    print("Your balance is", deposit)
    print("You have bet %d amount on %s" % (stake, bet_char))
    print("Your winnings are", winnings)
    return current_balance


def main():
    deposit = balance()
    while True:
        game=input("Press enter to continue or q to quit")
        if game=='q':
            break
        deposit= spin(deposit)
        print("Your new balance is",deposit)


main()






