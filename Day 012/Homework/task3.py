# 4) გადახედეთ რესურსებში მოცემულ მაგალითებს ლოგიკურ ოპერატორებზე და გააკეთეთ 5 , სადაც გამოიყენებთ შედარების და ლოგიკურ ოპერატორებს



age = 20
if age >= 18 and age <= 65:
    print("ასაკი მუშაობისთვის მისაღებია")


temperature = 30
if temperature > 28 or temperature < 5:
    print("ტემპერატურა კრიტიკულია")


is_raining = False
if not is_raining:
    print("სეირნობა შეიძლება")


username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("ავტორიზაცია წარმატებულია")


score = 87
if score >= 90:
    print("შედეგი: შესანიშნავი")
elif score >= 75 and score < 90:
    print("შედეგი: კარგი")
else:
    print("შედეგი: დასამუშავებელია")
