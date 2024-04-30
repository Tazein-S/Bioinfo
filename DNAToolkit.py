### Created on 4/29/24 by Tazein Shah
### Based off the tutorial made by rebelScience on Youtube

#importing necessary packages
import collections

#define the nucleotides
Nucleotides = ["A", "C", "G", "T"]

# checking to see if the sequence we have is a DNA string
def validateSed(dna_seq):
  tmpseq = dna_seq.upper() #we need them to be uppercase because of the list we defined earlier
  for nuc in tmpseq:
    if nuc not in Nucleotides:
      return False
  return tmpseq

def countNucFrequency(dna_seq):
  return(dict(collections.Counter(dna_seq)))
  #tmpFreqDict = {nuc: 0 for nuc in Nucleotides} #setting up a dict where every value starts as 0
  #for nuc in dna_seq:
    #tmpFreqDict[nuc] += 1
  #return tmpFreqDict
