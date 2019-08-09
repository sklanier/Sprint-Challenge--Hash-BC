#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    #insert all ticket k:v pairs into hashtable
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    #find first flight by searching the table for the key with a value of NONE
    first_flight = hash_table_retrieve(hashtable, 'NONE')
    
    #insert first flight into route array at index 0
    route[0] = first_flight

    #for the length of the array (excluding our first flight), assign next index as next flight
    for i in range(len(route) - 1):
        route[i + 1] = hash_table_retrieve(hashtable, route[i])

    return route
