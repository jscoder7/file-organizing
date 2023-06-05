# # Python program to explain os.makedirs() method

# # importing os module
# import os

# directory = {"Music":"mp3","Video":"mp4","Document":"txt","Image":"jpg"}
# # criteria = {
#     "Documents": ['pdf', 'doc', 'docx', 'txt', 'rtf', 'odt', 'xls', 'xlsx', 'ppt', 'pptx'],
#     "Music": ['mp3', 'wav', 'flac', 'aac', 'ogg'],
#     "Videos": ['mp4', 'mov', 'avi', 'mkv', 'wmv', 'flv'],
#     "Images": ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'svg', 'tiff'],
#     "Presentations": ['ppt', 'pptx', 'key', 'odp'],
#     "Spreadsheets": ['xls', 'xlsx', 'csv', 'ods'],
#     "Code": ['py', 'java', 'cpp', 'html', 'css', 'js', 'php', 'rb'],
#     "Archives": ['zip', 'rar', 'tar', 'gz', '7z'],
#     "Executable": ['exe', 'msi', 'app', 'dmg'],
#     "Fonts": ['ttf', 'otf', 'woff', 'woff2'],
#     "Backup": ['bak', 'bakup', 'bak1']
# }


# for k,v in directory.items():
#     try:
#         path = os.path.join("C:/Users/CSC/Desktop/Directatory", k)
#         os.makedirs(path)
#         print(f"Directory {k} created successfully" )
#     except OSError as error:
# 	    print(f"Directory {k} can not be created")

"""

import os

print("Welcome to File Organizer!")
print("Organizing Files in Directory: Unorganized Files")

# enter types of directories sepearted by comma
dir_type = input("Enter the types of Directory you wish to create:").split(",")

current_folder_path = os.getcwd()  # Get current directory/folder


print("Creating destination Directories...")
for type in dir_type:
    print(f"- {type.capitalize()}")

for type in dir_type:
    final_path = os.path.join(current_folder_path, type)
    if not os.path.exists(final_path):
        os.makedirs(final_path)
        print(f"The new {type.capitalize()} directory is created!")
    else:
        print(f"The {type.capitalize()} directory already exists.")
"""
# C:/Users/CSC/Desktop/python 7d
import os
 

path = "C:/Users/CSC/Desktop/python 7d"

list = []
# current_path=os.getcwd() gets current path of folder where the script is running

for (root, dirs, file) in os.walk(path):
    for f in file:
        file_name=f.split(".")
        print(f"file name={file_name[0] }, with extention= {file_name[1]}")