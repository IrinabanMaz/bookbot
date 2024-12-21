from string import ascii_lowercase

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    
    count_chars(file_contents)


    print("Report on books/frankenstein.txt: ")
    num_words =count_words(file_contents) 
    print(f"There are {num_words} words in the book. \n")

    counts = count_chars(file_contents)

    for letter in counts:
        print(f"The letter \'{letter}\' appears {counts[letter]} times.")

def count_words( book ):
    return len(book.split())

def count_chars (book):
    
    counting_book = book.lower()


    counts = {}
    for letter in ascii_lowercase:
        counts[letter] = 0


    for char in counting_book:
        if char in counts:
            counts[char] += 1

    return counts
main()