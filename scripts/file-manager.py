import os
import shutil

floder = input('要整理的文件夹?( 默认当前文件夹 ): ')
if floder == '': floder = os.getcwd()
if not os.path.exists(floder):
    print('路径错误')
    exit()
os.chdir(floder)

files_dict = {}

for f in os.listdir(floder):
    file_path = os.path.join(floder, f)
    if os.path.isfile(file_path) and f[0] != '.':
        file_type = f.split('.')[-1].lower()
        if file_type in files_dict:
            files_dict[file_type].append(f)
        else:
            files_dict[file_type] = [f]

for ftype, fs in files_dict.items():
    if not os.path.exists(ftype):
        os.mkdir(ftype)
    if os.path.isdir(ftype):
        for f in fs:
            shutil.move(f, ftype)
    else: print('存在文件与文件夹重名: %s' % ftype)
