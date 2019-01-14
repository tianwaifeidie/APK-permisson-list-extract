#coding:utf-8
'''
simple demo of extracting apk permission list
the result will be saved in the "permission_list.csv"
please put all apk file in the "source_apk" folder
'''
from androguard.core.bytecodes.apk import APK
import os

def file_name(file_dir):
    file_list = []
    for root, dirs, files in os.walk(file_dir):
        file_list.append(files)
    return file_list[0]

def main():
    f = open('permission_list.csv','w')
    file_list = file_name('source_apk')
    print('processing...')
    for apk in file_list:
        try:
            a = APK('source_apk/' + apk)
            b = a.get_permissions()
            f.write(apk+',')
            for i in b:
                f.write(i+',')
            f.write('\n')
        except:
            print(apk+'occured an error!')
    f.close()
    print('finish...')


if __name__ == "__main__":
    main()