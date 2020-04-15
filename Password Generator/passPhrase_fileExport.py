"""
 ***************************************************************************
 * passPhrase Generator is a simple word phrase generator that stores 150k *
 * passwords generated. Simple but can be developed into much more such    *
 * as; adding a password strength checker or even amount to generate/save  *
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

passFile = open("password.txt", "w+")

for p1 in range(50000):
    passPhrase1 = " ".join((words[random.randint(0, len(words))] for i in range(1))) + "\n"
    passFile.writelines(passPhrase1)

for p2 in range(40000):
    passPhrase2 = " ".join((words[random.randint(0, len(words))] for i in range(2))) + "\n"
    passFile.writelines(passPhrase2)

for p3 in range(30000):
    passPhrase3 = " ".join((words[random.randint(0, len(words))] for i in range(3))) + "\n"
    passFile.writelines(passPhrase3)

for p4 in range(20000):
    passPhrase4 = " ".join((words[random.randint(0, len(words))] for i in range(4))) + "\n"
    passFile.writelines(passPhrase4)

for p5 in range(10000):
    passPhrase5 = " ".join((words[random.randint(0, len(words))] for i in range(5))) + "\n"
    passFile.writelines(passPhrase5)

passFile.close()
