import json
import pathlib

path = pathlib.Path().resolve()

def admin(name):
    pass

def getAdmin():
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

def main():
    pass

if __name__ == '__main__':
    main()