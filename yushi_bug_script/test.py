import math
import time
import random
import sklearn.preprocessing
import sys
from milvus import *

m = Milvus()
m.connect(host="192.168.1.10", port=19530)

nq = 10000000
dimension = 128
top_k = 20

vector_tmp = [[random.random() for i in range(dimension)] for i in range(nq)]

vectors = vector_tmp
vectors = sklearn.preprocessing.normalize(vector_tmp, axis=1, norm="l2").tolist()

print(vectors[0])
sys.exit()
# res = 0 
# for item in vectors[0]:
#        res = res + math.pow(item, 2)
# print(res)
# sys.exit()
top_k_ids_l2 = []
top_k_ids_ip = []
for metric_type in [MetricType.L2, MetricType.IP]:
        table_name = "test_%s" % int(metric_type)
        m.delete_table(table_name)
        time.sleep(2)
        m.create_table({
                "table_name": table_name,
                "dimension": dimension,
                "index_file_size": 1024,
                "metric_type": metric_type
        })

        m.add_vectors(table_name, vectors, ids=[i for i in range(nq)])

        m.create_index(table_name, {'index_type': IndexType.IVFLAT,
                                'nlist': 16384})

        status, results = m.search_vectors(table_name, top_k, 64, [vectors[0]])
        # print(results)
        for item in results:
                for tmp in item:
                        if metric_type == MetricType.L2:
                                top_k_ids_l2.append(tmp.id)
                        else:
                                top_k_ids_ip.append(tmp.id)

print(top_k_ids_ip)
print(top_k_ids_l2)
result = set(top_k_ids_ip).intersection(set(top_k_ids_l2))
print(float(len(result)))