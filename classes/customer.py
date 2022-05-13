from os import access
from classes.csvhelp import CsvHelper

class Customer:
    File_Path = "../data/customers.csv"

    def __init__(self, id,account_type,first_name,last_name,current_video_rentals):
        self.id = id
        self.account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals

    @classmethod
    def load_all_customers(cls):
        return CsvHelper.read_all(cls.File_Path, cls)

    @classmethod
    def save_customer(cls, new_customer):
        return CsvHelper.write_one(cls.File_Path, new_customer)
    
    @classmethod
    def save_all_customers(cls, customers):
        return CsvHelper.write_all(cls.File_Path, customers)