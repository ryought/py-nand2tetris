#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def realtime_plot():
    fig, ax = plt.subplots(1,1)
    x = np.arange(-np.pi, np.pi, 0.1)
    y = np.sin(x)

    # 初期化的に一度プロット
    lines, = ax.plot(x,y)

    while True:
        x += 0.1
        y = np.sin(x)

        # 上で受けたlinesに乗ってる描画データを更新する
        lines.set_data(x,y)
        # 軸は自動修正されない、手動で設定する
        ax.set_xlim((x.min(), x.max()))

        # ポーズ
        plt.pause(0.01)

realtime_plot()


