from Bio import SeqIO
import pandas as pd

class Kmer:
    counter = 0
    sequence = ''
    def __init__(self, kmer_name):
        self.sequence = kmer_name
        self.length = len(kmer_name)
        self.loci_list = []

    def increase(self):
       self.counter += 1

    def increase_n(self, n):
       self.counter += n

    def locate(self, locus):
        self.loci_list.append(locus)

    def infogram(self, chromosome):
        self.info = pd.DataFrame({'Sequence': ['-/-'] * (len(self.loci_list)),
                                  'Locus': self.loci_list, 'Chromosome': [chromosome] * len(self.loci_list)})
        self.info.at[0, 'Sequence'] = self.sequence
        return self.info


def genome_walking(seq, k):
    seq_lng = len(seq)
    kmer_dict = {}
    for index in range(seq_lng - k + 1):
        current_kmer = seq[index:(index + k)]
        if current_kmer in kmer_dict:
            kmer_dict[current_kmer].increase()
        else:
            kmer_dict[current_kmer] = Kmer(current_kmer)
            kmer_dict[current_kmer].increase()
        kmer_dict[current_kmer].locate([index, (index + k)])
    return kmer_dict

def most_frequent_kmer(kmer_list):
    most_frequent = Kmer('CCC')
    for element in kmer_list.keys():
        if kmer_list[element].counter > most_frequent.counter:
            most_frequent = kmer_list[element]
    return most_frequent.infogram(id)

for record in SeqIO.parse(r'{name}'.format(name=input()), 'fasta'):
    sequence, id = str(record.seq).upper(), record.id
    kmer_list = genome_walking(sequence, int(input()))
    print(most_frequent_kmer(kmer_list))