# ------------------------------------------------------------------------------------------------------------
# CNN(Convolutional Neural Network)でMNISTを試す
# ------------------------------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from keras.datasets import mnist
from keras import backend as ke
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D


# ------------------------------------------------------------------------------------------------------------
# ハイパーパラメータ
# ------------------------------------------------------------------------------------------------------------
# ハイパーパラメータ ⇒ バッチサイズ、エポック数
# 例えば、訓練データが60,000個で、batch_sizeを6,000とした場合、
# 学習データをすべて使うのに60,000個÷6,000＝10回のパラメータ更新が行われる。
# これを1epochと言う。epochが10であれば、10×10＝100回のパラメータ更新が行われることとなる。
# epoch数は損失関数(コスト関数)の値がほぼ収束するまでに設定する。
batch_size = 6000           # バッチサイズ
epochs = 5                  # エポック数


# ------------------------------------------------------------------------------------------------------------
# 正誤表関数
# ------------------------------------------------------------------------------------------------------------
def show_prediction():
    n_show = 100                                 # 全部は表示すると大変なので一部を表示
    y = model.predict(X_test)
    plt.figure(2, figsize=(10, 10))
    plt.gray()
    for i in range(n_show):
        plt.subplot(10, 10, (i+1))               # subplot(行数, 列数, プロット番号)
        x = X_test[i, :]
        x = x.reshape(28, 28)
        plt.pcolor(1 - x)
        wk = y[i, :]
        prediction = np.argmax(wk)
        plt.text(22, 25.5, "%d" % prediction, fontsize=12)
        if prediction != np.argmax(y_test[i, :]):
            plt.plot([0, 27], [1, 1], color='red', linewidth=10)
        plt.xlim(0, 27)
        plt.ylim(27, 0)
        plt.xticks([], "")
        plt.yticks([], "")


# ------------------------------------------------------------------------------------------------------------
# keras backendの表示
# ------------------------------------------------------------------------------------------------------------
# print(ke.backend())
# print(ke.floatx())


# ------------------------------------------------------------------------------------------------------------
# MNISTデータの取得
# ------------------------------------------------------------------------------------------------------------
# 初回はダウンロードが発生するため時間がかかる
# 60,000枚の28x28ドットで表現される10個の数字の白黒画像と10,000枚のテスト用画像データセット
# ダウンロード場所：'~/.keras/datasets/'
# ※MNISTのデータダウンロードがNGとなる場合は、PROXYの設定を見直してください
#
# MNISTデータ
#  ├ 教師データ (60,000個)
#  │  ├ 画像データ
#  │  └ ラベルデータ
#  │
#  └ 検証データ (10,000個)
#     ├ 画像データ
#     └ ラベルデータ

# ↓教師データ          ↓検証データ
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# ↑画像    ↑ラベル     ↑画像    ↑ラベル


# ------------------------------------------------------------------------------------------------------------
# 画像データ(教師データ、検証データ)のリシェイプ
# ------------------------------------------------------------------------------------------------------------
img_rows, img_cols = 28, 28
if ke.image_data_format() == 'channels_last':
    X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1)
    X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)
else:
    X_train = X_train.reshape(X_train.shape[0], 1, img_rows, img_cols)
    X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)

# 配列の整形と、色の範囲を0～255 → 0～1に変換
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255


# ------------------------------------------------------------------------------------------------------------
# ラベルデータ(教師データ、検証データ)のベクトル化
# ------------------------------------------------------------------------------------------------------------
y_train = np_utils.to_categorical(y_train)      # 教師ラベルのベクトル化
y_test = np_utils.to_categorical(y_test)        # 検証ラベルのベクトル化


# ------------------------------------------------------------------------------------------------------------
# ネットワークの定義 (keras)
# ------------------------------------------------------------------------------------------------------------
print("")
print("●ネットワーク定義")
model = Sequential()

# 入力層 28×28×3
model.add(Conv2D(16, kernel_size=(3, 3), activation='relu', input_shape=input_shape, padding='same'))     # 01層：畳込み層16枚
model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))                                          # 02層：畳込み層32枚
model.add(MaxPooling2D(pool_size=(2, 2)))                                                                 # 03層：プーリング層
model.add(Dropout(0.25))                                                                                  # 04層：ドロップアウト
model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))                                          # 05層：畳込み層64枚
model.add(MaxPooling2D(pool_size=(2, 2)))                                                                 # 06層：プーリング層
model.add(Flatten())                                                                                      # 08層：次元変換
model.add(Dense(128, activation='relu'))                                                                  # 09層：全結合出力128
model.add(Dense(10, activation='softmax'))                                                                # 10層：全結合出力10

# model表示
model.summary()

# コンパイル
# 損失関数 ：categorical_crossentropy (クロスエントロピー)
# 最適化   ：Adam
model.compile(loss='categorical_crossentropy',
              optimizer='Adam',
              metrics=['accuracy'])

print("")
print("●学習スタート")
f_verbose = 1  # 0:表示なし、1：詳細表示、2：表示
hist = model.fit(X_train, y_train,
                 batch_size=batch_size,
                 epochs=epochs,
                 validation_data=(X_test, y_test),
                 verbose=f_verbose)


# ------------------------------------------------------------------------------------------------------------
# 損失値グラフ化
# ------------------------------------------------------------------------------------------------------------
# Accuracy (正解率)
plt.plot(range(epochs), hist.history['accuracy'], marker='.')
plt.plot(range(epochs), hist.history['val_accuracy'], marker='.')
plt.title('Accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='lower right')
plt.show()

# loss (損失関数)
plt.plot(range(epochs), hist.history['loss'], marker='.')
plt.plot(range(epochs), hist.history['val_loss'], marker='.')
plt.title('loss Function')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper right')
plt.show()


# ------------------------------------------------------------------------------------------------------------
# テストデータ検証
# ------------------------------------------------------------------------------------------------------------
print("")
print("●検証結果")
t_verbose = 1  # 0:表示なし、1：詳細表示、2：表示
score = model.evaluate(X_test, y_test, verbose=t_verbose)

print("")
print("batch_size = ", batch_size)
print("epochs = ", epochs)

print('Test loss:', score[0])
print('Test accuracy:', score[1])


print("")
print("●混同行列(コンフュージョンマトリックス) 横：識別結果、縦：正解データ")
predict_classes = model.predict_classes(X_test[1:60000, ], batch_size=batch_size)
true_classes = np.argmax(y_test[1:60000], 1)
print(confusion_matrix(true_classes, predict_classes))


# ------------------------------------------------------------------------------------------------------------
# 正誤表表示
# ------------------------------------------------------------------------------------------------------------
show_prediction()
plt.show()
