
def parse_input(user_input): # Function to parse user input
    number = user_input.split()
    user_number = 0
    if number[0].isnumeric():
        user_number = int(number[0])
    elif number[0] == "exit":
        user_number = "exit"
    else:
        user_number = "Is not a number, please try again"
    return user_number


def caching_fibonacci(user_number):  # Function to calculate fibonacci numbers
    n = user_number
    cache = {}    
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return n
        elif n in cache:
            return cache[n]
        cache[n] = fibonacci(n-1) + fibonacci(n-2)        
        return cache[n] 
    fibonacci(n)
    if user_number <= 0:
        fib_nums = 0
    elif user_number == 1:
        fib_nums = 1
    else:
        fib_nums = cache[user_number]
    return fib_nums # Return the result of the fibonacci function
        
def main(): # Main function
   print("Welcome to the fibonnaaci calculator. Tipe 'exit' to quit the program!")
   while True:
        user_input = input(f"Please input integer number:").strip().lower() # Input command from user
        user_number = parse_input(user_input)
        if user_number == "Is not a number, please try again": # Check if the input is a number
            print(user_number)
        elif user_number == "exit": # Check if the input is exit
            print("Goodbye!")
            break       
        else: # If the input is a number, call the caching_fibonacci function
            print(caching_fibonacci(user_number))
        
if __name__ == "__main__":
    main() # Call main function
