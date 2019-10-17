import numpy as np

fname = '/nas_poc/yuncong/ann_1000m/bigann_base.bvecs'
x = np.memmap(fname, dtype='uint8', mode='r')
for i in range(10):
        print(x[i])

d = x[:4].view('int32')[0]
data = x.reshape(-1, d + 4)[0:10000, 4:]


print(data[0])

print(len(data[0]))














'''
def load_bvecs_data(fname, base_len, idx):
    begin_num = base_len * idx
    # print(fname, ": ", begin_num)
    x = np.memmap(fname, dtype='uint8', mode='r')
    d = x[:4].view('int32')[0]
    data = x.reshape(-1, d + 4)[begin_num:(begin_num + base_len), 4:]
    data = (data + 0.5) / 255
    # data = normaliz_data(data)
    return data
'''