import sys


def parse_record(line: str) -> dict:
    line = line.split(";")
    if len(line) != 3:
        raise ValueError('В одной строке не три поля!')
    city, temp, date = line
    if not city or not date:
        raise raise ValueError('Город или дата пустые!')
    try:
        temp = float(temp)
    except ValueError:
        raise ValueError('В поле температуры записано не число!')

    return {'city':city, 'temp':temp, 'date':date}


def read_valid(lines: list[str]) -> list[dict]:
    ls = []
    for line in lines:
        if not line:
            continue
        try:
            d = parse_record(line)
            ls += [d]

        except ValueError:
            continue
    return ls


def average_by_city(records: list[dict]) -> dict:
    records = read_valid(records))
    total = {}
    count = {}
    d = {}
    for line in records:
        city, temp, date = d['city'], d['temp'], d['date']
        total[city] = total.get(city, 0) + float(temp)
        count[city] = count.get(city, 0) + 1

    for key in total:
        d[key] = round(total[key]/count[key], 1)
    return d


def warmest_city(records: list[dict]) -> str:
    d = average_by_city(records)
    mx = max(d.items(), key=lambda x:[-x[1], x[0]])
    return f'Город с наибольшей ср температурой: {mx[0]} со значением {mx[1]}'
