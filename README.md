# Two Container Django App

The simplest app out there. This is a combination of two different Django Applications. The first one is a REST API that pass only a GET request. The other one recieves that request and displays it using an HttpResponse object.

When both the apps run inside two different containers on the same host machine, they share data.

I have used docker compose, so there is no need to add additional network configurations to make these two containers talk. The configuration is written inside the docker-compose.yml file.

The api named **myapi** runs on port 8000 inside the container while it has been mapped to the port 7000 inside the host machine.
The app which calls the api named **minombre** runs on port 8001 inside the container while it has been mapped to the port 70001 inside the host machine.

It is very important to put **127.0.0.1** inside the ALLOWED_HOSTS under settings.py of the api, otherwise it won't be able to send data.