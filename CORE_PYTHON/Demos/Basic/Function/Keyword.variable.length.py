def emp(**data):
    for key, val in data.items():
        print(key,':',val)

emp(id=100, name='ABC',sal=40000,dept='IT')