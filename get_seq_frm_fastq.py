__author__ = 'proline'
import datetime

def getTime():
    return datetime.datetime.now()

time = getTime()
filename_timestamp = time.strftime("%m%d%y_%H%M_")
fastqseq_output = filename_timestamp+"fastq_seq.txt"

fastq_file = file(raw_input ('Enter fastq file name: '), 'r')
fastq_sequence = open(fastqseq_output, 'w')

def get_sequence_fastq():

    lines = fastq_file.readlines()
    for index, eachline in enumerate(lines):
        if eachline[0] == '@':
            sequence = lines[index+1]
            fastq_sequence.write(sequence)
    return

    fastq_file.close()
    fastq_sequence.close()

seq = get_sequence_fastq()