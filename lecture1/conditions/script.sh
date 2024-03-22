#!/bin/bash

number1=200

if [ $number1 -eq 199 ]  
then
    echo "the condition is True"
    p=1
else
    echo "the number isnt 199"
    p=2
fi

echo $p
# if [ $number1 -eq 200 ]
# then
#     echo "the number isnt 199"
# fi


# -eq -nq  -lt -le -gt -ge    # these are the comparison operators.