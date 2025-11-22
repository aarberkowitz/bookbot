from stats import *

def main():
	frankensteins_text = get_book_text("books/frankenstein.txt")
	word_counter(frankensteins_text)
	char_dict = character_counter(frankensteins_text)
	print(char_dict)

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

main()
