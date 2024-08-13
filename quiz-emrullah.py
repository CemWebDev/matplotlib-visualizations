def calculate_average_with_input():
    grades = []
    for i in range(4):
        grade = float(input(f"{i+1}. ders notunu girin: "))
        grades.append(grade)
    
    average = sum(grades) / len(grades)
    
    if average >= 85:
        return "Başarılı"
    elif average >= 70:
        return "Geçti"
    elif average >= 50:
        return "Şartlı Geçti"
    else:
        return "Başarısız"


sonuc = calculate_average_with_input()
print(sonuc)
