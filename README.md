# PyQt6-Auth-UI-Modern

A stylish and functional desktop application for user registration and login, built with **Python** and **PyQt6**. This project focuses on high-quality UI design, providing a smooth transition between different authentication states.

## 🚀 Overview
This system serves as a robust starting point for any desktop application requiring user management. It features:
- **Main Portal:** A welcoming entry screen.
- **Login Interface:** A secure-looking area for returning users.
- **Account Creation:** A streamlined registration form.

## 🛠️ Tech Stack
- **Language:** Python 🐍
- **GUI Framework:** `PyQt6`.
- **UI Design:** XML-based `.ui` files created with Qt Designer.
- **Styling:** Advanced CSS-like `QSS` (Qt Style Sheets) for rounded corners and hover effects.

## 📊 Project Workflow
1. **Entry Point:** `Main.py` initializes the `mainWindow`.
2. **Navigation:** Uses a signal-slot mechanism to switch between windows (Login/Register) while closing the previous ones to save memory.
3. **UI Loading:** Dynamically loads design files using `loadUi()`, allowing for easy design updates without touching the backend logic.
4. **Visuals:** Integrates custom background images and icons to create a professional look and feel.

## ⚙️ Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sarahalsamadi/PyQt6-Auth-UI-Modern.git](https://github.com/sarahalsamadi/PyQt6-Auth-UI-Modern.git)

2. **Install required dependencies:**
   ```bash
  pip install PyQt6
3. **Run the Application:**
  ```bash
  python Main.pypython Main.py
