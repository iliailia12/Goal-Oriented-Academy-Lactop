# 8) მომხმარებელს ისევ შემოატანინეთ რიცხვი და მე-7 დავალებაში მიღებული სიის თავში ჩაამატეთ ეს რიცხვი აყვანილი მე-3 ხარისხში


numbers = []

for i in range(5):
    num = int(input(f"შეიყვანეთ {i+1}-ე რიცხვი: "))
    numbers.append(num)

new_num = int(input("შეიყვანეთ კიდევ ერთი რიცხვი: "))

cubed_num = new_num ** 3

numbers.insert(0, cubed_num)

print(numbers)
