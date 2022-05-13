from classes.customer import Customer
from classes.video import Video

class Store:

    def __init__(self, store_name):
        self.store_name = store_name
        self.all_customers = Customer.load_all_customers()
        self.video_inventory = Video.load_all_videos()

    def add_new_customer(self, customer_info):
        self.all_customers.append(Customer(**customer_info))
        Customer.save_customer(customer_info)

    def update_all_customers(self, customers_info):
        Customer.save_all_customers(customers_info)

    def update_all_movies(self, movies):
        Video.save_all_movies(movies)
    
    def get_cust_by_id(self, passed_in_id):
        for customer in self.all_customers:
            if int(customer.id) == int(passed_in_id):
                return customer
        return None

    def if_video_exists(self, title): 
        for video in self.video_inventory:
            if video.title.lower() == title.lower():
                return True
        return False

    def get_video_by_title(self, title): 
        for video in self.video_inventory:
            if video.title.lower() == title.lower():
                return video
        return None

    def get_video_inventory(self):
        print('\n')
        print('**Current Inventory**')
        print('\n')
        for i, video in enumerate(self.video_inventory):
            print(f'Title: {video.title}, Rated: {video.rating}, ID: {video.id}, Release: {video.release_year}, Available: {video.copies_available}')