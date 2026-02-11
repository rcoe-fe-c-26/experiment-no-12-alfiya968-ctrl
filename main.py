# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths (e.g., three, four, 
# five, etc.) found within the file.
# Coder: Alfiya Rizvi
# Date: 10-2-26



import string

length = int(input())

with open("story.txt", "r") as file:
    text = file.read()

for ch in string.punctuation:
    text = text.replace(ch, " ")

words = text.split()

result = sorted(set(w.lower() for w in words if len(w) == length))

print(f"Words with length {length} are: {result}")
