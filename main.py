from msilib.schema import AdminUISequence
from DNA_toolkit import * 
from utilities import colored
import random as rm

dna_rnd ="".join([rm.choice(Nucleotides)
                  for nuc in range(40)])

DNAStr = validateSeq('GGTTAGGGTTAGGGTTAGGGTTAGGGTTAGGG')

       
print(f'\nПоследовательность ДНК: {colored(DNAStr)} \n')

print(f'[1] + Sequence length:: {len(DNAStr)} \n')
print(f'[2] + Nucleotide frequency: { countNucFrequenc(DNAStr)}\n')
print(f'[3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}\n')
print(f"[4] + DNA Chain + Reverse Complement:\n5'{colored(DNAStr)} 3' ")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3'{colored(reverse_complement(DNAStr))} 5'\n")
print(f'[5] CG-composition: {gc_content(DNAStr)}%\n')
print(f'[6] Amino acids in DNA:{translate_seq(DNAStr)}\n')
aminoacid = input('Write an amino acid:')
print(f'[7] Codon frequency:{codon_usage(DNAStr,aminoacid) } \n')
print(f'[8] Amino acid sequence:\n')
for frame in gen_reading_frames(DNAStr):
    print(frame)
