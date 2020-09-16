FROM apache/airflow:1.10.11-python3.7
ENV AIRFLOW_HOME=/home/airflow

USER root
RUN apt-get update -qq && apt-get install git gcc g++ -qqq

USER airflow
WORKDIR /home/airflow
COPY ./requirements.txt /home/airflow/
RUN pip3 install --upgrade pip --user
RUN pip3 install -r /home/airflow/requirements.txt -q --user
