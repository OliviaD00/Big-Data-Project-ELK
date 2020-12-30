# Big-Data-Project-ELK - Ingestion Tweets with Nifi
Implementation of the ingestion and analyze of tweets using Nifi and the ELK suite together. We develop which part of the Architecture of the project, we success to test and which part we still have to focus on. But, our tests give a view of what can be done and help us to learn a lot about Nifi. 

# Steps to implement the project 

## Installation 

### Install Docker

To install Docker, you can follow this tutorial :  https://docs.docker.com/get-docker/    
On Windows, you can use this one : https://docs.docker.com/docker-for-windows/install/
Be aware of the RAM that you allocated to Docker, we put 8GO of RAM for images build in Docker. 

### Build an image of Nifi and the ELK suite

For doing that, you can create a image of the ELK suite by run this command in the directory ./docker of the project : 

`docker build --tag myelastic .` 

You just created a docker image of the ELK suite according of the configuration of the Dockerfile in this repository.   

Then you can run this command :  
`docker-compose up`    

It runs a container of the image that you created (ELK suite) and a container of the Apache Nifi official image. If Elasticsearch doesn't launch, it tries again for 30 times according of the configuration of the docker-compose.yml in this repository. 

### Ask for a Twitter developer account 

For getting and aggregate tweets content, you need a Twitter developer account.  
If you don't have one, you will have to create one here : https://developer.twitter.com/en/apply-for-access by submetting and answering questions of a form. 

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

### Configure index on Elasticsearch via Kibana

In order to correctly load data, we have to create an index in Elasticsearch.   
We will create it with this following command :   

``` 
PUT /tweets

{
      "mappings" : {
        "properties" : {
          "created_at" : {
            "type" : "date",
			"format": "E MMM dd HH:mm:ss z yyyy||E MMM dd HH:mm:ss Z yyyy",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "favorited" : {
            "type" : "boolean"
          },
          "id_str" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "lang" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "possibly_sensitive" : {
            "type" : "boolean"
          },
          "retweeted" : {
            "type" : "boolean"
          },
          "source" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "text" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "url_0" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "url_1" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "url_2" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "url_3" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "url_display_0" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "url_display_1" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "url_display_2" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "url_display_3" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "url_expanded_0" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "url_expanded_1" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "url_expanded_2" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "url_expanded_3" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "user_created_at" : {
            "type" : "date",
			"format" : "E MMM dd HH:mm:ss z yyyy||E MMM dd HH:mm:ss Z yyyy"
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "user_description" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "user_favourites_count" : {
            "type" : "long"
          },
          "user_followers_count" : {
            "type" : "long"
          },
          "user_friends_count" : {
            "type" : "long"
          },
          "user_id_str" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "user_listed_count" : {
            "type" : "long"
          },
          "user_name" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "user_screen_name" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "user_verified" : {
            "type" : "boolean"
          }
        }
      }
    }
  }
}

```

## Get started 

**1. Make sure that Docker is running and runs two containers : once for the Apache Nifi image and once for ELK suite. If it is not : go back to Installation > Build an image of Nifi and the ELK suite.**
**2. Verify if Elasticsearch is running by checking at http://localhost:9200/  **

*ajouter une image de localhost screen*  

**3. Put an index in Kibana. For that, you have to go to http://localhost:5601/app/dev_tools#/console. In Dev Tools, you have to put a new Index named "tweets" (see Configuration > Configure index on Elasticsearch via Kibana).**    
Submit it and look if you get this message in response :  
```
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "tweets"
}
```
*ajouter une image de Kibana index tweets*  
**4. Then open nifi : http://localhost:8080/nifi/**  
**5. Load the template tweet_nifi.xml in this subfolder.**    
- For doing that, first upload the template in nifi (after downloaded it in this github)  

*ajouter l'image upload template nifi*  

- Then press on the button template, hold it and deposite it lower.

*ajouter l'image add template nifi*

- Then select the template that you want (in this case : tweet_nifi.xml) and click on the buttom add

*ajouter l'image select template nifi*

**6. Then you will have to configure the first processor named Ingest Tweets from Public Feed (GetTwitter Processor) by adding our Consumer Key & Secret and Token Access Key & Secret that you can find on your application in your Twitter Developer Account.** 

*ajouter l'image gettwitter config*  

**7. Then you can start the Nifi pipeline by clicking on the button play.**  

*ajouter l'image start the violence*  

# Problems encountered

## Docker 

- Max VM is too low for launching Elasticsearch **solved**

In this case, we need to run these two commands to give much space :  
 `wsl -d docker desktop`  
 Then, `systclm -w vm.max_map_count=262144`
  
## Nifi and Twitter 

- Stay blocked to the step "Drop Invalid Tweets" **not solved** 

In this case, we say blocked to the processor of Nifi that says "if there is no text in the tweets (= empty) don't forward it". So, it might be the keys of twitter account authentification (maybe they were not totally actives when we make the tests) that have a little problem.

*photo pb Twitter flow (encore une fois)*

- Time to have access

Speaking about keys, we take **more than 10 days** to obtain our twitter developer accounts, which gives use the keys needed to connect and to use the processor "GetTwitter" of Nifi. Twitter needed more informations about our project. 

# Ways to improve

## Use another method
On the architecture illustration of the project, we want to display information of tweet's content in Slack. It is possible but we need to use another method for doing that. We need to use OpenDistro version of Elasticsearch (available with AWS image of Elasticsearch).
All files (nifi configuration and docker-compose.yml) about this method are in /OpenDistroMethod.   

In this case, Nifi configuration is a little different : 

*ajouter l'image other_config_twitter_nifi*

In Kibana, in Devtools, the index will be also different : 

```
{
  "properties": {
    "created_at": {
      "type": "date",
      "format": "EEE MMM dd HH:mm:ss Z yyyy"
    },
    "retweeted_status.created_at": {
      "type": "date",
      "format": "EEE MMM dd HH:mm:ss Z yyyy"
    },
    "user.created_at": {
      "type": "date",
      "format": "EEE MMM dd HH:mm:ss Z yyyy"
    },
    "retweeted_status.user.created_at": {
      "type": "date",
      "format": "EEE MMM dd HH:mm:ss Z yyyy"
    },
    "coordinates.coordinates": {
      "type": "geo_point"
    },
    "place.bounding_box": {
      "type": "geo_shape",
      "coerce": true,
      "ignore_malformed": true
    }
  }
}
```

But with this method, we get an error : "Unable to revice connection : https://localhost:9200/". We find on Internet that it will be linked to the certificates of even if we disable SSL. 

## Check each Processor one by one of Nifi with a Processor Putfile

In order, to check where exactly it goes wrong, we can check each processor output (if failure) in a file (Processor Putfile). 

## To not use Docker

We use Docker to facilate deployment and sharing but it causes a lot of troubles itself. Maybe, things would have been easier if we didn't use Docker. 

