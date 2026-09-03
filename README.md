# 📂 Smart File Organizer

A Python-based automation tool that organizes files into category-based folders, safely handles duplicate filenames, records activity logs, and stores file history using SQLite.

---

## ✨ Features

* 📁 Automatically scans files from the `Input` folder
* 🔍 Detects file types using file extensions
* 🗂️ Organizes files into category-based folders
* 🔄 Safely handles duplicate filenames
* 📝 Automatically renames duplicate files
* 📊 Generates an organization summary
* 🧾 Maintains an activity log
* 🗄️ Stores file history in SQLite
* 🛡️ Handles errors without crashing
* ⚙️ Uses a separate configuration file for file categories

---

## 🛠️ Tech Stack

**Language:** Python

**Libraries / Modules:**

* `os`
* `shutil`
* `sqlite3`
* `datetime`

---

## 📁 Project Structure

```text
Smart_File_Organizer/
│
├── organizer.py
├── config.py
├── organizer.db
├── organizer.log
├── README.md
│
├── Input/
│
├── PDF Files/
├── Images/
├── Text Files/
├── CSV Files/
├── Word Files/
├── Excel Files/
└── PowerPoint Files/
```

---

## ⚙️ How It Works

The organizer follows a simple automated workflow:

**1. Place files**

Put your files inside the `Input` folder.

**2. Scan**

The program scans the files inside the `Input` folder.

**3. Detect**

Each file is matched with its extension and category.

**4. Organize**

The file is moved into the appropriate category folder.

**5. Handle duplicates**

If a file with the same name already exists, the program creates a unique name automatically.

Example:

```text
report.pdf
report_1.pdf
report_2.pdf
```

**6. Record activity**

Every successful move, rename, or error is recorded in the log file and SQLite database.

**7. Show summary**

The program displays the number of files moved, errors, and category-wise results.

---

## 📌 Supported File Types

| Extension | Category         |
| --------- | ---------------- |
| `.pdf`    | PDF Files        |
| `.jpg`    | Images           |
| `.png`    | Images           |
| `.jpeg`   | Images           |
| `.txt`    | Text Files       |
| `.csv`    | CSV Files        |
| `.docx`   | Word Files       |
| `.xlsx`   | Excel Files      |
| `.pptx`   | PowerPoint Files |

---

## 🚀 How to Run

### 1. Open the project folder

Open the project in VS Code or PowerShell.

### 2. Place files inside `Input`

Example:

```text
Input/
├── report.pdf
├── notes.txt
└── photo.jpg
```

### 3. Run the program

```powershell
python organizer.py
```

### 4. Result

The files are automatically organized:

```text
PDF Files/
└── report.pdf

Text Files/
└── notes.txt

Images/
└── photo.jpg
```

---

## 🗄️ Database

The project uses **SQLite** to maintain file activity history.

The database records:

| Field     | Description                 |
| --------- | --------------------------- |
| File Name | Name of the processed file  |
| Action    | MOVED, RENAMED, or ERROR    |
| Category  | Destination category        |
| Timestamp | Date and time of the action |

Database file:

```text
organizer.db
```

---

## 📝 Activity Log

The project also maintains a text-based activity log.

Log file:

```text
organizer.log
```

Example:

```text
[02-09-2026 06:02 PM] report.pdf renamed to report_1.pdf and moved to PDF Files
```

---

## 🧪 Testing

The project was tested with:

* Supported file types
* Multiple files at once
* Duplicate filenames
* Unsupported file types
* Empty `Input` folder
* Repeated program runs
* SQLite activity logging
* Error handling

---

## 🔮 Future Improvements

* Add support for more file types
* Add a graphical user interface
* Add scheduled automatic organization
* Add file statistics and reporting
* Add undo / restore functionality
* Add configuration through a user-friendly interface

---

## 👩‍💻 Author

**Bhumi Sharma**

Built as a practical Python automation project for learning, portfolio development, and real-world problem solving.
