import wikipedia

def get_wiki_summary():
    query = input("Question: ")
    print (wikipedia.summary(query))

def get_short_summary():
    query = input("Question: ")
    print (wikipedia.summary(query, sentences = 2))

def get_localised_summary():
    query = input("Question: ")
    lang = input("Language code: ")
    if (lang.isspace()):
        lang = "en" 
        # Change to "es" for Spanish
    wikipedia.set_lang(lang)
    print(wikipedia.summary(query, sentences = 3))

# get_wiki_summary()
# get_short_summary()
get_localised_summary()
