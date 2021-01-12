#加载需要的模块
import os
import sys
import requests
from imp import reload
reload(sys)



#得到ts链接，参数url为.m3u8链接
def get_ts(url):
	path = "E://爬虫视频"											#默认视频存储路径
	
	all_url = url.split('/')										#split根据'/'把字符串分裂成列表
	url_pre = '/'.join(all_url[:-1]) + '/'							#舍弃末尾的一项，拼接成新的网址
	url_next = all_url[-1]											#取all_url列表末尾的一项
	
	m3u8_txt = requests.get(url, headers = {'Connection':'close'})	#requests.get()函数返回的是requests.models.Response对象
	with open(url_next, 'wb') as m3u8_content:						#创建m3u8文件，
		m3u8_content.write(m3u8_txt.content)						#m3u8_txt.content是字节流
	
	movies = []			#创建列表，存储获得的完整的.ts视频链接
	
	urls = open(url_next, 'rb')
	for line in urls.readlines():
		line2 = line.decode()						# bytes -> str
		if '.ts' in line2:							#提取.ts文件链接
			movies.append(url_pre + line2[:-1])		#拼接成完整的.ts网络链接，并保存在movies列表中,line2[:-1]删除掉末尾的换行符
		else:
			continue
	urls.close()									#关闭
	return movies									#返回列表`


    #分片下载函数，参数movies为.ts链接。
def down_ts(movies):
    #os.chdir(path)
    print("下载中")
    for _url in movies:
	movie_name = _url.split('/')[-1][-6:]		#在连接中提取后六位作为文件名           
	
	error_get = []								#创建列表，存储出错的链接
	try:
		movie = requests.get(_url, headers = {'Connection':'close'}, timeout = 60)			#打开.ts链接
	except:
		error_get.append(_url)
		continue
	print(movie_name)
	movie_content = open('E://爬虫视频/' + movie_name, 'wb')								#在本地创建文件
	movie_content.writelines(movie)															#下载分片
	if error_get:
		down_ts(error_get)																	#重新下载出错列表
	else:
	print("下载成功")
    print("所有分片下载完成")
    num = len(movies)																			#获取列表元素的个数
    return num																					#返回元素的个数



#合并分片
def merge_ts(num):
	path = "E:\\爬虫视频"

	new_path = ("%s\out.ts" % path)
	f = open(new_path, 'wb+')								#二进制文件写操作

	for i in range(0, num):
		filepath = ("%s\%03d.ts" % (path, i))				#视频片段的名字及路径
		print(filepath)
		for line in open(filepath, "rb"):
			f.write(line)
		f.flush()
	f.close()
	print("合并完成,开始转码")



#转码为MP4
def change_mp4(name):
	fn = 'E:\\爬虫视频\out.ts'
	output = "E:\\爬虫视频\%s.mp4" % name
	cmd = "ffmpeg " + "-i " + fn + " -acodec copy -vcodec copy -f mp4 " + output
	print(cmd)
	os.system(cmd)
	print("转码完成完成")

#清空原始文件
def del_ts(num):
	path = "E://爬虫视频/out.ts"						#要删除文件的路径
	os.remove(path)										#清除文件
	for i in range(0, num):
		path = ("E://爬虫视频/%03d.ts" % i)				#要删除文件的路径
		os.remove(path)									#清除文件
	print("清理完成，程序结束")



if __name__ == "__main__":
	url = input("请输入.m3u8链接：")
	movie_name = input("请输入视频名称")
	movie_all = []
	movie_all = get_ts(url)  
	num = down_ts(movie_all)
	merge_ts(num)
	change_mp4(movie_name)
	del_ts(num)

    



