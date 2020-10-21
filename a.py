'''
import numpy as npy

# データ生成
xnum = 8
views =[235,375,568,931,1497,1542,3176,1084]
users =[24,93,154,370,746,868,1809,699]

# データをblog_data.npzファイルに保存する
npy.savez('blog_data.npz',X=views,X_min=min(views),X_max=max(views),X_n=len(views),Y=users)

# データをblog_data.npzファイルから取り出す
sample_data = npy.load('blog_data.npz')

print(sample_data['X'])
print(sample_data['X_min'])


import numpy as npy
import matplotlib.pyplot as plt
#%matplotlib inline

# データをblog_data.npzファイルから取り出す
sample_data = npy.load('blog_data.npz')

plt.figure(figsize=(4,4))
plt.plot(sample_data['X'],sample_data['Y'],marker='o',linestyle='None',markeredgecolor='black',color='cornflowerblue')
plt.xlim(sample_data['X_min'],sample_data['X_max'])
plt.grid(True)

# 表示する
plt.show()
'''


import numpy as npy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#%matplotlib inline

# 平均誤差関数
def mse_line(x,t,w):
    y = w[0]*x + w[1]
    # 要素の平均を求める
    mse = npy.mean((y-t)**2)
    
    return mse

# データの読み込み
sample_data = npy.load('blog_data.npz')

# データの計算
xn = 100
w0_range = [-5, 5]
w1_range = [-1000, 1000]
w0 = npy.linspace(w0_range[0],w0_range[1],xn)
w1 = npy.linspace(w1_range[0],w1_range[1],xn)
# グリッドを作成する
ww0, ww1 = npy.meshgrid(w0, w1)
J = npy.zeros((len(w0), len(w1)))

for i0 in range(len(w0)):
    for i1 in range(len(w1)):
        J[i1, i0] = mse_line(sample_data['X'],sample_data['Y'],(w0[i0], w1[i1]))

# 表示
plt.figure(figsize=(9.5, 4))
plt.subplots_adjust(wspace=0.5)

ax = plt.subplot(1,2,1,projection='3d')

ax.plot_surface(ww0, ww1, J, rstride=10, cstride=10, alpha=0.3, color='blue', edgecolor='black')

ax.set_xticks([-10, 0, 10])
ax.set_yticks([-1000, 0, 1000])
ax.set_zticks([0, 10000000, 100000000])
ax.view_init(20, 60)

plt.subplot(1,2,2)
cont = plt.contour(ww0, ww1, J, 30, colors='black', levels=[100000, 1000000, 10000000])
cont.clabel(fmt='%d', fontsize=8)
plt.grid(True)
plt.show()