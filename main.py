def main():
     path = "books/frankenstein.txt"
     file_contents = read_file(path)
     total_words = count_words(file_contents)
     letters = letter_count(file_contents)
     sorted_list = dict_to_list(letters)
     
     print(f"--- Begin report of {path} ---")
     print(f"{total_words} words found in the document")
     print()

     for letter in sorted_list:
         if not letter["letter"].isalpha():
             continue
         print(f"The '{letter['letter']}' character appears {letter['count']} times")
         
     print()
     print("--- End report ---")

    
def read_file(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(file_contents):
        total_words = len(file_contents.split())
        return total_words

def letter_count(file_contents):
     letters = {}
     lower_case = file_contents.lower()
     for letter in lower_case:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
     return letters

def sort_on(dictionary):
    return dictionary["count"]

def dict_to_list(nums_char_dict):
     sorted_list = []
     for letter, count in nums_char_dict.items():
        sorted_list.append({"letter": letter, "count": count})
     sorted_list.sort(key=sort_on, reverse=True)
     return sorted_list

main()