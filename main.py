from methods import *
from time import time

sentence = input("\033[38;5;231mType words to check its spelling:\033[0m\n")
words_list = sentence.lower().split()

start = time()

dictionary = get_dictionary()

misspelled_words = get_misspelled(dictionary, words_list)

print_underlined(words_list, misspelled_words)

suggestions = get_suggestions(dictionary, misspelled_words)

print_suggestions(misspelled_words, suggestions)

print(f"\033[38;5;231m\nProgram executed in: {time() - start } sec\033[0m\n")
