# Airflow as Pipeline Orchestrator 
> Example of usage and deployment of Airflow scheduling and monitoring workflows with docker-compose.

![Airflow Webserver](/images/airflow-webserver.png)

## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
  * [Architecture Diagram](#architecture)
  * [Missing parts](#missing-parts)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Executing the project](#installation)
* [Contributing](#contributing)
* [Acknowledgements](#acknowledgements)

## About the project

Project showing an example of how to build a production [Airflow](https://airflow.apache.org/) with [Docker](https://www.docker.com/), managed by [Docker-compose](https://docs.docker.com/compose/) and using [ELT](https://en.wikipedia.org/wiki/Extract,_load,_transform) pipelines to ingest and move data through [Data Lake](https://aws.amazon.com/big-data/datalakes-and-analytics/what-is-a-data-lake/) stages.

### Build With
I already have mentioned some technologies I used to build this project but not all of them. Therefore, here is a summary of them:

* **Python**: Programming language which Airflow is built and also used to connect to GCP and manipulate data;
* **Pip**: Is the package installer for Python
* **Airflow**: Is a platform created by the community to programmatically author, schedule and monitor workflows. In our case, data pipelines.
* **Docker** and **Docker-compose**: With Docker we create images to run as containers and packages up code and all its dependencies. Therefore the application runs quickly and reliably from one computing environment to another.
* **Cloud Storage**: Is an object storage from Google Cloud Platform (GCP) and usually used as Data Lake because of your main characteristics as unlimited storage with no minimum object size, easily transfer and others likely any Hadoop data repository
* **YAML file**: Is a serialization language often used as a format for configuration files, but its object serialization abilities make it a viable replacement for languages like JSON. In this project we use like a configuration file to build our Airflow DAGs

### Architecture Diagram
This is a fingerprint of project's architecture.

![Project Architecture](/images/project-architecture.png)

We are extracting data **from GitHub**, **storing it on Storage** stage ,called _Raw Data_, exactly as data is found. Extracting from **Raw Data stage**, doing some data manipulations (turning into _tabular data_) and storing on a second stage called _Refined Data_. All with Python code orchestrated by Airflow running inside of a Docker Container. 

### Missing Parts

With this porfolio project, also would like to show how to deploy the project using VM (Compute Engine from GCP or EC2 from AWS).

## Getting Started

What we need and what to do to execute this project, is basically:
* Start a container
* Enter Airflow server
* Control and see your DAGs and tasks

### Prerequisites

Will need:

* Install Docker: I'm using _version 19.03.12_
* Install Docker-compose: _version 1.26.2_
* Configure `google_credentials.json`: To access GCP you have to create a project and [generate an service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) by JSON file. Rename by `google_credentials.json` and put on root folder.

### Executing the project
After complete the prerequisites, we are ready to execute the project with a simple command inside project directory:

`sudo docker-compose up --build -d`

Now access on your browser:

`localhost:8080`

#### Docker-compose commands and parameters meaning

* `up`: Builds, (re)creates, starts, and attaches to containers for a service.
* `--build`: Make Docker build images before starting containers.
* `-d`: Detached mode: Run containers in the background, print new container names.

And you're going to have Airflow server running on your *localhost* on *port 8080*

## Contributing

1. Fork it (<https://github.com/francamacdowell/orchestrator-airflow>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Acknowledgements
* [A collection of .gitignore templates](https://github.com/github/gitignore)
* [A good README template](https://github.com/dbader/readme-template)

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki