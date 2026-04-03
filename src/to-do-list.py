tasks = []
while True:
    print("--------------------------------")
    print("To-Do List Menu:")
    print("--------------------------------")
    print("1.Добавить элемент в список")
    print("2.Вывести список")
    print("3.Отметить как выполненая")
    print("4.Удалить задачу")
    print("5.Отметить как невыполненая")
    print("6.Выход")
    print("--------------------------------")
    choice = input("Выберите пункт меню:")
    if  choice == "1":
        task = input("Введите задачу: ")
        tasks.append({'Задача':task,'Статус':False})
    elif choice == "2":
        for i, task in enumerate(tasks):
            status = "✅" if task["Статус"] else "❌"
            print(f"{i+1}. {task['Задача']} {status}")
            input("Нажмите Enter чтобы продолжить...")
        if not tasks:
            print("Список задач пуст")
            input("Нажмите Enter чтобы продолжить...")
    elif choice == "3":
        index = int(input("Введите номер задачи для отметки как выполненая: ")) -1
        if 0 <= index < len(tasks):
            tasks[index]["Статус"] = True
            if not tasks:
                print("Список задач пуст")
            input("Нажмите Enter чтобы продолжить...")
        else:
            print("Неверный номер задачи! Попробуйте снова")
    elif choice == "4":
        index = int(input("Введите номер задачи для удаления:"))
        if 0 <= index < len(tasks):
            del tasks[index]
        else:
            print("Неверный номер задачи! Попробуйте снова")
    elif choice == "5":
        
        index = int(input("Введите номер задачи для отметки как невыполненая: ")) -1
        if not tasks:
            print("Список задач пуст")
            input("Нажмите Enter чтобы продолжить...")
        elif 0 <= index < len(tasks):
            tasks[index]["Статус"] = False
        else:
            print("Неверный номер задачи! Попробуйте снова")
    elif choice == "6":
        break
    else:
        print("Выбран неизвестный пункт меню! Попробуйте снова")