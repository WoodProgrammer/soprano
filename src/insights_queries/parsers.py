import os
import yaml
import logging
class Parser(object):
    def __init__(self):
        self.query_path = "/opt/query/queries.yaml"
        self.query_map = []

    def parse_query_list(self):
        with open(self.query_path, "r") as stream:
            try:
                self.query_map = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                logging.error(exc)

        return self.query_map["queries"]