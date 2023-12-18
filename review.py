class Review:
    all_reviews = []  # Class variable to store all review instances

    def __init__(self, customer, restaurant, rating):
        """
        Initialize a new Review instance.

        Args:
            customer (Customer): The customer who authored the review.
            restaurant (Restaurant): The restaurant being reviewed.
            rating (int): The star rating for the restaurant review.
        """
        self.customer = customer
        self.restaurant = restaurant
        self.rating_value = rating
        Review.all_reviews.append(self)  # Add the review to the list of all reviews
        restaurant.reviews.append(self)  # Add the review to the restaurant's list of reviews
        customer.reviews.append(self)  # Add the review to the customer's list of reviews

    def rating(self):
        """
        Get the star rating for the review.

        Returns:
            int: The star rating for the review.
        """
        return self.rating_value

    @classmethod
    def all(cls):
        """
        Get a list of all review instances.

        Returns:
            list: List of all review instances.
        """
        return cls.all_reviews

    def customer(self):
        """
        Get the customer who authored the review.

        Returns:
            Customer: The customer instance who authored the review.
        """
        return self.customer

    def restaurant(self):
        """
        Get the restaurant being reviewed.

        Returns:
            Restaurant: The restaurant instance being reviewed.
        """
        return self.restaurant
