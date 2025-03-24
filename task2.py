
def generator_numbers(text: str):
    for i in text:
        if i.isdigit():
            yield int(i)

def generator_letters(text: str):
    for i in text:
        if i.isalpha():
            yield i

def generator_punctuation(text: str):
    for i in text:
        if not i.isalnum():
            yield i 

def main():
    text = "Hello 123 World!"
    numbers = generator_numbers(text)
    letters = generator_letters(text)
    punctuation = generator_punctuation(text)   
    print(list(numbers))
    print(list(letters))
    print(list(punctuation))

if __name__ == "__main__":
    main()