# 2) მომხმარებელს შეაყვანინე ნებისმიერი რიცხვი N. გამოიყენე for ციკლი და დაბეჭდე 1-დან N-მდე არსებული ყველა მარტივი რიცხვი (prime numbers).


N = int(input("შეიყვანეთ ნებისმიერი რიცხვი N: "))


for num in range(2, N+1):       
    is_prime = True
    for i in range(2, int(num**0.5) + 1):            
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
