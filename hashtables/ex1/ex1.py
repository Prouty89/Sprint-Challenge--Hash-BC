#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                       )


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # Determine the length of "weights"

    for index in range(length):
        # Compare difference between limitation and weight provided
        diff = limit - weights[index]
        # Check table before weights or added, then proceed by adding more weights to table
        # Limit checking
        target = hash_table_retrieve(ht, diff)
        # If target is not empty, continue
        if target is not None:
            # sum  of Index weight and target limit checking
            return index, target
        # Weights are stored in table
        hash_table_insert(ht, weights[index], index)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


weights_4 = [8, 8]

print(get_indices_of_item_weights(weights_4, 4, 16))
