"""Ticket Booking System GUI

Simple Tkinter-based seat booking simulation (10 rows x 10 seats).
"""
import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.title("Ticket Booking System")

# selected buttons list, seat grid, ticket count
l = []
m = []
val = 0

rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]


def white(btn):
    color = btn.cget("bg")

    if color == "light green":
        btn.configure(bg="white")
        if btn not in l:
            l.append(btn)
    elif color == "white":
        btn.configure(bg="light green")
        if btn in l:
            l.remove(btn)


def clear_prev():
    for btn in l[:]:
        if btn.cget("state") == "normal":
            btn.config(bg="light green")
            l.remove(btn)


def tkt_count():
    global val

    try:
        n = simpledialog.askinteger("Tickets", "How many TICKETS?")
        if n is None:
            return
        if n < 1 or n > 10:
            messagebox.showerror("Error", "Please enter a number between 1 and 10")
            return
        val = n
        messagebox.showinfo("Success", f"Selected {n} ticket(s)")
    except Exception:
        return


def box(r, c):
    global val

    if val == 0:
        return

    if val == 1:
        white(m[r][c])
        return

    clear_prev()

    if c + val > 10:
        messagebox.showwarning("Not Possible", f"Only {10 - c} tickets can be booked")
        return

    for j in range(c, c + val):
        btn = m[r][j]
        if btn.cget("state") == "disabled":
            messagebox.showwarning("Already Booked")
            return

    for j in range(c, c + val):
        btn = m[r][j]
        btn.config(bg="white")
        if btn not in l:
            l.append(btn)


def cancel_tickets():
    text = simpledialog.askstring("Cancel Tickets", "Enter the Seat Range")

    if not text:
        messagebox.showerror("Error", "Invalid Form")
        return

    disp = text.upper()
    text = disp

    if "-" not in text:
        text = text + "-" + text

    try:
        s, e = text.upper().split("-")
        r1, c1 = s[0], int(s[1:])
        r2, c2 = e[0], int(e[1:])

        if r1 != r2:
            messagebox.showerror("Error", "Please cancel seats within the same row")
            return

        ri = rows.index(r1)

        for c in range(c1 - 1, c2):
            btn = m[ri][c]
            if btn.cget("state") != "disabled":
                seat_label = f"{rows[ri]}{c+1}"
                messagebox.showerror("Error", f"Seat {seat_label} is not booked")
                return

        for c in range(c1 - 1, c2):
            btn = m[ri][c]
            btn.config(state="normal", bg="light green")

        messagebox.showinfo("Cancelled", f"{disp} cancelled successfully")

    except Exception:
        messagebox.showerror("Error", "INVALID")


def book():
    global val

    for btn in l:
        btn.config(state="disabled")
    l.clear()
    val = 0


txt = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

for c in range(10):
    label = tk.Label(root, text=str(c + 1))
    label.grid(row=0, column=c + 1, pady=5)

for i in range(10):

    label = tk.Label(root, text=txt[i])
    label.grid(row=i + 1, column=0, padx=10)
    p = []

    for j in range(10):

        btn = tk.Button(root, width=10, height=2, bg="light green", command=lambda r=i, c=j: box(r, c))
        btn.grid(row=i + 1, column=j + 1, padx=3, pady=3)
        p.append(btn)
    m.append(p)

btn_tickets = tk.Button(root, height=2, width=12, text="BOOK MY SHOW", bg="light blue", command=tkt_count)
btn_tickets.grid(row=12, column=3, padx=5, pady=15)

btn_book = tk.Button(root, height=2, width=12, text="BOOK", bg="orange", command=book)
btn_book.grid(row=12, column=6, padx=5, pady=15)

btn_cancel = tk.Button(root, height=2, width=12, text="CANCEL", bg="red", command=cancel_tickets)
btn_cancel.grid(row=12, column=9, padx=5, pady=15)

root.mainloop()
