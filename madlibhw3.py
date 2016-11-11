# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

import nltk
import random
#nltk.download('punkt')
from nltk.book import *
from nltk import word_tokenize,sent_tokenize

# Copied from sample code
def spaced(word):
    if word in [",", ".", "?", "!", ":"]:
        return word
    else:
        return " " + word

print("\n\nSTART*******\n\n")

print("----------Original text:----------\n\n")

# Isolate first 150 characters
tokens = text2[:150]

# Print original text using spaced
original_text_list = map(lambda word: spaced(word), tokens)
print("".join(original_text_list))

print("\n\n----------Choose Words:----------\n\n")
# 5 Parts of speech: Verb, Adjective, Noun, Plural Noun, Adverb.
parts_of_speech = {"VB" : [0.10, "a Verb", ""], "JJ" : [0.10, "an Adjective", ""], "NN" : [0.15, "a Noun", ""], "NNS" : [0.15, "a Plural Noun", ""], "ADV" : [0.10, "an Adverb", ""]}

# Ask for word of appropriate type
# Loop over all tags and prompt for a word
for tag in parts_of_speech:
    # Store word in dict
    parts_of_speech[tag][2] = input("Please enter " + parts_of_speech[tag][1] + ": ")

print("\n\n")

# Identify parts of speech with nltk
tagged_tokens = nltk.pos_tag(tokens)

# Follow logic from example to change words

# Aggregator list
final_words = []

for (word, tag) in tagged_tokens:
    # If word isn't a replacement part of speech or random chance is greater than limit
    if tag not in parts_of_speech or random.random() > parts_of_speech[tag][0]:
        final_words.append(spaced(word))
    # If word is a replacement and random chance less than or equal to limit
    else:
        final_words.append(spaced(parts_of_speech[tag][2]))

# Print Madlib output
print("----------MadLib text:----------\n\n")
print("".join(final_words))
                           
print("\n\nEND*******")
