from . import *

def create_json(filename, data):
    if not ".json" in filename:
        filename+=".json"
    jsondata=json.dumps(data, indent=4)
    file=open(filename, "w")
    file.write(jsondata)
    file.close()
