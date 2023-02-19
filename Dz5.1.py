result = []


def divider(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('NO NULL')
        return 0
    except TypeError:
        print('STR')
        return 0


data = {10: 2,
        2: 5,
        "123": 4,
        18: 0,
        '1': 15,
        8: 4}

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)
