import sqlite3
import re

# Initialize DB
def init_db():
    conn = sqlite3.connect('miners.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS miners (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            national_id TEXT NOT NULL,
            location TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Input validation functions
def validate_name(name):
    return bool(re.fullmatch(r"[A-Za-z ]{2,50}", name))

def validate_national_id(nrc):
    return bool(re.fullmatch(r"\d{6}/\d{2}/\d", nrc))  # Example format: 123456/78/9

def validate_location(location):
    return len(location.strip()) >= 2

# CLI Simulation
def ussd_entry():
    code = input("Dial USSD code (e.g. *123#): ").strip()
    if code == "*123#":
        ussd_menu()
    else:
        print("Invalid USSD code. Try again.")
        ussd_entry()

# Menu options
def ussd_menu():
    print("\n Miner Registration USSD Portal")
    print("1. Register as a Miner")
    print("2. View All Registrations")
    print("3. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        register_miner()
    elif choice == "2":
        view_miners()
    elif choice == "3":
        print("Session ended.")
    else:
        print("Invalid option. Try again.")
        ussd_menu()

# Registration process
def register_miner():
    print("\n  Miner Registration ")

    while True:
        name = input("Enter Full Name: ").strip()
        if validate_name(name):
            break
        print("Invalid name. Use letters only (2-50 characters).")

    while True:
        nrc = input("Enter National ID (e.g. 123456/78/9): ").strip()
        if validate_national_id(nrc):
            break
        print("Invalid NRC format. Use 123456/78/9 format.")

    while True:
        location = input("Enter Location: ").strip()
        if validate_location(location):
            break
        print("Location must be at least 2 characters.")

    conn = sqlite3.connect('miners.db')
    c = conn.cursor()
    c.execute("INSERT INTO miners (name, national_id, location) VALUES (?, ?, ?)",
              (name, nrc, location))
    conn.commit()
    conn.close()

    print("\n✅ Registration Successful!")
    ussd_menu()

# View all registrations
def view_miners():
    conn = sqlite3.connect('miners.db')
    c = conn.cursor()
    c.execute("SELECT * FROM miners")
    rows = c.fetchall()
    conn.close()

    if not rows:
        print("⚠️ No registered miners found.")
    else:
        print("\n--- Registered Miners ---")
        for row in rows:
            print(f"{row[0]}. {row[1]} | NRC: {row[2]} | Location: {row[3]}")
    ussd_menu()

# Run the app
if __name__ == "__main__":
    init_db()
    ussd_entry()
