import json
from setting import path, con
"""
Открываем json файл и, в цикле, вносим по одной записи в бд.
Вручную обрабатываем строки так, чтобы подошло под формат (последний столбец самый мудреный).
Все записи, кроме id имеют тип String
"""


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
