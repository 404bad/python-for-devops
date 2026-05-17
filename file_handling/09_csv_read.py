#CSV file handling

#used for reports, exports, monitoring data

# read csv reader()

import csv

with open ("users.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)




