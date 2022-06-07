# only remove double words in root

keyword_file = '/Volumes/big4photo/Documents/photo mechanic/2022_06_07_structured_reywords.TXT'
keyword_file_edit = '/Volumes/big4photo/Documents/photo mechanic/2022_06_07_structured_keywords_edit.TXT'

with open(keyword_file, 'r') as work_file:
    all_words = work_file.readlines()
    print(f'lines number {len(all_words)}')
    striped_words = [word.strip() for word in all_words]
    count = 0
    for x in range(len(all_words)):
        words_count = striped_words.count(all_words[x].rstrip())
        if all_words[x][0].isalpha() and words_count > 1:
            print(all_words[x])
            all_words[x] = ''
            count += 1
with open(keyword_file_edit, 'w') as edit_file:
    edit_file.writelines(all_words)
with open(keyword_file_edit, 'r') as check:
    optimized_words = check.readlines()
    print(f'lines in edit file {len(optimized_words)}')
print(f'removed {count} words')
print(count == len(all_words) - len(optimized_words))
