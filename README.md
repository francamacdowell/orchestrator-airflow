# Airflow as pipeline orchestrator 
> Example usage and deployment of Airflow scheduling and monitoring workflows with docker-compose.


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

### Build with
I already have mentioned some technologies I used to build this project but not all of them. Therefore, here is a summary of them:

* Python: Programming language which Airflow is used and also used to connect do GCP and manipulate data;
* Pip: Is the package installer for Python
* Airflow: is a platform created by the community to programmatically author, schedule and monitor workflows. In our case, data pipelines.
* Docker and Docker-compose: With Docker we create images to run as containers and packages up code and all its dependencies. Therefore the application runs quickly and reliably from one computing environment to another.
* Cloud Storage: Is an object storage from Google Cloud Platform (GCP) and usually used as Data Lake because of your main characteristics as unlimited storage with no minimum object size, easily transfer and others likely any Hadoop data repository
* YAML files: Is a serialization language often used as a format for configuration files, but its object serialization abilities make it a viable replacement for languages like JSON. In this project we use like a configuration file to build our Airflow DAGs

### Architecture Diagram
This is a fingerprint of project's architecture.

![Project Architecture](/images/project-architecture.png)

We are extracting data from Github, storing on Storage stage called Raw Data exactly as data is find on GitHub. Extracting from Raw Data stage, doing some data manipulations and storing as Python DataFrame in a second stage called Refined Data. All of this with python code orchestrated by Airflow running inside of a Docker Container. 

### Missing Parts

Within this porfolio project I would like to show how to deploy the project in a VM (Compute Engine from GCP or EC2 from AWS).

Also how to update with new code.

## Getting Started

Now we are going to see what we need and what to do to execute this project, which is basically:
* Start a container
* Enter Airflow server
* Control and see your DAGs

### Prerequisites

I'll need these softwares installed:

* Docker: I'm using _version 19.03.12_
* Docker-compose: _version 1.26.2_
* Configure `google_credentials.json`: To access GCP you have to create a project and [generate an service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) by JSON file. Rename by `google_credentials.json` and put on root folder.

### Executing the project
After complete the prerequisites, we are ready to execute the project with a simple command inside project directory:

`sudo docker-compose up --build -d`

#### Docker-compose commands and parameters

* `up`: Builds, (re)creates, starts, and attaches to containers for a service.
* `--build`: Make Docker build images before starting containers.
* `-d`: Detached mode: Run containers in the background, print new container names.

And you're going to have Airflow server running on your *localhost* on *port 8080*

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
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