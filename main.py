stringg = input("Введите строку, которую нужно развернуть: ")  # Запрашиваем строку, которую нужно развернуть
splited = stringg[::-1].split()[::-1]  # Разворачиваем строку
stringg = "Вот ваша развернутая строка:"  # Создаем конструктор
for i in splited:  # Для каждого слова в развернутой строке
    stringg += " " + i  # Добавляем к конструктору
print(stringg)  # Выводим получившееся из конструктора сообщение
