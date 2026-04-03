n = int(input("Введите число: "))
user_lisrt = []
i   =  0 
while i < n:
    string = "Введите элемент списка: "+ str(i+1) + ":"
    user_lisrt.append(input(string))
    i += 1

print(user_lisrt)