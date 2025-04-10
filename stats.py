def count_words(book_text):
    wordcount = len(book_text.split())

    return wordcount

def count_characters(book_text):
    unique_chars_set = set(book_text.lower())

    unique_chars_dict = {}

    for char in unique_chars_set:
        count = 0

        for i in range(0, len(book_text)):
            if book_text[i].lower() == char:
                count += 1
        
        unique_chars_dict[char] = count
    
    return unique_chars_dict

def book_report(wordcount, unique_chars_dict):
    sorted_list_dict = []

    for char in unique_chars_dict:
        if char.isalpha():
            sorted_list_dict.append((char, unique_chars_dict[char]))

    sorted_list_dict.sort(key=lambda x: x[1], reverse=True)
    
    for item in sorted_list_dict:
        print(f"{item[0]}: {item[1]}")