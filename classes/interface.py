from classes.store import Store
import re

class Terminal:

    def __init__(self, store_name):
      self.Store = Store(store_name)

    def menu(self):
        return (f'== Welcome to Code Platoon Video! ==\n 1. View store video inventory\n 2. View customer rented videos\n 3. Add new customer\n 4. Rent video\n 5. Return video\n 6. Exit\n')

    def customer_data(self):
        account_types = ['sx', 'px', 'sf', 'pf']
        customer_data = {}
        customer_data['id'] = input('Enter customer id:\n')
        while self.Store.get_cust_by_id(customer_data['id']):
            customer_data['id'] = input('\nThis customer ID has already been used. \nPlease enter a different customer ID: ')
        customer_data['account_type'] = input('Enter account type: \n').lower()
        if customer_data['account_type'] not in account_types:
            print('You did not enter a valid account type.')
            return
        customer_data['first_name'] = input('Enter first name: \n')
        customer_data['last_name'] = input('Enter last name: \n')
        customer_data['current_video_rentals'] = ''
        self.Store.add_new_customer(customer_data)

    def rent_video(self, video_title, customer_renting_vid):
        if(not (self.Store.if_video_exists(video_title))):
            print('Please choose a video in our inventory.')
            return 
        customer_info = self.Store.get_cust_by_id(customer_renting_vid)
        selected_video = self.Store.get_video_by_title(video_title)
        cust_account_type = customer_info.account_type
        cust_movies_rented = customer_info.current_video_rentals.split('/')
        video_rating = selected_video.rating
        vid_copies_avail = selected_video.copies_available
        if vid_copies_avail == 0:
            print('No copies are available of this movie.')
            return
        elif (self.Store.if_video_exists(video_title)):
            if cust_account_type == 'sx' or cust_account_type == 'sf':
                if video_rating == 'R' and cust_account_type == 'sf':
                    print('This movie is rated R.')
                    return
                elif cust_movies_rented == ['']:
                    customer_info.current_video_rentals = video_title
                    self.Store.update_all_customers(self.Store.all_customers)
                    selected_video.copies_available = int(selected_video.copies_available) - 1
                    self.Store.update_all_movies(self.Store.video_inventory)
                    return
                else:
                    print('Max amount of rentals alloted.')
                    return
            elif cust_account_type == 'px' or cust_account_type == 'pf':
                if video_rating == 'R' and cust_account_type == 'pf':
                    print('This movie is rated R.')
                    return
                elif len(cust_movies_rented) == 3:
                    print('Max amount of rentals alloted.')
                    return 
                else:
                    if cust_movies_rented == ['']:
                       customer_info.current_video_rentals = video_title 
                    else:
                        customer_info.current_video_rentals = customer_info.current_video_rentals + '/' + video_title
                    self.Store.update_all_customers(self.Store.all_customers)
                    selected_video.copies_available = int(selected_video.copies_available) - 1
                    self.Store.update_all_movies(self.Store.video_inventory)
                    return

    def return_video(self, video_title, customer_renting_vid):
        if(not (self.Store.if_video_exists(video_title))):
            print('That video was not rented out from our store.')
            return
        customer_info = self.Store.get_cust_by_id(customer_renting_vid)
        selected_video = self.Store.get_video_by_title(video_title)
        cust_movies_rented = customer_info.current_video_rentals
        if re.search(rf"[\/]?{video_title}".lower(), cust_movies_rented.lower()):
            if re.search(rf"{video_title}[\/]?".lower(), cust_movies_rented.lower()):
                cust_movies_rented = re.sub(rf"{video_title}[\/]?", '', cust_movies_rented, flags=re.IGNORECASE)
            else:
                cust_movies_rented = re.sub(rf"[\/]?{video_title}", '', cust_movies_rented, flags=re.IGNORECASE)

            customer_info.current_video_rentals = cust_movies_rented
            self.Store.update_all_customers(self.Store.all_customers)
            selected_video.copies_available = int(selected_video.copies_available) + 1
            self.Store.update_all_movies(self.Store.video_inventory)
                
    def run(self):
        while True:
            mode = input(self.menu()) 
            if mode == '1':
                self.Store.get_video_inventory()
            elif mode == '2':
                cust_id = input('Enter customer id: ')
                matching_customer = self.Store.get_cust_by_id(cust_id)
                if not matching_customer:
                    print('This Customer does not exist.')
                else:
                    customers_movies = matching_customer.current_video_rentals.replace('/', ', ')
                    if customers_movies == '':
                        print('This customer has no current rentals.')
                    else:
                        print(f"Current rentals: {customers_movies}")
            elif mode == '3':
                self.customer_data()
            elif mode == '4':
                video_title = input("Video by title: ")
                customer_renting_vid = input("Customer ID: ")
                self.rent_video(video_title, int(customer_renting_vid))
            elif mode == '5':
                video_title = input("Video by title: ")
                customer_renting_vid = input("Customer ID: ")
                self.return_video(video_title, int(customer_renting_vid))
            elif mode == '6':
                break