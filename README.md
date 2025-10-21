# 🗂️ Universal File Sorter (Python)

A lightweight Python script that automatically organizes your **OneDrive**, **Documents**, and **Downloads** folders into clean, structured subfolders.
Works on any Windows system

---

## 🚀 Features
- Detects OneDrive path automatically (any name or account type)
- Sorts files by type:
  - `.doc`, `.docx` → `/Documents/docs`
  - `.pdf` → `/Documents/pdfs`
  - `.xls`, `.xlsx`, `.csv` → `/Documents/spreadsheets`
  - Images → `/OneDrive/Pictures`
- Creates folders if missing
- Safe, lightweight, and fully portable

---

## ⚙️ Usage
1. **Download** the script or clone this repo:
   ```bash
   git clone https://github.com/adamkimmins/universal-file-sorter.git
2. **Open** the folder:
   ```bash
   cd universal-file-sorter
3. **Run** the script:
   ```bash
   python universal_sorter.py
