def find_max():
    numbers = []
    for i in range(4):
        number = float(input("number: "))
        numbers.append(number)
        
    max_number = max(numbers)
    
    return max_number

print(find_max())