import csv

FILENAME = "weather.csv"


def csv_creater(arr):
    with open(FILENAME, "w", newline="") as file:
        columns = ["weekday", "temperature", "speed", "probability"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(arr)


def csv_reader():
    with open(FILENAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["weekday"], ",", row["temperature"], ",", row["speed"], ",", row["probability"])
