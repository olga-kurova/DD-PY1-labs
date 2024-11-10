# TODO Найдите количество книг, которое можно разместить на дискете

# Информационный объем дискеты равен 1,44 Мб
diskette_size = 1.44 * 1024 * 1024

# Количество страниц в книге
pages_per_book = 100

# Число строк на странице
rows_per_page = 50

# Количество символов в строке
chars_per_row = 25

# Для хранения кода одного символа нужно 4 байта
char_size_in_bytes = 4

# Рассчитываем общий объем памяти, необходимый для хранения одной книги
book_size_in_bytes = pages_per_book * rows_per_page * chars_per_row * char_size_in_bytes

# Рассчитываем количество книг, которое можно разместить на дискете
number_of_books = diskette_size / book_size_in_bytes

print("Количество книг, помещающихся на дискету:", int(number_of_books))
