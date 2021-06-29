# oscillatorDB

## Set Up
This module requires:
* PyMongo
* dnsPython

These can be installed via pip or conda. Alternatively, environment.yml is a conda environment containing all the necessary packages. To use it:
```
conda env create -f environment.yml
conda activate oscillatorDB
```
## Database Description

The data base stores:
*ID: model's ID number (str)
*num_nodes: number of species (int)
*num_reactions: number of reactions (int)
*model: antimony string for the model
*oscillator: If the model oscillates or not (boolean). True if does, False if it does not. String 'damped' if the model is damped.

## Connecting to MongoDB
After importing mongoMethods, establish a connection to the database and access the data.
```
import mongoMethods as mm

connection = mm.get_connection()
col = mm.collection
```
## Queries

Queries are specified by a dictionary containing the traits of interest. There are two query helper methods in the module to get a list of IDs or the antimony strings of models that match the query. 
```
import mongoMethods as mm

connection = mm.get_connection()
col = mm.collection

# Get IDs of oscillators with 3 nodes
query = { "num_nodes" : 3, "oscillator" : True)}
model_IDS = get_ids(query)

# Get antimony string for model 12345
query = { "ID" : "1234" }
ant = get_antimony(query)
```

The collection can also be directly queried. Importing mongoMethods is still required to access the database.
```
import mongoMethods as mm

connection = mm.get_connection()
col = mm.collection

# Get oscillators with 3 nodes and 5 reactions
query = { "num_nodes" : 3, "num_reactions" : 5, "oscillator" : True }
entries = collection.find(query)

# Get the IDs of models that match the query
for entry in entries:
    print(entry['ID'])
```

