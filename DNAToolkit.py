### Created on 4/29/24 by Tazein Shah
### Based off the tutorial made by rebelScience on Youtube

#define the nucleotides
nucleotides = ["A", "C", "G", "T"]

# checking to see if the sequence we have is a DNA string
def validateSed(dna_seq):
    tmpseq = dna_seq.upper() #we need them to be uppercase because of the list we defined earlier
    for nuc in tmpseq:
        if nuc not in nucleotides:
            return False
    return tmpseq

def countNucFrequency(dna_seq):
    tmpFreqDict = {nuc: 0 for nuc in Nucleotides} #setting up a dict where every value starts as 0
    for nuc in dna_seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

def dnaTranscribe(dna_seq):
    tmpseq = dna_seq.upper() #we need them to be uppercase because of the list we defined earlier
    tmpseq = tmpseq.replace('T','U')
    return tmpseq

def complementingDNA(dna_seq):
    tmpseq = dna_seq.upper() #we need them to be uppercase because of the list we defined earlier    
    reverse_seq = tmpseq[::-1] #reverse the sequence
    comp_dna = '' #create an empty string
    
    for nuc in reverse_seq:
        if nuc == 'A':
            comp_dna += str('T')
            
        if nuc == 'T':
            comp_dna += str('A')
            
        if nuc == 'C':
            comp_dna += str('G')
            
        if nuc == 'G':
            comp_dna += str('C')
    
    return comp_dna

            

                   
            
