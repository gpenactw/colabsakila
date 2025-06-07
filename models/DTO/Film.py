class Film:
    def __init__(self, film_id, title, description, release_year, language_id, original_language_id, rental_duration,
                 rental_rate, length, replacement_cost, rating, special_features, last_update):
        self.film_id = film_id
        self.title = title
        self.description = description
        self.release_year = release_year
        self.language_id = language_id
        self.original_language_id = original_language_id
        self.rental_duration = rental_duration
        self.rental_rate = rental_rate
        self.length = length
        self.replacement_cost = replacement_cost
        self.rating = rating
        self.special_features = special_features
        self.last_update = last_update