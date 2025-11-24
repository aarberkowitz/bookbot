from stats import *
import sys




def main():

	frankensteins_text = get_book_text(book_path)
	char_dict = character_counter(frankensteins_text)
	sorted = sorter(char_dict)
	print('=' * 12 + " BOOKBOT " + '=' * 12)
	print(f"Analyzing book found at {book_path}...")
	print('-' * 12 + " Word Count " + '-' * 12)
	print(word_counter(frankensteins_text))
	print('-' * 12 + " Character Count " + '-' * 12)
	for item in sorted:
		print(f"{item['char']}: {item['num']}")
	print('=' * 15 + " END " + '=' * 15)


def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def usage_check():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	return False

usage_check()
book_path = sys.argv[1]
main()
