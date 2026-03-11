def dict_from_keys(keys_arr, value_arr):
    if len(keys_arr) != len(value_arr):
        raise ValueError("Arrays are not the same length")

    return dict(zip(keys_arr, value_arr))


keys = ["a", "b", "c", "d"]
vals = [1, 2, 3, 4]
result = dict_from_keys(keys, vals)
print(result)


def flatten_list(lst):
    result = []

    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    print(result)
    return result


nested = [1, [2, 3], [4, [5, 6]], 7]
flatten_list(nested)


def roatate_array(arr, k):
    n = len(arr)
    reverse(arr, 0, n - 1)
    print(arr)
    reverse(arr, 0, k - 1)
    print(arr)
    reverse(arr, k, n - 1)
    print(arr)


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


roatate_array([1, 2, 3, 4, 5], 2)
