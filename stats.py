def word_counter(text_of_book):
	num_words = len(text_of_book.split())
	return f"Found {num_words} total words"

def character_counter(text):
	counts = {}
	characters = []

	text = text.lower()
	for letter in text:
		if letter not in counts:
			counts[letter] = 1
		else:
			counts[letter] += 1
	for letter, num in counts.items():
		if letter.isalpha():
			characters.append({
				"char": letter,
				"num": num
				})
	return characters

def sort_on(items):
	return items["num"]

def sorter(items):
	items.sort(reverse=True, key=sort_on)
	return items
