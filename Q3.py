def convert_temperature(temp,scale):
    if scale=='C':
        converted_temp=(9/5)*temp+32
        original_scale="Celsius"
        new_scale="Fahrenheit"
    elif scale=='F':
        conerted_temp=(5/9)*(temp-32)
        original_scale="Fahrenheit"
        new_scale="Celsius"
    else:
        raise ValueError("Invalid scale use C for celsius and F for Fahrenheit")
    return converted_temp
def main():
    temp=float(input("Enter the temperture: "))
    scale=input("Enter the scale C or F: ")
    converted_temp=convert_temperature(temp,scale)
    print(converted_temp)
if __name__ == "__main__":
    main()