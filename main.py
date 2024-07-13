def main():
     path = "books/frankenstein.txt"
     file_contents = read_file(path)
     total_words = count_words(file_contents)
     print(total_words)
    
def read_file(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(file_contents):
        total_words = len(file_contents.split())
        return total_words
    
main()