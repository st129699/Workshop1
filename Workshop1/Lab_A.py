import csv
import math
from scipy import stats
data = []

with open('Точная шкала.csv', mode='r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    for row in reader:
        if row:
            value = row[0].strip()
            if value:
                data.append(float(value))

def math_e(data):
    return round(sum(data)/len(data), 5)

def dev(data):
    dev = []
    for i in range(len(data)):
        dev.append(round(data[i] - math_e(data), 2))
    return dev

def dispersion(data):
    dev_sq = []
    for i in range(len(dev(data))):
        dev_sq.append(dev(data)[i] * dev(data)[i])
    return sum(dev_sq)/len(dev_sq)

def std_deviation(data):
    return math.sqrt(dispersion(data))

def std_error(data):
    return std_deviation(data)/math.sqrt(len(data))

confidence = 0.95
df = len(data) - 1
t = stats.t.ppf((1 + confidence) / 2, df)

def conf_interval(data):
    interval = []
    left = math_e(data) - (t * std_error(data))
    right = math_e(data) + (t * std_error(data))
    interval.append(round(left, 5))
    interval.append(round(right, 5))
    return interval

def pair_points(data):
    delta_y = data[-1] - data[0]
    n = len(data)
    k = round(delta_y/(n - 1), 5)
    b = data[0]
    return b, k


mean_value = math_e(data)
deviation_value = std_deviation(data)
ci = conf_interval(data)
pair = pair_points(data)

results = [
    ["Среднее арифметическое", mean_value],
    ["Стандартное отклонение", deviation_value],
    ["Нижняя граница доверительного интервала", ci[0]],
    ["Верхняя граница доверительного интервала", ci[1]],
    ["Начальное значение (b) - метод парных точек", pair[0]],
    ["Наклон (k) - метод парных точек", pair[1]]
]


with open('результаты_анализа_ТочнаяШкала.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(results)

print("Результаты сохранены в файл 'результаты_анализа.csv'")