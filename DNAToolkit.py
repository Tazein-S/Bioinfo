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
    tmpFreqDict = {nuc: 0 for nuc in nucleotides} #setting up a dict where every value starts as 0
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

def GCcontent(dna_seq):
    GC_count = (dna_seq.count('C')) + (dna_seq.count('G'))
    total = (GC_count) + (dna_seq.count('A')) + (dna_seq.count('T'))
    GC_per = 100 * float(GC_count)/float(total)
    GC_per = round(GC_per, 6)
    
    return (str(GC_per) + ' %')            

def hammingDistance(s,t):
    counter = 0
    
    for i in range(len(s)):
        if s[i] != t[i]:
            counter += 1    
            
    return counter

def RNAtoProtein(rna_seq):
    RNA_to_protein = {
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}
    
    protein_str = ''
    
    #from online, cuts the RNA_str into sets of three
    split_str = [rna_seq[i:i+3] for i in range(0, len(rna_seq), 3)]
    
    for codon in split_str:
        if RNA_to_protein[codon] != 'Stop':
            protein_str += (RNA_to_protein[codon])
        else:
            pass
    return(protein_str)
    
def motifDNA(dna_seq,motif):
    motif_positions = []
    
    for i in range(len(dna_seq)):    
        value = dna_seq[i:i+len(motif)]
        
        if value == motif:
            motif_positions.append(i+1)
            
    motif_positions = ((' '.join(map(str, motif_positions))))
    
    return motif_positions