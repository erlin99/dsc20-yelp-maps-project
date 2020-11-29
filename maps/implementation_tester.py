from utils import *
from abstractions import *
import abstractions
from recommend import *
import recommend
import test_functions as test
import unittest

class TestProblemOne(unittest.TestCase):
    def test_map_and_filter(self):
        print()
        square = lambda x: x * x
        is_odd = lambda x: x % 2 == 1
        try:
            self.assertTrue(map_and_filter([1, 2, 3, 4, 5], square, is_odd) == [1, 9, 25])
        except AssertionError:
            print("Failed Test 1 for Map and Filter")

        try:
            self.assertTrue(map_and_filter(['hi', 'hello', 'hey', 'world'],lambda x: x[4], lambda x: len(x) > 4) == ['o', 'd'])
        except AssertionError:
            print("Failed Test 2 for Map and Filter")

        print("FINISHED TESTING MAP AND FILTER")


    def test_key_of_min_value(self):
        print()
        try:
            self.assertTrue(key_of_min_value({1: 6, 2: 5, 3: 4}) == 3)
        except AssertionError:
            print("Failed Test 1 for Key of Min Val")

        try:
            self.assertTrue(key_of_min_value({'a': 6, 'b': 5, 'c': 4}) == 'c')
        except AssertionError:
            print("Failed Test 2 for Key of Min Val")

        try:
            self.assertTrue(key_of_min_value({'hello': 'world', 'hi': 'there'}) == 'hi')
        except AssertionError:
            print("Failed Test 3 for Key of Min Val")

        print("FINISHED TESTING KEY OF MIN VAL")



    def test_enumerate(self):
        print()
        try:
            self.assertTrue(enumerate([6, 1, 'a']) == [[0, 6], [1, 1], [2, 'a']])
        except AssertionError:
            print("Failed Test 1 for Enumerate")

        try:
            self.assertTrue(enumerate('five', 5) == [[5, 'f'], [6, 'i'], [7, 'v'], [8, 'e']])
        except AssertionError:
            print("Failed Test 2 for Enumerate")

        print("FINISHED TESTING ENUMERATE")


class TestProblemTwo(unittest.TestCase):
    def test_1(self):
        soda_reviews = [make_review('Soda', 4.5), make_review('Soda', 4)]
        soda = make_restaurant('Soda', [127.0, 0.1], ['Restaurants', 'Breakfast & Brunch'], 1, soda_reviews)
        try:
            self.assertTrue(restaurant_ratings(soda) == [4.5, 4])
        except AssertionError:
            print("Failed Implementation Test 1 for Problem 2")

    def test_functionality(self):
        woz_reviews = [make_review('Wozniak Lounge', 4), make_review('Wozniak Lounge', 3), make_review('Wozniak Lounge', 5)]
        woz = make_restaurant('Wozniak Lounge', [127.0, 0.1], ['Restaurants', 'Pizza'], 1, woz_reviews)
        try:
            self.assertTrue(restaurant_num_ratings(woz) == 3)
        except AssertionError:
            printf("Failed Implementation Test 2 for Problem 2")

        try:
            self.assertTrue(restaurant_mean_rating(woz) == 4.0) # should be a decimal
        except AssertionError:
            print("Failed Implementation Test 3 for Problem 2")


class TestProblemThree(unittest.TestCase):
    def test_distance(self):
        print()
        try:
            self.assertTrue(distance([0, 0], [3, 4]) == 5.0)
        except AssertionError:
            print("Failed Distance Test #1")

        try:
            self.assertTrue(distance([6, 1], [6, 1]) == 0.0)
        except AssertionError:
            print("Failed Distance Test #2")

        try:
            self.assertTrue(distance([-2, 7], [-3.5, 9]) == 2.5)
        except AssertionError:
            print("Failed Distance Test #3")

    def test_find_closest(self):
        print()
        try:
            self.assertTrue(find_closest([6, 1],[[1, 5], [3, 3]]) == [3, 3])
        except AssertionError:
            print("Failed Find Closest Test #1")

        try:
            self.assertTrue(find_closest([1, 6], [[1, 5], [3, 3]]) == [1, 5])
        except AssertionError:
            print("Failed Find Closest Test #2")

        try:
            self.assertTrue(find_closest([0, 0], [[-2, 0], [2, 0]]) == [-2, 0])
        except AssertionError:
            print("Failed Find Closest Test #3")

        try:
            self.assertTrue(find_closest([0, 0], [[1000, 1000]]) == [1000, 1000])
        except AssertionError:
            print("Failed Find Closest Test #4")

        try:
            self.assertTrue(find_closest([0, 0], [[2, 2], [0, 3]]) == [2, 2])
        except AssertionError:
            print("Failed Find Closest Test #5")

        try:
            self.assertTrue(find_closest([0, 0], [[5, 5], [2, 7]]) == [5, 5])
        except AssertionError:
            print("Failed Find Closest Test #6")


class TestProblemFour(unittest.TestCase):
    def test_1(self):
        r1 = make_restaurant('A', [-10, 2], [], 2, [make_review('A', 4),])
        r2 = make_restaurant('B', [-9, 1], [], 3, [make_review('B', 5), make_review('B', 3.5)])
        c1 = [0, 0]
        groups = group_by_centroid([r1, r2], [c1])
        try:
            self.assertTrue(test.deep_check_same_elements(groups, [[r1, r2]]) == True)
        except AssertionError:
            print("Failed Test 1")

    def test_2(self):
        r1 = make_restaurant('A', [-10, 2], [], 2, [make_review('A', 4),])
        r2 = make_restaurant('B', [-9, 1], [], 3, [make_review('B', 5),make_review('B', 3.5),])
        r3 = make_restaurant('C', [4, 2], [], 1, [make_review('C', 5)])
        c1 = [0, 0]
        c2 = [3, 4]
        groups = group_by_centroid([r1, r2, r3], [c1, c2])
        try:
            self.assertTrue(test.deep_check_same_elements(groups, [[r1, r2], [r3]]) == True)
        except AssertionError:
            print("Failed Test 2")


    def test_3(self):
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
            print("Failed Test 3")

    def test_4(self):
         r = make_restaurant('Zero', [0, 0], [], 1, [make_review('Zero', 5)])
         groups = group_by_centroid([r], [[x, y] for x in [1, -1] for y in [1, -1]])
         try:
             self.assertTrue(test.deep_check_same_elements(groups, [[r]]) == True)
         except AssertionError:
             print("Failed Test 4")


class TestProblemFive(unittest.TestCase):
    def test_implementation(self):
        cluster1 = [
            make_restaurant('A', [-3, -4], [], 3, [make_review('A', 2)]),
            make_restaurant('B', [1, -1],  [], 1, [make_review('B', 1)]),
            make_restaurant('C', [2, -4],  [], 1, [make_review('C', 5)])
        ]

        try:
            self.assertTrue(find_centroid(cluster1) == [0.0, -3.0])
        except AssertionError:
            print("Failed Implementation Test")


class TestProblemEight(unittest.TestCase):
    def test_1(self):
        user = make_user('Cheapskate', [make_review('A', 2),make_review('B', 5),make_review('C', 2),make_review('D', 5),])
        cluster = [make_restaurant('A', [5, 2], [], 4, [make_review('A', 5)]), \
                   make_restaurant('B', [3, 2], [], 2, [make_review('B', 5)]), \
                   make_restaurant('C', [-2, 6], [], 4, [make_review('C', 4)]), \
                   make_restaurant('D', [4, 2], [], 2, [make_review('D', 3),make_review('D', 4)])]
        fns = [restaurant_price, restaurant_mean_rating]
        pred = best_predictor(user, cluster, fns)
        try:
            self.assertTrue([round(pred(r), 5) for r in cluster] == [2.0, 5.0, 2.0, 5.0])
        except AssertionError:
            print("Failed Test #1")

    def test_2(self):
        user = make_user('Cheapskate', [ \
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
            print("Failed Test #2")

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
            print("Failed Test #3")

    def test_4(self):
        user = make_user('Cheapskate', [ \
               make_review('A', 2), \
               make_review('B', 5), \
               make_review('C', 2), \
               make_review('D', 5)])
        cluster = [make_restaurant('A', [5, 2], [], 4, [make_review('A', 5)]), \
                   make_restaurant('B', [3, 2], [], 2, [make_review('B', 5)]), \
                   make_restaurant('C', [-2, 6], [], 4, [make_review('C', 4)]), \
                   make_restaurant('E', [1, 2], [], 4, [make_review('E', 4)]),]
        fns = [restaurant_mean_rating, restaurant_price]
        pred = best_predictor(user, cluster, fns) # Make sure you're only using user-reviewed restaurants!
        try:
            self.assertTrue([round(pred(r), 5) for r in cluster] == [2.0, 5.0, 2.0, 2.0])
        except AssertionError:
            print("Failed Test #4")

class TestProblemNine(unittest.TestCase):
    def test_1(self):
        user = make_user('Mr. Mean Rating Minus One', [ \
               make_review('A', 3), \
               make_review('B', 4), \
               make_review('C', 1)])
        cluster = [make_restaurant('A', [1, 2], [], 4, [make_review('A', 4),make_review('A', 4)]), \
                   make_restaurant('B', [4, 2], [], 3, [make_review('B', 5)]), \
                   make_restaurant('C', [-2, 6], [], 4, [make_review('C', 2)]), \
                   make_restaurant('D', [4, 4], [], 3.5, [make_review('D', 2.5),make_review('D', 3.5)])]
        restaurants = {restaurant_name(r): r for r in cluster}
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
            print("Failed Implementation Test")

class TestProblemTen(unittest.TestCase):
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
            print("Failed Implementation Test")



if __name__ == '__main__':
    unittest.main()
