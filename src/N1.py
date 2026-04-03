# for i in range(1, 10):
#     print(i)

# count = 0
# word = "Введите слово!!!:"
# for i in word:
#     if i == "!":
#         count += 1
# print("Exclamation mark found", count)

# i = 5
# while i <= 15:
#     print(i)
#     i += 2

# a = True

# while a:
#     if input("Enter date ") == "exit":
#         a = False

# for i in range(1, 10):
#     if i == 5:
#         break
#     if i % 2 == 0:
#          continue   
#     print(i)

#поиск определенного символа в строке
for i in "hello":
    if i == 'k':
        found = True
        break
else :
    found = False
print(found)