import numpy as np
import json

FILENAME='/home/zilliz/workspace/milvus/milvus_sift100w/query.npy'

def load_vec_list():
        file_name = FILENAME
        data = np.load(file_name)
        vec_list = data[0:100]
        vec_list = vec_list.tolist()
        return vec_list
def main():
        vec_list = load_vec_list()
        a = {"query_records":vec_list,"top_k":10,"table_name":"ann_1000m_sq8"}
        j = json.dumps(a, sort_keys=True, indent=4, separators=(',', ': '))
        print(j)

if __name__ == '__main__':
    main()
