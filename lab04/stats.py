import sys


def parse_record(line: str) -> dict:
    line = line.split(";")
    if len(line) != 3:
        raise ValueError('В одной строке не три поля!')
    city, temp, date = line
    if not city or not date:
        raise ValueError('Город или дата пустые!')
    try:
        temp = float(temp)
    except ValueError:
        raise ValueError('В поле температуры записано не число!')

    return {'city':city, 'temp':temp, 'date':date.split()}


def read_valid(lines: list[str]) -> list[dict]:
    global cnt_t
    global cnt_f
    ls = []
    for line in lines:
        if not line:
            continue
        try:
            d = parse_record(line)
            cnt_t += 1
            ls += [d]

        except ValueError:
            cnt_f += 1
            continue
    print(cnt_t)
    print(cnt_f)
    return ls


def average_by_city(records: list[dict]) -> dict:
    records = read_valid(records)
    total = {}
    count = {}
    d = {}
    for line in records:
        city, temp, date = line['city'], line['temp'], line['date']
        total[city] = total.get(city, 0) + float(temp)
        count[city] = count.get(city, 0) + 1

    for key in total:
        d[key] = round(total[key]/count[key], 1)
    return d


def warmest_city(records: list[dict]) -> str:
    d = average_by_city(records)
    mx = sorted(d.items(), key=lambda x:[-x[1], x[0]])[0]

    # return f'Город с наибольшей ср температурой: {mx[0]} со значением {mx[1]}'
    return mx[1]

cnt_t, cnt_f = 0, 0
# lines = sys.stdin.read().splitlines()
# print(read_valid(lines))
# print(average_by_city(lines))
# print(warmest_city(lines))
# print(cnt_f, cnt_t)