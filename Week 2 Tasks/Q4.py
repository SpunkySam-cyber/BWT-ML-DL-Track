def find_max_min(numbers_list):
    if not numbers_list:
        raise ValueError("The list cannot be empty")
    
    max_num = min_num = numbers_list[0]
    
    for num in numbers_list:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    
    return max_num, min_num

def main():
    numbers = []
    for i in range(5):
        number = float(input(f"Enter number {i+1}: "))
        numbers.append(number)
    

        max_number, min_number = find_max_min(numbers)
        print(f"The maximum number is: {max_number}")
        print(f"The minimum number is: {min_number}")
    

if __name__ == "__main__":
    main()
