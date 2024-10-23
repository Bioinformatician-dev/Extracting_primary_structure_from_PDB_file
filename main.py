 DOWNLOADING PDB FILE
# EXTRACTING PRIMARY STRUCTURE
# SAVING IT TO A FASTA FILE

from pathlib import Path
from Bio.PDB import PDBList
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

out_dir = Path(r"path of file") # destination path for our PDB file
out_fasta_path = out_dir/"fasta_from_pdb.fasta" # destination path for out fasta file
pdb_code = "6GDI" # PDB ID of our desired protein
file_name = "pdb"+pdb_code+".ent"
pdb_file_path = out_dir/file_name

# try and except block to prevent re downloading the same file on multiple executions of the code
try:
    # trying to open the file
    # will print the given error message if PDB file already exists
    fr = open(pdb_file_path,"r")
    fr.close()
    print("pdb file already exist")

except:
    # will download the file only if it doen not already exists
    pdbl = PDBList()
    pdbl.retrieve_pdb_file(pdb_code, pdir = out_dir, file_format = "pdb")
# Parsing primary structure from the PDB file
record_list = SeqIO.parse(file_name,"pdb-atom")
fasta_record_list = []
for record in record_list:
    header = ">" + record.id
    sequence = record.seq
    fasta_record_list.append(SeqRecord(id = header, seq = sequence))

# writing the primary structures to fasta file
SeqIO.write(fasta_record_list,out_fasta_path,"fasta")
print("Fasta file successfully created at: ", out_fasta_path )