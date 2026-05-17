# write csv writer()

import csv

rows =[
        ["name","role"],
        ["kailash","devops"]
]

with open ("users.csv","a") as file:
    writer = csv.writer(file)

    writer.writerows(rows)


