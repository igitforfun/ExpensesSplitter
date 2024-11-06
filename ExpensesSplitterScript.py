
import argparse

prompt = "\nWhat do you want to do? \n\
1.Add expenses\n\
2.Remove expenses\n\
3.Show expenses summary\n"

# expensedict = {} #expenses items for indexing
namelist = [] #name of participants
moneylist = [] #how much each participants owe or get back
formatted_expenselist = []

def show_explist():
    print("\n====================List of Expenses====================")
    for i in range(len(formatted_expenselist)):
        print(f"{i+1}. {formatted_expenselist[i]}")
    print("========================Summary===========================")
    for j in range(len(namelist)):
        if int(moneylist[j]) < 0:
            print(f"{namelist[j]} owes {moneylist[j]}")
        elif int(moneylist[j]) > 0:
            print(f"{namelist[j]} needs to get back {moneylist[j]} ")
        else:
            print(f"{namelist[j]} don't owe or receive")
    print("==========================End===========================\n")

def remove_expenses():
    print(f"Which expenses do you want to remove?")
    show_explist()
    sel = int(input('Select a number: '))
    if (sel <= 0) or (sel >len(formatted_expenselist)):
        print("Invalid input! Please select a valid number based on list")
        remove_expenses()
    else:
        sel_index = sel - 1
        payer = str(formatted_expenselist[sel_index].split('paid by ')[-1])
        amt = int((formatted_expenselist[sel_index].split('paid by ')[0]).split('$')[-1])
        for j in range(len(namelist)):
            if namelist[j] == payer:
                moneylist[j] -= amt * (len(namelist)-1)/(len(namelist))
            else:
                moneylist[j] += amt/len(namelist)
        formatted_expenselist.remove(formatted_expenselist[sel_index])


def add_expenses():
    not_found = True
    exp_name = str(input("Name of expenses?\n"))
    payer = str(input(f"Who paid?\n {namelist}\n"))
    amt = int(input(f"How much?\n"))
    for j in range(len(namelist)):                                              #loop through each names and calculate owe/gain
        if namelist[j] == payer:
            not_found = False
    if not_found is True:
        print("Participant not found!")
    else:
        for j in range(len(namelist)):
            if namelist[j] == payer:
                moneylist[j] += amt * (len(namelist)-1)/(len(namelist))
            else:
                moneylist[j] -= amt/len(namelist)    
        formatted_expenselist.append(f"{exp_name} : ${amt} paid by {payer}")

def main():                                      
    num = int(input("How many people in the trip:"))                          #Get number of people
    for i in range(num):
        namelist.append(str(input(f"Name of person {i+1}: ")))                #Create namelist and moneylist
        moneylist.append(0)
    while True:                                                               #Constantly running the script
        opt = int(input(prompt))
        if opt == 1:
            add_expenses()
        if opt == 2:
            remove_expenses()
        if opt == 3:
            show_explist()

if __name__ == '__main__':
    main()
