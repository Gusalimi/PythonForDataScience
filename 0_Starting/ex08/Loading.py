# import os


def ft_tqdm(lst: range) -> None:
    """Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested."""
    i = 0
    length = len(lst)
    for i in range(length):
        yield lst[i]
        current = int(((i + 1)/len(lst))*100)

        # without os:
        progress = '█'*current
        spaces = ' '*int(100 - current)
        num_progress = str(i + 1) + '/' + str(length)

        # with os:
        # os_width = os.get_terminal_size().columns
        # print(' ' * (os_width - 1), end='\r')
        # width = os_width - (len(f"{current}%||{i + 1}/{len(lst)}")) - 27
        # progress = '█'*int(current * width / 100)
        # spaces = ' '*int((100 - current) * width / 100)
        # num_progress = str(i + 1) + '/' + str(length)

        print(f"{current}%|{progress}{spaces}| {num_progress}", end='\r')
