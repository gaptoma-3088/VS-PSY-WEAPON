#!/data/data/com.termux/files/usr/bin/python
import numpy as np
import IPython.display as display
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import random

# --- 1. ПОДГОТОВКА (Вне цикла, чтобы не тормозило) ---
num_points = random.uniform(8800000, 9000000)
int_num_points = int(num_points)

r = np.random.uniform(1.5, 5.0, int_num_points)
theta = np.random.uniform(0, 2 * np.pi, int_num_points)
z = np.random.normal(0, 0.12, int_num_points) * (r**0.5)

x = r * np.cos(theta)
y = r * np.sin(theta)
colors = plt.cm.YlOrRd(1 - (r - 1.5) / 3.5)

# Сфера (горизонт событий)
u_s = np.linspace(0, 2 * np.pi, 15)
v_s = np.linspace(0, np.pi, 15)
xs = 1.1 * np.outer(np.cos(u_s), np.sin(v_s))
ys = 1.1 * np.outer(np.sin(u_s), np.sin(v_s))
zs = 1.1 * np.outer(np.ones(np.size(u_s)), np.cos(v_s))


# --- 2. АНИМАЦИЯ ---
#angle = 0
random_angle = random.uniform(0, 360)
try:
    while random_angle <= 360:
        num_points = random.uniform(8800000, 9000000)
        int_num_points = int(num_points)

        r = np.random.uniform(1.5, 5.0, int_num_points)
        theta = np.random.uniform(0, 2 * np.pi, int_num_points)
        z = np.random.normal(0, 0.12, int_num_points) * (r**0.5)

        x = r * np.cos(theta)
        y = r * np.sin(theta)
        colors = plt.cm.YlOrRd(1 - (r - 1.5) / 3.5)

        # Сфера (горизонт событий)
        u_s = np.linspace(0, 2 * np.pi, 15)
        v_s = np.linspace(0, np.pi, 15)
        xs = 1.1 * np.outer(np.cos(u_s), np.sin(v_s))
        ys = 1.1 * np.outer(np.sin(u_s), np.sin(v_s))
        zs = 1.1 * np.outer(np.ones(np.size(u_s)), np.cos(v_s))

        # Создаем фигуру
        fig = plt.figure(figsize=(10, 7), facecolor='black')
        ax = fig.add_subplot(111, projection='3d', facecolor='black')

        # Рандомный параметр elev от 0 до 1000
        random_elev = random.uniform(0, 24000)

        # Рисуем объекты
        ax.scatter(x, y, z, c=colors, s=0.7, alpha=0.3, edgecolors='none')
        ax.plot_surface(xs, ys, zs, color='black')

        # Ограничения и оси
        ax.set_xlim([-5, 5])
        ax.set_ylim([-5, 5])
        ax.set_zlim([-5, 5])
        ax.axis('off')

        # Применяем вращение (azim) и рандомный наклон (elev)
        ax.view_init(elev=random_elev, azim=random_angle)

        # Вывод кадра
        display.clear_output(wait=True)
        display.display(plt.gcf())
        plt.close(fig) # Важно: закрываем фигуру, чтобы не было утечки памяти

        random_angle += 1
        time.sleep(0.00000000001)

except Exception as e:
    print(f"Произошла ошибка: {e}")
