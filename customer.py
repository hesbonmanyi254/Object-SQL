from review import Review  # Import the Review class

class Customer:
    all_customers = []  # Class variable to store all customer instances

    def __init__(self, given_name, family_name):
        """
        Initialize a new Customer instance.

        Args:
            given_name (str): The given name of the customer.
            family_name (str): The family name of the customer.
        """
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []  # List to store reviews associated with this customer
        Customer.all_customers.append(self)

    def get_given_name(self):
        """
        Get the given name of the customer.

        Returns:
            str: The given name of the customer.
        """
        return self.given_name

    def get_family_name(self):
        """
        Get the family name of the customer.

        Returns:
            str: The family name of the customer.
        """
        return self.family_name

    def full_name(self):
        """
        Get the full name of the customer (given name + family name).

        Returns:
            str: The full name of the customer.
        """
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        """
        Get a list of all customer instances.

        Returns:
            list: List of all customer instances.
        """
        return cls.all_customers

    def restaurants(self):
        """
        Get a list of unique restaurants reviewed by the customer.

        Returns:
            list: List of unique restaurants reviewed by the customer.
        """
        return list(set([review.restaurant for review in self.reviews]))

    def add_review(self, restaurant, rating):
        """
        Add a new review for a restaurant.

        Args:
            restaurant (Restaurant): The restaurant to review.
            rating (int): The rating for the restaurant review.
        """
        new_review = Review(self, restaurant, rating)
        self.reviews.append(new_review)

    def num_reviews(self):
        """
        Get the total number of reviews authored by the customer.

        Returns:
            int: The total number of reviews.
        """
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, full_name):
        """
        Find a customer by their full name.

        Args:
            full_name (str): The full name to search for.

        Returns:
            Customer or None: The customer instance if found, otherwise None.
        """
        for customer in cls.all_customers:
            if customer.full_name() == full_name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, given_name):
        """
        Find all customers with a given name.

        Args:
            given_name (str): The given name to search for.

        Returns:
            list: List of customer instances with the given name.
        """
        return [customer for customer in cls.all_customers if customer.given_name == given_name]
