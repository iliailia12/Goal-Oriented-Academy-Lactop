# 6) გაიმეორეთ for და while ციკლები, უყურეთ 20 გაკვეთილის ჩანაწერს და გააკეთეთ მათზე 3-3 მაგალითები


# 1 for ციკლების მაგალითები



# 1) 
fruits = ["ვაშლი", "ბანანი", "მანგო"]
for fruit in fruits:
    print( fruit)

# 2)
for i in range(1, 6):
    print(i, "x 2 =", i*2)

# 3)
names = ["ანა", "გიორგი", "ნიკა"]
for index, name in enumerate(names):
    print("ინდექსი:", index, "სახელი:", name)





# 2️  while ციკლების მაგალითები

# 1)  
i = 1
while i <= 5:
    print(i)
    i += 1

# 2) ს 
letters = ["ა", "ბ", "გ", "დ"]
index = 0
while index < len(letters):
    print( letters[index])
    index += 1

# 3)  
number = 0
while True:
    number += 3
    print( number)
    if number >= 15:
        break