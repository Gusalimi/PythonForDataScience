def ft_filter(func, lst):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if func is None:
        return (iter([item for item in lst if item]))
    return (iter([item for item in lst if func(item)]))


# def main():
#     lst = [0, 1, 2, 3, 4, 5]
#     print("lst = [0, 1, 2, 3, 4, 5]\n")
#     print(" FT ".center(20, '='))
#     print(ft_filter.__doc__)
#     print(list(ft_filter(lambda x: x % 2 == 0, lst)))
#     print(list(ft_filter(None, lst)))
#     print(list(ft_filter(lambda x: x % 2 == 0, [])))
#     print()
#     print(" NORMAL ".center(20, '='))
#     print(filter.__doc__)
#     print(list(filter(lambda x: x % 2 == 0, lst)))
#     print(list(filter(None, lst)))
#     print(list(ft_filter(lambda x: x % 2 == 0, [])))


# if __name__ == "__main__":
#     main()
