# Udacity Item Catalog Project

## Description

I made this program made as part of Udacity Fullstack Development Nanodegree course. The objective is develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## Requirements

- Python 3.6
- All the packages included in requirements.txt
- VirtualBox

## Instructions

1) Go to the project root directory
2) Use the command to install all the packages required to the project
`pip install -r requirements.txt`
3) Change the etc/hosts following the steps in Windows or Mac
`127.0.0.1  mylocaldjangoapp.com`
4) Use the command to start the server
`python manage.py runserver mylocaldjangoapp.com:80`
5) The default username and password for admin panel is:
`webmaster  webmaster1234`
6) Open the browser with URL
`http://mylocaldjangoapp.com/`
7) It is possible to navigate without login, but you can try to login after the first experience

# Editing your /etc/hosts file on a Mac

If you're using a Mac with OS X, to edit your /etc/hosts file, open a Terminal window and run the following command:

`sudo nano /private/etc/hosts`
You may be asked for your password to edit the file. Enter your password.

You can now add entries to the file.

#Editing your /etc/hosts file using Windows

If you're using Windows, to edit your \etc\hosts file, open [SystemRoot]\system32\drivers\etc\hosts and edit the file. (The \etc\hosts file usually exists at %windir%\system32\drivers\etc\hosts.) If the directory and file don't exist, you can create them. Some versions of Windows require that users have admin privileges to create or make changes to this file.
