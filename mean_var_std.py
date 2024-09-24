import numpy as np

def calculate(arr):

    if len(arr)!=9:
        raise ValueError('List must contain nine numbers.')

    arr = np.array(arr).reshape(3,3)
    flatten_arr = arr.flatten()

    sum_col = list(np.sum(arr, axis=0))
    sum_row = list(np.sum(arr, axis=1))
    flatten_sum = sum(list(flatten_arr))

    mean_col = list(np.mean(arr, axis=0))
    mean_row = list(np.mean(arr, axis=1))
    flatten_mean = np.mean(flatten_arr)

    std_col = list(np.std(arr, axis=0))
    std_row = list(np.std(arr, axis=1))
    flatten_std = np.std(flatten_arr)

    var_col = list(np.var(arr, axis=0))
    var_row = list(np.var(arr, axis=1))
    flatten_var = np.var(flatten_arr)

    min_col = list(np.min(arr, axis=0))
    min_row = list(np.min(arr, axis=1))
    flatten_min = np.min(flatten_arr)

    max_col = list(np.max(arr, axis=0))
    max_row = list(np.max(arr, axis=1))
    flatten_max = np.max(flatten_arr)


    calculations = {
    'mean':[
        mean_col,
        mean_row,
        flatten_mean
    ],
    'variance': [
        var_col,
        var_row,
        flatten_var
    ],
    'standard deviation': [
        std_col,
        std_row,
        flatten_std
    ],
    'max': [
        max_col,
        max_row,
        flatten_max
    ],
    'min': [
        min_col,
        min_row,
        flatten_min
    ]
    ,
    'sum': [
        sum_col,
        sum_row,
        flatten_sum
    ]}

    return calculations
