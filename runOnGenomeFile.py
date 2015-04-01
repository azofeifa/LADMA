'''
Created on Jul 29, 2014

@author: Joey Azofeifa
'''
import sys
import MisMatchProgram as mm
def readInGenomeFilePutIntoHASH(genomeFILE):
    FH      = open(genomeFILE)
    HASH    = {}
    seq     = ""
    chrom   = ""
    for line in FH:
        if ">" in line and seq and chrom:
            HASH[chrom] = seq
            chrom       = line.strip("\n").lstrip(">")
        elif ">" in line and not chrom:
            chrom       = line.strip("\n").lstrip(">")
        else:
            seq         = seq + line.strip("\n")
    if chrom and seq:
        HASH[chrom]     = seq
    print HASH.keys(), sum([len(seq) for seq in HASH.values() ])
    return HASH
def getHITS(genomeHASH, regex, mismatches):
    FHW = open("results.tsv")
    FHW.write("chromosome, Motif Start Coordinate, Motif Stop Coordinate, Number of Mismatches, Sequence\n")
    
    for chrom in genomeHASH:
        print "working on", chrom
        seq     = genomeHASH[chrom]
        R       = mm.RG(regex)
        HITS    = R.search(seq, ERROR_TOL=mismatches)
        for start, stop, ERROR, sequence in HITS:
            FHW.write(chrom+"\t" + str(start) + "\t" + str(stop) + "\t" + str(ERROR) + "\t" + sequence + "\n")
    FHW.close()

if __name__ == '__main__':
    
    genomeFILE  = sys.argv[1]
    genomeHASH  = readInGenomeFilePutIntoHASH(genomeFILE)
    
    regex       = sys.argv[2]
    mismatches  = sys.argv[3]
    
    
    pass