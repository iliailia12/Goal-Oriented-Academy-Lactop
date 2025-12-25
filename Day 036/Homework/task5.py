# 3) შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია და პასუხად აბრუნებს თითოეული რიცხვის ნამრავლს. გამოიძახეთ ეს ფუნქცია, გადაეცით მას სასურველი სია და ჩასვით ის print-ში.



def multiply_list(numbers):
    result = 1   
    for num in numbers:
        result *= num   
    return result

numbers = [2, 3, 4]

print(multiply_list(numbers))
