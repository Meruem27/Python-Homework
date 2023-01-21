import math

def Transcription(string):
    list = []
    for i in string:
        if i == 'A':
            list.append('U')
        elif i == 'T':
            list.append('A')
        elif i == 'C':
            list.append('G')
        elif i == 'G':
            list.append('C')
        else:
            list.append(i)
    transcriptional_rna = ''.join(list)
    return transcriptional_rna

file = open("cds_seq.txt")
table = {
        'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
        'AAC': 'N', 'AAU': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGU': 'S', 'AGA': 'R', 'AGG': 'R',
        'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
        'CAC': 'H', 'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
        'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
        'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
        'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
        'UUC': 'F', 'UUU': 'F', 'UUA': 'L', 'UUG': 'L',
        'UAC': 'Y', 'UAU': 'Y', 'UAA': '*', 'UAG': '*',
        'UGC': 'C', 'UGU': 'C', 'UGA': '*', 'UGG': 'W',
    }
dic={}
for line in file:
    if(line.startswith('>')):
        gene_name = line
        gene = ""
    else:
        gene+=line
        dic[gene_name]=gene
for GENE_NAME in dic.keys():
    print(GENE_NAME.strip('\n'))
    n = math.floor(len(dic[GENE_NAME])/3)
    protein = dic[GENE_NAME]
    protein = protein.replace("\n", "")
    protein = Transcription(protein)
    for i in range(0,3*n,3):
        PROTEIN = protein[i:i+3]
        PROTEIN = table[PROTEIN]
        print(PROTEIN,end="")
        if(PROTEIN=='*'):
            print("")
            break
