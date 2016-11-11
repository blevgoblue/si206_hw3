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
# 5 Parts of speech: Verb, Adjective, Noun, Plural Noun, Adverb

# Ask for word of appropriate type

# Follow logic from example to change words


# Print Madlib output

print("\n\nEND*******")
