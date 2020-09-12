import os
import csv
import re

# Define file to analyse
selection = 'paragraph_3.txt'

text_path = os.path.join("Resources", selection)
output_file = os.path.join("analysis", "output.txt")

def load_file(text_path):
    with open(text_path, 'r') as text_file:
        return text_file.read()

# Define emply list for character counts
char_count = []

# -------------------------------------------------------- 
# Incrementally split paragraph into sentences and then words
para = load_file(text_path)
sentences = re.split("(?<=[.!?]) +", para)
words = re.split(' ', para)

# Remove extra commas from sentences and counting the number of
# characters in a word
for word in words:
    if ',' in word:
        word = re.sub('[,]', '', word)
        char_count.append(len(word))
    else:
        char_count.append(len(word))

    # To match the example, comment out if code and use code below:
    # char_count.append(len(word))

# -------------------------------------------------------- 
# Output file
file = open(output_file, "w") 
file.write("Paragraph Analysis")
file.write("\n----------------------------")
file.write("\nApproximate Word Count: " + str(len(words)))
file.write("\nApproximate Sentence Count: " + str(len(sentences)))
file.write("\nAverage Letter Count: " + str(round(sum(char_count)/len(char_count), 1)))
file.write("\nAverage Sentence Count: " + str(round(len(words)/len(sentences), 1)))