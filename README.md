# Airflow like DAG with Celery and RabbitMQ

## Purpose

I was tired of orchestrating small asynchronous workflows with bash scripts and wanted something a little more sophisticated but not as heavy as Airflow so I gave a shot to [this article from Tony Wang on Medium](https://medium.com/@tonywangcn/how-to-build-docker-cluster-with-celery-and-rabbitmq-in-10-minutes-13fc74d21730#.7e2hlx22g). However it wasn't exactly what I wanted to do so I implemented my own (very similar) method.

## Installation

1. Install Docker on your computer, I recommend installing it with the executable from [Docker's website](https://docs.docker.com/install/). Registration is required but I did run into some trouble installing Docker via brew so that it why I recommend it, however use whatever method that suits you best.
2. Run `docker-compose build` to build the cluster.
3. Run `docker-compose up` to get the cluster running.
4. Call the `run_task.py` script inside your worker using the command `docker exec -it <CONTAINER_ID> python run_tasks.py` where `<CONTAINER_ID>` can be found using `docker ps`.

## What it do?

Let A1, A2 and B be 3 tasks we need to orchestrate.
- A1 takes 2 seconds to complete
- A2 takes 3 seconds to complete
- B takes 2 seconds to complete

The `run_tasks.py` script launches A1 and A2 in parallel, waits for both to be completed and then launches B. You should be able to see the timestamp for the beginning of those tasks on the `docker-compose up` terminal window and the timestamp for the end of those tasks on the `docker exec` terminal window so you can attest it does work.

The expected behavior is that step A takes 3 seconds (A1 and A2 in parallel) and step B takes 2 seconds.