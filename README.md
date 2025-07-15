# 🔐 Password Manager & Generator

A simple, secure, and flexible Python-based password manager and generator. This tool allows users to generate strong passwords, store them locally in an encrypted format, and retrieve them securely when needed.

---

## ⚙️ Features

- ✅ Secure password generation (customizable length, symbols, etc.)
- ✅ Store and retrieve login credentials
- ✅ AES encryption for stored passwords
- ✅ Master password access control
- ✅ Local storage (encrypted file or database)
- ✅ Terminal-based or CLI-driven interface

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/TrevorMartes/password-manager.git
cd password-manager
````

### 2. Install Dependencies

If your project uses external libraries like `cryptography`:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install cryptography
```

### 3. Run the Tool

```bash
python password_manager.py
```

You'll be prompted to:

* Set or enter a master password
* Generate a password or store/retrieve existing credentials

---

## 🛠️ Usage Examples

### Generate a Secure Password

```bash
> Generate password
> Length: 16
> Include: uppercase, lowercase, numbers, symbols
Generated: $P9K*3sRt!dVm2qB
```

### Store Credentials

```bash
> Add new entry
> Website: github.com
> Username: johndoe
> Password: (auto-generate or paste your own)
```

### Retrieve Credentials

```bash
> Lookup
> Website: github.com
Found:
Username: johndoe
Password: $P9K*3sRt!dVm2qB
```

---

## 🔐 Security

* Passwords are stored using **AES encryption**
* Master password is required to decrypt stored credentials
* Data is saved to a local file (e.g. `vault.enc`) or SQLite DB
* No external network requests — 100% offline

---

## 📦 Dependencies

* `cryptography`
* `getpass` (standard library)
* `os`, `sys`, `base64`, `json`

---

## 🧭 Roadmap

* [ ] GUI version using Tkinter or PyQt
* [ ] Cross-platform packaging (via PyInstaller)
* [ ] Password strength meter
* [ ] Cloud sync support (optional & encrypted)

---

## 📜 License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](./LICENSE) file for details.

---

## 👤 Author

Created by \TrevorMartes

Feel free to contribute, report issues, or suggest improvements!

---
