def check_even_or_odd(number):
    if number%2==0:
        print("The number is even")
    else:
        print("The number is odd")

def main():
    number=int(input(" Enter number to check: "))
    check_even_or_odd(number)
    
if __name__ == "__main__":
    main()