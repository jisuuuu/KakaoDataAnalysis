# -*- coding: utf-8 -*-
import konlpy
from konlpy.tag import Kkma

kkma = Kkma()
doc = konlpy.corpus.kolaw.open('constitution.txt').read()
nouns = kkma.nouns(doc)
print(nouns)