import os
import shutil
import calendar
from datetime import datetime

def OrganizeDirectory(sourcePath, fileIgnore, fileMapping, fileDirectories):
    # Check Directory
    if os.path.isdir(sourcePath):

        for file in os.listdir(sourcePath):
            filePath = os.path.join(sourcePath, file)

            if os.path.isfile(filePath) and not (file in fileIgnore):
                #Get File Extension
                fileExt = str(os.path.splitext(filePath)[1])

                # Get File Type
                fileType = "Others"
                for  key, value in fileMapping.items():
                    if fileExt in value:
                        fileType = key

                # Identify Destination Folder
                destinationFolder = fileDirectories[fileType]
                currentMonth = datetime.now().month
                currentYear = datetime.now().year

                destinationFolder += "/" + str(currentYear)
                # Check Year Folder
                if os.path.exists(destinationFolder):
                    destinationFolder += "/" + calendar.month_name[currentMonth]
                    # Check Month Folder
                    if not os.path.exists(destinationFolder):
                        os.mkdir(destinationFolder)
                else:
                    # Create Folders
                    os.mkdir(destinationFolder)
                    destinationFolder += "/" + calendar.month_name[currentMonth]
                    os.mkdir(destinationFolder)

                destinationPath = os.path.join(destinationFolder, file)

                # Move File
                shutil.move(filePath, destinationPath)

    else:
        print("Directory: " + sourcePath + " does not exist!")


# File Type Mapping
fileMapping = {
    "Document": [".txt", ".doc", ".docx", ".odt", ".rtf", ".pdf", ".key", ".ppt", ".pptx", ".csv", ".xls", ".xlsx", ".xlsm"],
    "Media": [".bin", ".vcd", ".ai", ".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".png", ".svg", ".mp3", ".mp4"],
    "Code": [".aspx", ".html", ".css", ".js", ".php", ".py", ".c", ".cgi", ".cs", ".vb", ".sh"],
    "Package": [".7z", ".pkg", ".rar", ".zip", ".msi", ".exe", ".gadget", ".jar"],
    "Data": [".dta", ".db", ".log", ".sav", ".sql", ".tar", ".xml"],
    "System": [".bak", ".cfg", ".dll", ".sys", ".tmp", ".drv"]
}

# Destination Paths
fileDirectories = {
    "Document": "/Users/ahbaooo/Downloads/Documents",
    "Package": "/Users/ahbaooo/Downloads/Packages",
    "System": "/Users/ahbaooo/Downloads/System",
    "Others": "/Users/ahbaooo/Downloads/Others",
    "Media": "/Users/ahbaooo/Downloads/Media",
    "Data": "/Users/ahbaooo/Downloads/Data",
    "Code": "/Users/ahbaooo/Downloads/Code"
}

# Files to Ignore
fileIgnore = [".DS_Store", ".localized"]

# Run Script
directoryToOrganize = "/Users/ahbaooo/Downloads"
OrganizeDirectory(directoryToOrganize, fileIgnore, fileMapping, fileDirectories)
