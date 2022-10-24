

from collections import Counter
from bio_structurs import *



Nucleotides = ['A','C','G','T']
DNA_ReverseComplement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

def nucleotide_frequency(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
        return tmpFreqDict

#proverka
def validateSeq(dna_seq):

 tmpseq = dna_seq.upper()
 for nuc in tmpseq:
       if nuc not in Nucleotides:
           return False

 return tmpseq

def countNucFrequenc(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
            tmpFreqDict[nuc] +=1
    return tmpFreqDict


def transcription(seq):
    #DNA -> RNA
    return seq.replace("T","U")

def reverse_complement(seq):

    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]


def gc_content(seq):

    return round((seq.count('C')+seq.count('G'))/len(seq)*100)

def translate_seq(seq,init_pos=0):

       return [DNA_Codons[seq[pos:pos+3]]for pos in range(init_pos,len(seq) -2,3)]



def codon_usage(seq, aminoacid):
     #   """Provides the frequency of each codon encoding a given aminoacid in a DNA sequence"""
        tmpList = []
        for i in range(0, len(seq) - 2, 3):
                if DNA_Codons[seq[i:i + 3]] == aminoacid:
                    tmpList.append(seq[i:i + 3])

        # elif self.seq_type == "RNA":
        #     for i in range(0, len(self.seq) - 2, 3):
        #         if RNA_Codons[self.seq[i:i + 3]] == aminoacid:
        #             tmpList.append(self.seq[i:i + 3])

        freqDict = dict(Counter(tmpList))
        totalWight = sum(freqDict.values())
        for seq in freqDict:
            freqDict[seq] = round(freqDict[seq] / totalWight, 2)
        return freqDict



def gen_reading_frames(seq):
#Generate the six reading frames of
       frames = []
       frames.append(translate_seq(seq, 0))
       frames.append(translate_seq(seq, 1))
       frames.append(translate_seq(seq, 2))
       return frames

# def reading_frames(seq):
#     for frame in gen_reading_frames(seq):
#        return frame
