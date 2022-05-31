# -*- coding: utf-8 -*-

import os
import io
import sys

#カレントディレクトリを変更
os.chdir(r'C:\Users\hntrk\github\log_pyQ')

#printの出力結果をUTF-8に
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

print(os.getcwd())
print ('defaultencoding:', sys.getdefaultencoding())

f = open('sample_text.txt', 'r', encoding='utf-8')
sampleTxts = f.readlines()
f.close

for sampleTxt in sampleTxts:
	sampleTxt_split = sampleTxt.split()

	print(sampleTxt_split, file=sys.stderr)
