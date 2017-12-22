#coding: utf-8
from dynamic_programming import dynamic_programming


def FPTAS(number, capacity, weight_cost, scaling_factor=4):

    new_capacity = int(float(capacity) / scaling_factor)
    new_weight_cost = [(round(float(weight) / scaling_factor) + 1, cost) for weight, cost in weight_cost]
    return dynamic_programming(number, new_capacity, new_weight_cost)
