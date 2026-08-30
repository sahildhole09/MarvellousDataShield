# Marvellous Data Shield - Automated Backup & File Monitoring System

## Project Description

Marvellous Data Shield is an "Automated Backup & File Monitoring System" developed in Python. It compares a source directory with a backup directory, detects new and modified files using file hashes, backs up only the changed files, creates a ZIP archive, generates logs and sends the backup report through email.

## Features

- Detects new files in the source directory.
- Detects modified files by comparing file hashes.
- Identifies unchanged files.
- Copies only new and modified files to the backup directory.
- Preserves the directory structure while backing up files.
- Creates a timestamped ZIP archive of the backup.
- Creates daily log files inside the `Log` directory.
- Generates a backup report.
- Sends the backup report through Gmail SMTP.
- Supports automatic/scheduled backups at a specified interval.

## Project Structure

```text
MarvellousDataShield/
│
├── MarvellousDataShield.py
├── DuplicateDetection.py
├── ReportAndLog.py
├── Email.py
├── Data/
│   └── BackupScanner.py
├── Log/
├── Archive/
└── README.md
```

> `Data/BackupScanner.py` is required because `DuplicateDetection.py` imports `GetRelativeFileData` from it.

## Technologies Used

- Python 3
- OS and file-system operations
- SHA/hash-based file comparison through the project's `BackupScanner` module
- `shutil` for file copying and ZIP archive creation
- `schedule` for automatic periodic backups
- `smtplib` and `email.mime.text` for email reporting

## Requirements

Install Python 3.x and the Python package used for scheduling:

```bash
pip install schedule
```

The remaining modules used by the project (`os`, `sys`,`hashlib`, `time`, `shutil`,`smtplib`, and `email`) are part of Python's standard library.

## Installation

1. Clone or download the project.
2. Open a terminal in the project directory.
3. Install the dependency:

```bash
pip install -r requirements.txt
```

4. Make sure the project contains the required `Data/BackupScanner.py` module.
5. Configure the email details in `MarvellousDataShield.py` before running the project.

## Email Configuration

The main program currently contains placeholder values:

```python
SenderEmail = "your_email@gmail.com"
SenderPassword = "app_password"
ReceiverEmail = "receiver_email@gmail.com"
```

Replace them with your Gmail address, Gmail App Password, and receiver email address.

For Gmail SMTP, the project uses:

- SMTP server: `smtp.gmail.com`
- Port: `587`
- TLS encryption

Use a Gmail App Password rather than your normal Gmail password.

## How to Run

The command-line syntax is:

```bash
python MarvellousDataShield.py <SourceDirectory> <BackupDirectory> <Interval>
```

Example:

```bash
python MarvellousDataShield.py Data Backup 5
```

This means:

- `Data` → source directory
- `Backup` → backup directory
- `5` → run the backup every 5 minutes

The program performs one backup immediately and then continuously checks for scheduled backups.

## Working

The backup process works in the following order:

1. Checks whether the source directory exists.
2. Creates the backup directory if it does not exist.
3. Compares source and backup directories.
4. Detects new, modified and unchanged files.
5. Copies new and modified files to the backup directory.
6. Creates a timestamped ZIP archive.
7. Creates a log entry.
8. Generates a backup report.
9. Sends the report through email.
10. Waits for the configured interval and repeats the process.

## Generated Files

### Log

Daily logs are stored in:

```text
Log/DataShield_YYYY-MM-DD.log
```

### Archive

ZIP archives are stored in:

```text
Archive/DataShield_YYYYMMDD_HHMMSS.zip
```

## Example Output

```text
************************************************************
MARVELLOUS DATA SHIELD
Automated Backup & File Monitoring System
************************************************************

NEW FILES : 2
  + file1.txt
  + project/file2.py

MODIFIED FILES : 1
  * report.txt

UNCHANGED FILES : 5

Backed up : file1.txt
Backed up : project/file2.py
Backed up : report.txt

Archive created successfully

Backup Completed Successfully
```

## Important Notes

- The source directory must exist before starting the program.
- The backup directory can be created automatically by the program.
- Only new and modified files are copied during a backup.
- The scheduled backup process keeps running until the program is stopped.
- Keep `MarvellousDataShield.py`, `DuplicateDetection.py`, `ReportAndLog.py`,`Email.py` and the `Data` module in the correct project structure.

## Stopping the Program

Because scheduled monitoring runs continuously, stop it from the terminal using:

```text
Ctrl + C
```

## Author

Name : Sahil Ashok Dhole

Course : Python Automation & Machine Learning

Project : Marvellous Data Shield - Automated Backup & File Monitoring System

**Marvellous Data Shield**

An automated backup and file monitoring project implemented in Python.
