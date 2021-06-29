import os
import mongoMethods as mm

'''
Running this script will add new models to the database. There is currently no safeguard to prevent duplicate entries.
You will probably need to edit this depending on how your files are structured.
Please use carefully
'''


connection = mm.get_connection()
col = mm.collection

# Path to models to add
dir = "C:\\Users\\tatka\\Desktop\\Models\\3node_fail\\antimony"
nNodes = 3
oscillator = False

modelList = []
os.chdir(dir)
for filename in os.listdir(dir):
    os.chdir(dir)
    if not filename.endswith('.ant'):
        continue


    ant_lines = mm.load_lines(filename)
    nReactions = mm.get_nReactions(ant_lines)
    ant = mm.load_antimony(filename)

    modelDict = {'ID': filename[11:-4],
                 'num_nodes': nNodes,
                 'num_reactions': nReactions,
                 'model': ant,
                 'oscillator': oscillator}
    modelList.append(modelDict)

col.insert_many(modelList)

