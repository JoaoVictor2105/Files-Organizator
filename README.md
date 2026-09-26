# Files-Organizator

A simple command-line tool built in Python to automatically organize files inside a folder — either by **file type/extension** or by **creation date**.

This project was built as a learning exercise to practice Python fundamentals: file system operations, functions, dictionaries, control flow, and basic GUI interaction with `tkinter`.

## Features

- 📂 **Folder selection via GUI** — pick the folder to organize using a native file explorer window (no need to type the path manually).
- 🗂️ **Organize by extension** — files are sorted into category folders based on their extension:
  | Category | Extensions |
  |---|---|
  | Images | `.jpg`, `.jpeg`, `.png`, `.gif` |
  | Document | `.pdf`, `.doc`, `.docx`, `.txt`, `.ppt`, `.pptx`, `.xls`, `.xlsx` |
  | Video | `.mp4`, `.mkv`, `.mov`, `.flv` |
  | Music | `.mp3`, `.wav` |
  | Archives | `.zip`, `.rar`, `.7z` |
  | Code | `.py`, `.html`, `.js`, `.css` |
  | Others | any extension not listed above |
- 📅 **Organize by date** — files are sorted into folders named by their creation date (`YYYY-MM-DD`).
- 🔁 **Interactive menu** — choose an action, run it, and keep going until you're done.

## Requirements

- Python 3
- `tkinter` (included with most standard Python installations)

No external/third-party packages are required — the project only uses Python's standard library (`os`, `shutil`, `datetime`, `tkinter`).

## Usage

1. Run the script:
```bash
   python file_organizer.py
```
2. A folder selection window will open — choose the folder you want to organize.
3. Choose an option from the menu:

FILE ORGANIZER - choose an option:

Organize files by extension type
Organize files by date
Exit
4. The tool will move the files into subfolders and print a summary of each move in the terminal.

## Project structure

Files-Organizator/
├── file_organizer.py # main script
└── README.md


## Known limitations / edge cases still being handled

This project is being developed incrementally, so a few edge cases are still open work:

- Duplicate file names at the destination (e.g. moving a file to a folder that already has a file with the same name).
- Files with no extension.
- Empty source folder.

## Roadmap (planned extras)

- [ ] Dry-run mode (preview changes without moving files)
- [ ] Activity log
- [ ] `argparse` support for running without the GUI
- [ ] Duplicate file detection
- [ ] JSON-based configuration for custom categories
- [ ] Undo last organization

## License

This is a personal learning project — feel free to use it as a reference.
