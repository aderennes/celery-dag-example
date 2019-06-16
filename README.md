# Airflow like DAG with Celery and RabbitMQ

## Purpose

I was tired of orchestrating small asynchronous workflows with bash scripts and wanted something a little more sophisticated but not as heavy as Airflow so I gave a shot to [this article from Tony Wang on Medium](https://medium.com/@tonywangcn/how-to-build-docker-cluster-with-celery-and-rabbitmq-in-10-minutes-13fc74d21730#.7e2hlx22g). However it wasn't exactly what I wanted to do so I implemented my own (very similar) method.

## Installation

1. Install Docker on your computer, I recommend installing it with the executable from [Docker's website](https://docs.docker.com/install/). Registration is required but I did run into some trouble installing Docker via brew so that it why I recommend it, however use whatever method that suits you best.
2. Run `docker-compose build` to build the cluster.
3. Run `docker-compose up` to get the cluster running.
4. Call the `run_task.py` script inside your worker using the command `docker exec -it <CONTAINER_ID> python run_tasks.py` where `<CONTAINER_ID>` can be found using `docker ps`.