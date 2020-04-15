"""
 ***************************************************************************
 * passPhrase_single generates a single password term until the output of  *
 * 0 is used to break the program. Simple but effective in greater lengths *
 *                                                                         *
 *                                                                         *
 * developed by Stefan Batricevic                                          *
 * https://github.com/rnbwn                                                *
 ***************************************************************************
"""
import urllib.request
import random

word_url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"

response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()
words = long_txt.splitlines()

upper_words = [word for word in words if word[0].isupper()]
name_words = [word for word in upper_words if not word.isupper()]

print("To exit password generator type '0'")
while True:
    pass_range = int(input("Select word range: "))
    display_pass = " ".join((words[random.randint(0, len(words))] for i in range(pass_range))) + "\n"
    print(display_pass, "\n")

    if pass_range == 0:
        break

