file1 = open("cds_from_genomic.txt")
file2 = open("gene_id.txt")
file3 = open("cds_seq.txt","w")
dic = {}
for line1 in file1:
    if(line1.startswith('>')):
        line1 = line1.strip('>lcl|')
        line1 = line1.split(' ')
        gene_name = line1[0]
        gene = ""
    else:
        gene += line1
        dic[gene_name]=gene
for line2 in file2:
    line2 = line2.strip('\n')
    if line2 in dic.keys():
        file3.writelines(">"+line2+"\n")
        file3.writelines(dic[line2])
