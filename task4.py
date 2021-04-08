import sys
from faker import Faker
import io
import csv

if len(sys.argv) != 3:
    print("Incorect input. Must contain 2 arguments: number of entries and locale (e.g. 10 en_US)")
    exit()
elif not sys.argv[1].isnumeric() or int(sys.argv[1]) < 0:
    print("Incorect input. First argument must be positive integer number (e.g. 10)")
    exit()
elif sys.argv[2] != "en_US" and sys.argv[2] != "ru_RU" and sys.argv[2] != "uk_UA":
    print("Incorect input. Second argument must be locale (en_US or ru_RU or uk_UA)")
    exit()

faker = Faker(sys.argv[2])

for i in range(int(sys.argv[1])):
    output = io.StringIO()
    csvdata = [faker.name(), faker.address(), faker.phone_number()]
    csv.writer(output, lineterminator = "\n").writerow(csvdata)
    print(output.getvalue().replace("\n", " "))