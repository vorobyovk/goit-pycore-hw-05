

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, CONTACTS): # Add contact by name
    if len(args) > 2:
        return f"Too many arguments {args}"
    if len(args) == 2:
        name, phone = args
    else:
        if len(args) == 1:
            name = args[0]
            phone = input("Please input phone: ").strip().lower()
        else:
            name = input("Please input name: ").strip().lower() 
            phone = input("Please input phone: ").strip().lower()
    print(f"Added Name: {name}, Phone: {phone}")    
    CONTACTS[name] = phone
    return "Contact added."
    
    
def change_contact(args, CONTACTS):   # Change contact by name
    if len(args) > 2:
        return f"Too many arguments {args}"
    if len(args) == 2:
        name, phone = args
    else: 
        if len(args) == 1:
            name = args[0]
            phone = input("Please input phone: ").strip().lower()
        else:
            print(len(args))   
            name = input("Please input name: ").strip().lower() 
            phone = input("Please input phone: ").strip().lower()
    if name in CONTACTS:
        CONTACTS[name] = phone
    else:
        print(f"Contact {name} not found")  

def get_contact(args, CONTACTS):  # Get contact by name
    if len(args) == 1:        
        name = args[0]
    else: 
        name = input("Please input name: ").strip().lower()    
    if name in CONTACTS:
        return f"Phone: {CONTACTS[name]}"
    else:
        return f"Contact {name} not found"  

def all(CONTACTS): # Get all contacts
    print(CONTACTS)

def main(): # Main function
   CONTACTS = {}
   print("Welcome to the assistant bot!\nYou can use command hello, add, change, phone, all or exit/close")
   while True:
        user_input = input(f"Please input command:").strip().lower() # Input command from user
        command, *args = parse_input(user_input)
        if command == "hello": 
            print("How can I help you?\n You can use command hello, add, change, phone, all or exit/close")
        elif command == "add":
            add_contact(args, CONTACTS)
        elif command == "change":
            change_contact(args, CONTACTS)
        elif command == "phone":
            print(get_contact(args, CONTACTS))
        elif command == "all":
            all(CONTACTS)
        elif command == "exit" or user_input == "close":
            print(f"Goodbye!")
            break 
        else:
            print("Command not found! Please try again")

if __name__ == "__main__":
    main() # Call main function