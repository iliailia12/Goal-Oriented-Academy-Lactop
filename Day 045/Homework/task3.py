# 3) 50-დან 150-მდე ყველა რიცხვზე გააკეთე ციკლი და ცალცალკე დაითვალე ლუწი და კენტი რიცხვების ჯამი. ბოლოს დაბეჭდე ორივე ჯამი.





even_sum = 0
odd_sum = 0

for number in range(50, 151):
    if number % 2 == 0:
        even_sum += number   
    else:
        odd_sum += number    