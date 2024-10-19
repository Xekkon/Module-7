airports = {}

def add_airport():
    icao = input("Enter ICAO code: ").upper()
    name = input("Enter airport name: ")
    airports[icao] = name
    print(f"Airport {name} added successfully.\n")

def fetch_airport():
    icao = input("Enter ICAO code: ").upper()
    if icao in airports:
        print(f"Airport Name: {airports[icao]}\n")
    else:
        print("Airport not found.\n")

while True:
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        add_airport()
    elif choice == "2":
        fetch_airport()
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")