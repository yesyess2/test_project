# DNA Toolset/Code testing file

from bio_seq import *
from utilities import read_FASTA, readTextFile, writeTextFile

test_dna = bio_seq()
test_dna.generate_rnd_seq(60, "DNA")
print(test_dna.get_seq_biotype())
print(test_dna.get_seq_info())
print(test_dna.nucleotide_frequency())
print(test_dna.transcription())
print(test_dna.reverse_complement())
print(test_dna.gc_content())
print(test_dna.gc_content_subsec())
print(test_dna.translate_seq())
print(test_dna.codon_usage('M'))

for rt in test_dna.gen_reading_frames():
    print(rt)

#print(test_dna.proteins_from_rf(['M', 'N', 'E', 'Y', 'T', 'L', 'Y', 'A', 'V', 'C', 'S', '_']))

print(test_dna.all_proteins_from_orfs())

writeTextFile("test.txt", test_dna.seq, "w")

writeTextFile("test.txt", test_dna.seq, "w")
for rt in test_dna.gen_reading_frames():
    writeTextFile("test.txt", str(rt),'a')  #a: append, not overwrite

fasta = read_FASTA("fasta_samples.txt")
print(fasta)


