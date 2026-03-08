sentence = input("Enter sentence: ")

words = sentence.split()
reversed_words = words[::-1]

print(" ".join(reversed_words))