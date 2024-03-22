#!/bin/bash

dir_name="jenkinsdemo1"
if [ -d $dir_name ]
then
    cd  $dir_name && git pull
else
    git clone https://github.com/devopsPRO27/jenkinsdemo1
fi