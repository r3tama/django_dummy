# django_dummy
A repo for testing Django functionalities

## Installation and usage
You can run the proyect dockerized in a container executing the commands:

`docker-compose build`

And then 

`docker-compose up`

You should then have a container called __django_learning__ running the django server.

## Project Functionality 
The project consists in a polling system that shows you in the index page the 5 most recent polls done:
If you click in one of them you have the option to vote. After voting it will show you the ammounts of votes
  that each option has, and also the posibility to return to the index

You can add polls in the generic admin panel that django provides that is allowed via the /admin url:
localhost:8000/admin 

For accessing the admin panel you will need to create a admin user with the command:
`python manage.py createsuperuser`, you will need to run it in the docker container

You can directly access the shell by executing :
`make shell`

