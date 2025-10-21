import os
import shutil
from pathlib import Path

# To detect user folders
user_home = Path.home()

# To detect OneDrive
possible_onedrives = [p for p in user_home.glob("OneDrive*") if p.is_dir()]
onedrive = possible_onedrives[0] if possible_onedrives else None
# Fixes a bug where program can't open certain onedrives

# Use OneDrive/Documents, else normal Documents dir
if onedrive and (onedrive / "Documents").exists():
    documents = onedrive / "Documents"
else:
    documents = user_home / "Documents"

# Thank you downloads for not being difficult
downloads = user_home / "Downloads"

# Main File type groups, add any you wish here only
image_ext = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff")
doc_ext = (".doc", ".docx")
pdf_ext = (".pdf",)
spreadsheet_ext = (".xls", ".xlsx", ".csv")

# Destination folders inside Documents, change name in "" only
docs_folder = documents / "Docs"
pdfs_folder = documents / "PDFs"
sheets_folder = documents / "Spreadsheets"

# Main function
def safe_move(src, dest_folder):
    dest_folder.mkdir(parents=True, exist_ok=True)
    dest = dest_folder / src.name
    try:
        shutil.move(str(src), str(dest))
        print(f"Moved: {src.name} → {dest_folder}")
    except Exception as e:
        print(f"Skipped {src.name}: {e}")

# Prompt
print("This program will organize your OneDrive, Downloads and Documents folders.")
print("• All Images → Pictures")
print("• All Docs, PDFs, and Spreadsheets → Documents\n")

user_input = input("Are you sure you want to continue? (y/n): ")

# Check value loop
while user_input != "y":
    if user_input == "n":
        exit("Goodbye")
    else:
        print("what")
        #humor
        user_input = input("I said type 'y' or 'n': ")

#  Onedrive
if onedrive:
    print(f"\n ☁︎ Sorting files in OneDrive: {onedrive}")
    for file in onedrive.glob("*"):
        if file.is_file():
            ext = file.suffix.lower()
            if ext in image_ext:
                safe_move(file, onedrive / "Pictures")
            elif ext in doc_ext:
                safe_move(file, docs_folder)
            elif ext in pdf_ext:
                safe_move(file, pdfs_folder)
            elif ext in spreadsheet_ext:
                safe_move(file, sheets_folder)

#  Documents
if documents.exists():
    print(f"\n📄 Sorting files in Documents: {documents}")
    for file in documents.glob("*"):
        if file.is_file():
            ext = file.suffix.lower()
            if ext in doc_ext:
                safe_move(file, docs_folder)
            elif ext in spreadsheet_ext:
                safe_move(file, sheets_folder)
            elif ext in pdf_ext:
                safe_move(file, pdfs_folder)
            elif ext in image_ext:
                safe_move(file, onedrive / "Pictures")

#  Downloads 
if downloads.exists():
    print(f"\n⬇️  Sorting files in Downloads: {downloads}")
    for file in downloads.glob("*"):
        if file.is_file():
            ext = file.suffix.lower()
            if ext in doc_ext:
                safe_move(file, docs_folder)
            elif ext in spreadsheet_ext:
                safe_move(file, sheets_folder)
            elif ext in pdf_ext:
                safe_move(file, pdfs_folder)
            elif ext in image_ext:
                safe_move(file, onedrive / "Pictures")
#print
print("\n✅ Sorting complete")



