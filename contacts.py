contacts = [  ]

def add_contact(name, phone):
    contacts.append({'name': name, 'phone': phone})

def list_contacts():
    for c in contacts:
        print(c["name"], ":", c["phone"])

def search_contact(name):
    for c in contacts:
        if c["name"] == name:
            return c
    return None

add_contact("Arash", "09120000000")
add_contact("Sara", "09350000000")

list_contacts()

result = search_contact("Sara")
if result:
    print("Found:", result)
else:
    print("Not found")