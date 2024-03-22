#!/bin/bash

if [ -f date.log ]
then
    echo the file already exists
else
    touch date.log
fi