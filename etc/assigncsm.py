
from kafka import KafkaConsumer, TopicPartition

consumer = KafkaConsumer(bootstrap_servers="39.103.166.17")
consumer.assign([TopicPartition(topic="")])