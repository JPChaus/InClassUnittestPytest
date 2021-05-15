def main():
    word = input(("Enter a string, any string: "))
    palindrome(word);

def palindrome(word):
    if(word == word[::-1]):
        print("Given string is a palindrome!")
    else:
        print("Given string is not a palindrome.")

if __name__ == '__main__':
    main()