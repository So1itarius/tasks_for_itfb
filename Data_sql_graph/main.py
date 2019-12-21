from setting import con
import matplotlib.pyplot as plt

cur = con.cursor()

cur.execute("select district, count(periodofplacement) as count_f from regional_fairs group by district")
rows = cur.fetchall()
x = []
y = []
for row in rows:
    print(row)
    x.append(row[0])
    y.append(row[1])
con.close()
fig, ax = plt.subplots()

ax.bar(x, y)

ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(100)  # ширина Figure
fig.set_figheight(6)  # высота Figure


if __name__ == "__main__":
    """
    Бд создается предварительно в DB Browser и помещается в папку проекта. Также при помощи DB Browser создается 
    таблица regional_fairs (scheme.txt) с колонками, ранвыми шапке наименований из файла. Файл db_inserter.py 
    заполняет базу данными из скаченного файла. На данный момент бд заполнена нужными данными. 
    """
    # рисуем зависимость: Район и количество ярмарок
    plt.show()
