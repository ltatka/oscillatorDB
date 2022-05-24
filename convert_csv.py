import json
import csv
with open("/home/hellsbells/projects/oscillator_backup/networks.json") as json_file:
    data = json.load(json_file)


model = data[0]


csv_file = open("/home/hellsbells/projects/oscillator_backup/networks.csv", "w")

csv_writer = csv.writer(csv_file)
header = model.keys()
csv_writer.writerow(header)

for i in range(len(data)):
    model = data[i]

    row = [model["_id"], model["ID"], model["num_nodes"], model["num_reactions"], model["model"], model["modelType"]]
    csv_writer.writerow(row)

csv_file.close()

json_file.close()
