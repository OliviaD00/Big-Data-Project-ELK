

# Big-Data-Project-ELK - Monitoring Log Kafka 
Implementation of the monitoring of logs using Kafka and the ELK suite together. 

# Steps to implement the project 
1. Start zookeeper : `zkserver`
2. Start Kafka (in the kafka folderr) : `.\bin\windows\kafka-server-start.bat .\config\server.properties`
3. Create a new topic in kafka : `kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic logtest`
4. Start the log generator/sender to kafka : `python.exe .\log_generator.py`
5. We can see the logs using the consumer script : `python.exe .\consumerKafka.py`
<img src="img/logs_in_consumer.png">

# Problems encountered

# Ways to improve

