import os
import time

cursor = ">"
journal_list = []

def clear_screen():
    os.system("cls")

def create_journal(journal_name):
    if (os.path.isdir("journals")):
        with open(os.path.join(f"journals/" + journal_name + ".txt"), "a"):
            input(f"Journal With The Name {journal_name} Has Been Created Successfully! Press Any Key To Continue.")
            journal_list.append(journal_name)
    else:
        print("Directory Does Not Exist! Creating Directory.")
        os.mkdir("journals")
        input("Directory Created Successfully. Re-Run To Create The Journal!")

def display_journals():
    for journal in journal_list:
        print(journal)

def quit_app():
    quit()

while True:
    print("1. Create Journal (creates a folder named 'journals' If Not Present Already.)")
    print("2. Add Journal Entries")
    print("3. Delete Journal / Journal Entries")
    print("4. View Journals")
    print("5. Quit")
    chosen = input(f"Select An Option {cursor} ")

    if (int(chosen) == 1):
        clear_screen()
        journal_name = input(f"What Do You Want To Call Your Journal? {cursor} ")
        create_journal(journal_name)
        pass
    elif(int(chosen) == 2):
        clear_screen()
        pass
    elif(int(chosen) == 3):
        clear_screen()
        pass
    elif(int(chosen) == 4):
        clear_screen()
        display_journals()
    elif(int(chosen) == 5):
        quit_app()
    else:
        clear_screen()
        print("Enter A Valid Option")
        time.sleep(2)
        clear_screen()