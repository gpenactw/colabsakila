class Actor:
    def __init__(self, actor_id, first_name, last_name, last_update):
        self.actor_id = actor_id
        self.first_name = first_name
        self.last_name = last_name
        self.last_update = last_update
        
class Address:
    def __init__(self, address_id, address, address2, district, city_id, postal_code, phone,location, last_update):
        self.address_id = address_id
        self.address = address
        self.address2 = address2
        self.district = district
        self.city_id = city_id
        self.postal_code = postal_code
        self.phone = phone
        self.location = location
        self.last_update = last_update
        
class Category:
    def __init__(self, category_id, name, last_update):
        self.category_id = category_id
        self.name = name
        self.last_update = last_update

class City:
    def __init__(self, city_id, city, country_id, last_update):
        self.city_id = city_id
        self.city = city
        self.country_id = country_id
        self.last_update = last_update

class Country:
    def __init__(self, country_id, country, last_update):
        self.country_id = country_id
        self.country = country
        self.last_update = last_update

class Customer:
    def __init__(self, customer_id, store_id, first_name, last_name, email, address_id, active, create_date, last_update):
        self.customer_id = customer_id
        self.store_id = store_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address_id = address_id
        self.active = active
        self.create_date = create_date
        self.last_update = last_update


