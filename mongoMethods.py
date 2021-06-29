from pymongo import MongoClient


# user: data
# pwd:  VuRWQ
astr = "mongodb+srv://data:VuRWQ@networks.wqx1t.mongodb.net"
client = MongoClient(astr)
database_names = client.list_database_names()
db = client['networks']
db = client.networks
collection = db['networks']
cur = collection.find({})


def print_entries(cursor=cur, n=None):
    '''
    Prints entries in the database
    :param n: optional, print out the first n entries. By default n is none and all entries are printed.
    :return: print out of every entry dictionary
    '''
    if not n:
        for doc in cursor:
            print(doc)
    else:
        count = 1
        for doc in cursor:
            print(doc)
            if count < n:
                count += 1
            else:
                break

def get_connection():
    '''
    Connect to the mongoDB
    :return: a MongoClient object connected to the database
    '''
    return MongoClient("mongodb+srv://data:VuRWQ@networks.wqx1t.mongodb.net")

def load_lines(path):
    '''
    Load an antimony model from a local machine split into lines
    :param path: path to the .ant file
    :return: Returns the antimony test as a list of strings. Omits the first line if it is a comment.
    '''
    with open(path, "r") as f:
        ant = f.read()
        f.close()
    lines = ant.split('\n')
    # First line is comment for fitness, ignore
    if lines[0].startswith('#'):
        lines = lines[1:]
    return lines

def load_antimony(path):
    '''
    Load an antimony model from a local machine split into lines
    :param path: path to the .ant file
    :return: a single antimony string for the model. Includes all lines including comments.
    '''
    # THIS WILL INCLUDE THE FIRST COMMENTED LINE!
    with open(path, "r") as f:
        ant = f.read()
        f.close()
    return ant

def get_nReactions(ant):
    '''
    Count how many reactions are in the model
    :param ant: antimony strings split by line, usually loaded with load_lines
    :return: integer, number of reactions
    '''
    # Takes a list of strings for each line in ant file
    nReactions = 0
    for line in ant:
        if not line.startswith('var'):
            if line.startswith('k'):
                break
            nReactions += 1
    return nReactions

def get_ids(query):
    '''
    Get the IDs of models that match the query
    :param query: A dictionary of model traits to look for
    :return: A list of IDs (str) for the matching models
    '''
    doc = collection.find(query)
    result = []
    for x in doc:
        result.append(x['ID'])
    return result

def get_antimony(query):
    '''
    Get the antimony string(s) of models that match the query
    :param query: A dictionary of model traits to look for
    :return: If there is only a single matching model, returns the string for that model.
             Otherwise, returns a list of model strings.
    '''
    doc = collection.find(query)
    result = []
    for x in doc:
        result.append(x['model'])
    if len(result) == 0:
        print('No entries found.')
    elif len(result) == 1:
        return result[0]
    else:
        return result

