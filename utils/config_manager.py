from . import *

def update_last_access():
    configfile=open("config.json","r")
    jsondict=json.load(configfile)
    jsondict["last_access"]=time.localtime()
    jsondata=json.dumps(jsondict, indent=4)
    configfile.close()
    configfile=open("config.json","w")
    configfile.write(jsondata)
    configfile.close()