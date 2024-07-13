def main():
     path = "books/frankenstein.txt"
     file_contents = read_file(path)
     total_words = count_words(file_contents)
     letters = letter_count(file_contents)
     print(letters)
    
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
    
main()