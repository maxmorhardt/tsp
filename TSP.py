# Traveling Salesman Problem
# By: Max Morhardt

# Imports
import sys
from itertools import permutations
import random

"""=================BRUTE FORCE================="""

"""Adds all vertices outside the source node to a list"""
def create_cities_to_permute(graph, source):
    cities = []
    for city in range(len(graph)):
        if city != source:
            cities.append(city)
    return cities

"""Brute force approach by finding all route permutations and returning the shortest distance"""
def brute_force(graph, source):
    cities = create_cities_to_permute(graph, source)
    route_permutations = permutations(cities)
    min_distance = sys.maxsize
    best_route = ()
    # Loop through each route permutation
    for route in route_permutations:
        curr_distance = 0
        curr_city = source
        # Loop through each city in the route and sum the distances
        for city in route:
            curr_distance += graph[curr_city][city]
            curr_city = city
        # Add the distance back to the source city
        curr_distance += graph[curr_city][source]
        # Update best route and minimum distance if it's better than the others
        if curr_distance < min_distance:
            min_distance = curr_distance
            best_route = route
    return min_distance, best_route

"""Runs brute force and prints the results"""
def print_brute_force(graph, source, city_dict):
    print("--------Brute Force--------")
    distance, route = brute_force(graph, source)
    full_route = str(city_dict[source])
    for city in route:
        full_route += ", " + city_dict[city]
    print("Minimum Distance:", distance, "Miles")
    print("Route:", full_route)

""""=================BACKTRACKING================="""

# List to keep track of route distances
final_distances = []

"""Recursively solves TSP using backtracking"""
def backtracking(graph, visited, source, n, count, cost):
    # Base case where a hamilton cycle has been reached
    if count == n and graph[source][0]:
        final_distances.append(cost+graph[source][0])

    # Traverse other options
    for city in range(n):
        if visited[city] == False and graph[source][city]:
            visited[city] = True
            backtracking(graph, visited, city, n, count+1, cost+graph[source][city])
            visited[city] = False

"""Runs backtracking and prints the results"""
def print_backtracking(graph, source):
    n = len(graph)
    visited = []
    for i in range(n):
        visited.append(False)
    visited[source] = True
    backtracking(graph, visited, source, n, 1, 0)

    print("\n--------Backtracking--------")
    print("Minimum Distance:", min(final_distances), "Miles")

"""Main function"""
def main():
    # Maps index in graph to state name
    city_dict = {0: "Boston",
                 1: "New York City",
                 2: "Raleigh",
                 3: "Atlanta"}

    # Adjacency matrix
    graph = [[0, 187, 710, 946],
             [187, 0, 427, 760],
             [710, 427, 0, 356],
             [946, 760, 356, 0]]

    # Source city index
    source = 0

    print_brute_force(graph, source, city_dict)
    print_backtracking(graph, source)

if __name__ == "__main__":
    main()
