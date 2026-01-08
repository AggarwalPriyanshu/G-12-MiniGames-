## 🚀 Getting Started

### Prerequisites
1.  **Python:** Ensure Python 3.x is installed.
2.  **MySQL:** A local MySQL server must be running.
3.  **Connector:** Install the required library via pip:
    ```bash
    pip install mysql-connector-python
    ```

### Configuration
Update the connection details in `CS_Project_File.py` and `File_Handling.py` to match your local MySQL credentials:
```python
con = mc.connect(host="localhost", user="root", passwd="your_password")
Execution
To experience the full application (Login + Games):

Bash

python CS_Project_File.py
To bypass authentication and play games directly:

Bash

python Games.py
📂 Project Structure
CS_Project_File.py: The main entry point and Account Management dashboard.

File_Handling.py: Handles all Backend logic, CSV operations, and OTP recovery.

Games.py: The core gaming engine containing all mini-game logic.

GAMERS.csv: Local storage for user records.

🗺️ Roadmap
[ ] Remove local MySQL dependency for easier portable deployment.

[ ] Implement a global NoSQL cloud database (e.g., MongoDB/Firebase).

[ ] Add more complex GUI elements using libraries like Tkinter or PyQt.

Developed by Priyanshu Aggarwal & Aditya Pandey
