
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


def sort(data: List[Tuple[int, int, int]]) -> List[int]:
    # We will use selection sort and convert input data into a list of Order objects
    orders = [Order(order_id, selection_time, shipping_time) for order_id, selection_time, shipping_time in data]

    n = len(orders)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            # Calculate delivery time for each order
            delivery_time_i = orders[i].selection_time + orders[i].shipping_time
            delivery_time_j = orders[j].selection_time + orders[j].shipping_time

            if delivery_time_j < delivery_time_i:
                min_idx = j

        # Swap orders
        orders[i], orders[min_idx] = orders[min_idx], orders[i]

    # Extract the sorted order IDs
    sorted_ids = [order.id for order in orders]

    return sorted_ids

'''
Use for your local testing
'''
# if __name__ == '__main__':
#     data = [(1, 500, 100), (2, 700, 100), (3, 100, 100)]
#     result = sort(data)
#     print(result)