## Project Owner  ; HESBON ANGWENYI
## Project Name   ; Yelp-style Object Relations

# Overview
This project implements a simplified Yelp-style domain with three models: Restaurant, Customer, and Review. 
It explores object relationships and provides methods for initializing, reading, and writing data, as well as aggregate and association methods.

# Table Contents
1.Installation
2.Usage
3.Structure
4.Models
5.Methods

## Installation
To install the required dependencies, use the pipenv install

## Usage
1.Ensure you have installed the dependencies.
2. Create sample data and test the code in the main.py file through typing pipenv run python main.py

## Structure
# The project consists of three main classes:
1.Customer: Represents a customer.
2.Restaurant: Represents a restaurant.
3.Review: Represents a review, associating a customer with a restaurant and a rating.


## Models
# Customer
1.__init__(given_name, family_name): Initializes a new Customer instance.
2.given_name(): Returns the customer's given name.
3.family_name(): Returns the customer's family name.
4.full_name(): Returns the full name of the customer.
5.all(): Returns all customer instances.
6.restaurants(): Returns a unique list of restaurants reviewed by the customer.
7.add_review(restaurant, rating): Adds a new review for a restaurant.
8.num_reviews(): Returns the total number of reviews authored by the customer.
9.find_by_name(name): Class method to find a customer by their full name.
10.find_all_by_given_name(name): Class method to find all customers with a given name.

# Restaurant
1.__init__(name): Initializes a new Restaurant instance.
2.name(): Returns the restaurant's name.
3.all(): Returns all restaurant instances.
4.reviews(): Returns a list of unique reviews for the restaurant.
5.customers(): Returns a unique list of customers who have reviewed the restaurant.
6.average_star_rating(): Returns the average star rating for the restaurant based on its reviews.


# Review
1.__init__(customer, restaurant, rating): Initializes a new Review instance.
2.rating(): Returns the star rating for the review.
3.all(): Returns all review instances.
4.customer(): Returns the customer who authored the review.
5.restaurant(): Returns the restaurant being reviewed.

## LICENCE 
This project is being licensed under MIT License

Copyright (c) 2023 hesbonmanyi254

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

