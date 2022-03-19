import os

os.chdir(r'C:\Users\hntrk\log_pyQ')

print(os.getcwd())

f = open('sample_text.txt', 'r', encoding='utf-8')
sampleTxts = f.readlines()
f.close

for sampleTxt in sampleTxts:
	sampleTxt_split = sampleTxt.split()

	print(sampleTxt_split)