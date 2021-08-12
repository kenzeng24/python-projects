import re 
import os 
import sys 
import pandas as pd 
import numpy as np 
import spacy 
from spacy.lang.en.stop_words import STOP_WORDS as stopwords 

def _get_wordcounts(x):
	return len(str(x).split()) 

def _get_charcounts(x):
	return len(''.join(x.split())) 

def _get_avg_wordlength(x):
	return  _get_wordcounts(x) / _get_wordcounts(x)

def _get_stopwords_count(x): 
	return len([t for t in x.split() if t in stopwords])

def _get_hashtags_counts(x): 
	return len([t for t in x.split() if t.startswith("#")])

def _get_mentions_counts(x):
	return len([t for t in x.split() if t.startswith("@")])

def _get_digits_counts(x):
	return len([t for t in x.split() if t.isdigit()])

def _get_uppercase_counts(x):
	return len([t for t in x.split() if t.isupper()])

def _get_lowercase_counts(x):
        return len([t for t in x.split() if t.islower()])

def _get_count_exp(x):
	pass 
