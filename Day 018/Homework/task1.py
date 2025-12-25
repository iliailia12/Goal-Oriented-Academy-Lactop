# )მომხმარებელს შემოატანინეთ ორი რიცხვი,შეამოწმეთ თუ პირველი რიცხვი მეტია მეორე რიცხვზე დაპრინტე რომ ‘first is more than second’,ასევე შეამოწმე თუ პირველი რიცხვი ნაკლებია მეორე 
# რიცხვზე დაპრინტე რომ ‘first is less than second’ და სხვა დანარჩენ შემთხვევაში დაპტინტე რომ ‘first number equal to second number’



first = float(input("შეიყვანეთ პირველი რიცხვი: "))
second = float(input("შეიყვანეთ მეორე რიცხვი: "))

# 
if first > second:
    print("first is more than second")
elif first < second:
    print("first is less than second")
else:
    print("first number equal to second number")
