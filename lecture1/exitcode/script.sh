#!/bin/bash

git clone https://github.com/devopsPRO27/jenkinsdemo1/invitations
ec=$?

echo "the exit code is -> $ec "

if [ $ec -gt 0 ]
then 
    apt update && apt install git
fi