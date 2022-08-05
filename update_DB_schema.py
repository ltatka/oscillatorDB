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

modelTypes = ["oscillator", "random"]

for modelType in modelTypes:

    currentDB = mm.query_database({"modelType": modelType})

    models = []

    for i, model in enumerate(currentDB):
        entry = {
            "ID": model["ID"],
            "modelType": model["modelType"],
            "name": None,
            "isPublished": False,
            "publishingInfo": {"author": None,
                               "Journal": None},
            "isEvolved": False,

            "antimonyModel": {"antString": model["model"],
                              "numBoundary": None,
                              "numFloat": None,
                              "numSpecies": model["num_nodes"],
                              "numReactions": model["num_reactions"]},
        }
        if modelType == "random":
            entry["evolutionInfo"] = None
        else:
            try:
                entry["evolutionInfo"]: {"combinedReactions": model["combinedReactions"],
                                         "deletedReactions": model["deletedReactions"],
                                         "addReactionProbabilities": model["addReactionProbabilities"],
                                         "initialReactionProbabilities": model["initialProbabilities"],
                                         "reactionCounts": None
                                         }
            except:
                entry["evolutionInfo"]: {"addReactionProbabilities": [0.25, 0.25, 0.25, 0.25],
                                         "initialReactionProbabilities": [0.1, 0.4, 0.4, 0.1],
                                         "combinedReactions": None,
                                         "deletedReactions": None,
                                         "reactionCounts": None
                                         }
            try:
                entry["evolutionInfo"]["reactionCounts"] = model["reactionCounts"]
            except:
                pass

        models.append(entry)
    networkDB = client['networkDB']
    collection = db['networkDB']
    if modelType == "oscillator":
        entry_all = {
            "dbName": "networkDB",
            "allModelTypes": ["oscillator", "random"],
            "models": models,
            "totalModels": len(models)
        }
        collection.insert_one(entry_all)
    else:
        r = collection.find({})

        oldLen = r[0]["totalModels"]
        newVals = { "$set": {'models': r[0]['models']+models, "totalModels": len(models)+oldLen}}

        collection.update_one({"dbName":"networkDB"}, newVals)

