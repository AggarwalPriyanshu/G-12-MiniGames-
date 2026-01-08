  # 🎮 G-12: The CLI Game Zone & User Management System

![Python](https://img.shields.io/badge/Language-Python%203.x-blue)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange)
![CLI](https://img.shields.io/badge/Interface-CLI-lightgrey)
![Auth](https://img.shields.io/badge/Feature-User%20Authentication-success)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

**G-12** is a robust **Command Line Interface (CLI) application** developed as a **full-stack Python project**.  
It combines a **secure user authentication system** with an engaging collection of **mini-games**, ranging from mathematical puzzles and logic challenges to high-intensity quizzes.


---

## ✨ Key Features

### 👤 User Management System
- **Secure Authentication**  
  Login and Sign-up functionality with password-protected user accounts.

- **Persistent Storage**  
  Dual-mode storage using **MySQL** for database management and **CSV files** for local backups.

- **Account Recovery**  
  Built-in *Forgot Password* feature using a simulated **OTP (One-Time Password)** system.

- **CRUD Operations**  
  Users can **View, Edit, or Delete** their account details directly from the main dashboard.

---

### 🕹️ The Game Zone
- **Fun Games**
  - Stone-Paper-Scissors  
  - Lucky Draw  
  - Guess the Number  
  - Prank Calculators  

- **Mind Games**
  - Multi-category Quiz system:
    - Technology  
    - Astronomy  
    - Nature  
    - Sports  
    - History  

- **IQ Puzzles**
  - **FPB (Fermi, Pico, Bagels)**  
    A deductive logic number-guessing game available in **Single-player** and **Multi-player** modes.

---

## 🛠️ Tech Stack
- **Language:** Python 3.x  
- **Database:** MySQL (`mysql-connector-python`)  
- **File Handling:** CSV module for local backups  
- **Standard Libraries:**  
  - `random` – game logic  
  - `time` – UI delays  
  - `os` – file management  

---

## 🚀 Getting Started

### Prerequisites
- **Python:** Python 3.x installed  
- **MySQL:** Local MySQL server running  
- **Connector:** Install required library  
  ```bash
  pip install mysql-connector-python
Configuration

Update the database credentials in:

CS_Project_File.py

File_Handling.py

```
con = mc.connect(
    host="localhost",
    user="root",
    passwd="your_password"
)
```
---

### Execution


- Run full application (Authentication + Games):

```
python CS_Project_File.py
```

- Run games directly (Bypass authentication):

```
python Games.py
```
---
### 📂 Project Structure



```
G-12/
│
├── CS_Project_File.py   # Main entry point & account management dashboard
├── File_Handling.py    # Backend logic, CSV operations, OTP recovery
├── Games.py            # Core gaming engine (all mini-games)
├── GAMERS.csv          # Local storage for user records
```

### 🗺️ Roadmap



-Remove local MySQL dependency for easier portability

-Implement a global NoSQL cloud database or host MySQL on a centralized server

---

### 👤 Author


### Priyanshu Aggarwal
Electronics & Communication Engineering

📧 Email: Priyanshuaggarwal.in@gmail.com

🔗 LinkedIn: https://linkedin.com/in/priyanshu1201

💻 GitHub: https://github.com/AggarwalPriyanshu

---

⭐ If you find this repository useful, feel free to star it!
