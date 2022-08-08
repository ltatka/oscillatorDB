import mongoMethods as mm
from pymongo import MongoClient

astr = "mongodb+srv://data:VuRWQ@networks.wqx1t.mongodb.net"
client = MongoClient(astr)
database_names = client.list_database_names()
print(database_names)
# db = client['networks']
db = client.networks
collection = db['networks']
cur = collection.find({})

# modelTypes = ["oscillator", "random"]
#
#
#
#
# currentDB = mm.query_database({})
#
# models = []
#
# min_reactions = 1000
# min_species = 1000
# max_reactions = 0
# max_species = 0
#
# for i, model in enumerate(currentDB):
#     if i%100 == 0:
#         print(i)
#     entry = {
#         "ID": model["ID"],
#         "modelType": model["modelType"],
#         "name": None,
#         "isPublished": False,
#         "author": None,
#         "journal": None,
#         "isEvolved": True,
#         "antimonyModel": model['model'],
#         "numBoundary": None,
#         "numFloat": None,
#         "numSpecies": model['num_nodes'],
#         "numReactions": model['num_reactions'],
#         "addReactionProbabilities": [0.25, 0.25, 0.25, 0.25],
#         "initialReactionProbabilities": [0.1, 0.4, 0.4, 0.1],
#     }
#     try:
#         entry["combinedReactions"] = model["combinedReactions"]
#     except:
#         entry["combinedReactions"] = None
#
#     try:
#         entry['deletedReactions'] = model['deletedReactions']
#     except:
#         entry['deletedReactions'] = None
#
#     try:
#         entry['reactionCounts'] = model['reactionCounts']
#     except:
#         entry['reactionCounts'] = None
#
#     if entry['numSpecies'] < min_species:
#         min_species = entry['numSpecies']
#     if entry['numReactions'] < min_reactions:
#         min_reactions = entry['numReactions']
#     if entry['numSpecies'] > max_species:
#         max_species = entry['numSpecies']
#     if entry['numReactions'] > max_reactions:
#         max_reactions = entry['numReactions']
#
#     models.append(entry)

networkDB = client['meta_data']
collection = db['meta_data']

entry = {'totalModels': 10127,
         'totalOscillators': 2065,
         'totalRandom': 8062,
         'modelTypes': ["oscillator", "random"]}

collection.insert_one(entry)
# for entry in models:
#     collection.insert_one(entry)
#
#
# r = collection.find({})
