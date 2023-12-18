from review import Review  # Import the Review class

class Restaurant:
    all_restaurants = []  # Class variable to store all restaurant instances

    def __init__(self, name):
        """
        Initialize a new Restaurant instance.

        Args:
            name (str): The name of the restaurant.
        """
        self.name = name
        self.reviews = []  # List to store reviews associated with this restaurant
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        """
        Get the name of the restaurant.

        Returns:
            str: The name of the restaurant.
        """
        return self.name

    @classmethod
    def all(cls):
        """
        Get a list of all restaurant instances.

        Returns:
            list: List of all restaurant instances.
        """
        return cls.all_restaurants

    def reviews(self):
        """
        Get a list of unique reviews associated with the restaurant.

        Returns:
            list: List of unique reviews for the restaurant.
        """
        return list(set([review for review in self.reviews]))

    def customers(self):
        """
        Get a list of unique customers who have reviewed the restaurant.

        Returns:
            list: List of unique customers who have reviewed the restaurant.
        """
        return list(set([review.customer for review in self.reviews]))

    def average_star_rating(self):
        """
        Calculate the average star rating for the restaurant.

        Returns:
            float: The average star rating, or 0 if there are no reviews.
        """
        if not self.reviews:
            return 0
        total_ratings = sum([review.rating for review in self.reviews])
        return total_ratings / len(self.reviews)
