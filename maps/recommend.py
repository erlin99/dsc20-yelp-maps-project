"""A Yelp-powered Restaurant Recommendation Program"""

from abstractions import *
from data import ALL_RESTAURANTS, CATEGORIES, USER_FILES, load_user_file
from ucsd import main, trace, interact
from utils import distance, mean, zip, enumerate, sample
from visualize import draw_map

##################################
# Phase 2: Unsupervised Learning #
##################################

def find_closest(location, centroids):
    """Return the centroid in centroids that is closest to location.
    If multiple centroids are equally close, return the first one.

    >>> find_closest([3.0, 4.0], [[0.0, 0.0], [2.0, 3.0], [4.0, 3.0], [5.0, 5.0]])
    [2.0, 3.0]
    """
    # BEGIN Question 3
    return min(centroids, key = lambda x: abs(distance(location, x)))
    # END Question 3


def group_by_first(pairs):
    """Return a list of lists that relates each unique key in the [key, value]
    pairs to a list of all values that appear paired with that key.

    Arguments:
    pairs -- a sequence of pairs

    >>> example = [ [1, 2], [3, 2], [2, 4], [1, 3], [3, 1], [1, 2] ]
    >>> group_by_first(example)  # Values from pairs that start with 1, 3, and 2 respectively
    [[2, 3, 2], [2, 1], [4]]
    """
    keys = []
    for key, _ in pairs:
        if key not in keys:
            keys.append(key)
    return [[y for x, y in pairs if x == key] for key in keys]


def group_by_centroid(restaurants, centroids):
    """Return a list of clusters, where each cluster contains all restaurants
    nearest to a corresponding centroid in centroids. Each item in
    restaurants should appear once in the result, along with the other
    restaurants closest to the same centroid.
    """
    # BEGIN Question 4
    closest_to = []
    for restaurant in restaurants:
        closest = find_closest(restaurant_location(restaurant), centroids)
        temp = [closest, restaurant]
        closest_to.append(temp)

    return group_by_first(closest_to)
    # END Question 4


def find_centroid(cluster):
    """Return the centroid of the locations of the restaurants in cluster."""
    # BEGIN Question 5
    latitudes = []
    longitudes = []
    for restaurant in cluster:
        latitudes.append(restaurant_location(restaurant)[0])
        longitudes.append(restaurant_location(restaurant)[1])

    return [mean(latitudes), mean(longitudes)]
    # END Question 5


def k_means(restaurants, k, max_updates=100):
    """Use k-means to group restaurants by location into k clusters.
    >>> 
    
    """
    assert len(restaurants) >= k, 'Not enough restaurants to cluster'
    old_centroids, n = [], 0

    # Select initial centroids randomly by choosing k different restaurants
    centroids = [restaurant_location(r) for r in sample(restaurants, k)]

    while old_centroids != centroids and n < max_updates:
        old_centroids = centroids
        # BEGIN Question 6
        clusters = group_by_centroid(restaurants, centroids)
        x = 0
        for cluster in clusters:
            centroid = find_centroid(cluster)
            centroids[x] = centroid
            x += 1
        # END Question 6
        n += 1
    return centroids


################################
# Phase 3: Supervised Learning #
################################

def find_predictor(user, restaurants, feature_fn):
    """Return a rating predictor (a function from restaurants to ratings),
    for a user by performing least-squares linear regression using feature_fn
    on the items in restaurants. Also, return the R^2 value of this model.

    Arguments:
    user -- A user
    restaurants -- A sequence of restaurants
    feature_fn -- A function that takes a restaurant and returns a number
    """
    xs = [feature_fn(r) for r in restaurants]
    ys = [user_rating(user, restaurant_name(r)) for r in restaurants]

    # BEGIN Question 7
    # means 
    mean_x = mean(xs)
    mean_y = mean(ys)

    # calculating the sum of squares 
    s_xx = sum([(x - mean_x)**2 for x in xs])
    s_yy = sum([(y - mean_y)**2 for y in ys])
    s_xy = sum([(x - mean_x)*(y - mean_y) for x, y in zip(xs, ys)])

    # regression coefficients 
    b = s_xy / s_xx
    a = mean_y - b * mean_x
    
    r_squared = (s_xy**2) / (s_xx * s_yy) 
    # END Question 7

    def predictor(restaurant):
        return b * feature_fn(restaurant) + a

    return predictor, r_squared


def best_predictor(user, restaurants, feature_fns):
    """Find the feature within feature_fns that gives the highest R^2 value
    for predicting ratings by the user; return a predictor using that feature.

    Arguments:
    user -- A user
    restaurants -- A list of restaurants
    feature_fns -- A sequence of functions that each takes a restaurant

    >>> user = make_user('Cheapskate', [make_review('A', 2),make_review('B', 5),make_review('C', 2),make_review('D', 5),])
    >>> cluster = [make_restaurant('A', [5, 2], [], 4, [make_review('A', 5)]), \
                make_restaurant('B', [3, 2], [], 2, [make_review('B', 5)]), \
                make_restaurant('C', [-2, 6], [], 4, [make_review('C', 4)]), \
                make_restaurant('D', [4, 2], [], 2, [make_review('D', 3),make_review('D', 4)])]
    >>> fns = [restaurant_price, restaurant_mean_rating]
    >>> best_predictor(user, cluster, fns)
    """
    reviewed = user_reviewed_restaurants(user, restaurants)
    # BEGIN Question 8
    results = []
    # loop through all the funcions
    for fn in feature_fns:
        function, r_square = find_predictor(user, reviewed, fn)
        result = [r_square, function]
        results.append(result)
    
    return max(results)[1]
    # END Question 8


def rate_all(user, restaurants, feature_fns):
    """Return the predicted ratings of restaurants by user using the best
    predictor based on a function from feature_fns.

    Arguments:
    user -- A user
    restaurants -- A list of restaurants
    feature_fns -- A sequence of feature functions
    """
    predictor = best_predictor(user, ALL_RESTAURANTS, feature_fns)
    reviewed = user_reviewed_restaurants(user, restaurants)
    # BEGIN Question 9
    predicted = dict()
    for r in restaurants: 
        r_name = restaurant_name(r)
        if r in reviewed:
            predicted[r_name] = user_rating(user, r_name)
        else:
            predicted[r_name] = predictor(r)
    
    return predicted
    # END Question 9


def search(query, restaurants):
    """Return each restaurant in restaurants that has query as a category.

    Arguments:
    query -- A string
    restaurants -- A sequence of restaurants
    """
    # BEGIN Question 10
    result = []
    for r in restaurants:
        if query in restaurant_categories(r):
            result.append(r)

    return result
    # END Question 10


def feature_set():
    """Return a sequence of feature functions."""
    return [lambda r: mean(restaurant_ratings(r)),
            restaurant_price,
            lambda r: len(restaurant_ratings(r)),
            lambda r: restaurant_location(r)[0],
            lambda r: restaurant_location(r)[1]]


@main
def main(*args):
    import argparse
    parser = argparse.ArgumentParser(
        description='Run Recommendations',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-u', '--user', type=str, choices=USER_FILES,
                        default='test_user',
                        metavar='USER',
                        help='user file, e.g.\n' +
                        '{{{}}}'.format(','.join(sample(USER_FILES, 3))))
    parser.add_argument('-k', '--k', type=int, help='for k-means')
    parser.add_argument('-q', '--query', choices=CATEGORIES,
                        metavar='QUERY',
                        help='search for restaurants by category e.g.\n'
                        '{{{}}}'.format(','.join(sample(CATEGORIES, 3))))
    parser.add_argument('-p', '--predict', action='store_true',
                        help='predict ratings for all restaurants')
    parser.add_argument('-r', '--restaurants', action='store_true',
                        help='outputs a list of restaurant names')
    args = parser.parse_args()

    # Output a list of restaurant names
    if args.restaurants:
        print('Restaurant names:')
        for restaurant in sorted(ALL_RESTAURANTS, key=restaurant_name):
            print(repr(restaurant_name(restaurant)))
        exit(0)

    # Select restaurants using a category query
    if args.query:
        restaurants = search(args.query, ALL_RESTAURANTS)
    else:
        restaurants = ALL_RESTAURANTS

    # Load a user
    assert args.user, 'A --user is required to draw a map'
    user = load_user_file('{}.dat'.format(args.user))

    # Collect ratings
    if args.predict:
        ratings = rate_all(user, restaurants, feature_set())
    else:
        restaurants = user_reviewed_restaurants(user, restaurants)
        names = [restaurant_name(r) for r in restaurants]
        ratings = {name: user_rating(user, name) for name in names}

    # Draw the visualization
    if args.k:
        centroids = k_means(restaurants, min(args.k, len(restaurants)))
    else:
        centroids = [restaurant_location(r) for r in restaurants]
    draw_map(centroids, restaurants, ratings)