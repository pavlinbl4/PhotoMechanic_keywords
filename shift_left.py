keyword_file_edit = '/Users/evgeniy/Pictures/ExportKeywords_UTF8_edit.TXT'

with open(keyword_file_edit,'r') as work_file:
    words = work_file.readlines()
    print([words[1]])
    for x in range(1,8):
        print(words[x].lstrip('').rstrip())