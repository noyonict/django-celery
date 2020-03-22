# Django-Celery
*Schedular job with Celery and RabbitMQ*
***
*The project contains two Django app*
- **django_celery** - Django Celery is responsible for two iterative tasks named "task_1" and "task_2".  Both tasks contain some dummy code and they will sleep for 2 and 3 seconds respectively. These tasks will run in every second. 

- **progress_bar** - Every 5 seconds ajax call will made by front-end to backend API for progress bar status with the current status of the progress bar. The value of the progress bar will show the front-end progress bar which is provided by API. The status value will be between 0 to 100. If you browse http://127.0.0.1:8000/ then you will see the progress bar status.

# Requirements
```sh
$ celery==4.4.2
$ Django==3.0.4
$ djangorestframework==3.11.0
```

# Installation Guide Using Dockerfile
1. Install docker for windows and mac from (https://www.docker.com/products/docker-desktop)
2. Install Docker on Ubuntu
    ```sh
    $ sudo apt-get update
    $ sudo apt install docker.io
    $ sudo systemctl start docker
    $ sudo systemctl enable docker
    $ docker --version
    ```
2. Follow the commends
    ```sh
    $ git clone https://github.com/noyonict/django-celery.git
    $ cd django-celery
    $ docker-compose build
    $ docker-compose up
    ```
3. Then browse: 127.0.0.1:8000
4. All done
