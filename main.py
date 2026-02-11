# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths (e.g., three, four, 
# five, etc.) found within the file.
# Coder: Alfiya Rizvi
# Date: 10-2-26



print("--- Extracting Words from Text File ---")

length = int(input("Enter Length of Words: "))


with open("story.txt", "r") as file:
    text = file.read()


import string

for ch in string.punctuation:
    text = text.replace(ch, " ")

words = text.split()


filtered = [w.lower() for w in words if len(w) == length]

unique_words = sorted(set(filtered))

print(f"\nWords with length {length} are: {unique_words}")

