def ft_statistics(*args: any, **kwargs: any) -> None:
    """Prints the statistics of the given arguments."""
    for elem in args:
        if (not isinstance(elem, (int, float))):
            print("ERROR")
            return
    for elem in kwargs:
        if (not isinstance(kwargs[elem], str)):
            print("ERROR")
            return
    for elem in kwargs.values():
        if (len(args) == 0):
            print("ERROR")
            continue
        if (elem == "mean"):
            print(f"mean: {sum(args) / len(args)}")
        elif (elem == "median"):
            print(f"median: {sorted(args)[len(args) // 2]}")
        elif (elem == "quartile"):
            q25 = float(sorted(args)[len(args) // 4])
            q75 = float(sorted(args)[len(args) // 4 * 3])
            print(f"quartile: {[str(q25), str(q75)]}")
        elif (elem == "std"):
            std = (sum((x - (sum(args) / len(args))) ** 2
                       for x in args) / len(args)) ** 0.5
            print(f"std: {std}")
        elif (elem == "var"):
            var = sum((x - (sum(args) / len(args))) ** 2
                      for x in args) / len(args)
            print(f"var: {var}")
