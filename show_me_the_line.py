#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : get_total_lines_in_py.py 
# @time  : 2017/10/17 23:57:30
# @description：获取指定目录下的所有.py结尾的有效行数（不包括注释和空行）
import os

line_count = 0  # 统计总行数
file_count = 0  # 统计文件个数


def get_lines(path, file_suffix):
    global line_count
    global file_count
    # 过滤掉以.(隐藏文件)和__(类似__init__.py)开头的文件
    files = [f for f in os.listdir(path) if not (f.startswith('.') or f.startswith('__'))]
    for f in files:

        if os.path.isdir(f):
            path = os.path.join(path, f)
            os.chdir(path)
            path = os.getcwd()
            get_lines(path, file_suffix)
            os.chdir('..')
            path = os.getcwd()

        # 获取所有行数
        # if os.path.isfile(f) and os.path.splitext(f)[1] == file_suffix:
        #     with open(f, 'r', encoding='utf-8') as ff:
        #         lines = len(ff.readlines())
        #         line_count += lines
        #         file_count += 1
        #         print('{}: {} lines'.format(f, lines))
        if os.path.isfile(f) and os.path.splitext(f)[1] == file_suffix:
            with open(f, 'r', encoding='utf-8') as ff:
                for line in ff.readlines():
                    if line.startswith('#') or line == '\n':
                        line_count += 0
                    else:
                        line_count += 1
            file_count += 1

    return file_count, line_count


if __name__ == '__main__':
    # given_path = os.path.join('/Users/jockie/programs/pycharm/python100', '')
    # print(os.path.abspath('.'))
    os.chdir('/Users/jockie/programs/pycharm/python100')
    given_path = os.getcwd()
    print(given_path)
    file_type = '.py'
    total = get_lines(given_path, file_type)
    total_file = total[0]
    total_line = total[1]
    print('共{}个{}文件，有效行数共{}行'.format(total_file, file_type, total_line))
