    raw = []
    results = []

    with open(filename, "r") as f:
        raw = [line for line in f]

    pattern = r'all\s+(\d+)\s([A-Za-z_]*)\s*(\d+)\s(\d+):(\d+)\s(.*)'

    for line in raw:
        match = re.findall(pattern, line)
        (size, month, day, hour, minute, filename) = (int(match[0][0]), match[0][1], int(match[0][2]), int(match[0][3]), int(match[0][4]), match[0][5])
        results.append((size, month, day, hour, minute, filename))