# 1) მომხმარებელს შემოატანინეთ რიცხვი და შეამოწმეთ თუ ის არის დადებითი დაბეჭდეთ The number is positive, სხვა შემთხვეაში თუ რიცხვი არის უარყოფითი დაბეჭდეთ The number is negative, ხოლო სხვა შემთხვევაში დაბეჭდეთ The number is zero



number = float(input("შეიყვანეთ რიცხვი: "))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")
