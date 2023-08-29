keyword_file = '/Users/evgeniy/Pictures/ExportKeywords_UTF8.TXT'
keyword_file_edit = '/Users/evgeniy/Pictures/ExportKeywords_UTF8_edit.TXT'


# Открываю исходный каталог ключевых слов
with open(keyword_file, 'r') as source_file:
    lines = source_file.readlines()

    # Удаляю все невидимые символы табуляции переноса из слов
    striped_words = [word.strip() for word in lines]

    # Запускаю цикл по количеству строк в файле
    for x in range(len(lines)):
        #  count the number of occurrences of a specific word in the list of stripped words
        words_count = striped_words.count(lines[x].rstrip())

        # Если в строке находится слово они синоним они категории, то оно начинается с буквы.
        # Если слово начинается с буквы и содержится один раз списке слов то добав табудяцию, записываю его файл
        if lines[x][0].isalpha() and words_count == 1:
            lines[x] = '\t' + lines[x]
            print('\t' + lines[x].rstrip())
    #  Если слово встречается больше чем один раз то в строчку ничего не записывает
        # Странное решение так получается что стираю все двойные слова
        elif lines[x][0].isalpha() and words_count > 1:
            print(f'word {lines[x].strip()} take place {words_count} in file')
            lines[x] = ''
with open(keyword_file_edit, 'w') as edit_file:
    edit_file.writelines(lines)
