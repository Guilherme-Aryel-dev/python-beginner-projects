# 🐍 Python Beginner Projects

Small real-world projects I build while learning Python. After each lesson, I create a project that practices the new concepts.

> 📚 **Learning path:** Curso em Vídeo (Python 3) → CS50P (Harvard) → SQL → FastAPI

---

## Projects

### 1. 🍔 Snack Bar Cashier
📁 `snack-bar-cashier/`

A simple cashier system for a snack bar. The attendant enters the customer's name and the price of each item, and the program prints a receipt with the total.

**Concepts practiced:** `input()`, `int()`, variables, arithmetic, `print()`

**Example:**
```
Can you tell me your name? Aryel
Burger price: 25
Fries price: 12
Soda price: 8

Customer: Aryel
Burger: 25
Fries: 12
Soda: 8
Total: 45
Thank you, Aryel! Come back soon!
```

---

### 2. 🏋️ Gym Registration System
📁 `gym-registration/`

A registration system for a gym. It collects the member's data and validates each field.

**Concepts practiced:** `input()`, `int()`, `float()`, `type()`, f-strings, string methods (`isalpha()`, `isalnum()`, `islower()`, `isupper()`, `isnumeric()`)

**Example:**
```
Name: Aryel | Only letters? True
Username: aryel2026 | Letters and digits only? True | Lowercase? True
Plan: VIP | Uppercase? True
Age: 18 | Only digits? True | Next year: 19
Current weight: 80.0 kg
Weight type: <class 'float'>
Goal: +3.5 kg | Target weight: 83.5 kg
```

---

### 3. 🚗 Ride Receipt
📁 `ride-receipt/`

A receipt generator for a ride-hailing app. It reads the ride data, calculates the fare and splits the total between passengers.

**Concepts practiced:** `float()`, `int()`, arithmetic operators (`//`, `%`), string methods, string multiplication, f-string alignment and formatting (`^`, `:>10.2f`)

**Example:**
```
==============================
         TRIP RECEIPT
==============================
Passenger name: Aryel | Only letters? True
Plate: ABC1D23 | Valid? True | Uppercase? True
Distance: 12.5 km
Duration: 1h 15 min
------------------------------
Base fare:     R$       5.00
Distance:      R$      26.25
Time:          R$      26.25
------------------------------
TOTAL:         R$      57.50
Per passenger: R$      28.75
==============================
```

---

## ▶️ How to run

1. Install [Python 3](https://www.python.org/downloads/)
2. Clone this repository:
   ```
   git clone https://github.com/Guilherme-Aryel-dev/python-beginner-projects.git
   ```
3. Run a project:
   ```
   python snack-bar-cashier/main.py
   ```

## 🚀 Next steps

- [ ] Validate user input with `if` / `else`
- [ ] Use loops to add any number of items to the receipt
- [ ] Save registrations to a file

## 👤 Author

**Guilherme Aryel** · [GitHub](https://github.com/Guilherme-Aryel-dev) · [LinkedIn](https://www.linkedin.com/in/guilherme-aryel-05aa1440a/)
