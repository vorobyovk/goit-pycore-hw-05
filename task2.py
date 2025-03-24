
def generator_numbers(text:str): # define generator number function
    args = text.split(' ')
    print(args)
    numbers = [] 
    for word in args:    
        if is_digit(word) == True:             
            numbers.append(word)
    return numbers

def is_digit(string): # define function for check word is digit or not 
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

def sum_profit(text: str, func: str): # define function for sum profit
    summ = 0
    nums = func(text)
    for num in nums:
        summ += float(num)
    return summ    

def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів." # string for check 
    total_income = sum_profit(text, generator_numbers) # call the function
    print(f"Загальний дохід: {total_income}") # print result
    

if __name__ == "__main__":
    main()