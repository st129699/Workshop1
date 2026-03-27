# prepare_data.py
import csv
from collections import Counter

# ===== 1. Загрузка данных из вашего CSV =====
data = []
with open('точная шкала.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for row in reader:
        if row:
            try:
                # Если в CSV один столбец
                data.append(float(row[0]))
            except:
                # Если в CSV несколько столбцов, берем первый числовой
                for val in row:
                    try:
                        data.append(float(val))
                        break
                    except:
                        pass

print(f"Загружено {len(data)} измерений")

# ===== 2. Данные для графика временной зависимости =====
with open('tochnaya_shkala.txt', 'w') as f:
    for i, val in enumerate(data, 1):
        f.write(f"{i} {val:.2f}\n")
print("✓ Создан: tochnaya_shkala.txt")

# ===== 3. Данные для гистограммы =====
# Определяем интервалы для гистограммы
min_val = min(data)
max_val = max(data)
print(f"Диапазон значений: {min_val:.2f} - {max_val:.2f}")

# Разбиваем на интервалы (например, 8 интервалов)
k = 8
h = (max_val - min_val) / k
intervals = []

for i in range(k):
    left = min_val + i * h
    right = left + h
    center = (left + right) / 2
    intervals.append({'left': left, 'right': right, 'center': center, 'count': 0})

# Подсчет попаданий в интервалы
for val in data:
    for interval in intervals:
        if interval['left'] <= val < interval['right'] or (val == max_val and interval['right'] == max_val):
            interval['count'] += 1
            break

# Сохраняем для гистограммы
with open('histogram_data.txt', 'w') as f:
    for interval in intervals:
        f.write(f"{interval['center']:.3f} {interval['count']}\n")
print("✓ Создан: histogram_data.txt")

# ===== 4. Данные для графика относительной частоты =====
with open('relative_freq.txt', 'w') as f:
    for interval in intervals:
        rel_freq = interval['count'] / len(data)
        f.write(f"{interval['center']:.3f} {rel_freq:.4f}\n")
print("✓ Создан: relative_freq.txt")

print("\nВсе файлы подготовлены! Теперь можно запускать gnuplot.")