from msilib.schema import AdminUISequence
from DNA_toolkit import * 
from utilities import colored
import random as rm

dna_rnd ="".join([rm.choice(Nucleotides)
                  for nuc in range(40)])

DNAStr = validateSeq('GGTTAGGGTTAGGGTTAGGGTTAGGGTTAGGG')

       
print(f'\nПоследовательность ДНК: {colored(DNAStr)} \n')

print(f'[1] + Длина последовательности: {len(DNAStr)} \n')
print(f'[2] + Частота нуклеотидов: { countNucFrequenc(DNAStr)}\n')
print(f'[3] + ДНК/РНК Транскрипция: {colored(transcription(DNAStr))}\n')
print(f"[4] + Цепочка ДНК + Обратный комплемент:\n5'{colored(DNAStr)} 3' ")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3'{colored(reverse_complement(DNAStr))} 5'\n")
print(f'[5] CG-состав: {gc_content(DNAStr)}%\n')
print(f'[6] Аминокислоты в ДНК:{translate_seq(DNAStr)}\n')
aminoacid = input('Напиши аминокислоту:')
print(f'[7] Частота кодонов: {codon_usage(DNAStr,aminoacid) } \n')
print(f'[8] Последовательность аминокислот:\n')
for frame in gen_reading_frames(DNAStr):
    print(frame)