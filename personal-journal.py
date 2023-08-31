import os
import time

cursor = ">"

def clear_screen():
    os.system("cls")

def create_journal(journal_name):
    if (os.path.isdir("journals")):
        with open(os.path.join(f"journals/" + journal_name + ".txt"), "a"):
            input(f"Journal With The Name {journal_name} Has Been Created Successfully! Press Any Key To Continue.")
    else:
        print("Directory Does Not Exist! Creating Directory.")
        os.mkdir("journals")
        with open(os.path.join("journals/" + journal_name + ".txt"), "a"):
            input("Directory And Journal Created Successfully.")

def display_journals():
    listNum = 1
    if (os.path.exists("journals")):
        for journal in os.listdir("journals"):
            print(f"{listNum}. {journal}")
            listNum += 1
    else:
        print("Directory Does Not Exist Or There Are No Journals Saved.")
    
    input("\nPress Any Key To Go Back.")

def add_journal_entries(journal_name, journal_entry):
    if (os.path.isdir("journals")):
        if (os.path.exists(f"journals/{journal_name}.txt")):
            with open(f"journals/{journal_name}.txt", "a") as file:
                file.write(journal_entry)
                print("Written Entry Successfully!")
        else:
            print("Not Found")
    else:
        print("Can't Find Any Journals Or The Directory May Be Missing.")
    
    input("\nPress Any Key To continue")


def read_entries(journal_name):
    if (os.path.exists(f"journals/{journal_name}.txt")):
        with open(f"journals/{journal_name}.txt", "r") as file:
            print(f"\n{file.read()}")
    else:
        print("Journal Not Found")
    
    input("\nPress Any Key To continue")

def quit_app():
    quit()

while True:
    clear_screen()
    print("1. Create Journal (creates a folder named 'journals' If Not Present Already.)")
    print("2. Add Journal Entries")
    print("3. Read Entries")
    print("4. Display Journals Saved")
    print("5. Quit")
    chosen = input(f"Select An Option {cursor} ")

    if (int(chosen) == 1):
        clear_screen()
        journal_name = input(f"What Do You Want To Call Your Journal? {cursor} ")
        create_journal(journal_name)
    elif(int(chosen) == 2):
        clear_screen()
        journal_name = input(f"What Journal Do You Want To Write To? {cursor} ")
        journal_entry = input(f"Enter Your Entry Here\n{cursor} ")
        add_journal_entries(journal_name, journal_entry)
    elif(int(chosen) == 3):
        clear_screen()
        journal_To_Read = input(f"Which Journal Do You Want To Read? { cursor} ")
        read_entries(journal_To_Read)
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