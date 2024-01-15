#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_product = 0
    sum_weight = 0
    weight_ave = 0
    for item in my_list:
        sum_product += item[0] * item[1]
        sum_weight += item[1]
    weight_ave = sum_product / sum_weight
    return weight_ave
