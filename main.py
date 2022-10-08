import json
import pathlib

path = str(pathlib.Path().resolve()) + "/jsons"


def validate(nfof, genre):
    if nfof == 'f':
        if genre == 'scifi' or genre == 'fantasy' or genre == 'horror' or genre == 'mystery':
            return True
        else:
            return False
    elif nfof == 'n':
        if genre == 'science' or genre == 'business' or genre == 'timemanagement' or genre == 'education' or genre == 'biography':
            return True
        else:
            return False
    else:
        return False

def admin(name):
    f = open(f"{path}/database.json")
    cmd = input(f"{name}> ")   
    if cmd == 'new':
        bookname = input("Book Name: ")
        nfof = input("Fiction or Non-Fiction(f/n): ").lower()
        genre = input("Book Genre: ").lower()
        if validate(nfof, genre):
            dictionary = {}
            refrences = input("Refrences for name(sep=,): ")
            temp = {
                "description": dictionary[nfof][genre][bookname]["description"],
                "rating": dictionary[nfof][genre][bookname]["rating"],
                "name": bookname,
                "available": True,
                "refrences": refrences.split(','),
                "reviews": dictionary[nfof][genre][bookname]["reviews"]
            }
            dictionary = json.load(f)
            dictionary[nfof][genre][bookname] = temp
        else:
            print("Invalid Details")
    elif cmd == 'available':
        bookname = input("Book Name: ")
        nfof = input("Fiction or Non-Fiction(f/n): ").lower()
        genre = input("Book Genre: ").lower()
        if validate(nfof, genre):
            dictionary = {}
            refs = dictionary[nfof][genre][bookname][refrences]
            temp = {
                "description": dictionary[nfof][genre][bookname]["description"],
                "rating": dictionary[nfof][genre][bookname]["rating"],
                "name": bookname,
                "available": True,
                "refrences": refs,
                "reviews": dictionary[nfof][genre][bookname]["reviews"]
            }
            dictionary = json.load(f)
            dictionary[nfof][genre][bookname] = temp
        else:
            print("Invalid Details")
    elif cmd == 'unavailable':
        bookname = input("Book Name: ")
        nfof = input("Fiction or Non-Fiction(f/n): ").lower()
        genre = input("Book Genre: ").lower()
        if validate(nfof, genre):
            dictionary = {}
            refs = dictionary[nfof][genre][bookname]["refrences"]
            temp = {
                "description": dictionary[nfof][genre][bookname]["description"],
                "rating": dictionary[nfof][genre][bookname]["rating"],
                "name": bookname,
                "available": False,
                "refrences": refs,
                "reviews": dictionary[nfof][genre][bookname]["reviews"]
            }
            dictionary = json.load(f)
            dictionary[nfof][genre][bookname] = temp
        else:
            print("Invalid Details")
    elif cmd == 'ref':
        bookname = input("Book Name: ")
        nfof = input("Fiction or Non-Fiction(f/n): ").lower()
        genre = input("Book Genre: ").lower()
        if validate(nfof, genre):
            dictionary = {}
            dictionary = json.load(f)
            refrences = input("Refrences for name(sep=,): ")
            av = dictionary[nfof][genre][bookname]["avaliable"]
            temp = {
                "description": dictionary[nfof][genre][bookname]["description"],
                "rating": dictionary[nfof][genre][bookname]["rating"],
                "name": bookname,
                "available": av,
                "refrences": refrences.split(','),
                "reviews": dictionary[nfof][genre][bookname]["reviews"]
            }
            dictionary[nfof][genre][bookname] = temp
        else:
            print("Invalid Details")

def checkAdmin():
    f = open(f'{path}/admin.json')
    pin = int(input("Enter your admin pincode: "))
    data = {}
    json.load(f, data)
    valid = False
    for admin in data:
        if data[admin] == pin:
            name = admin
            valid = True
    if valid:
        print(f"Welcome {name}.")
        admin(name)
    if not valid:
        print("Invalid Pin")

def search(keywords):
    f = open(f"{path}/database.json")
    books = json.load(f)
    for nfof in books:
        for genre in nfof:
            for book in genre:
                if book == keywords.lower():
                    return book
                    

def main():
    print(search("bored"))

if __name__ == '__main__':
    main()