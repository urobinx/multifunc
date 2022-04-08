import json
from kafka import KafkaProducer


def producer_primes(ls=None):
    producer = KafkaProducer(bootstrap_servers="39.103.166.17",
                             value_serializer=lambda m: json.dumps(m).encode("utf8"))
    producer.send("primes", ls)
    producer.flush()


if __name__ == "__main__":
    pass
