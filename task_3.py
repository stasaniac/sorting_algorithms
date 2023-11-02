#!/usr/bin/env python3
'''
Std. no: 2778835
'''

from typing import Optional, List, Tuple, Union


class Order:
    def __init__(self, id: int, selection_time: int, shipping_time: int,
                 next: Optional["Order"] = None):
        self.id: int = id
        self.selection_time: int = selection_time
        self.shipping_time:  int = shipping_time

        '''
        Remove me if you don't need me.
        Or, add a method to assign to me if you want to use linked lists.
        '''
        self.next: Union[Order, None] = next

    '''
    Make your life easier and your code prettier, use `Operator Overloading`.
    '''
# We're going to implement a sorting algorithm called quicksort.
# We want to sort a list of 'Order' objects based on their combined selection and shipping times.

def quick_sort_algorithm(data: List[Order]) -> List[Order]:
    # If there are only one or zero elements in the data, it's already sorted.
    if len(data) <= 1:
        return data

    # To sort the data efficiently, we'll use a technique called the quicksort algorithm.
    # It works by picking a 'pivot' element and partitioning the data into two smaller sublists.
    # One sublist contains elements less than the pivot, and the other sublist contains elements greater than the pivot.
    # We'll keep track of these sublists using a 'stack' data structure.

    stack = [(0, len(data) - 1)]  # We start with the entire list.

    while stack:
        # We pop a segment from the stack.
        low, high = stack.pop()

        if low < high:
            # We choose a 'pivot' element from the segment. Let's call it 'pivot_order'.
            pivot_order = data[low + (high - low) // 2]

            # We'll partition the segment into two sublists, one with elements less than the pivot and the other with elements greater.
            i = low - 1  # Initialize i to the left of the segment.
            j = high + 1  # Initialize j to the right of the segment.

            while True:
                i += 1
                while (data[i].selection_time + data[i].shipping_time) < (
                        pivot_order.selection_time + pivot_order.shipping_time):
                    i += 1

                j -= 1
                while (data[j].selection_time + data[j].shipping_time) > (
                        pivot_order.selection_time + pivot_order.shipping_time):
                    j -= 1

                if i >= j:
                    # If i and j have crossed each other, we've partitioned the segment.
                    break

                # Swap the elements at i and j.
                data[i], data[j] = data[j], data[i]

            # Push the left and right subsegments onto the stack for further sorting.
            stack.append((low, j))
            stack.append((j + 1, high))

    # Finally, we return the sorted data.
    return data


# This function performs quicksort on 'Order' objects based on their selection and shipping times.


def sort(data: List[Tuple[int, int, int]]) -> List[int]:
    # Here we have a list of orders, each represented as (order_id, selection_time, shipping_time).

    # First, we will create an empty list to store the sorted order IDs.
    sorted_order_ids = []

    # Now, we will go through each order in the input data.
    for order_id, selection_time, shipping_time in data:
        # In order to figure out when an order will be ready for shipping, we are going to add selection_time and shipping_time.
        delivery_time = selection_time + shipping_time

        # Here we will store the order ID and its calculated delivery time as a tuple.
        order_info = (order_id, delivery_time)

        # Here we will add this tuple to our list of order information.
        sorted_order_ids.append(order_info)

    # Now, we will sort our list of order information based on delivery time.
    sorted_order_ids.sort(key=lambda x: x[1])

    # Finally, we will extract just the order IDs from our sorted list.
    sorted_ids = [order[0] for order in sorted_order_ids]

    # We will return the sorted order IDs.
    return sorted_ids

'''
Use for your local testing
'''
# if __name__ == '__main__':
#     data = [(1, 500, 100), (2, 700, 100), (3, 100, 100)]
#     result = sort(data)
#     print(result)

