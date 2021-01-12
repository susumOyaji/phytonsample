
#必要なモジュールは次のとおりです。

#加载需要的模块
import os
import sys
import requests
from imp import reload
reload(sys)

#取得.m3u8リンク
#この小さな白は、ここでは、Webソースを分析するためのリンクを取得する方法を提供していない、プラグインを利用する単純な暴力的な取得方法を直接共有します。 ここでは、Adobe HDS / HLS Video Saverをお勧めしますが、使用方法も簡単で、ビデオ付きの Web ページでプラグインを直接開くことができます。 ベン・シャオバイは、多くの場合、下のクリアキーをクリックして、すでに得られたリンクをきれいにすることを思い出させるためにここにいます。

#ビデオスライスをローカルにダウンロードし、コードを最初に読むのはやめましょう。

#tsリンクが得られる,パラメータurlは.m3u8リンクである
def get_ts(url):
	path = "E:#Clone Videos";#既定のビデオ保存パス
	
	#String all_url = url.split('/');
  #'https:#d.ossrs.net:8088/live/livestream.m3u8'										
	List<String> all_url = url.split('/');    #split は '/' に基づいて文字列をリストに分割します
  String url_pre = all_url.join();#'/'.join(all_url[-1]) + '/';			#最後の項目を破棄し、新しい URL にステッチします
	String url_next = all_url[-1];											#リストall_url末尾にある項目を取得します
	
	String m3u8_txt = requests.get(url, headers = {'Connection':'close'});	#requests.get() 関数は requests.models.Response オブジェクトを返します
	final m3u8_txt = await http.get(url);
  
  
  with open(url_next, 'wb') as m3u8_content:						#m3u8 ファイル(m3u8_content)を新規作成します
		m3u8_content.write(m3u8_txt.content);						#m3u8_txt.content はバイト ストリームです
	
	  	movies = [];			#取得した完全な .ts ビデオ リンクを格納するリストを作成します
	
	String urls = open(url_next, 'rb');
	for (line in urls.readlines()){
		line2 = line.decode();						## bytes -> str
		if ('.ts' in line2){							#抽出.tsファイルのリンク
			movies.append(url_pre + line2[:-1]);
    }  		#完全な .ts ネットワーク リンクにステッチされ、movies リストに保存され、line2[:-1] は末尾の改行を削除します
		else{
			continue;
    }
  }    
	urls.close();									#閉じます
	return movies;								#一覧に戻ります
	



##これは、.m3u8 リンクに従って完全な .ts ファイルへのリンクを取得する、ダウンロード の最初のステップです。
##次に、2 番目の手順を開始し、ダウンロードします (上のコード)。

#スライスダウンロード関数、引数moviesは.tsリンクです。
int down_ts(movies){
    ##os.chdir(path)
    print("Downloaded");
    for(url in movies){
	    movie_name = _url.split('/')[-1][-6:];   #接続で最後の 6 ビットをファイル名として抽出します。           
	    error_get = [];  #エラーが発生したリンクを格納するリストを作成します。
      try{
        movie = requests.get(_url, headers = {'Connection':'close'}, timeout = 60);  #.ts リンクを開きます#打开.ts链接
      } on Exception catch(e){
        error_get.append(_url);
      }
      continue;
    }
    print(movie_name);
    movie_content = open('E:#Reptile video/' + movie_name, 'wb'); #ファイルをローカルに作成します#在本地创建文件
	  movie_content.writelines(movie); #スライスをダウンロードします#下载分片
	  if (error_get){
	    down_ts(error_get);  #エラー一覧を再ダウンロードします#重新下载出错列表
    }
	  else{
	    print("ダウンロードは成功しました。");
    }  
        print("すべてのスライスのダウンロードが完了しました。");
        num = len(movies);																			#リスト要素の数を取得します#获取列表元素的个数
    return num;																					#要素の数を返します#返回元素的个数
}

##これまでのところ、我々はすべての.tsファイルをローカルにダウンロードし、所有者は.m3u8形式のビデオをダウンロードしようとすると、また、すべての大きな神のブログに波が押し寄わせると、コードをつなぎ合わせ、その後、単独で理解を消化し、エラーやより簡単な方法がある場合は、ガイドに行きます。
##3. マージビデオスライスコードは、私が言いたいのは、すべてコメントです:

#分割をマージします
void merge_ts(num){
	String path = "E:\\Reptile video";

	String new_path = ("%s\out.ts" % path);
	String f = open(new_path, 'wb+');								##バイナリ書き込み操作二进制文件写操作

	for (i in range(0, num)){
		String filepath = ("%s\%03d.ts" % (path, i));				#ビデオクリップの名前とパス#视频片段的名字及路径
		print(filepath);
		for ( String line in open(filepath, "rb")){
			f.write(line);
    }  
		f.flush();
  }  
	f.close();
	print("マージが完了しました,トランスコードを開始します");
}


#MP4形式のビデオにトランス
#コード ここで所有者のためのツールはffmpegであり、これは公式ウェブサイトへのリンクを添付して、追加のダウンロードを必要とします。
#ダウンロード後,ffmpegをwindowsの.exeに追加する必要がある.
#ここでは、コードです
#トランスコードはMP4です
void change_mp4(name){
	String fn = 'E:\\Reptile video\out.ts';
	String output = "E:\\Reptile video\%s.mp4" % name;
	String cmd = "ffmpeg " + "-i " + fn + " -acodec copy -vcodec copy -f mp4 " + output;
	print(cmd);
	os.system(cmd);
	print("トランスコードが完了しました");
}


#元のファイルを空にします
void del_ts(num){
	String path = "E:#Reptile video/out.ts";						#ファイルを削除するパス
	os.remove(path);										#ファイルをクリアします
	for (int i in range(0, num)){
		path = ("E:#Reptile video/%03d.ts" % i);				#ファイルを削除するパス
		os.remove(path);	
  }  								#ファイルをクリアします
	print("クリーンアップが完了し、プログラムが終了します");
}


##メイン関数コードを次に示します。

#if __name__ == "__main__":
	String url = 'https:#d.ossrs.net:8088/live/livestream.m3u8';#input("input to .m3u8 Link-Addres：");
	String movie_name = input("input to VideoName");
	String movie_all = [];
	movie_all = get_ts(url);  
	num = down_ts(movie_all);
	merge_ts(num);
	change_mp4(movie_name);
	del_ts(num);

##これで作業が完了し、小さなパートナーがダウンロードが遅いと感じた場合は、マルチスレッドを追加できます。 順徐ステッチコードによると、それは建物の所有者の元の完全なコードです。
##最後に、ガイドハを歓迎します。
