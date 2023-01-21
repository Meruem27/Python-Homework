import csv
file1 = open("SCI影响因子.csv")
file2 = open("需要检索的杂志列表.txt")
file3 = open("输出结果.csv",'w',newline='')
file1 = csv.reader(file1)
writer = csv.writer(file3)
writer.writerow(["期刊名字","20年IF","21年IF","JCR分区","中科院分区"])
next(file1)
for line1 in file2:
    line1 = line1.strip("\n")
    for line2 in file1:
        if(line1==line2[0]):
            line2[0] = line2[0].title()
            line2.pop(3)
            line2.pop(3)
            line2.pop(5)
            writer.writerow(line2)
            break
        else:
            continue
