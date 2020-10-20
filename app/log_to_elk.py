'''
Goal: ship state changes and commands to Elastic cluster
Also append the timestamp to each log doc going to ELK
'''

from elasticsearch import Elasticsearch
from datetime import datetime

class Log_to_elk:
    def __init__(self, data):
        self.hosts = ["127.0.0.1:9200"]
        self.es = Elasticsearch(hosts=self.hosts)
        self.index_name = "sim_logs"

        # assume that the data is in a JSON format
        self.data = data

        self.add_ts_to_data()

        # create the index in case it does not already exist
        self.create_index()

        self.ship_to_elk()


    def create_index(self):
        self.es.indices.create(index=self.index_name, ignore=400)

    def add_ts_to_data(self):
        self.data['timestamp']: datetime.now()

    def ship_to_elk(self):
        res = self.es.index(index=self.index_name, body=self.data, doc_type="_doc")
