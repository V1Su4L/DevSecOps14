#!/bin/bash

if [ ! -f /usr/bin/figlet ]
then
    apt update && apt  install figlet
fi

figlet "$(uname)"


# if [ [ expr 1 + 6 -eq 11 ] -O [ "ggg" -n  ] ]