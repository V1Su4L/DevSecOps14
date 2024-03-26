#!/bin/bash

# Task 1
echo Hello, World!

# Task 2
DATE=$(date '+%m-%d-%Y')
TIME=$(date '+%l:%M %p')
echo "Today's date is $DATE and the time is $TIME"

# Task 3
echo Shell Scripting is Fun!

# Task 4
HOST=$(hostname)
echo "This script is running on \"$HOST\""

# Task 5
if [ -e file_path ]
then
    echo file_path passwords are enabled.
    if [ -w file_path ]
    then
        echo "You have permissions to edit \"file_path\"."
    else
        echo "You do NOT have permissions to edit \"file_path\".".
    fi
else
    echo file_path do NOT exists.
fi

# Task 6
DIR_NAME=dir
if [ -d $DIR_NAME ]
then
    echo "Directory exists"
else
    echo "Directory doesn't exist"
fi

#  Task 7
NUMBER=2
if [ $(($NUMBER % 2)) -eq 0 ]
then
    echo even
else
    echo odd
fi

#  Task 8
USER=lior
if [ w | grep $USER ]
then
    echo $USER
else
    echo No user logged in
fi

#  Task 9
TEXT=""
if [ -z $TEXT ]
then
    echo empty string
else
    echo $TEXT
fi

#  Task 10
PATH='/usr/bin'

echo Enter Package name to install:
read PACKAGE

if command -v $PACKAGE
then
    echo "command  $PACKAGE available , lets run it ."

else
    echo "command  $PACKAGE isnt available ...."
    apt update && apt install  figlet -y
fi

$PACKAGE

#Task 11
echo Enter package name to uninstall
read PACKAGE_NAME

if command -v $PACKAGE_NAME
then
    sudo apt uninstall $PACKAGE_NAM
else
    echo "Package $PACKAGE_NAME does not exist."
fi

# Task 13
echo Enter Directory Path
read DIRECTORY

if [ -d $DIRECTORY]
then
    if [ -z "$(ls -A "$DIRECTORY")" ]
    then
        echo Directory is empty
    else
        echo Directory has files
    fi
fi

# Task 14
echo enter first number
read NUM1
echo enter second number
read NUM2

if [ $NUM1 -gt $NUM2 ]
then
    echo $NUM1
else
    echo $NUM2
fi

# Task 15
mkdir NewDir
cd NewDir

# Task 16
date

# Task 17
echo Enter Process Name
read PROCESS

if [ $(ps -C $PROCESS) > /dev/null ]
then
    echo "The process $PROCESS is running"
else
    echo "The process $PROCESS isn't running".
fi
