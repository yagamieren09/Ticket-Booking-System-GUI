Ticket Booking System GUI
Project Title
Ticket Booking System GUI

Overview
A simple desktop seat-booking simulation built with Python and Tkinter. The app models a 10x10 seating layout (rows A–J, seats 1–10), supports interactive seat selection, batch ticket booking (1–10 seats), and cancellation of booked seat ranges (e.g., A1-A5). The UI uses color and button states to reflect availability, selection, and booked seats.

Features
10 rows (A–J), 10 seats per row (1–10)
Click-to-select individual seats
Select multiple adjacent seats in a single booking (choose 1–10 tickets)
Book selected seats (disables buttons)
Cancel a booked seat range via input (e.g., A1-A5)
Prevents double-booking with validation and user warnings
Clear visual states:
Light Green — Available
White — Selected
Disabled — Booked
How It Works
Seats are represented by tk.Button arranged in a grid.
Selecting ticket count (1–10) defines how many adjacent seats to reserve when clicking a seat.
When booking is confirmed, selected buttons change to the disabled state to indicate they are booked.
Cancellation accepts a seat range (same row) and re-enables those booked seats after validation.
Input and edge cases are handled with messagebox and simpledialog.
Installation
Prerequisites:
Python 3.8+ installed.
Tkinter (usually included with standard Python installations).
On Debian/Ubuntu: sudo apt-get install python3-tk
On macOS with Homebrew: included with official Python; otherwise use the system Python or install via the official installer.
Steps:
Clone the repository:
git clone https://github.com/yagamieren09/Ticket-Booking-System-GUI.git
cd Ticket-Booking-System-GUI
(Optional) Create a virtual environment:
python -m venv .venv
.venv\\Scripts\\activate   # Windows
source .venv/bin/activate  # macOS / Linux
There are no external Python packages required beyond the standard library. If you add dependencies later, list them in requirements.txt and run:
pip install -r requirements.txt
How To Run
Run the main script:
python app.py
If you kept the original filename (e.g., obaa (1).py), you can run it directly, but it is recommended to rename it to app.py for convenience.
Screenshots
Add screenshots to the screenshots/ directory and reference them here:

screenshots/selection.png — seat selection view
screenshots/booked.png — after booking seats
screenshots/cancel.png — cancellation dialog
Replace placeholders with actual images and update this section.

Future Improvements
Add persistent storage (JSON or SQLite) to save bookings between sessions.
Add seat pricing and dynamic totals.
Improve accessibility (keyboard navigation, clearer color contrast).
Add booking confirmation dialog summarizing seats and totals.
Support non-contiguous and multi-row group selection with an algorithm to find best-fit contiguous seats.
Add unit tests for booking and cancellation logic and separate UI from business logic.
Package as a standalone executable with PyInstaller for distribution.
Tech Stack
Python 3.8+
Tkinter (standard library)
Recommended Folder Structure
Ticket-Booking-System-GUI/
├── app.py
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── screenshots/
│   ├── selection.png
│   ├── booked.png
│   ├── cancel.png
├── docs/
│   ├── design.md
├── tests/
│   ├── test_booking_logic.py
Notes:

Rename the script to app.py for clarity and predictable run instructions.
For larger projects, separate UI code (ui.py) from booking logic (booking.py).
You can copy and paste this text directly into your README.md file. Let me know if you need further assistance!

GPT-4o • 1x
