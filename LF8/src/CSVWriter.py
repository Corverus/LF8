import csv
import os
from datetime import datetime
import pandas as pd

def fillCSV(parameter_label, parameter_value):
    filename = os.path.join('../LF8/src/output', 'LF8' + parameter_label + '.csv')
    header = ['datetime', 'value']
    now = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    data = [now, parameter_value]
    with open(filename, 'a', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header
        try:
            df = pd.read_csv(filename)
        except:
            writer.writerow(header)

        # write the data
        writer.writerow(data)
            

for x in range(0, 100, 5):
    fillCSV('ocupied harddrive space', x)