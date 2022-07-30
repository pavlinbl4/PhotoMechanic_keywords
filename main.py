keyword_file = '/Users/evgeniy/Pictures/ExportKeywords_UTF8.TXT'
keyword_file_edit = '/Users/evgeniy/Pictures/ExportKeywords_UTF8_edit.TXT'

with open(keyword_file, 'r') as source_file:
    lines = source_file.readlines()
    print([lines[2]])
    striped_words = [word.strip() for word in lines]
    for x in range(len(lines)):
        words_count = striped_words.count(lines[x].rstrip())
        if lines[x][0].isalpha() and words_count == 1:
            lines[x] = '\t' + lines[x]
            print('\t' + lines[x].rstrip())
        elif lines[x][0].isalpha() and words_count > 1:
            lines[x] = ''
with open(keyword_file_edit, 'w') as edit_file:
    edit_file.writelines(lines)
