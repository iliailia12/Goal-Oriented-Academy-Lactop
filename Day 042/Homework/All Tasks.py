# 1) დაწერე ფუნქცია სახელად `add_numbers`, რომელსაც გადაეცემა ორი რიცხვი.
# ფუნქციამ უნდა დააბრუნოს ამ ორი რიცხვის ჯამი.

# 2) დაწერე ფუნქცია სახელად `average`, რომელსაც გადაეცემა სამი რიცხვი.
# დააბრუნე ამ სამი რიცხვის საშუალო არითმეტიკული.

# 3) დაწერე ფუნქცია სახელად `max_number`, რომელსაც გადაეცემა ორი რიცხვი.
# დააბრუნე უდიდესი რიცხვი.

# 4) დაწერე ფუნქცია სახელად `even_or_odd`, რომელსაც გადაეცემა ერთი რიცხვი.
# თუ რიცხვი ლუწია, დააბრუნე `"ლუწი"`, თუ კენტია — `"კენტი"`.

# 5) დაწერე ფუნქცია სახელად `sum_list`, რომელსაც გადაეცემა სია რიცხვებით.
# ფუნქციამ უნდა დააბრუნოს სიაში არსებული რიცხვების ჯამი.

# 6) დაწერე ფუნქცია სახელად `filter_even`, რომელსაც გადაეცემა სია რიცხვებით.
# დააბრუნე ახალი სია, რომელშიც მხოლოდ ლუწი რიცხვები იქნება.

# 7) დაწერე ფუნქცია სახელად `word_length`, რომელსაც გადაეცემა ერთი სიტყვა (სტრინგი).
# დააბრუნე ამ სიტყვის სიგრძე (რამდენი ასოა მასში).

# 8) დაწერე ფუნქცია სახელად `longest_word`, რომელსაც გადაეცემა სია სიტყვებით.
# დააბრუნე ყველაზე გრძელი სიტყვა ამ სიიდან.

# 9) დაწერე ფუნქცია სახელად `square`, რომელსაც გადაეცემა ერთი რიცხვი.
# დააბრუნე ამ რიცხვის კვადრატი.                                                                                                                                                                                                                                                                                                                                                                                                           


# 1
def add_numbers(a, b):
    return a + b

# 2
def average(a, b, c):
    return (a + b + c) / 3

# 3
def max_number(a, b):
    if a > b:
        return a
    else:
        return b

# 4
def even_or_odd(n):
    if n % 2 == 0:
        return "ლუწი"
    else:
        return "კენტი"

# 5
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# 6
def filter_even(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# 7
def word_length(word):
    return len(word)

# 8
def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# 9
def square(n):
    return n ** 2


# პრინტი

# მაგალითები ფუნქციების გამოყენებისთვის

# 1
result1 = add_numbers(5, 7)
print(result1)   

# 2
result2 = average(3, 6, 9)
print(result2)   

# 3
result3 = max_number(10, 20)
print(result3)   

# 4
result4 = even_or_odd(7)
print(result4)   

# 5
numbers_list = [1, 2, 3, 4, 5]
result5 = sum_list(numbers_list)
print(result5)   

# 6
result6 = filter_even(numbers_list)
print(result6)   

# 7
result7 = word_length("გამარჯობა")
print(result7)   

# 8
words_list = ["კომპიუტერი", "პროგრამირება", "კოდი"]
result8 = longest_word(words_list)
print(result8)   

# 9
result9 = square(8)
print(result9)   
