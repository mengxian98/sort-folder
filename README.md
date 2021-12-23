# Sort Folder
A Python script to automate the sorting of files in a folder.

## What It Does
The Python script performs the following task:
* Tracks a specific directory for new files
* Identify the file type: *Media*, *Document*, *Data*, ...
* Sorts the file based on its file type
* Create sub-folders based on date added
* Moves the file to the new location

## How to Use
1. Clone this project
2. Update the directory to sort in ```directoryToOrganize```
3. Include any files that should be ignored in ```fileIgnore```
4. Update the destination directories under ```fileDirectories```
5. Setup necessary folders to store the organized files

# Run as Background Process (MacOS)
To run the script as a background process in Mac, use **Automator**. Select a new *Folder Action* workflow and add *Shell Script*:
```
cd "\Users\..."
python cleanfolder.py
```
