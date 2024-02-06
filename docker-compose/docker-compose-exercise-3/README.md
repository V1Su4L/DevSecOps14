# docker-compose-exercise

## Project 
### Database
A MySQL database with a script for one  table with movies .

### Webapp
The webapp retrieves the movies from the database and shows them in a HTML page. the server is flask based.

## Exercise
## 1. Running the database and webapp
First create a separate network for the database and webapp by running: `docker network create --driver bridge docker-compose-exercise`

Start the containers by running:
* Database: `docker run -d --name database --net=docker-compose-exercise -e MYSQL_ROOT_PASSWORD=movie123 `
* Webapp: `docker run -d --name webapp --net=docker-compose-exercise -p 8080:80-compose-exercise-webapp`

Open your browser and go to http://localhost:8080. You will now see the movies from the database displayed by the webapp.

## 2. Running with Docker Compose
To run the containers you had to execute 3 commands. It would be easier if we only had to execute one command. We can achieve this by using Docker Compose.

### Creating a docker-compose.yml
Create a docker-compose.yml file to run the webapp and the database. 

Once your created the docker-compose.yml file, run:
```
docker-compose up
```
