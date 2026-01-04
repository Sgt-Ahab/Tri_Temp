# Tri-Temp — Temperature Conversion Module

This is a module I am creating, debuted at **2:49 AM on 8/29/2025**.

## Project Intent
This project is intended to do the following:

- Take user input
- Accept a specified temperature unit
- Convert the temperature to the remaining units

This project is coded in **Python** and **C++** as a programming exercise.  
Once released, there is no planned long-term afterwork.

---

## Program Restrictions & Running

### Python
- Handles numeric input validation internally.
### Python (Running)
- Run the program from the repository folder:

`python tri_temp.py`


### C++
- **Only receives numeric input** for temperature values.
- Non-numeric input will result in a looping prompt.
- This behavior is left as **user integrity by design**, as numeric stream validation has not yet been covered.
### C++ (Running)
- Compile with your preferred C++ toolchain/IDE *(example commands vary by system).*

---

## Timeline of Work

- **12/15/25 – 12/20/25**  
  *(Delayed due to sickness)*

- **12/31/25 – 01/03/26 + 01/04/26**  
  C++ implementation completed.
  Python Code completed and tested.
  Said I wanted it Public ASAP early 01/04/26.

---

## Program Logic

The program follows this logic:

1. Takes user input for temperature and unit.
2. Unit options:
   - `C` → Celsius  
   - `K` → Kelvin  
   - `F` → Fahrenheit
3. Mathematical formulas remain untouched.
4. Output displays:
   - The base temperature
   - The two converted temperatures  
   (rounded to two decimal places)
5. User is prompted to enter a new value or quit.
6. Program exits if the user selects `N`.

---

## Unit Test List (Manual Verification)

Use these inputs and confirm the expected outputs match (rounded to two decimals).
*Note: Small floating-point rounding differences may occur depending on runtime; expected values are shown to two decimals.*

### Test 1 — Freezing Point of Water
**Input:** `0 C`  
**Expected:**  
- Base: `0.00 C`  
- Fahrenheit: `32.00 F`  
- Kelvin: `273.15 K`

### Test 2 — Boiling Point of Water
**Input:** `212 F`  
**Expected:**  
- Base: `212.00 F`  
- Celsius: `100.00 C`  
- Kelvin: `373.15 K`

### Test 3 — Absolute Zero
**Input:** `0 K`  
**Expected:**  
- Base: `0.00 K`  
- Celsius: `-273.15 C`  
- Fahrenheit: `-459.67 F`

### Test 4 — Room Temperature Sanity Check
**Input:** `25 C`  
**Expected:**  
- Base: `25.00 C`  
- Fahrenheit: `77.00 F`  
- Kelvin: `298.15 K`

---

## Addition Log

- **8/29/2025**  
  Creation of `readme.txt` and logic flow for project concept.  
  Began main repository work and module skeletons.

- **12/31/2025**  
  Coded first portion. Trimmed README to align with mission objective:  
  *Simple CLI Temperature Conversion.*

- **01/03/2026**  
  Added folders for two program languages: Python and C++.  
  Decorated project and updated README.  
  
- **01/04/2026**
  C++ completed. Python reworked into a single-file implementation.
  `readme.txt` -> `README.md`; *LICENSE* made.

---
