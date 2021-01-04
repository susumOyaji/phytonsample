#プログラムのファイル名: convert_m3u8.py

# -*- coding:utf-8 -*-

import sys
import os
from glob import glob

#获取需要转换的路径
def get_user_path(argv_dir):
    if os.path.isdir(argv_dir):
        return argv_dir
    elif os.path.isabs(argv_dir):
        return argv_dir
    else:
        return False



#对转换的TS文件进行排序
def get_sorted_ts(user_path):
    ts_list = glob(os.path.join(user_path,'*.ts'))
    print(ts_list)
    boxer = []
    for ts in ts_list:
        if os.path.exists(ts):
            #print(os.path.splitext(os.path.basename(ts)))
            file,_ = os.path.splitext(os.path.basename(ts))
            boxer.append(int(file))
    boxer.sort()
    print(boxer)
    return boxer

#文件合并
def convert_m3u8(boxer,o_file_name):
    cmd_arg = str(ts0)+"+"+str(ts1)+" "+o_file_name
    tmp = []
    for ts in boxer:
        tmp.append(str(ts)+'.ts')
    cmd_str = '+'.join(tmp)
    exec_str = "copy /b "+cmd_str+' '+o_file_name
    print("copy /b "+cmd_str+' '+o_file_name)
    os.system(exec_str)





if __name__=='__main__':
    print(sys.argv[1:])
    argv_len = len(sys.argv)
    if argv_len == 3:
        o_dir,o_file_name =sys.argv[1:]
        print(o_dir+":"+o_file_name)
        user_path = get_user_path(o_dir)
        print(user_path)
        if not user_path:
            print("入力したパスが正しくありません:-(")#;)
        else:
            if os.path.exists(os.path.join(user_path,o_file_name)):
                print(' ターゲット ファイルは既に存在し、プログラムは実行を停止します。 ')
                exit(0)
            os.chdir(user_path)
            convert_m3u8('2.ts','4.ts',o_file_name)
            boxer = get_sorted_ts(user_path)
            convert_m3u8(boxer,o_file_name)
            print(os.getcwd())
    else:
        print("引数の数が無効です");

#注: コードが少なく、原理も単純で、断片化されたビデオを 1 つのビデオ ファイルに順番に結合します。
#使用方法は次のとおりです。
#python convert_m3u8.py m3u8 ビデオのディレクトリ変換後のファイルの名前です
#最初のパラメータはm3u8ビデオのディレクトリです(m3u8の断片化されたビデオは携帯電話で非表示であり、コンピュータにファイルをエクスポートする前に隠しファイルを表示する必要があり、Android携帯電話で隠しフォルダの前に隠します)。 名前の変更は削除できます)、2 番目の引数は変換するファイルの名前です。
