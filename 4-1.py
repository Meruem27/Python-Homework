import csv
for n in range(9,-1,-1):
    result = 0
    name = input("请输入要查询的期刊名字:")
    file = open("SCI影响因子.csv")
    file = csv.reader(file)
    next(file)
    for line in file:
        if(name.upper()==line[0]):
            print(
'''期刊名字: {}
20年IF: {}
21年IF: {}
JCR分区: {}
中科院分区: {}'''.format(line[0],line[1],line[2],line[5],line[6]))
            result=1
            break
        else:
            continue
    print("您还有{}次查询机会！".format(n))
    if(result!=1):
        print("对不起，期刊未检索到！")
print("小程序10次查询机会已用尽！")
print("谢谢使用，再见！")
