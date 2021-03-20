from googletrans import Translator
from wonderwords import RandomSentence
import random
translator = Translator()
#s = RandomSentence()

x, y, z = 'es', 'en', 'fr'
default_language = y
selected_translation = x

first_sen, second_sen, third_sen = RandomSentence(), RandomSentence(), RandomSentence()

sample_database = [first_sen.sentence().replace('.', ''), second_sen.sentence().replace('.', ''), third_sen.sentence().replace('.', '')]
#sample_database = ["first sentence random", "another sentence that may work", "i hope this works"]

def trans_select_language(target, baseLanguage, destLanguage):
    translated_sentence = translator.translate(target, src=baseLanguage, dest=destLanguage)
    return translated_sentence.text

def word_selection():
    selection = random.choice(sample_database)
    translated_selection = trans_select_language(selection, default_language, selected_translation)
    print("Today's sentence is |{}|, that translates |{}| ".format(selection, translated_selection))
    #this for loop iterates through the phrase to desglose each word of it, and gives you the translation
    for word in selection.split():
        translated_selection = translator.translate(word, dest=selected_translation)
        print("the word |{}| translates as : |{}| ".format(word, translated_selection.text))

    second_selection = trans_select_language(random.choice(sample_database), default_language, selected_translation)

    print("Another sentence is: \n".format(default_language))
    print(second_selection)

    user_selection = input("Can you translate this sentence? (y/n) \n").lower()
    translated_selection = translator.translate(second_selection, dest=default_language)
    translated_selection = translated_selection.text

    if user_selection == "y":
        user_translation = input("What would be the translation in |{}| ?\n".format(default_language)).lower()
        if user_translation.lower() == translated_selection.lower():
            print("Correct! Your translation is perfect. ")
        else:
            print("Translation would be : \n")
            print(translated_selection)
            print(analyze_sentence(user_translation.lower(), translated_selection.lower()))
    else:
        print("Vale, la traduccion seria: \n")
        print(translated_selection)
        exit()

def analyze_sentence(sentence, wantedLook):
    c = len(wantedLook.split())
    t = 0
    for word in sentence.split():
        for secondword in wantedLook.split():
            if word == secondword and t < c:
                t += 1

    result = "Your translation was {} % correct".format((t/c) * 100)
    return result


word_selection()
