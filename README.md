# SimplyPyTranslator
Simple Translator in Python using functions from wonderwords and googletranslate

This script requires the following modules:
-wonderwords
-googletranslate

Install using: 
  pip install wonderwords
  pip install googletranslate
  
  
The script contains the following editable variables "x", "y", "z" as language selection
the variable default_language is the language where we are going to receive the original sentences, while the selected_translation variable is the target language where we want that sentence to be translated into. 

Description of the script:

After receiving the first translated sentence, we receive a breakdown of each word of the sentence (while they may be out of context, and the translation could be a synonim), and finally as a practice excercise the script is going to ask the user if he wants to translate another given word and will return the percentage of accuracy of the translation (In a literal way)

