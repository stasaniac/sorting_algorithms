#!/usr/bin/env python3
'''
Std. no: 2778835
'''

from typing import Optional, List, Tuple, Union


class Job:
    def __init__(self, id: int, p: int, w: int, next: Optional["Job"] = None):
        self.id: int = id
        self.p:  int = p
        self.w:  int = w

        '''
        Remove me if you don't need me.
        Or, add a method to assign to me if you want to use linked lists.
        '''
        self.next: Union[Job, None] = next

    '''
    Make your life easier and your code prettier, use `Operator Overloading`.
    '''


def merge_sort(arr: List[Job]):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left: List[Job], right: List[Job]):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        left_value = left[left_idx].p / left[left_idx].w
        right_value = right[right_idx].p / right[right_idx].w

        if left_value <= right_value:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

def smiths_rule_sorting_algorithm(data: List[Job]) -> List[Job]:
    return merge_sort(data)


def sort(data: List[Tuple[int, int, int]]) -> List[int]:
    jobs = [Job(job_id, p, w) for job_id, p, w in data]
    sorted_jobs = smiths_rule_sorting_algorithm(jobs)
    sorted_job_ids = [job.id for job in sorted_jobs]
    return sorted_job_ids

'''
Use for your local testing
'''
# if __name__ == '__main__':
#     data = [(1, 500, 100), (2, 700, 100), (3, 100, 100)]
#     result = sort(data)
#     print(result)



