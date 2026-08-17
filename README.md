# 🚀 RepoPilot

**RepoPilot is a Python-based Git automation tool that watches a project folder for file changes and helps automate Git commits and pushes to GitHub.**

This project was built to explore Git automation, file-system monitoring, and Python integration with Git.

## ✨ Features

* 📁 Watches the project folder for file changes
* 🔍 Detects changes automatically
* 📝 Creates Git commits with generated commit messages
* 🚀 Pushes changes to the connected GitHub repository
* 🛡️ Ignores Git's internal `.git` folder to avoid unnecessary triggers
* 🐍 Built with Python

## 🛠️ Technologies

* Python
* Git
* GitHub
* File-system monitoring

## 📂 Project Structure

```text
RepoPilot/
│
├── main.py
├── test.py
├── test2.py
├── test3.py
└── README.md
```

## ⚙️ How It Works

```text
File Change
    ↓
RepoPilot detects the change
    ↓
Git changes are identified
    ↓
A commit is created
    ↓
Changes are pushed to GitHub
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sudharsan124/RepoPilot.git
```

### 2. Open the project

```bash
cd RepoPilot
```

### 3. Install the required Python package

If your version of RepoPilot uses a file-system monitoring package, install the required dependency:

```bash
pip install watchdog
```

### 4. Run RepoPilot

```bash
python main.py
```

Make changes to files inside the watched project directory and RepoPilot will detect them.

## 🎯 Why I Built This

I built RepoPilot as a hands-on project to understand how Git and GitHub can be automated using Python.

Instead of manually checking for changes, committing files, and pushing them to GitHub, I wanted to experiment with building a small tool that could handle the workflow automatically.

## 📚 What I Learned

Through this project, I practiced:

* Python file-system monitoring
* Git commands and workflows
* GitHub repositories and remote branches
* Automated commits and pushes
* Debugging Git-related issues
* Handling `.git` folder changes
* Working with Git history

## 🔮 Future Improvements

Some features I may add in future versions:

* Better commit-message generation
* Configuration file for repository settings
* Selective file watching
* Better error handling
* GitHub API integration
* Simple graphical interface
* Improved logging

## 👨‍💻 Author

**Sudharsan B**

Computer Science Engineering Student

GitHub: [@sudharsan124](https://github.com/sudharsan124) |
LinkedIn: [Sudharsan B](https://www.linkedin.com/in/sudharsan-balachandar)

---

⭐ If you find this project interesting, feel free to explore the code and follow the project as it evolves.

