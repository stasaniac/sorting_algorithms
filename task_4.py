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

# We're going to implement the merge sort algorithm.
# This function sorts a list of 'Order' objects based on their combined selection and shipping times.

def merge_sort(data: List[Order]) -> List[Order]:
    # If there's only one or zero elements in the data, it's already sorted.
    if len(data) <= 1:
        return data

    # We'll divide the data into two halves.
    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]

    # We'll recursively sort both halves.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Now, we'll merge the sorted halves back together.
    return merge(left_half, right_half)

# This function splits and sorts the 'Order' objects using the merge sort algorithm.

def merge(left: List[Order], right: List[Order]) -> List[Order]:
    result = []
    left_idx, right_idx = 0, 0

    # We'll merge the two sorted lists back together while maintaining the sorting order.
    while left_idx < len(left) and right_idx < len(right):
        if (left[left_idx].selection_time + left[left_idx].shipping_time) <= (
                right[right_idx].selection_time + right[right_idx].shipping_time):
            # If the left element is smaller or equal, we append it to the result.
            result.append(left[left_idx])
            left_idx += 1
        else:
            # Otherwise, we append the right element.
            result.append(right[right_idx])
            right_idx += 1

    # After merging, there might be remaining elements in either left or right lists.
    # We add them to the result.
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result

# This function merges two sorted lists while preserving the sorting order.


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


if __name__ == '__main__':
    data = [(1, 500, 100), (2, 700, 100), (3, 100, 100)]
    result = sort(data)
    print(result)






