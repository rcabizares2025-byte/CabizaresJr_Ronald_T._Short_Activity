sentence = input("Enter a sentence: ")

print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())

print("Number of 'a's:", sentence.count("a")) #Can change the letter

if sentence.startswith("Hello"):
    print("The sentence starts with 'Hello'")
else:
    print("The sentence does not start with 'Hello'")

words = sentence.split()

print("Words in the sentence:")
for word in words:
    print(word)
