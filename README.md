<p align="center">
  <img src="logo.png" alt="RepoPilot Logo" width="180">
</p>

<h1 align="center">RepoPilot</h1>

<p align="center">
  Python-powered Git automation for automatic commit and push workflows.
</p>

**RepoPilot is a Python-based Git automation tool that automatically detects a Git repository, watches for file changes, and helps automate Git commits and pushes to GitHub.**

This project was built to explore Git automation, file-system monitoring, repository detection and Python integration with Git.

## ✨ Features

* 📁 Automatically detects the Git repository
* 🔍 Detects file changes automatically
* 📝 Creates Git commits with generated commit messages
* 🚀 Pushes changes to the connected GitHub repository
* 🛡️ Protects the RepoPilot repository from automatic pushes
* 🚫 Ignores Git's internal `.git` folder to avoid unnecessary triggers
* 🐍 Built with Python

## 🛠️ Technologies

* Python
* Git
* GitHub
* Watchdog
* File-system monitoring

## 📂 Project Structure

```text
RepoPilot/
│
├── .gitignore
├── logo.png
├── main.py
├── README.md
└── requirements.txt
```

## ⚙️ How It Works

```text
File Change
    ↓
RepoPilot detects the change
    ↓
Git repository is identified
    ↓
GitHub remote is checked
    ↓
RepoPilot repository?
    ↓
   YES → Automatic push cancelled
    ↓
    NO
    ↓
Git add
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

Install the required dependency:

```bash
pip install -r requirements.txt
```

### 4. Run RepoPilot

Run RepoPilot from inside the Git repository you want to monitor:

```bash
python path/to/RepoPilot/main.py
```

RepoPilot will automatically detect the Git repository and start watching for file changes.

##🛡️ Safety

RepoPilot includes a safety check to prevent it from automatically pushing changes to its own repository.

If RepoPilot detects its own repository, the automatic push is cancelled.

Other Git repositories can be processed normally.

## 🎯 Why I Built This

I built RepoPilot as a hands-on project to understand how Git and GitHub can be automated using Python.

Instead of manually checking for changes, committing files, and pushing them to GitHub, I wanted to experiment with building a small tool that could handle the workflow automatically.

## 📚 What I Learned

Through this project, I practiced:

* Python file-system monitoring
* Git commands and workflows
* GitHub repositories and remote branches
* Automated commits and pushes
* Automatic repository detection
* Git safety checks
* Debugging Git-related issues
* Handling .git folder changes
* Working with Git history

## 🔮 Future Improvements

Some features I may add in future versions:

* Better commit-message generation
* Configuration file for repository settings
* Selective file watching
* Better error handling
* Automatic branch detection
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

