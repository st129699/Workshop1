import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# ========== ЗАГРУЗКА ДАННЫХ С ПРАВИЛЬНЫМ ПУТЕМ ==========
file_path = r'C:\Lab\Workshop1\tochnaya_shkala.csv'

data = []
with open(file_path, mode='r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    for row in reader:
        if row:
            try:
                data.append(float(row[0]))
            except:
                pass

print(f"Загружено {len(data)} измерений")

# ========== 1. ГРАФИК ВРЕМЕННОЙ ЗАВИСИМОСТИ ==========
plt.figure(figsize=(10, 6))
x = list(range(1, len(data) + 1))
plt.scatter(x, data, s=30, color='blue', alpha=0.6, label='Измерения')
plt.xlabel('Номер измерения', fontsize=12)
plt.ylabel('Частота, кГц', fontsize=12)
plt.title('Зависимость результатов наблюдений от времени', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('C:\\Lab\\Workshop1\\time_dependence.png', dpi=150)
print("✓ Сохранен: time_dependence.png")
plt.close()

# ========== 2. ГИСТОГРАММА РАСПРЕДЕЛЕНИЯ ==========
plt.figure(figsize=(10, 6))

k = 8
counts, bins, patches = plt.hist(data, bins=k, color='skyblue', 
                                   edgecolor='black', alpha=0.7)

plt.xlabel('Частота, кГц', fontsize=12)
plt.ylabel('Число наблюдений', fontsize=12)
plt.title('Гистограмма распределения результатов наблюдений', fontsize=14)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('C:\\Lab\\Workshop1\\histogram.png', dpi=150)
print("✓ Сохранен: histogram.png")
plt.close()

# ========== 3. ГРАФИК ОТНОСИТЕЛЬНОЙ ЧАСТОТЫ ==========
plt.figure(figsize=(10, 6))

counter = Counter(round(x, 2) for x in data)
values = sorted(counter.keys())
freqs = [counter[v] for v in values]
rel_freqs = [f / len(data) for f in freqs]

plt.plot(values, rel_freqs, 'o', color='red', markersize=8, 
         markeredgecolor='black', label='δn = Δn/n')
plt.plot(values, rel_freqs, '--', color='gray', alpha=0.5)

plt.xlabel('Частота, кГц', fontsize=12)
plt.ylabel('δn = Δn/n', fontsize=12)
plt.title('График относительной частоты', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('C:\\Lab\\Workshop1\\relative_freq.png', dpi=150)
print("✓ Сохранен: relative_freq.png")

# ========== ВЫВОД СТАТИСТИКИ ==========
print("\n" + "="*50)
print("СТАТИСТИЧЕСКИЕ ХАРАКТЕРИСТИКИ")
print("="*50)
print(f"Количество измерений: {len(data)}")
print(f"Минимум: {min(data):.2f} кГц")
print(f"Максимум: {max(data):.2f} кГц")
print(f"Среднее: {np.mean(data):.4f} кГц")
print(f"Стандартное отклонение: {np.std(data, ddof=1):.4f} кГц")

from scipy import stats
mean = np.mean(data)
std_err = np.std(data, ddof=1) / np.sqrt(len(data))
t = stats.t.ppf(0.975, len(data) - 1)
delta = t * std_err
print(f"95% Доверительный интервал: [{mean - delta:.4f}; {mean + delta:.4f}] кГц")

print("\nГрафики сохранены в папку: C:\\Lab\\Workshop1\\")