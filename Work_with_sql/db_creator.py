import json

import psycopg2

from Work_with_sql.setting import path, con

print("Database opened successfully")

cur = con.cursor()
with open(path, "r") as read_file:
    data = json.load(read_file)
    a = []
    b = []
    for j in range(len(data)):
        if j != 0:
            a1 = str(tuple(a)).replace("'", "")
            b1 = str(tuple(b)).replace("{", "'{") \
                .replace("}", "}'") \
                .replace("'type'", "type") \
                .replace("'Point'", "Point") \
                .replace("'coordinates'", "coordinates")
            cur.execute(
                f"INSERT INTO regional_fairs {a1} VALUES {b1}"
            )
        a.clear()
        b.clear()
        for i in data[j].keys():
            a.append(i)
            b.append(data[j][i])

con.commit()
print("Record inserted successfully")

con.close()
