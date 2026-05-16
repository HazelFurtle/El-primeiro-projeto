meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "LEONARDO": "Ser humano deste planeta terra"
            }

word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")

if word in meme_dict.keys():
    print(meme_dict[word])
    # O que devemos fazer se a palavra for encontrada?
    
else:
    print("num existe :(")
    # O que devemos fazer se a palavra não for encontrada?

# :)
