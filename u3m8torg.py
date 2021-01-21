# 加载需要的模块
import os
import sys
import requests
from imp import reload
reload(sys)


# tsリンクが得られる,パラメータurlは.m3u8リンクである
def get_ts(url):
    path = "C://Clone_Videos"  # 既定のビデオ保存パス

    all_url = url.split('/')  # split は '/' に基づいて文字列をリストに分割します
    url_pre = '/'.join(all_url[:-1]) + '/'  # 最後の項目を破棄し、新しい URL にステッチします
    url_next = all_url[-1]  # リストall_url末尾にある項目を取得します

    # requests.get()函数返回的是requests.models.Response对象
    m3u8_txt = requests.get(url, headers={'Connection': 'close'}, verify=False)
    with open(url_next, 'wb') as m3u8_content:  # m3u8ファイルを作成し、
        m3u8_content.write(m3u8_txt.content)  # m3u8_txt.content はバイト ストリームです

    movies = []  # 取得した完全な .ts ビデオ リンクを格納するリストを作成します

    urls = open(url_next, 'rb')
    for line in urls.readlines():
        line2 = line.decode()						# bytes -> str
        if '.ts' in line2:  # 抽出.tsファイルのリンク
            # 完全な .ts ネットワーク リンクにステッチされ、movies リストに保存され、line2[:-1] は末尾の改行を削除します
            movies.append(url_pre + line2[:-1])
        else:
            continue
    urls.close()  # 閉じます
    return movies  # 一覧に戻ります


# スライスダウンロード関数、引数moviesは.tsリンクです。
def down_ts(movies):
    # os.chdir(path)
    i = 0
    print("Downloaded中")
    for _url in movies:
        movie_name = ("%03d.ts" % (i))  # ビデオクリップの名前とパス(_url.split('/')[-1][-6:])  # 接続で最後の 6 ビットをファイル名として抽出します。
        error_get = []  # エラーが発生したリンクを格納するリストを作成します。
        try:
            movie = requests.get(_url, headers={'Connection': 'close'}, timeout=60,verify=False)  # .ts リンクを開きます
            print('movie',movie)
        except:
            error_get.append(_url)
            continue
        print('movie_name',movie_name)
        movie_content = open('C://Reptile_video/' + movie_name, 'wb')  # ファイルをローカルに作成します
        movie_content.writelines(movie)  # スライスをダウンロードします
        if error_get:
            down_ts(error_get)  # エラー一覧を再ダウンロードします
        else:
            print("ダウンロードは成功しました。")
            i = i+1            
    print("すべてのスライスのダウンロードが完了しました。")
    num = len(movies)  # リスト要素の数を取得します

    return num  # 要素の数を返します


# 分割をマージします
def merge_ts(num):
    path = "C:\\Reptile_video"

    new_path = ("%s\out.ts" % path) #結合マージfile名
    f = open(new_path, 'wb+')  # バイナリ書き込み操作

    for i in range(0, num):
        filepath = ("%s\%03d.ts" % (path, i))  # ビデオクリップの名前とパス
        print(filepath)
        for line in open(filepath, "rb"):
            f.write(line)
        f.flush()
    f.close()
    print("マージが完了しました,トランスコードを開始します")


# トランスコードはMP4です
def change_mp4(name):
    fn = 'C:\\Reptile_video\out.ts'
    output = "C:\\Reptile_video\%s.mp4" % name
    cmd = "ffmpeg " + "-i " + fn + " -acodec copy -vcodec copy -f mp4 " + output
    print(cmd)
    os.system(cmd)
    print("トランスコードが完了しました")



# 元のファイルを空にします
def del_ts(num):
    path = "C://Reptile_video/out.ts"  # ファイルを削除するパス
    os.remove(path)  # ファイルをクリアします
    for i in range(0, num):
        path = ("C://Reptile_video/%03d.ts" % i)  # ファイルを削除するパス
        os.remove(path)  # ファイルをクリアします
    print("クリーンアップが完了し、プログラムが終了します")


# メイン関数コードを次に示します。
if __name__ == "__main__":
    url = 'https://d.ossrs.net:8088/live/livestream.m3u8'# input("请输入.m3u8链接：")
    movie_name = 'sample'  # input("input to VideoName")
    movie_all = []
    movie_all = get_ts(url)
    num = down_ts(movie_all)
    merge_ts(num)
    change_mp4(movie_name)
    #del_ts(num)
