def word_counter(text_of_book):
	num_words = len(text_of_book.split())
	return print(f"Found {num_words} total words")

def character_counter(text):
	characters = {}

	text = text.lower()
	for letter in text:
		if letter not in characters:
			characters[letter] = 1
		else:
			characters[letter] += 1
	return characters
