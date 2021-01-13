# 加载需要的模块
import os
import sys
import requests
from imp import reload
reload(sys)


# tsリンクが得られる,パラメータurlは.m3u8リンクである
def get_ts(url):
    path = "C://Clone_Videos"  # 既定のビデオ保存パス

    all_url = url.split('/')  # split根据'/'把字符串分裂成列表
    url_pre = '/'.join(all_url[:-1]) + '/'  # 舍弃末尾的一项，拼接成新的网址
    url_next = all_url[-1]  # 取all_url列表末尾的一项

    # requests.get()函数返回的是requests.models.Response对象
    m3u8_txt = requests.get(url, headers={'Connection': 'close'}, verify=False)
    with open(url_next, 'wb') as m3u8_content:  # 创建m3u8文件，
        m3u8_content.write(m3u8_txt.content)  # m3u8_txt.content是字节流

    movies = []  # 取得した完全な .ts ビデオ リンクを格納するリストを作成します

    urls = open(url_next, 'rb')
    for line in urls.readlines():
        line2 = line.decode()						# bytes -> str
        if '.ts' in line2:  # 提取.ts文件链接
            # 拼接成完整的.ts网络链接，并保存在movies列表中,line2[:-1]删除掉末尾的换行符
            movies.append(url_pre + line2[:-1])
        else:
            continue
    urls.close()  # 关闭
    return movies  # 返回列表`


# スライスダウンロード関数、引数moviesは.tsリンクです。
def down_ts(movies):
    # os.chdir(path)
    error_get = []  # エラーが発生したリンクを格納するリストを作成します。
    print("Downloaded中")
    for _url in movies:
        movie_name = _url.split('/')[-1][-6:]  # 接続で最後の 6 ビットをファイル名として抽出します。
        try:
            movie = requests.get(
                _url, headers={'Connection': 'close'}, timeout=60)  # .ts リンクを開きます
            print(movie)
        except:
            error_get.append(_url)
            continue
        print(movie_name)
        movie_content = open('C://Reptile_video/' +
                             movie_name, 'wb')  # ファイルをローカルに作成します
        movie_content.writelines(movie)  # スライスをダウンロードします
        if error_get:
            down_ts(error_get)  # エラー一覧を再ダウンロードします
        else:
            print("ダウンロードは成功しました。")
    print("すべてのスライスのダウンロードが完了しました。")
    num = len(movies)  # リスト要素の数を取得します

    return num  # 要素の数を返します


# 合并分片
def merge_ts(num):
    path = "C:\\Reptile_video"

    new_path = ("%s\out.ts" % path)
    f = open(new_path, 'wb+')  # 二进制文件写操作

    for i in range(0, num):
        filepath = ("%s\%03d.ts" % (path, i))  # 视频片段的名字及路径
        print(filepath)
        for line in open(filepath, "rb"):
            f.write(line)
        f.flush()
    f.close()
    print("合并完成,开始转码")


# 转码为MP4
def change_mp4(name):
    fn = 'E:\\爬虫视频\out.ts'
    output = "E:\\爬虫视频\%s.mp4" % name
    cmd = "ffmpeg " + "-i " + fn + " -acodec copy -vcodec copy -f mp4 " + output
    print(cmd)
    os.system(cmd)
    print("转码完成完成")

# 清空原始文件


def del_ts(num):
    path = "E://爬虫视频/out.ts"  # 要删除文件的路径
    os.remove(path)  # 清除文件
    for i in range(0, num):
        path = ("E://爬虫视频/%03d.ts" % i)  # 要删除文件的路径
        os.remove(path)  # 清除文件
    print("清理完成，程序结束")


if __name__ == "__main__":
    # input("请输入.m3u8链接：")
    url = 'https://d.ossrs.net:8088/live/livestream.m3u8'
    movie_name = 'sample.mp4'  # input("input to VideoName")
    movie_all = []
    movie_all = get_ts(url)
    num = down_ts(movie_all)
    merge_ts(num)
    change_mp4(movie_name)
    del_ts(num)
