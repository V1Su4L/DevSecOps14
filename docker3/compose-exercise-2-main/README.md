# todo app

in this demo you need to build a docker-compose file to start this web app

## front end 
### react app application that you need to generate a dockerfile for
### this react app run the 3000 th port 
### use npm i to download all the packages 
### the application depnds on the backend 

## back end 
### node app that you will extract as an image using docker file 
### use npm i to download all the packages 
### this react app run the 3001 th port 
### the application depnds on the mongo db  

## database:
mongo data base 
on port 27017
enviroment variables:

|  MONGODB_INITDB_ROOT_USERNAME  | MONGODB_INITDB_ROOT_PASSWORD |
| ------------------------------ | ---------------------------- |
| appocation                     | any_pass                     |

you need to add volume to the db at - vol name :/data/db

no need for connection string 
use this command to test the compose :
##docker-compose up -d  
