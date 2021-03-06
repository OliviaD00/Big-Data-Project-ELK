
# Big-Data-Project-ELK - Ingestion CSV profile with Nifi
Implementation of the ingestion and analyze of CSV using Nifi and the ELK suite together. 

# Steps to implement the project 

## Installation 

### Install Docker

To install Docker, you can follow this tutorial :  https://docs.docker.com/get-docker/    
On Windows, you can use this one : https://docs.docker.com/docker-for-windows/install/    
Be aware of the RAM that you allocated to Docker, we put 8GO of RAM for images build in Docker. 

### Build an image of Nifi and the ELK suite

For doing that, you can create a image of the ELK suite by run this command in the directory where the Dockerfile is : 

`docker build --tag myelastic .`   

To run the container :  
`docker run -p 9200:9200 -p 9300:9300 -p 5601:5601 -e LOGSTASH=0 -ti -e ES_CONNNECT_RETRY=300 myelastic`

You just created a docker image of the ELK suite according of the configuration of the Dockerfile in this repository.   

Then you can run to launch Nifi in another CMD (terminal) :  
`docker run -p 8080:8080 -v <path localisation of CSV's file>:/input -ti apache/nifi`    

It runs a container of the image that you created (ELK suite) and a container of the Apache Nifi official image. If Elasticsearch doesn't launch, it tries again for 30 times according to the running command of myelastic. 

## Configuration

### Configure Nifi

To configure Nifi, you have to create 5 Processors of Nifi :   
- GetFile (to get CSV) 
- ExecuteScript (to execute a ruby script to convert CSV into JSON array)
- SplitJson (to convert JSON array into individual ones)
- PutElasticsearch (to put into Elasticsearch to the port 9300)
- PutFile (to put failure in file)
   
<img src="img/nifi_csv_config.png">

The configuration is in nifi_csv_config.xml. Once loaded, you just need to put /input in the "input repository" parameter in the properties.   
    
<img src="img/get file config.png">

## Get started 

**1. Make sure that Docker is running and runs two containers : once for the Apache Nifi image and once for ELK suite. If it is not : go back to Installation > Build an image of Nifi and the ELK suite**  

**2. Verify if Elasticsearch is running by checking at http://localhost:9200/**  

<img src="img/localhost screen.png">
  
**3. Then open nifi : http://localhost:8080/nifi/**   

**4. Load the template nifi_csv_config.xml in this subfolder.**    

- For doing that, first upload the template in nifi (after downloaded it in this github)  

<img src="img/upload template nifi.png">

- Then press on the button template, hold it and deposite it lower.

<img src="img/add template nifi.png">

- Then select the template that you want (in this case : tweet_nifi.xml) and click on the buttom add

<img src="img/select template nifi.png">

**6. Then you will have to configure the first processor named Get File by adding your specific input repository** 

<img src="img/get file config.png">

**7. Then you can start the Nifi pipeline by clicking on the button play.**  

<img src="img/start the pipeline.png">

**8. Then ! You can play with Kibana and Elasticsearch :) You will certainly must to create an index pattern on Kibana after sending a few JSON documents**


# Problems encountered

## Docker 

- Max VM is too low for launching Elasticsearch **solved**

In this case, we need to run these two commands to give much space :  
 `wsl -d docker desktop`  
 Then, `systclm -w vm.max_map_count=262144`
  
- Problem of access of the data in the volume defined :
In this case, one must check the path of the volume in the host machine to see if it is correctly written or check access with : https://github.com/docker/for-win/issues/3385

## Others

Some time our solution doesn't work well in the passage to Nifi to Elasticsearch. We don't know why, and in this case, we have to put manually CSV into Elasticsearch via a Python script. 

# Ways to improve 

## To not use Docker

We use Docker to facilitate deployment and sharing but it causes a lot of troubles itself. Maybe, things would have been easier if we didn't use Docker. 
