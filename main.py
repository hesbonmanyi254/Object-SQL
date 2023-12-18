# main.py

from customer import Customer
from restaurant import Restaurant
from review import Review

# Create sample data
hesbon_angwenyi = Customer("Hesbon", "Angwenyi")
jane_smith = Customer("Jane", "Smith")
michael_nyanyuki = Customer("Michael", "Nyanyuki")
morgan_ngetich = Customer("Morgan", "Ngetich")
alice_jones = Customer("Alice", "Jones")
bob_miller = Customer("Bob", "Miller")
susan_kim = Customer("Susan", "Kim")
david_smith = Customer("David", "Smith")

restaurant_a = Restaurant("Restaurant A")
restaurant_b = Restaurant("Restaurant B")
restaurant_c = Restaurant("Restaurant C")
restaurant_d = Restaurant("Restaurant D")

# Add reviews
hesbon_angwenyi.add_review(restaurant_a, 4)
hesbon_angwenyi.add_review(restaurant_b, 3)
jane_smith.add_review(restaurant_a, 5)
hesbon_angwenyi.add_review(restaurant_a, 2)
michael_nyanyuki.add_review(restaurant_c, 4)
morgan_ngetich.add_review(restaurant_c, 5)
alice_jones.add_review(restaurant_b, 3)
bob_miller.add_review(restaurant_a, 5)
susan_kim.add_review(restaurant_d, 2)
david_smith.add_review(restaurant_d, 4)


print("Customers:")
for customer in Customer.all():
    print(f"{customer.full_name()} has reviewed: {[review.restaurant.get_name() for review in customer.reviews]}")

print("\nRestaurants:")
for restaurant in Restaurant.all():
    print(f"{restaurant.get_name()} has reviews from: {[customer.full_name() for customer in restaurant.customers()]}")

print("\nReviews:")
for review in Review.all():
    print(f"Customer: {review.customer.full_name()}, Restaurant: {review.restaurant.get_name()}, Rating: {review.rating()}")


print("\nAdditional Examples:")
for customer in Customer.all():
    print(f"Number of reviews by {customer.full_name()}: {customer.num_reviews()}")

hesbon = Customer.find_by_name("Hesbon Angwenyi")
print(f"Find customer by name: {hesbon.full_name()}")

# Find all customers by given name
morgans = Customer.find_all_by_given_name("Morgan")
for morgan in morgans:
    print(f"Find all customers by given name: {morgan.full_name()}")