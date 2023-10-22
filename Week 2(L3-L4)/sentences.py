import random

def main():
    sentence = make_sentence(quantity=1, tense='past')
    sentences = make_sentence(quantity=1, tense='present')
    sentencess = make_sentence(quantity=1, tense='future')
    sentencesss = make_sentence(quantity=0, tense='past')
    sentencessss = make_sentence(quantity=0, tense='present')
    sentencesssss = make_sentence(quantity=0, tense='future')

    
    print(sentence.capitalize())
    print(sentences.capitalize())
    print(sentencess.capitalize())
    print(sentencesss.capitalize())
    print(sentencessss.capitalize())
    print(sentencesssss.capitalize())

def get_determiner(quantity):
    if quantity == 1:
        determiners = ["a", "one", "the"]
    else:
        determiners = ["some", "many", "the"]
    determiner = random.choice(determiners)
    return determiner

def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women"]
    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                 "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think",
                 "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]
    verb = random.choice(verbs)
    return verb

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    sentence = "{} {} {}".format(determiner, noun, verb)
    return sentence

main()