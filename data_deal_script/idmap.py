

filename = '/home/zilliz/workspace/ann_1000m_idmap.txt'
writename = '/home/zilliz/workspace/new_idamp.txt'

data = []
fname = open(writename,'a')
def main():
        with open(filename, 'r') as f:
                for line in f.readlines():
                        line = line.strip().split(" ")
                        print(line)
                        # print(len(line[1]))
                        if len(line[1]) == 9:
                                # print(line[1][0:3]," ",line[1][3:])
                                tmp = int(line[1][0:3]) * 100000 + int(line[1][3:])
                                # print(tmp)
                        else:
                                tmp = int(line[1][0:4]) * 100000 + int(line[1][4:])
                                # print(tmp)
                        line = line[0] + " " + str(tmp)
                        # print(line)
                        fname.write(line + '\n')
                        data.append(line)

                        # print(line[1][0:5])
                        


if __name__ == '__main__':
    main()