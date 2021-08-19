import os

os.system(f'cls')
os.system(f'prompt Translator: ')

# Left side for English right side for French
# In the lists feminine is first masculine is second.
glossary = {
"administration": "administration",
"advance": "avance",
"am": "ai",
"and": "et",
"august": "août",
"be": "être",
"business": "enterprise",
"by": "par",
"call": "appelez",
"calisthenics": "gymnastique suédoise",
"diploma": "diplôme",
"end": "finir",
"from": "de",
"graduating": "graduation",
"i": "je",
"in": "au",
"is": "est",
"i'm": "j'ai",
"life": "vie",
"like": "aimer",
"marketing": "commercialisation",
"me": "moi",
"my": ["ma", "mon"],
"m'appelez": "call me",
"name": "nom",
"of": "en",
"old": ["vieille", "vieux"],
"program": "programme",
"programming": "programmation",
"school": "l'école",
"schools": "écoles",
"started": "a débuté",
"studying": "en train d'étudier",
"to": "a",
"the": ["la", "le"],
"this": ["cette", "ce"],
"usually": "d'habitude",
"wake": "réveiller",
"will": "sera",
"with": "avec",
"years": ["années", "ans"],
}

while True:
    mymessage = str(input("Enter your sentence here: "))
    message = mymessage.lower().strip()
    if mymessage == "exit" or mymessage == "":
        break

    else:
        frenchTranslator = message.split(" ")

        list = [ str(l) for l in frenchTranslator ]

        newList = []

        for w in list:
            if "." in w:
                index = w.find(".")
                w = w[:index]
            if "," in w:
                index = w.find(",")
                w = w[:index]
            if ":" in w:
                index = w.find(":")
                w = w[:index]
            if ";" in w:
                index = w.find(";")
                w = w[:index]
            if "!" in w:
                index = w.find("!")
                w = w[:index]
            if "?" in w:
                index = w.find("?")
                w = w[:index]

            newList.append(w)

        frenchTranslator = newList
        print(frenchTranslator)

        frenchText = ""

        for w in frenchTranslator:
            if w in glossary:
                frenchText += f'{glossary[w]} '

            elif w not in glossary:
                frenchText += f'{w.capitalize()} '

        print(frenchText)
