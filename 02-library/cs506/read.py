def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    res = []
    csv_file = open(csv_file_path,'r')
    for line in csv_file.readlines():
        row = []
        values = line.strip('\n').split(',')
        for val in values:
            try:
                converted = int(val)
            except ValueError:
                converted = val.strip("\"")
            row.append(converted)
        res.append(row)
    print(res)
    return res

