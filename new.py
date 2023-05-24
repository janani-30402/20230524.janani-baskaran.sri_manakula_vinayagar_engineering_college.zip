import csv
import time
import psutil

def replace_words(base_text, device_values):
    for key, val in device_values.items():
        base_text = base_text.replace(key, val)
    return base_text


with open('t8.shakespeare.txt', 'r') as f:
    input_text = f.read()


with open('find_words.txt', 'r') as f:
    find_words_list = [line.strip() for line in f.readlines()]


with open('french_dictionary.csv', 'r') as f:
    reader = csv.reader(f)
    french_dict = {rows[0]: rows[1] for rows in reader}

replaced_words = set()
num_replacements = {}
for word in find_words_list:
    if word in french_dict:
        replaced_words.add(word)
        if word in num_replacements:
            num_replacements[word] += 1
        else:
            num_replacements[word] = 1
        input_text = input_text.replace(word, french_dict[word])

with open('output.txt', 'w') as f:
    f.write(input_text)

print("Unique list of words that was replaced with French words from the dictionary:")
print(replaced_words)

print("Number of times a word was replaced:")
print(num_replacements)

print("Time taken to process:")
print(time.process_time())

print("Memory taken to process:")
print(psutil.Process().memory_info().rss)