def get_num_words(text_book):
    num_words = len(text_book.split())
    print(f"{num_words} words found in the document")

def get_num_char(text_book):
    text_lower = text_book.lower()  # Convert text to lowercase for uniform counting
    char_counts = {}   # Dictionary to hold character counts
   
    # Debug print: Show a small part of the text to ensure it's correctly converted
    #print(f"First 100 characters (lowercase): {repr(text_lower[:100])}")
   
    for char in text_lower:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

