# Big-Data-Project-ELK
This a Project for the ING5 Class of Big Data at ECE Paris;
Members of the group : Alexis DIREZ, Neil SEGARD, Olivia DALMASSO

The project has to focus on Open Source distributed systems. For doing that we choose ElasticSearch (a plateform distributed systems). 

# Progress of the project
We test several uses cases and technologies with Elasticsearch. 
The goal was to implement Elasticsearch with two others Open Source distributed systems : Nifi (Dataflow system) and Kafka. 
We present our technical results in the several branches of this project. But the architecture/design is presented here in the main. 

# All technologies involved in our project and its uses cases

## Elasticsearch

*ajouter le logo d'Elasticsearch en image sur le read.me* 

Elasticsearch is a distributed, open source search and analytics engine for all types of data. It provides a distributed, multitenant-capable full-text search engine, it uses JSON documents to store Data. It allows some powerful queries with a system of score and a lot of possibilities of aggregation. It is developed in Java. It is often used with the ELK suite (Elasticsearch - Logstash - Kibana), allowed this distributed open source engine to complete extract-load-transform actions, aggregations and storage of documents and at the end monitoring and data vizualisation : a complete and flexible tool ! 

## Kibana

*ajouter le logo de Kibana en image sur le read.me* 

Kibana is the Datavisualisation tool of the ELK suite. It allows us to create some visualisations and Dashboard (quite useful for monitoring) with data loaded on Elasticsearch. Kibana gives us also the possibility to implement Machine Learning on the Datasets to try to make some previsions. 

## Logstash and beats

*ajouter le logo de Logstash et de beats en image sur le read.me* 

Logstash can be assimilate as the ETL of the ELK suite. It collectes, transforms and analyses logs. Beats are transfert agents which allow to centralize logs and files. It uses modules that provide modele for ingestion and indexation of classic type of data. Beats can be used as ingest pre-process pipelines and can be used like Kafka. Beats can directly communicate with Elasticsearch or pass data into Logstach in order to continue the transformation of the data. 

## Nifi

*ajouter le logo de Nifi en image sur le read.me* 

Apache NiFi is a software project used to automate the flow of data between software systems (Dataflow system). It can also be used as an ETL Extract, transform and load data. It was developed by the NSA then open-sourced. 
Nifi uses template, processors to describe relations between software systems. It offers some specifics features which can help to provide security using TLS encryption, the ability to operate within clusters... 
Nifi, as a Dataflow systems, can schedule the flow of data between software systems using classic schedule methods : round robin, FIFO, LIFO...

## Docker

*ajouter le logo de Docker en image sur le read.me* 
Docker is a open source software that gives the possibility to launch applications and software using images and containers. Images are version of applications and softwares. One can find a lot of existing images in the Docker Hub (open library for container images from applications, software and open source projects). When you launch an image, you create a container. Each containers uses an operating system and has a part of memory allowed. Docker has specifics features which can let containers use volume in the host machine, and others features useful (improving security...). Docker is used to deploy software rapidly. 

## Kafka 

*ajouter le logo de Kafka en image sur le read.me* 
*à développer en fonction de vos recherches*
Kafka is a open source distributed streaming platform, used since 2012. It uses messaging agents and it is written in Scala. Kafka can be used as an messaging, streaming, dataflow of data system in real time. 

# Uses cases

## Ingestion of data in ElasticSearch with Nifi

### Description of the Use Case

Companies use cases : I want to load, extract, transform data with ingestion pipelines and make some dataflow with only one tool and then analyse, make some queries on a search engine platform. 

#### Ingestion of CV's Data

#### Ingestion of tweets in the filed of Big Data

#### Ingestion of CSV

### Technologies involved



### Architecture of the project 

*ajouter les images du drive sur le read.me for each category*

#### Ingestion of CV's Data

#### Ingestion of tweets in the filed of Big Data

#### Ingestion of CSV

### Implementation of Code (Technical projects)

It will be explained in each branch (with steps to implement it and a list of problems encountered) : 
- Branch Ingestion of CV's Data
- Branch Ingestion of Tweets in the field of Big Data
- Branch Ingestion of CSV (People Profile)

## Monitoring of logs with Kafka and Elasticsearch

### Description of the Use Case

### Technologies involved

For this use case, 


### Architecture of the project 

*ajouter l'image du drive sur le read.me*

### Implementation of Code 

It will be explained (with steps to implement and a list of problems encountered) in the branch Monitoring_Log_Kafka.

## Sources 

- Documentation for Elasticsearch
- Documentation for Docker
- Documentation for Nifi 
- Documentation for Kafka
- Basic Documentation for Syslog
- Some tutoriels designed by the community : 
..- 
..-
..-
..- 

