import csv
import os


class CsvHelper:
    File_Path = os.path.abspath(os.path.dirname(__file__))

    @staticmethod
    def get_full_path(filename):
        return os.path.join(CsvHelper.File_Path, filename)

    @staticmethod
    def read_all(filename, ClassName):
        items = []
        with open(CsvHelper.get_full_path(filename), "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for data_dict in reader:
                items.append(ClassName(**data_dict))
        return items

    @staticmethod
    def write_one(filename, item):
        print(item)
        with open(CsvHelper.get_full_path(filename), "a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=item.keys())
            writer.writerow(item)


    def write_all(filename, items):
        if len(items) == 0:
            return
        with open(CsvHelper.get_full_path(filename), "w") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(items[0].__dict__.keys())
            for item in items:
                writer.writerow(item.__dict__.values())