import yaml
from yaml import load, load_all
from Formatter import Formatter

pretty = Formatter()

stream = open('sample.yaml','r')

data = load_all(stream, Loader=yaml.FullLoader)

#print(pretty(data))

for doc in data:    
    print("New Document:")
    if type(doc) is list:
        print(pretty(doc))
        #print(doc)
    else:
        print(pretty(doc))
        #for key, value in doc.items():
        #    print(key + ": " + str(value))

