
def get_book_text(filepath):
    with open(filepath) as f:
        return(f.read())
def main(filepath):
    get_book_text(filepath)

#main("books/frankenstein.txt")
text_book = get_book_text("books/frankenstein.txt")



get_num_words(text_book)