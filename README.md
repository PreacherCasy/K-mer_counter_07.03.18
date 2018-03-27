# K-mer_counter_07.03.18

## Description
A short class-oriented script evaluating raw k-mer statistics for FASTA-format nucleotide sequences.

## Launching
K-mer_counter is **not** integrated into Linux console; thus, you have to operate it as Python script from graphic environment (Pycharm recommended). Also, you need Pandas and Bio packages installed for correct launching.

## Structure
K-mer comprises of one user class, a user function and a script body.

### class Kmer

Class *Kmer* describes subsequences of length *k* within test sequence. As a class, *Kmer* possesses following attributes:

+ **Kmer.counter**: a counter item containing information about number of *k*-mer appearences in the test sequence;
+ **Kmer.sequence**: a sequence of Kmer in ATGC DNA nucleotides;
+ **Kmer.length**: an integer standing for *k*-mer length;
+ **Kmer.loci_list**: a list of coordinates of loci which the *k*-mer is located in within the sequence in question. By default, this list is empty.

Also, class *Kmer* supports following dependinf functions:

+ **Kmer.increase()**: increases **Kmer.counter** by 1;
+ **Kmer.increase_n(n)**: increases **Kmer_counter** by *n*;
+ **Kmer.locate(locus)**: adds indices for locus containing *k*-mer;
+ **Kmer.infogram()**: returns a data frame containing *k*-mer sequence, chromosome id and loci coordinates

### Function genome_walking(seq, k)

This function performes a full-sequence screening for all present *k*-mers and adds the to the **kmer_dict** *dict* variable. It takes two arguments:

+ **seq**: a sequence string variable;
+ **k**: an integer variable defining the length of sought *k*-mers.

The function returns **kmer_dict** object which contains *kmer* class objects attributed to their sequences (*string* values) posed as keys.

### Function most_frequent_kmer(kmer_dict):

This function finds the most frequent (e.g. possessing the highest **Kmer.counter** value) *k*-mer in the dictionary by comparing them with default *k*-mer of **Kmer.counter** zero. The output is a **Kmer.infogram()** attribute for the most frequent *k*-mer.

### Script body

The body takes filename as standart input and parses the file with Biopython SeqIO parser. After that, it receives **k** integer for to estimate length of the *k*-mers and performes **genome_walking(sequence, k)** function. Finally, it performs **most_frequent_kmer** over the resulting dictionary.

**NOTE**: Filename should be input without quotation marks!


## Example

Performing a code over *Yersinia pestis* complete genome DNA (see repository contents) gives the following result:


|Number    |Chromosome    |          Locus                 | Sequence |
|--- | --- | --- | ---    
|0   |AE009952.1    |[114042, 114065]                |CTACATGGATGTATTTACGGCGT|
|1   |AE009952.1    |[257511, 257534]                |      -/- |
|2   |AE009952.1    |[600502, 600525]                |      -/- |
|3   |AE009952.1    |[637950, 637973]                |      -/- |
|4   |AE009952.1    |[723871, 723894]                |      -/- |
|5   |AE009952.1    |[751338, 751361]                |      -/- |
|6   |AE009952.1    |[784541, 784564]                |      -/- |
|7   |AE009952.1    |[921257, 921280]                |      -/- |
|8   |AE009952.1    |[1055321, 1055344]              |      -/- |
|9   |AE009952.1    |[1367968, 1367991]              |      -/- |
|10  |AE009952.1    |[1488267, 1488290]              |      -/- |
|11  |AE009952.1    |[1633920, 1633943]              |      -/- |
|12  |AE009952.1    |[1788816, 1788839]              |      -/- |
|13  |AE009952.1    |[1825786, 1825809]              |      -/- |
|14  |AE009952.1    |[1867520, 1867543]              |      -/- |
|15  |AE009952.1    |[2156542, 2156565]              |      -/- |
|16  |AE009952.1    |[2356886, 2356909]              |      -/- |
|17  |AE009952.1    |[2465522, 2465545]              |      -/- |
|18  |AE009952.1    |[2476642, 2476665]              |      -/- |
|19  |AE009952.1    |[2615302, 2615325]              |      -/- |
|20  |AE009952.1    |[2882442, 2882465]              |      -/- |
|21  |AE009952.1    |[3050181, 3050204]              |      -/- |
|22  |AE009952.1    |[3127937, 3127960]              |      -/- |
|23  |AE009952.1    |[3464131, 3464154]              |      -/- |
|24  |AE009952.1    |[3621207, 3621230]              |      -/- |
|25  |AE009952.1    |[3633051, 3633074]              |      -/- |
|26  |AE009952.1    |[3639673, 3639696]              |      -/- |
|27  |AE009952.1    |[3647777, 3647800]              |      -/- |
|28  |AE009952.1    |[3905454, 3905477]              |      -/- |
|29  |AE009952.1    |[4008327, 4008350]              |      -/- |
|30  |AE009952.1    |[4413928, 4413951]              |      -/- |
|31  |AE009952.1    |[4576110, 4576133]              |      -/- |


| Алгоритм  | Время работы | Качество выравнивания (оставленные символы) |
|---------|------------|-------------------------------------------|
| ClustalW2 | 6.29         | 1749                                        |
| MUSCLE    | 4.20         | 1753                                        |
| Mafft     | 0.43         | 1780                                        |
| Kalign    | 0.32         | 1745                                        | 
| T-COFFEE  | 28.20        | 1722                                        |
| Prank     | 6.69         | 1709                                        |


BLASTing this sequence against whole NCBI library states that this sequence is related to intergenic spaces of several *Proteabcteria* G^-^-species. Thus, the frequency of this *k*-mer is increased due to its relation to stereotypical repeats.

## Acknowledgements
Eugene Bakin from Bioinformatic Institute for Python crash course.

[Corey Schafer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) for his perfect Python Class Tutorial. 
