#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                       )


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # Retrieve FIRST location = NONE, stored so comparative destination determined via ROUTE

    route[0] = hash_table_retrieve(hashtable, 'NONE')

    # Retrieve NEXT, skipping the FIRST location, use previous location as ref for following.

    for i in range(1, length):
        route[i] = hash_table_retrieve(hashtable, route[i - 1])

    return route

    # 'NoneType' object is not iterable
