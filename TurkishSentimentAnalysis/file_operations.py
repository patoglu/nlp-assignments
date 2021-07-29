import pandas as pd
import re
import string

def read_csv_files():
    dataset_test = pd.read_csv('test.csv', header= 0,
                            encoding= 'unicode_escape')

    dataset_train = pd.read_csv('train.csv', header= 0,
                            encoding= 'unicode_escape')


    dataset_test.to_csv("file1.csv", encoding="utf-8") #file 1 is test files

    dataset_train.to_csv("file2.csv", encoding="utf-8") #file 2 is train file.

def  convert_utf8(file_name,op_name):
    with open(file_name, 'r',encoding="utf-8",errors='ignore') as inp:
        with open(op_name, 'wb') as _file:
            for read in inp:
                _file.write(read.encode("utf-8"))
        _file.close()
    inp.close()


def convert_csv_format():
    dataset_train = pd.read_csv('train.csv', header= 0,
                            encoding= 'utf-8')
    dataset_train.to_csv("file2.csv", encoding="utf-8") 

def filter_kaggle():
    filenames = ['file1.csv', 'file2.csv']
    with open('last_file', 'w',encoding="utf8") as outfile:
        for fname in filenames:
            with open(fname,encoding="utf8") as infile:
                for line in infile:
                    line = line.replace('\n', 'jjjj')
                    for c in string.punctuation:
                        line= line.replace(c,' ')
                    for x in range(0, 10):
                        line = line.replace(str(x), ' ')
                    line = line.lower()
                    line = line.replace('comment', '')
                    line = line.replace('label', '')
                    line = line.replace('https', '')
                    line = line.replace('unnamed', '')
                    line = ' '.join(line.split())
                    line = line.replace('jjjj', '')
                    outfile.write(line)

def filter_wiki():
    with open('modified_wiki', 'w',encoding="utf8") as outfile:
        with open('new_wiki',encoding="utf8") as infile:
            for line in infile:
                
                line = line.lower()
                for c in string.punctuation:
                    line= line.replace(c,' ')
                    for x in range(0, 10):
                        line = line.replace(str(x), ' ')
                line = line.replace('\n', 'jjjj')
                line = line.replace('wikipedia', '')
                line = line.replace('curid', '')
                line = line.replace('wiki', '')
                line = line.replace('org', '')
                line = line.replace('title', '')
                line = line.replace('comment', '')
                line = line.replace('label', '')
                line = line.replace('https', '')
                line = line.replace('doc', '')
                line = line.replace('id', '')
                line = line.replace('url', '')
                line = line.replace('unnamed', '')
                
                line = ' '.join(line.split())
                line = line.replace('jjjj', ' ')
                outfile.write(line)

def combine_files():
    filenames = ['modified_wiki', 'last_file']
    with open('word2vecinput', 'w',encoding="utf8") as outfile:
        for fname in filenames:
            with open(fname,encoding="utf8") as infile:
                for line in infile:
                    outfile.write(line)
               

print("Doing file operations.. Please wait.")
#convert_csv_format()
read_csv_files()
convert_utf8("trwiki", 'new_wiki')
filter_wiki()
filter_kaggle()
combine_files()






