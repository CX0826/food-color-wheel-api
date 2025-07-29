import matplotlib.pyplot as plt
import numpy as np
import os

def create_wheel(colors_logged, save_path):
    color_angle_map = {
        "red": 0,
        "orange": 30,
        "yellow": 60,
        "green": 120,
        "blue": 240,
        "purple": 270,
        "brown": 75
    }

    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
    hues = np.linspace(0, 2 * np.pi, 360)
    for i, h in enumerate(hues):
        ax.bar(h, 1, width=0.017, color=plt.cm.hsv(i / 360), bottom=0)

    for color in colors_logged:
        angle_deg = color_angle_map.get(color.lower())
        if angle_deg is not None:
            angle_rad = np.deg2rad(angle_deg)
            ax.plot(angle_rad, 1.05, 'ko')

    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_axis_off()
    plt.tight_layout()

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, transparent=True)
    plt.close()
