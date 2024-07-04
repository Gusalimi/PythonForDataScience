def callLimit(limit: int):
    count = 0

    def callLimiter(function):

        def limit_function(*args: any, **kwds: any):
            nonlocal count
            count += 1
            if count > limit:
                print(f"Erreur: <function {function.__name__} at \
{hex(id(function))}> call too many times")
                return
            function()
        return limit_function
    return callLimiter
