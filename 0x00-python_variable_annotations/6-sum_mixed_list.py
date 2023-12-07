#!/usr/bin/env python3
"""
function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float
"""
from typing import List, Union

def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Return sum of mixed list
    """
    return sum(mxd_list)
