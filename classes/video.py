from classes.csvhelp import CsvHelper

class Video:
    File_Path = "../data/inventory.csv"

    def __init__(self, id, title, rating, release_year, copies_available):
        self.id = id
        self.title = title
        self.rating = rating
        self.release_year = release_year
        self.copies_available = copies_available

    @classmethod
    def load_all_videos(cls):
        return CsvHelper.read_all(cls.File_Path, cls)

    @classmethod
    def save_all_movies(cls, movies):
        return CsvHelper.write_all(cls.File_Path, movies)