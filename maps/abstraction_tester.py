import unittest
import test_functions as test
import recommend
from abstractions import *
import abstractions
old_sample = recommend.sample
test.swap_implementations(recommend)
from recommend import *

class TestProblemTwoAbstraction(unittest.TestCase):
    def test_1(self):
        test.swap_implementations(abstractions, rest=False)
        make_review = abstractions.make_review
        soda_reviews = [make_review('Soda', 4.5), make_review('Soda', 4)]
        soda = make_restaurant('Soda', [127.0, 0.1], ['Restaurants', 'Breakfast & Brunch'], 1, soda_reviews)
        try:
            self.assertTrue(restaurant_ratings(soda) == [4.5, 4])
        except AssertionError:
            print("Failed Abstraction Test 1 for Problem 2")


    def test_abstraction(self):
        test.swap_implementations(abstractions, rest_two=False)
        make_user, make_review, make_restaurant = abstractions.make_user, abstractions.make_review, abstractions.make_restaurant
        restaurant_num_ratings = abstractions.restaurant_num_ratings
        restaurant_mean_rating = abstractions.restaurant_mean_rating

        woz_reviews = [make_review('Wozniak Lounge', 4), make_review('Wozniak Lounge', 3), make_review('Wozniak Lounge', 5)]
        woz = make_restaurant('Wozniak Lounge', [127.0, 0.1], ['Restaurants', 'Pizza'], 1, woz_reviews)
        try:
            self.assertTrue(restaurant_num_ratings(woz) == 3)
        except AssertionError:
            print("Failed Abstraction Test 2 for Problem 2")

        try:
            self.assertTrue(restaurant_mean_rating(woz) == 4.0) # should be a decimal
        except AssertionError:
            print("Failed Abstraction Test 3 for Problem 2")

class TestProblemFourAbstraction(unittest.TestCase):
    def test_1(self):
        make_user, make_review, make_restaurant = recommend.make_user, recommend.make_review, recommend.make_restaurant
        distance = recommend.distance
        find_closest, group_by_centroid = recommend.find_closest, recommend.group_by_centroid


        r1 = make_restaurant('A', [-10, 2], [], 2, [make_review('A', 4),])
        r2 = make_restaurant('B', [-9, 1], [], 3, [make_review('B', 5), make_review('B', 3.5),])
        c1 = [0, 0]
        groups = group_by_centroid([r1, r2], [c1])
        try:
            self.assertTrue(test.deep_check_same_elements(groups, [[r1, r2]]) == True)
        except AssertionError:
            print("Failed Abstraction Test 1")


    def test_2(self):
        make_user, make_review, make_restaurant = recommend.make_user, recommend.make_review, recommend.make_restaurant
        distance = recommend.distance
        find_closest, group_by_centroid = recommend.find_closest, recommend.group_by_centroid

        r1 = make_restaurant('A', [-10, 2], [], 2, [make_review('A', 4),])
        r2 = make_restaurant('B', [-9, 1], [], 3, [make_review('B', 5),make_review('B', 3.5),])
        r3 = make_restaurant('C', [4, 2], [], 1, [make_review('C', 5)])
        c1 = [0, 0]
        c2 = [3, 4]
        groups = group_by_centroid([r1, r2, r3], [c1, c2])
        try:
            self.assertTrue(test.deep_check_same_elements(groups, [[r1, r2], [r3]]) == True)
        except AssertionError:
            print("Failed Abstraction Test 2")

    def test_3(self):
        make_user, make_review, make_restaurant = recommend.make_user, recommend.make_review, recommend.make_restaurant
        distance = recommend.distance
        find_closest, group_by_centroid = recommend.find_closest, recommend.group_by_centroid

        r1 = make_restaurant('A', [-10, 2], [], 2, [make_review('A', 4),])
        r2 = make_restaurant('B', [-9, 1], [], 3, [make_review('B', 5), make_review('B', 3.5),])
        r3 = make_restaurant('C', [4, 2], [], 1, [make_review('C', 5)])
        r4 = make_restaurant('D', [-2, 6], [], 4, [make_review('D', 2)])
        r5 = make_restaurant('E', [4, 2], [], 3.5, [make_review('E', 2.5),make_review('E', 3),])
        c1 = [0, 0]
        c2 = [3, 4]
        groups = group_by_centroid([r1, r2, r3, r4, r5], [c1, c2])
        try:
            self.assertTrue(test.deep_check_same_elements(groups, [[r1, r2], [r3, r4, r5]]) == True)
        except AssertionError:
            print("Failed Abstraction Test 3")


    def test_4(self):
        make_user, make_review, make_restaurant = recommend.make_user, recommend.make_review, recommend.make_restaurant
        distance = recommend.distance
        find_closest, group_by_centroid = recommend.find_closest, recommend.group_by_centroid

        r = make_restaurant('Zero', [0, 0], [], 1, [make_review('Zero', 5)])
        groups = group_by_centroid([r], [[x, y] for x in [1, -1] for y in [1, -1]])
        try:
            self.assertTrue(test.deep_check_same_elements(groups, [[r]]) == True)
        except AssertionError:
            print("Failed Abstraction Test 4")

class TestProblemFiveAbstraction(unittest.TestCase):
    def test_abstraction(self):
        cluster1 = [
            make_restaurant('A', [-3, -4], [], 3, [make_review('A', 2)]),
            make_restaurant('B', [1, -1],  [], 1, [make_review('B', 1)]),
            make_restaurant('C', [2, -4],  [], 1, [make_review('C', 5)])
        ]

        try:
            self.assertTrue(find_centroid(cluster1) == [0.0, -3.0])
        except AssertionError:
            print("Failed Abstraction Test")

class TestProblemSixAbstractionAndImplementation(unittest.TestCase):
    def test_1(self):
        recommend.sample = test.sample # deterministic sampling
        make_review, make_restaurant = recommend.make_review, recommend.make_restaurant
        k_means = recommend.k_means
        restaurants1 = [
            make_restaurant('A', [-3, -4], [], 3, [make_review('A', 2)]),
            make_restaurant('B', [1, -1],  [], 1, [make_review('B', 1)]),
            make_restaurant('C', [2, -4],  [], 1, [make_review('C', 5)]),
        ]
        centroids = k_means(restaurants1, 1) # should be 2-element lists of decimals
        try:
            self.assertTrue(centroids == [[0.0, -3.0]])
        except AssertionError:
            print("Failed Test #1!")


    def test_2(self):
        recommend.sample = test.sample # deterministic sampling
        make_review, make_restaurant = recommend.make_review, recommend.make_restaurant
        k_means = recommend.k_means
        restaurants2 = [
            make_restaurant('D', [2, 3], [], 2, [make_review('D', 2)]),
            make_restaurant('E', [0, 3], [], 3, [make_review('E', 1)]),
        ]
        centroids = k_means(restaurants2, 1)
        try:
            self.assertTrue(centroids == [[1.0, 3.0]])
        except AssertionError:
            print("Failed Test #2!")



    def test_3(self):
        recommend.sample = test.sample # deterministic sampling
        make_review, make_restaurant = recommend.make_review, recommend.make_restaurant
        k_means = recommend.k_means
        restaurants1 = [
            make_restaurant('A', [-3, -4], [], 3, [make_review('A', 2)]),
            make_restaurant('B', [1, -1],  [], 1, [make_review('B', 1)]),
            make_restaurant('C', [2, -4],  [], 1, [make_review('C', 5)]),
        ]
        centroids = k_means(restaurants1, 2)
        try:
            self.assertTrue(centroids == [[-3.0, -4.0], [1.5, -2.5]])
        except AssertionError:
            print("Failed Test #3!")


    def test_4(self):
        recommend.sample = test.sample # deterministic sampling
        make_review, make_restaurant = recommend.make_review, recommend.make_restaurant
        k_means = recommend.k_means
        cluster1 = [
            make_restaurant('A', [-3, -4], [], 3, [make_review('A', 2)]),
        ]
        cluster2 = [
            make_restaurant('B', [1, -1], [], 1, [make_review('B', 1)]),
            make_restaurant('C', [2, -4], [], 1, [make_review('C', 5)]),
            make_restaurant('D', [2, 3],  [], 2, [make_review('D', 2)]),
            make_restaurant('E', [0, 3],  [], 3, [make_review('E', 1)]),
            make_restaurant('F', [-1, 0], [], 3, [make_review('F', 1)]),
            make_restaurant('G', [4, 2],  [], 3, [make_review('E', 1)]),
        ]
        restaurants = cluster1 + cluster2
        centroids = k_means(restaurants, 2)
        centroids_list = [[round(x, 5), round(y, 5)] for x, y in centroids]
        try:
            self.assertTrue(centroids_list == [[-3.0, -4.0], [1.33333, 0.5]])
        except AssertionError:
            print("Failed Test #4!")


class TestProblemSevenAbstractionAndImplementation(unittest.TestCase):
    def test_1(self):
        user = make_user('John D.', [
            make_review('A', 1),
            make_review('B', 5),
            make_review('C', 2),
            make_review('D', 2.5),
        ])
        restaurant = make_restaurant('New', [-10, 2], [], 2, [make_review('New', 4)])

        cluster = [
            make_restaurant('B', [4, 2], [], 1, [make_review('B', 5)]),
            make_restaurant('C', [-2, 6], [], 4, [make_review('C', 2)]),
            make_restaurant('D', [4, 2], [], 3.5, [make_review('D', 2.5), make_review('D', 3)])
        ]

        pred, r_squared = find_predictor(user, cluster, restaurant_price)
        try:
            self.assertTrue(round(pred(restaurant), 5) == 4.0)
            self.assertTrue(round(r_squared, 5) == 1.0)
        except AssertionError:
            print("Failed Test #1")



    def test_2(self):
        user = make_user('John D.', [
            make_review('A', 1),
            make_review('B', 5),
            make_review('C', 2),
            make_review('D', 2.5),
        ])
        restaurant = make_restaurant('New', [-10, 2], [], 2, [make_review('New', 4)])

        cluster = [
            make_restaurant('B', [4, 2], [], 1, [make_review('B', 5)]),
            make_restaurant('C', [-2, 6], [], 4, [make_review('C', 2)]),
            make_restaurant('D', [4, 2], [], 3.5, [make_review('D', 2.5), make_review('D', 3)])
        ]

        pred, r_squared = find_predictor(user, cluster, restaurant_mean_rating)
        try:
            self.assertTrue(round(pred(restaurant), 5) == 3.9359)
            self.assertEqual(round(r_squared, 5), 0.99256)
        except AssertionError:
            print("Failed Test #2")


    def test_3(self):
        user = make_user('John D.', [
            make_review('A', 1),
            make_review('B', 5),
            make_review('C', 2),
            make_review('D', 2.5),
        ])
        restaurant = make_restaurant('New', [-10, 2], [], 2, [make_review('New', 4)])

        cluster = [
            make_restaurant('B', [4, 2], [], 1, [make_review('B', 5)]),
            make_restaurant('C', [-2, 6], [], 4, [make_review('C', 2)]),
            make_restaurant('D', [4, 2], [], 3.5, [make_review('D', 2.5), make_review('D', 3)])
        ]

        pred, r_squared = find_predictor(user, cluster, restaurant_num_ratings)
        try:
            self.assertTrue(round(pred(restaurant), 5) == 3.5)
            self.assertEqual(round(r_squared, 5), 0.12903)
        except AssertionError:
            print("Failed Test #3")

class TestProblemEightAbstraction(unittest.TestCase):
    def test_1(self):
        user = make_user('Cheapskate', [ \
               make_review('A', 2), \
               make_review('B', 5), \
               make_review('C', 2), \
               make_review('D', 5)])
        cluster = [make_restaurant('A', [5, 2], [], 4, [make_review('A', 5)]), \
                   make_restaurant('B', [3, 2], [], 2, [make_review('B', 5)]), \
                   make_restaurant('C', [-2, 6], [], 4, [make_review('C', 4)]), \
                   make_restaurant('D', [4, 2], [], 2, [make_review('D', 3),make_review('D', 4)])]
        fns = [restaurant_price, restaurant_mean_rating]
        pred = best_predictor(user, cluster, fns)
        try:
            self.assertTrue([round(pred(r), 5) for r in cluster] == [2.0, 5.0, 2.0, 5.0])
        except AssertionError:
            print("Failed Abstraction Test #1")

    def test_2(self):
        user = make_user('Cheapskate', [
               make_review('A', 2), \
               make_review('B', 5), \
               make_review('C', 2), \
               make_review('D', 5)])
        cluster = [make_restaurant('A', [5, 2], [], 4, [make_review('A', 5)]), \
                   make_restaurant('B', [3, 2], [], 2, [make_review('B', 5)]), \
                   make_restaurant('C', [-2, 6], [], 4, [make_review('C', 4)])]
        fns = [restaurant_price, restaurant_mean_rating]
        pred = best_predictor(user, cluster, fns)
        try:
            self.assertTrue([round(pred(r), 5) for r in cluster] == [2.0, 5.0, 2.0])
        except AssertionError:
            print("Failed Abstraction Test #2")

    def test_3(self):
        user = make_user('Cheapskate', [ \
               make_review('A', 2), \
               make_review('B', 5), \
               make_review('C', 2), \
               make_review('D', 5)])
        cluster = [make_restaurant('A', [5, 2], [], 4, [make_review('A', 5)]), \
                   make_restaurant('B', [3, 2], [], 2, [make_review('B', 5)]), \
                   make_restaurant('C', [-2, 6], [], 4, [make_review('C', 4)])]
        fns = [restaurant_mean_rating, restaurant_price]
        pred = best_predictor(user, cluster, fns)
        try:
            self.assertTrue([round(pred(r), 5) for r in cluster] == [2.0, 5.0, 2.0])
        except AssertionError:
            print("Failed Abstraction Test #3")

    def test_4(self):
        user = make_user('Cheapskate', [ \
               make_review('A', 2), \
               make_review('B', 5), \
               make_review('C', 2), \
               make_review('D', 5)])
        cluster = [make_restaurant('A', [5, 2], [], 4, [make_review('A', 5)]),
                   make_restaurant('B', [3, 2], [], 2, [make_review('B', 5)]),
                   make_restaurant('C', [-2, 6], [], 4, [make_review('C', 4)]),
                   make_restaurant('E', [1, 2], [], 4, [make_review('E', 4)])]
        fns = [restaurant_mean_rating, restaurant_price]
        pred = best_predictor(user, cluster, fns) # Make sure you're only using user-reviewed restaurants!
        try:
            self.assertTrue([round(pred(r), 5) for r in cluster] == [2.0, 5.0, 2.0, 2.0])
        except:
            print("Failed Abstraction Test #4")

class TestProblemNineAbstraction(unittest.TestCase):
    def test_2(self):
        user = make_user('Mr. Mean Rating Minus One', [
               make_review('A', 3), \
               make_review('B', 4), \
               make_review('C', 1)])
        cluster = [make_restaurant('A', [1, 2], [], 4, [make_review('A', 4),make_review('A', 4)]), \
                   make_restaurant('B', [4, 2], [], 3, [make_review('B', 5)]), \
                   make_restaurant('C', [-2, 6], [], 4, [make_review('C', 2)]), \
                   make_restaurant('D', [4, 4], [], 3.5, [make_review('D', 2.5),make_review('D', 3.5)])]
        recommend.ALL_RESTAURANTS = cluster
        to_rate = cluster[2:]
        fns = [restaurant_price, restaurant_mean_rating]
        ratings = rate_all(user, to_rate, fns)
        try:
            self.assertTrue(type(ratings) is dict)
            self.assertTrue(len(ratings) == 2)
            self.assertTrue(ratings['C'] == 1)
            self.assertTrue(round(ratings['D'], 5) == 2.0)
        except AssertionError:
            print("Failed Abstraction Test")

class TestProblemTenAbstraction(unittest.TestCase):
    def test_1(self):
        make_user, make_review, make_restaurant = recommend.make_user, recommend.make_review, recommend.make_restaurant
        search = recommend.search
        def make_testaurant(name, categories):
              return make_restaurant(name, [0, 0], categories, 1, [make_review(name, 5)])

        a = make_testaurant('A', ['Creperies', 'Italian'])
        b = make_testaurant('B', ['Italian', 'Coffee & Tea'])
        c = make_testaurant('C', ['Coffee & Tea', 'Greek', 'Creperies'])
        d = make_testaurant('D', ['Greek'])
        try:
            self.assertTrue(test.check_same_elements(search('Creperies', [a, b, c, d]), [a, c]))
            self.assertTrue(test.check_same_elements(search('Thai', [a, b, c, d]), []))
            self.assertTrue(test.check_same_elements(search('Coffee & Tea', [a, b, d]), [b]))
            self.assertTrue(test.check_same_elements(search('Greek', [a, b, c, d]), [c, d]))
            self.assertTrue(test.check_same_elements(search('Italian', [a, b, c, d]), [a, b]))
        except AssertionError:
            print("Failed Abstraction Test")

if __name__ == '__main__':
    unittest.main()
    #recommend.sample = old_sample
    #test.restore_implementations(recommend)
    test.restore_implementations(abstractions)
