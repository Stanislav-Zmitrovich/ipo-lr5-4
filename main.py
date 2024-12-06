# Запрашиваем у пользователя строку
input_string = input("Введите строку: ")

# Инициализируем переменную для хранения результата
reversed_string = ""

# Переменная для отслеживания текущего слова
current_word = ""

# Проходим по каждому символу в строке
for char in input_string:
    # Если символ не пробел, добавляем его к текущему слову
    if char != " ":
        current_word = char + current_word
    else:
        # Если символ пробел, добавляем развернутое слово к результату
        reversed_string += current_word + " "
        current_word = ""

# Добавляем последнее слово (если есть) после выхода из цикла
reversed_string += current_word

# Выводим результат
print("Строка с развернутыми словами:", reversed_string)
