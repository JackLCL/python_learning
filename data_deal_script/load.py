from milvus import Milvus, IndexType, MetricType, Status
import getopt
import os
import numpy as np
import sys
import time
import pandas as pd

milvus = Milvus()
HOST = "192.168.1.154"
PORT = 19530
# FILENAME = "/home/lcl/Desktop/Study/python_learning/data_deal/data/npy" # npy文件
FILENAME = "/home/lcl/Desktop/Study/python_learning/data_deal/data/csv" # csv文件
# FILENAME = "/home/lcl/Desktop/Study/python_learning/data_deal/data/txt"

def handle_status(status):
    if status.code != Status.SUCCESS:
        print(status)
        sys.exit(2)

def connect_server():
    print("connect to milvus")
    status = milvus.connect(host=HOST, port=PORT, timeout=1000 * 1000 * 20)
    handle_status(status=status)
    return status


def load_npy(file):
    data = np.load(file)
    vec_list = data.tolist()
    return vec_list


def npy_to_milvus(table):  
    connect_server()
    filenames = os.listdir(FILENAME)
    filenames.sort()
    for filename in filenames:
        print(filename + " ",end='')
        vec_list = load_npy(FILENAME + '/' + filename)
        time_start = time.time()
        status,ids = milvus.add_vectors(table_name=table, records=vec_list)
        time_end = time.time()
        handle_status(status=status)
        print("insert_time:"+str(time_end -time_start))
    print("Insert done!")


def load_csv(file):
    data = pd.read_csv(file, header=None)
    data = np.array(data)
    vec_list = data.tolist()
    return vec_list


def csv_to_milvus(table):
    connect_server()
    filenames = os.listdir(FILENAME)
    filenames.sort()
    for filename in filenames:
        print(filename + " ",end='')
        vec_list = load_csv(FILENAME + '/' + filename)
        print(vec_list)
        time_start = time.time()
        status,ids = milvus.add_vectors(table_name=table, records=vec_list)
        time_end = time.time()
        handle_status(status=status)
        print("insert_time:"+str(time_end -time_start))
    print("Insert done!")


def load_txt(file):
    pass



def txt_to_milvus(table):
    connect_server()
    filenames = os.listdir(FILENAME)
    filenames.sort()
    for filename in filenames:
        print(filename + " ",end='')
        vec_list = load_txt(FILENAME + '/' + filename)
        time_start = time.time()
        status,ids = milvus.add_vectors(table_name=table, records=vec_list)
        time_end = time.time()
        handle_status(status=status)
        print("insert_time:"+str(time_end -time_start))
    print("Insert done!")

def main():
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "hnctbf",
            ["table=","help"]
        )
    except getopt.GetoptError:
        print("Usage: python milvus_toolkit.py -q <nq> -k <topk> -c <table> -s")
        sys.exit(2)
    
    for opt_name,opt_value in opts:
        if opt_name in ("-h", "--help"):
            print("Usage: python3 load.py --table <table_name> -c -t -n -b -f")
            sys.exit(2)
        elif opt_name == "--table":
            table_name = opt_value
        elif opt_name == "-n":
            npy_to_milvus(table_name)
        elif opt_name == "-c":
            csv_to_milvus(table_name)
        elif opt_name == "-t":
            txt_to_milvus(table_name)
        elif opt_name == "-b":
            bvecs_to_milvus(table_name)
        elif opt_name == "-f":
            fvecs_to_milvus(table_name)



if __name__ == '__main__':
    main()