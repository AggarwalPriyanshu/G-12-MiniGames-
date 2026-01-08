🎮 G-12: The CLI Game Zone & User Management System
G-12 is a robust Command Line Interface (CLI) application developed as a full-stack Python project. It features a complete user authentication system integrated with a diverse collection of mini-games, ranging from mathematical puzzles and logic games to high-intensity quizzes.

✨ Key Features
👤 User Management System
Secure Authentication: Includes Login and Sign-up functionality with password-protected accounts.

Persistent Storage: Utilizes dual-mode storage using MySQL for database management and CSV files for local records.

Account Recovery: Features a built-in "Forgot Password" tool utilizing a simulated OTP (One-Time Password) system.

CRUD Operations: Users have the ability to View, Edit, or Delete their account details directly through the main dashboard.

🕹️ The Game Zone
Fun Games: Includes Stone-Paper-Scissors, Lucky Draw, Guess the Number, and Prank Calculators.

Mind Games: A multi-category Quiz system covering Technology, Astronomy, Nature, Sports, and History.

IQ Puzzles: Features "FPB" (Fermi, Pico, Bagels), a deductive logic number-guessing game available in both Single and Multi-player modes.

🛠️ Tech Stack
Language: Python 3.x.

Database: MySQL (via mysql-connector-python).

File Handling: CSV module for local data backups.

Standard Libraries: random for logic, time for UI delays, and os for file management.

🚀 Getting Started
Prerequisites
Python: Ensure Python 3.x is installed.

MySQL: A local MySQL server must be running.

Connector: Install the required library via pip: pip install mysql-connector-python.

Configuration
Update the connection details in CS_Project_File.py and File_Handling.py to match your local MySQL credentials: con = mc.connect(host="localhost", user="root", passwd="your_password")

Execution
To experience the full application (Login + Games), run: python CS_Project_File.py.

To bypass authentication and play games directly, run: python Games.py.

📂 Project Structure
CS_Project_File.py: The main entry point and Account Management dashboard.

File_Handling.py: Handles Backend logic, CSV operations, and OTP recovery.

Games.py: The core gaming engine containing all mini-game logic.

GAMERS.csv: Local storage for user records.

🗺️ Roadmap
Remove local MySQL dependency for easier portable deployment.

Implement a global NoSQL cloud database or host MySQL over a global server.

👤 Author
Priyanshu Aggarwal & Aditya Pandey

GitHub: @AggarwalPriyanshu
