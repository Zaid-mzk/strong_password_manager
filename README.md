# 🔒 Z+ Password Manager

Welcome to **Z+ Password Manager**, a secure and versatile application that helps users **generate, evaluate, and manage strong passwords**.  
The project supports multiple modes:  
- **Command-Line Interface (CLI)**  
- **Tkinter Desktop GUI**  
- **Flask Web Interface (local + deployable on Vercel)**  

---

## 🚀 Features

### ✅ Password Generation
- Create strong, randomized passwords instantly.
- Fully customizable: length, uppercase, lowercase, digits, symbols.

### ✅ Password Strength Checker
- Instantly analyze any password’s strength.
- Real-time feedback & suggestions for improvement.

### ✅ Guidelines for Strong Passwords
- Learn the fundamentals of unbreakable passwords.
- Practical tips for everyday use.

### ✅ Multiple Interfaces
- **CLI:** Run directly in terminal for quick checks.  
- **Tkinter GUI:** Offline desktop app, beginner-friendly.  
- **Flask Web App:** Dark-themed, responsive, and deployable to **Vercel** for online access.  

---

## 📂 Project Structure

Z+ Password Manager/
│── main.py # CLI tool
│── gui_tkinter.py # Tkinter desktop GUI
│── app.py # Flask web app
│── templates/
│ └── index.html # Web UI template
│── static/
│ └── style.css # Web UI styling
│── vercel.json # Vercel deployment config
│── requirements.txt # Python dependencies
│── README.md # Documentation


---

## ⚡ Installation & Local Usage

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Zaid-mzk/Strong_Password_Manager.git

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run in Different Modes
🔹 Command Line (CLI)
python main.py

🔹 Tkinter GUI
python gui_tkinter.py

🔹 Flask Web App (Local)
python app.py


Visit: http://127.0.0.1:5000/

🌐 Deploying to Vercel
1️⃣ Install Vercel CLI
npm install -g vercel

2️⃣ Add vercel.json
{
  "version": 2,
  "builds": [
    { "src": "app.py", "use": "@vercel/python" }
  ],
  "routes": [
    { "src": "/(.*)", "dest": "app.py" }
  ]
}

3️⃣ Deploy
vercel


Vercel will give you a live URL like:
https://zplus-password-manager.vercel.app/

🎯 Why Z+ Password Manager?

Works everywhere: CLI, Desktop, Browser, Cloud.

Strong, reliable, customizable passwords.

Beginner-friendly yet secure.

Can be hosted online for easy sharing and demos.

🤝 Contributions

Contributions are welcome!

Report bugs 🐛

Suggest features 💡

Open PRs 🚀

📧 Contact

Email: zaid270803@gmail.com 

GitHub: Zaid-mzk


---

✅ This README now covers:  
- **All modes (CLI, Tkinter, Flask)**  
- **Hosting on Vercel** with deployment steps  
- Clean professional structure  

