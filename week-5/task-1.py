import string

file = open("text.txt", "r", encoding="utf-8")
text = file.read().lower()
file.close()

for symbol in string.punctuation:
    text = text.replace(symbol, "")

lines = text.split("\n")
words = text.split()

freq = {}

for w in words:
    if w not in freq:
        freq[w] = 1
    else:
        freq[w] += 1

result = open("analysis.txt", "w", encoding="utf-8")
result.write("Lines: " + str(len(lines)) + "\n")
result.write("Words: " + str(len(words)) + "\n")
result.write("Word frequency:\n")

for w in freq:
    result.write(w + ": " + str(freq[w]) + "\n")

result.close()
