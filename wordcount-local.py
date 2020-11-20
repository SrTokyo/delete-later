#!/usr/bin/python

import os, subprocess
import sys
import glob

import codecs


inputdir="."

if len(sys.argv) >= 1:
	inputdir = sys.argv[1]

def processdir(dir):

    dirList = glob.glob(dir)
    wordcount={}
    for f in dirList:
        wordcountfile(f,wordcount)
    for w in wordcount:
        print(w,wordcount[w])

contador = 0
def wordcountfile(f, wordcount):
    file = codecs.open(f, "r", "utf-8")
    for word in file.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
        if wordcount == 2:
            contado = contador + int(word)
    file.close()
    return wordcount        

print(contador)

processdir(inputdir)
