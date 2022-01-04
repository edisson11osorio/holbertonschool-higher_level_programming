#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple3 = (0, 0)
    tuple1 = tuple_a + tuple3
    tuple2 = tuple_b + tuple3
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])
