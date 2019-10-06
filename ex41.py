# oop_test.py
import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):" :
        "Make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef __init__(self, ***)" :
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()" :
        "Set *** to an instance of class %%%.",
    "***.***(@@@)" :
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'" :
        "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == 'english':
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    # print(word), then get the list printed
    # but the each line is like b'account\n'
    # meaning they are of bytes type
    # then I have to convert/encode them to str type
    WORDS.append(str(word.strip(), encoding="utf-8"))
    # .strip() will clear each '\n' at the end of each line
    # yes, .strip() can work on 'bytes' type
    # then using utf-8 to encode the bytes to string
    # then append those strings (many words) one by one to a list

def convert(snippet, phrase): # (key, value) of a dict
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    # a concise way of saying the following 3 lines:
    # class_names = []
    # for w in random.samples(...):
        # class_names.append(w.capitalize())

    # random.sample() means use the .sample() in random module
    # .sample(population, k) means to return a list of k unique elements selected
    # from population
    # in this case, it return .count() words from WORDS without
    # changing the original WORDS list
    # a simple exampel of .smaple():
    # [Input]>>>> random.sample(range(1000), 10)
    # [Output]>>>> [945, 941, 508, 827, 109, 847, 182, 247, 233, 805]

    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        # return random ints between 1-3 (end included)
        param_count = random.randint(1, 3)

        # choose x (1<=x<=3) words from WORDS and join them into a string
        # say x = 3, the string might be 'word1, word2, word3'
        # then append this string to the list param_names
        # repeat this for range(0, ...) times
        param_names.append(', '.join(
            random.sample(WORDS, param_count)
        ))

    for sentence in snippet, phrase:
        result = sentence[:]
        # copy the entire lists of keys and values

        # fake class class names
        for word in class_names:
            result = result.replace("@@@", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets) # just shuffle the list snippets

        for snippet in snippets:
            phrase = PHRASES[snippet] #phrase can be any value extracted by its correspongding key
            question, answer = convert(snippet, phrase)
            if PHRASES_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
