""" def reverse_list(numbers):
    return numbers[::-1]

sonuc = reverse_list([1, 2, 3, 4])
print(sonuc) 

 """
 
"""  
 
def find_duplicates(numbers):
    duplicates = []
    for number in numbers:
        if numbers.count(number) > 1 and number not in duplicates:
            duplicates.append(number)
    return duplicates

sonuc = find_duplicates([1, 2, 3, 2, 4, 3, 5, 1])
print(sonuc)  
 """
 
""" def return_fixed_value():
    return 10

sonuc = return_fixed_value()
print(sonuc)  # Beklenen çıktı: 10
 """