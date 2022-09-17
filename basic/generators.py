import json
import datetime

data = {"jsondate": datetime.datetime(2020, 1, 1, 1, 1, 1).strftime("%Y-%m-%dT%H:%M:%S")}
assert json.dumps(data) == '{"jsondate": "2020-01-01T01:01:01"}', "json failed"
