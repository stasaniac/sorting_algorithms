#!/usr/bin/env python3
'''
Std. no: 2778835
'''

from typing import Optional, List, Tuple, Union



class Order:
    def __init__(self, id: int, selection_time: int, shipping_time: int):
        self.id: int = id
        self.selection_time: int = selection_time
        self.shipping_time: int = shipping_time

def merge_sort(data: List[Order]) -> List[Order]:
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left: List[Order], right: List[Order]) -> List[Order]:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if (left[i].selection_time + left[i].shipping_time) < (right[j].selection_time + right[j].shipping_time):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def sort(data: List[Tuple[int, int, int]]) -> List[int]:
    orders = [Order(id, selection_time, shipping_time) for id, selection_time, shipping_time in data]
    sorted_orders = merge_sort(orders)
    sorted_order_ids = [order.id for order in sorted_orders]
    return sorted_order_ids
'''
Use for your local testing
'''
if __name__ == '__main__':
    data = [(1, 500, 100), (2, 700, 100), (3, 100, 100)]
    result = sort(data)
    print(result)



