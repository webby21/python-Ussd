# USSD Miner Registration System (Python + SQLite)

A simple Python-based USSD simulation system for registering miners using a command-line interface (CLI). This project is designed to demonstrate backend development, database interaction, and input validation in a format similar to mobile USSD sessions.

##  Features

- Simulates USSD code dialing (e.g., `*123#`)
- Allows miners to register with:
  - Full Name
  - National ID (NRC)
  - Location
- Stores data in a local SQLite database
- View all registered miners
- Validates all user input for accuracy and security

## Tech Stack

- **Python 3**
- **SQLite** (built-in DB engine)
- **Regex** (for input validation)
- **CLI interface** (no external dependencies)

##  How to Run

1. Clone or download this repository:
   ```bash
   git clone https://github.com/webby21/python-Ussd.git
   cd ussd-miner-registration
