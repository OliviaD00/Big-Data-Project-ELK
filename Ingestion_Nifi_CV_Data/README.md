# Big-Data-Project-ELK - Ingestion CV with Nifi
Implementation of the ingestion and analyse of CV's (PDF files) using Nifi and the ELK suite together. 

# Steps to implement the project 

## Installation 

### Install Docker

To install Docker, you can follow this tutorial :  https://docs.docker.com/get-docker/    
On Windows, you can use this one : https://docs.docker.com/docker-for-windows/install/
Be aware of the RAM that you allocated to Docker, we put 8GO of RAM for images build in Docker. 

### Build an image of Nifi and the ELK suite

For doing that, you can create a image of the ELK suite by run this command in the directory /docker of the project : 

`docker build --tag myelastic .` 

You just created a docker image of the ELK suite according of the configuration of the Dockerfile in this repository.   

Then you can run this command :  
`docker-compose up`    

It runs a container of the image that you created (ELK suite) and a container of the Apache Nifi official image. If Elasticsearch doesn't launch, it tries again for 30 times according of the configuration of the docker-compose.yml in this repository. 

### Prepare the parser 
 

## Configuration

### Configure Nifi

To configure Nifi, you have to create 5 Processors of Nifi :   
- GetTwitter (to collecte tweets with identifiants),   
- EvaluateJsonPath (used to check if there is a text field present in tweets, if not it will not passed it), 
- RouteOnAttribute (check if the text field is empty or not : if it is empty it will not passed it),   
- JoltTransformJson (execute a script to make a first map of the data),   
- PutElasticsearchHttp (indexs data in Elasticsearch using the previous map).  

*photo pb Twitter flow*  

The configuration is in tweet_nifi.xml. Once loaded, you just need to put your own twitter developers account identifiant (key consumers and token keys) in Properties of the Component GetTwitter "Ingest Tweets from Public Feed".     

*photo config of component GetTwitter*  

## Get started 

**1. Make sure that Docker is running and runs two containers : once for the Apache Nifi image and once for ELK suite. If it is not : go back to Installation > Build an image of Nifi and the ELK suite.**
**2. Verify if Elasticsearch is running by checking at http://localhost:9200/  **

*ajouter une image de localhost screen*  
  
**4. Then open nifi : http://localhost:8080/nifi/**  
**5. Load the template parser.json.xml in this subfolder.**    
- For doing that, first upload the template in nifi (after downloaded it in this github)  

*ajouter l'image upload template nifi*  

- Then press on the button template, hold it and deposite it lower.

*ajouter l'image add template nifi*

- Then select the template that you want (in this case : tweet_nifi.xml) and click on the buttom add

*ajouter l'image select template nifi*

**6. Then you will have to configure the first processor named Get File (GetTwitter Processor) by adding your specific input repository 

*ajouter l'image getFile config*  

**7. Then you can start the Nifi pipeline by clicking on the button play.**  

*ajouter l'image start the pipeline*  

# Some results

Here, we can see some screen about visualisations and Dashboard that we make with test CV. 

## Make powerful queries 

*ajouter l'image quering data*    

*ajouter l'image test 3*    

## Make some dashboard 

*ajouter l'image test 1*   

*ajouter l'image test 2*   

# Problems encountered

## Docker 

- Max VM is too low for launching Elasticsearch **solved**

In this case, we need to run these two commands to give much space :  
 `wsl -d docker desktop`  
 Then, `systclm -w vm.max_map_count=262144`
  
- Problem of access of the data in the volume defined :
In this case, one must check the path of the volume in the host machine to see if it is correctly written or check access with : https://github.com/docker/for-win/issues/3385

## Parser 

The parser is not perfect. It didn't take into account special characters and it can split content of the CV not correctly sometimes (like taking an intership as a skill, or taking a name as a experience). 

## Others

Some time our solution doesn't work well in the passage to Nifi to Elasticsearch. We don't know why, and in this case, we have to put manually parsed PDF into JSON document into Elasticsearch (via Dev Tools from Kibana) with the command `POST cv_parser/_doc/NOM_Prenom`

# Ways to improve

## Find a way to directly parsed data with Nifi

We could try to execute directly a script with Nifi in order to parser data from PDF into JSON document. But it will take some time to define regular expressions and things like that. 
For doing that, we try this configuration of Nifi (as a beginning) :   

*ajouter l'image CV nifi config version 2* 

## Check each Processor one by one of Nifi with a Processor Putfile

In order, to check where exactly it goes wrong, we can check each processor output (if failure) in a file (Processor Putfile). 

## To not use Docker

We use Docker to facilate deployment and sharing but it causes a lot of troubles itself. Maybe, things would have been easier if we didn't use Docker. 

