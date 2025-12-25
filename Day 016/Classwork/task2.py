# 2) შექმენით პროგრამა, რომელიც მომხმარებელს შემოატანინებს პაროლს და შეამოწმებს თუ ის არის "1234"-ის ტოლი მაშინ დაბეჭდავთ "Password is correct", სხვა შემთხვევაში "Password is incorrect"




password = input("გთხოვთ, შეიყვანოთ პაროლი: ")

if password == "1234":
    print("Password is correct")
else:
    print("Password is incorrect")
