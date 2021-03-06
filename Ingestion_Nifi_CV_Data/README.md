
# Big-Data-Project-ELK - Ingestion CV with Nifi
Implementation of the ingestion and analyse of CV's (PDF files) using Nifi and the ELK suite together. 

# Steps to implement the project 

## Installation 

### Install Docker

To install Docker, you can follow this tutorial :  https://docs.docker.com/get-docker/    
On Windows, you can use this one : https://docs.docker.com/docker-for-windows/install/   
Be aware of the RAM that you allocated to Docker, we put 8GO of RAM for images build in Docker. 

### Build an image of Nifi and the ELK suite

For doing that, you can create a image of the ELK suite by run this command in the directory where the Dockerfile is located : 

`docker build --tag myelastic .`   

To run the container :  
`docker run -p 9200:9200 -p 9300:9300 -p 5601:5601 -e LOGSTASH=0 -ti -e ES_CONNNECT_RETRY=300 myelastic`

You just created a docker image of the ELK suite according of the configuration of the Dockerfile in this repository.   

Then you can run to launch Nifi in another CMD (terminal) :  
`docker run -p 8080:8080 -v <path localisation of CV's file>:/input -ti apache/nifi`    

It runs a container of the image that you created (ELK suite) and a container of the Apache Nifi official image. If Elasticsearch doesn't launch, it tries again for 30 times according of the running command of myelastic.

### Prepare the parser 

The parser will help to split the CV into several attributes looking for regular expressions (like experiences, skills, education...). We use one which was already developed : https://github.com/antonydeepak/ResumeParser.git .    

#### Build the image with Dockerfile

On the repository /parser, you have to build the image with the following command :
`docker build --tag parser .`

To run the container : 
`docker run -v <path localisation of CV's file>:/input -ti parser`

#### Modify the key words
The key words can be modify in the file « gazetteer » in the repository : ResumeParser/GATEFiles/plugins/ANNIE/resources/gazetteer/   
You can modify it with `notepad` or `nano`.    

#### Use the parser
On the repository ResumeParser/ResumeTrasducer, you have to : 

**1. Have a file of format PDF to parse**  

**2. Run the command :** 

```
> java -cp '.\bin\*;..\GATEFiles\lib\*;..\GATEFILES\bin\gate.jar;.\lib\*' code4goal.antony.resumeparser.ResumeParserProgram <input_file> [output_file]
```

**3. Take back the JSON created and put it in the path localisation of the host given to Nifi** 

## Configuration

### Configure Nifi

To configure Nifi, you have to create 4 Processors of Nifi :   
- GetFile (to get CV) 
- EvaluateJsonPath (to try to check if there is JSON)
- Attributes to JSON (to try to associate field to attribute)
- PutElasticsearch (to put into Elasticsearch to the port 9300)

We can imagine a version with only GetFile and PutElasticsearch.

<img src="img/cv nifi config.png">

The configuration is in parserJson.xml in the repository /parser. Once loaded, you just need to put /input in the "input repository" parameter in the properties.   

<img src="img/get file config.png">

## Get started 

**1. Make sure that Docker is running and runs three containers : once for the Apache Nifi image, once for the parser and once for ELK suite. If it is not : go back to Installation > Build an image of Nifi and the ELK suite, then prepare the parser**  

**2. Verify if Elasticsearch is running by checking at http://localhost:9200/**  

<img src="img/localhost screen.png">

**3. Use the parser to split CV (take a look at part Prepare the parser)**
  
**4. Then open nifi : http://localhost:8080/nifi/**   

**5. Load the template parserJson.xml in this subfolder.**    

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

**8. Then ! You can play with Kibana and Elasticsearch :) You might have to create an Index Partern on Kibana, once you loaded some JSON documents.** 

# Some results

Here, you can see some screen about visualisations and Dashboard that we make with test CV. 

## Make powerful queries 
 
<img src="img/quering data.png">
  
<img src="img/test 3.png">

## Make some dashboard 

<img src="img/test 1.png">

<img src="img/test 2.png">

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

<img src="img/cv nifi config version 2.png">

## Check each Processor one by one of Nifi with a Processor Putfile

In order, to check where exactly it goes wrong in the Dataflow with Nifi, we can check each processor output (if failure) in a file (Processor Putfile). 

## To not use Docker

We use Docker to facilitate deployment and sharing but it causes a lot of troubles itself. Maybe, things would have been easier if we didn't use Docker. 

