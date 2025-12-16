# 🔐 CryptoTool: Advanced Encryption Algorithms Suite

[![Language](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/) [![GUI](https://img.shields.io/badge/Interface-Tkinter-orange.svg)]() [![License](https://img.shields.io/badge/License-MIT-green.svg)]() [![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-blue)](https://www.linkedin.com/in/seif-elmuselmani/)

**CryptoTool** is a comprehensive cryptographic simulation software developed to bridge the gap between classical ciphers and modern encryption standards. It provides a clean, user-friendly interface to visualize how data is transformed securely.

> **Project Context:** Developed as a graduation project component to demonstrate mastery of algorithmic logic, data security concepts (DES/AES), and software architecture.

---

## 🚀 Key Features

This tool offers a robust implementation of various cryptographic techniques:

### 🏛️ Classical Ciphers (The Foundation)
* **Substitution:** Caesar, Monoalphabetic, Vigenère.
* **Polygraphic:** **Playfair Cipher** (Implementation of 5x5 Matrix & Digraph rules).
* **Transposition:** Row Transposition, Rail Fence.
* **Matrix-Based:** Hill Cipher (Linear Algebra operations).
* **Unbreakable:** One-Time Pad (OTP).

### 🛡️ Modern Standards (The Powerhouse)
* **DES (Data Encryption Standard):** Full 16-round Feistel network implementation.
* **AES (Advanced Encryption Standard):** The global standard for secure communication.
* **Security Modes:** Supports **CBC (Cipher Block Chaining)** mode for enhanced security to prevent pattern leakage.

---

## 📸 Screenshots

| **Main Dashboard** | **Encryption Demo** |
|:---:|:---:|
| ![Main UI](assets/menu_screenshot.png) | *Add a GIF or Image here* |

*(Ensure you have an `assets` folder with your screenshots)*

---

## 🛠️ Tech Stack

* **Core Language:** Python 3.x
* **User Interface:** Tkinter (Custom Styled)
* **Cryptography:** `PyCryptodome` (For standard block cipher implementations)
* **Mathematics:** `NumPy` (For Matrix manipulations in Hill Cipher)

---

## 📂 Project Structure

The project follows a clean, modular architecture:

```text
Crypto-Tool/
│
├── ciphers/            # Core Logic Modules
│   ├── classical/      # (Caesar, Playfair, etc.)
│   └── modern/         # (DES, AES implementations)
│
├── gui/                # UI & Event Handling
│   └── main_window.py
│
├── assets/             # Images & Icons
├── main.py             # Application Entry Point
└── requirements.txt    # Dependencies
