names = set()

while True:
    name = input("Enter a name(press Enter to quit): ")

    if name == "":
        break

    if name in names:
        print("Name already in use")
    else:
        print("New name")
        names.add(name)

print("\nHere are the list of names:")
for name in names:
    print(name)