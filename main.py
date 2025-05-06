
def get_book_text(filepath):
    with open(filepath) as f:
        return(f.read())
def main(filepath):
    get_book_text(filepath)

#main("books/frankenstein.txt")
text_book = get_book_text("books/frankenstein.txt")


def word_count(text_book):
    num_words = len(text_book.split())
    print(f"{num_words} words found in the document")

word_count(text_book)