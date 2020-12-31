
# Big-Data-Project-ELK - Monitoring Log Kafka 
Implementation of the monitoring of logs using Kafka and the ELK suite together. 

# Steps to implement the project 
1. Start zookeeper : `zkserver`
2. Create a new topic in kafka : `kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic logtest`
3. Start the log generator/sender to kafka : `python.exe .\log_generator.py`
4. We can see the logs using the consumer script : `python.exe .\consumerKafka.py`
# Problems encountered
<img src="img/logs_in_consumer.png">

# Ways to improve




