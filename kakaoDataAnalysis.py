# -*- coding: utf-8 -*-
import konlpy
from konlpy.tag import Okt
import pandas as pd
import operator

file = r"C:\Users\Choijisu\Documents\카카오톡 받은 파일\탈똥쟁이들.txt"
# TO-DO 기본 카톡 내용만 가능 문서? 같이 긴 내용 불가능 추가 개발 필요
dataFile = pd.read_csv(file, sep="\t", encoding="utf-8")
data = []
okt = Okt()
word_dict = dict()

#문자열에서는 삭제할 문자가 없어도 에러 안뜨는데 리스트는 뜬다
deleteS=['ㅜ', 'ㅠ', 'ㅋ', 'ㅇ', '𐌅', 'ㅗ']  #문자
deleteL=['이모티콘', '삭제된', '사진', '동영상']   #문자열
# TO-DO 해당 내용 삭제 안됨 추가 개발 필요

for i in range(len(dataFile)):
    l = dataFile.iloc[i, 0].split(']' )
    if len(l) > 1:
        l.pop(0)
        l.pop(0)

    for d in deleteL:
        if d in l:
            l.remove(d)

    if len(l) != 0:
        result = str(l[0])

        for d in deleteS:
            result = result.replace(d, '')

    if not result.isspace() and len(result) != 0:
        data.append(result)

#명사만 추출+빈도수 확인
for d in data:
    n_list = okt.nouns(d)

    for n in n_list:
        if len(n) > 1:
            if n not in list(word_dict.keys()): word_dict[n]=1
            else: word_dict[n]=word_dict[n]+1

sdict= sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True) #내림차순 정렬 딕셔너리=>리스트, value값 기준 정렬
for s in sdict:
    print(s)