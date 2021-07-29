
from gensim.models import KeyedVectors
import re, string, timeit
import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import f1_score
import os 
#os.system('file_operations.py')


algorithm = 1
model = KeyedVectors.load_word2vec_format('vectors', binary = False)
import pandas as pd
frame = pd.read_csv('file2.csv',header= 0,
                            encoding= 'utf-8')

frame_test = pd.read_csv('file1.csv',header= 0,
                            encoding= 'utf-8')

np.seterr(divide='ignore', invalid='ignore')
sentence_vectors = []
sentence_vectors_test = []
labels = []
test_labels = []

#https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
for index, row in frame.iterrows(): 
    filtered = row['comment']
    label = row['Label']
    for c in string.punctuation:
        filtered= filtered.replace(c,' ')
    for x in range(0, 10):
        filtered = filtered.replace(str(x), ' ')
    filtered = filtered.replace('\n', '')
    filtered = filtered.replace('.', '')
    if algorithm == 1:
        sum = np.zeros((100,)*1)
        counter = 0
        for word in filtered.split():
            counter += 1
            sum +=model[word]
        avg = sum / counter
    
        if  np.isnan(avg).any() == True:
            avg = np.zeros((100,)*1)
        sentence_vectors.append(avg)
        labels.append(label)
    
    


for index, row in frame_test.iterrows():
    filtered = row['comment']
    label = row['Label']
    for c in string.punctuation:
        filtered= filtered.replace(c,' ')
    for x in range(0, 10):
        filtered = filtered.replace(str(x), ' ')
    filtered = filtered.replace('\n', '')
    filtered = filtered.replace('.', '')


    if algorithm == 1:
        sum = np.zeros((100,)*1)
        counter = 0
        for word in filtered.split():
            counter += 1
            sum +=model[word]

            
        avg = sum / counter

        if  np.isnan(avg).any() == True:
            avg = np.zeros((100,)*1)
        sentence_vectors_test.append(avg)
        test_labels.append(label)



model = GaussianNB()
model.fit(np.array(sentence_vectors), np.array(labels))
prediction = model.predict(np.array(sentence_vectors_test))
print(f1_score(np.array(test_labels),prediction, average = 'micro'))