
def get_book_text(filepath):
    with open(filepath) as f:
        return(f.read())
def main(filepath):
    get_book_text(filepath)

#main("books/frankenstein.txt")
text_book = get_book_text("books/frankenstein.txt")

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
from stats import get_num_words
get_num_words(text_book)
print("--------- Character Count -------")
from stats import get_num_char
char_counts = get_num_char(text_book)
#print(f"Total 't' count: {char_counts.get('t', 0)}")
#for char, count in char_counts.items():
    #print(f"'{char}': {count}")

from stats import list_book

characters = list_book(char_counts)
for char in characters:
    if char[0].isalpha():
        print(f'{char[0]}: {char[1]}')
print("============= END ===============")
#t_positions = []
#for i, char in enumerate(text_book.lower()):
    #if char == 't':
        #t_positions.append(i)
        
#print(f"Number of 't's found directly: {len(t_positions)}")

#counts = get_num_char(text_book)
#for char, count in counts.items():
    #print(f"{repr(char)}: {count}")
#counts = get_num_char(text_book)
#print(f"Count for 't': {counts.get('t')}")