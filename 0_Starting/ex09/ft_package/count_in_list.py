def count_in_list(lst: list, item: any) -> int:
    """Count the number of times item appears in the list lst."""
    count = 0
    for i in lst:
        if i == item:
            count += 1
    return count
