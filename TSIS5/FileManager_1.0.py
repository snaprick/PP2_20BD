import os
import os.path
import time 
import shutil
from pathlib import Path

path = os.getcwd()

def Menu():
    print("1. Files")
    print("2. Directories")
    print("3. Exit")

def DirMenuChoices():
    print("0. Back")
    print("1. Content")
    print("2. Rename Directory")
    print("3. Number of files")
    print("4. Number of directories")
    print("5. Add file")
    print("6. Add new directory")

def FileMenuChoices():
    print("0. Back")
    print("1. Delete file")
    print("2. Rename File")
    print("3. Add content")
    print("4. Rewrite content")
    print("5. Return to the parent directory")

def ContentOfDir():
    content = os.listdir(curDir)
    for i in content:
        print(i)
def delete():
    print('Write the name of file')
    try:
        file = str(input())
        os.remove(file)
        print('File deleted')
    except FileNotFoundError:
        print('File not found')
def rename():
    print("Enter name of file")
    try:
        source = str(input())
        print('Enter the new name')
        dest = str(input())
        os.rename(source, dest)
    except FileNotFoundError:
        print("File not found")
def return_to_parent():
    print("Enter full path")
    try:
        file = str(input())
        path = Path(file).parent
        print(path)
    except FileNotFoundError:
        print("File not found")
def add():
    print('Enter the name of file to add data')
    try:
        file = str(input())
        with open(file, 'a') as file:
            file.write(str(input()))
        print('Data added successfully')
    except FileNotFoundError:
        print('File not found')
def rewrite():
    print('Enter the name of file to rewrite data')
    try:
        file = str(input())
        with open(file, 'w') as file:
            file.write(str(input()))
        print('Data rewrited successfully')
    except FileNotFoundError:
        print('File not found')
def rename_dir():
    print('Enter the name of directory')
    try:
        name = str(input())
        print('Enter the new name of directory')
        new = str(input())
        os.rename(name, new)
        print('Directory renamed successfully')
    except FileNotFoundError:
        print('Directory not found')
def number_of_files():
    cnt = 0
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                cnt += 1
    print('Number of files in directory = {}'.format(cnt))
def number_of_dir():
    with os.scandir(path) as entries:
        cnt = 0
        for entry in entries:
            if entry.is_dir():
                cnt += 1
    print('Number of directories in directory = {}'.format(cnt))
def list_content():
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                print(entry.name)
            if entry.is_dir():
                print(entry.name)
def create_dir():
    print('Enter the name of new directory')
    dir_name = str(input())
    os.mkdir(dir_name)
    print('Directory created successfully')

def create_file():
    print('Enter the name of new file')
    name = str(input())
    with open(name, "w") as file:
        print('File created successfully')
        file.close() 
print("FileMan v1.0")
while(True):
    curDir = os.getcwd()
    Menu()
    print(f'Current working directory is: {curDir}')
    Fchoice = int(input("Input:  "))

    if Fchoice == 1:
        FileMenuChoices()
        Schoice = int(input("Input:  "))
        if Schoice == 1:
            delete()
        if Schoice == 2:
            rename()
        if Schoice == 3:
            add()
        if Schoice == 4:
            rewrite()
        if Schoice == 5:
            return_to_parent()
        else:
            continue
    if Fchoice == 2:
        DirMenuChoices()
        Schoice = int(input("Input:  "))
        if Schoice == 1:
            list_content()
        if Schoice == 2:
            rename_dir()
        if Schoice == 3:
            number_of_files()
        if Schoice == 4:
            number_of_dir()
        if Schoice == 5:
            create_file()
        if Schoice == 6:
            create_dir()
        else:
            continue
    if Fchoice == 3:
        print("Goodbye")
    else:
        continue