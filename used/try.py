def get_sequence_pairs_from_string(string):
	output = ''
	for character1 in string:
		for character2 in string:
			if character1 != character2:
				output = output + character1 + character2 + ' '
	return (output[:-1])

def main():
	output = get_sequence_pairs_from_string('abc')
	print(output)

main()
