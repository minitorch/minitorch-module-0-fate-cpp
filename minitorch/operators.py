"""Collection of the core mathematical operators used throughout the code base."""

import math
# ## Task 0.1
from typing import Callable, Iterable
from functools import reduce as reduce_
#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
def mul(a: float, b: float) -> float:
    return a * b

# - id
def id(a: float) -> float:
    return a

# - add
def add(a: float, b: float) -> float:
    return a + b

# - neg
def neg(a: float) -> float:
    return -1*a

# - lt
def lt(a: float, b: float) -> bool:
    return a < b
# - eq
def eq(a: float, b: float) -> bool:
    return a==b

# - max
def max(a: float, b: float) -> float:
    return a if a > b else b

# - is_close
def is_close(a: float, b: float) -> bool:
    value = 1e-2
    return abs(a-b) < value

# - sigmoid
def sigmoid(a: float) -> float:
    return (
        1.0 / (1.0 + math.exp(-a)) if a >= 0 else (math.exp(a) / (1.0 + math.exp(a)))
    )

# - relu
def relu(a: float) -> float:
    return a if a > 0 else 0

# - log
def log(a: float) -> float:
    return math.log(a)

# - exp
def exp(a: float) -> float:
    return math.exp(a)

# - log_back
def log_back(a: float, n: float) -> float:
    return n / a

# - inv
def inv(a: float) -> float:
    return 1.0 / a

# - inv_back
def inv_back(a: float, n: float) -> float:
    return -n / a ** 2

# - relu_back
def relu_back(a: float, n: float) -> float:
    return n if a > 0 else 0

#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
def map(fn):
    """
    Higher-order function that applies a given function 
    to each element of an iterable
    """
    def map_fn(inp_list):
        return [fn(x) for x in inp_list]
    return map_fn

# - zipWith
def zipWith(fn):
    """
    Higher-order function that combines elements 
    from two iterables using a given function
    """
    def zipWith_fn(inp_list1, inp_list2):
        return [fn(x, y) for x, y in zip(inp_list1, inp_list2)]
    return zipWith_fn

# - reduce
def reduce(fn, initial):
    """
    Higher-order function that reduces an iterable 
    to a single value using a given function
    """
    def reduce_fn(inp_list):
        return reduce_(fn, inp_list, initial) 
    return reduce_fn
#
# Use these to implement
# - negList : negate a list
def negList(inp_list):
    """
    Negate all elements in a list using map
    """
    return map(neg)(inp_list)

# - addLists : add two lists together
def addLists(inp_list1, inp_list2):
    """
    Add corresponding elements from two lists using zipWith
    """
    return zipWith(add)(inp_list1, inp_list2)

# - sum: sum lists
def sum(inp_list):
    """
    Sum all elements in a list using reduce
    """
    return reduce(add, 0)(inp_list)

# - prod: take the product of lists
def prod(inp_list):
    """
     Calculate the product of all elements in a list using reduce
    """
    return reduce(mul, 1)(inp_list)

# TODO: Implement for Task 0.3.
