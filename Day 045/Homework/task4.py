# 4) შექმენი ფუნქცია, რომელიც მომხმარებელს შემოატანინებს 5 სახელს შექმნის ამ სახელებისგან სიას და დააბრუნებს საბოლოოდ ამ სიას



def get_names():
    names = []   
    for i in range(5):
        name = input(f"შეიყვანეთ {i+1}-ე სახელი: ")
        names.append(name)  
    return names

name_list = get_names()
print(name_list)
