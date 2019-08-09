#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

# get indices function
def get_indices_of_item_weights(weights, length, limit):

    #create hash table
    ht = HashTable(16)

    #for every weight given, make an index of keys
    for i in range(0, len(weights)):
        hash_table_insert(ht, weights[i], i)

    #for every key in the table, assign a value
    for i in range(0, len(weights)):
        value = hash_table_retrieve(ht, limit - weights[i])

        #because we have assigned all our values, we have no collisions
        if value != None:
            return (value, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
