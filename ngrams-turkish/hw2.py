import os
import sys
from collections import defaultdict
from pathlib import Path
import string
import math
import sys
import random



#One parameter probability calculator with GTSmoothing
def logp1(w1):
    prob = GT_smoothing_uni(w1) / ngram_number
    return math.log(prob,2)
#Two parameter probability calculator with GTSmoothing
def logp2(w2, w1):
    prob = GT_smoothing_bi(w2, w1) / GT_smoothing_uni(w1)
    return math.log(prob,2)
#Three parameter probability calculator with GTSmoothing
def logp3(w3, w2, w1):
    prob = GT_smoothing_tri(w3, w2, w1) / GT_smoothing_bi(w2, w1)
    return math.log(prob,2)
#Four parameter probability calculator with GTSmoothing
def logp4(w4, w3, w2, w1):
    prob = GT_smoothing_four(w4, w3, w2, w1) / GT_smoothing_tri(w3, w2, w1)
    return math.log(prob,2)
#Five parameter probability calculator with GTSmoothing
def logp5(w5, w4, w3, w2, w1):
    prob = GT_smoothing_five(w5, w4, w3, w2, w1) / GT_smoothing_four(w4, w3, w2, w1)
    return math.log(prob,2)

#GT Smoothing for one word.
def GT_smoothing_uni(w1):
    if unigram_dict[w1] == 0:
        unigram_dict[w1] = 1
    
    r = unigram_dict[w1]
    _r = (r + 1) * ( (N(unigram_dict_freq, r + 1) + 1 )/ ( N(unigram_dict_freq,r) + 1) )

    return _r
#GT Smoothing for two words.
def GT_smoothing_bi(w2, w1):
    if bigram_dict[w1][w2] == 0:
        bigram_dict[w1][w2] = 1
    r = bigram_dict[w1][w2]
    _r = (r + 1) * ( (N(bigram_dict_freq, r + 1) + 1 )/ ( N(bigram_dict_freq,r) + 1) )

    return _r
#GT Smoothing for three words.
def GT_smoothing_tri(w3, w2, w1):
    if trigram_dict[w1][w2][w3] == 0:
        trigram_dict[w1][w2][w3] = 1

    r = trigram_dict[w1][w2][w3]
    _r = (r + 1) * ( (N(trigram_dict_freq, r + 1) + 1 )/ ( N(trigram_dict_freq,r) + 1) )

    return _r
#GT Smoothing for four words.
def GT_smoothing_four(w4, w3, w2 , w1):

    if fourgram_dict[w1][w2][w3][w4] == 0:
        fourgram_dict[w1][w2][w3][w4] = 1
    r = fourgram_dict[w1][w2][w3][w4]
    _r = (r + 1) * ( (N(fourgram_dict_freq, r + 1) + 1 )/ ( N(fourgram_dict_freq,r) + 1) )

    return _r
#GT Smoothing for three words.
def GT_smoothing_five(w5, w4, w3, w2 , w1):
    if fivegram_dict[w1][w2][w3][w4][w5] == 0:
        fivegram_dict[w1][w2][w3][w4][w5]
    r = fivegram_dict[w1][w2][w3][w4][w5]

    _r = (r + 1) * ( (N(fivegram_dict_freq, r + 1) + 1 )/ ( N(fivegram_dict_freq,r) + 1) )

    return _r


#Function that calculates perplexity of given sentence and ngram type.
def perplexity(sentence, ngram_count, ngram_type):
    L = 0.0
    if ngram_type == 1:
        for i in range (len(sentence)):
            w1 = sentence[i]
            L += logp1(w1)
        L = pow(2, ((-1 * L) / ngram_count))

    elif ngram_type == 2:
       
        for i in range (len(sentence) - 1):
            if i == 0:
                w1 = sentence[i]
                L += logp1(w1)
            else:
                w1 = sentence[i]
                w2 = sentence[i + 1]
                L += logp2(w2, w1)
     
        L = pow(2, ((-1 * L) / ngram_count))
    elif ngram_type == 3:
        for i in range (len(sentence) - 2):
            if i == 0:
                w1 = sentence[i]
                L += logp1(w1)
            elif i == 1:
                w1 = sentence[i]
                w2 = sentence[i + 1]
                L += logp2(w2, w1)
            else:
                w1 = sentence[i]
                w2 = sentence[i + 1]
                w3 = sentence[i + 2]
                L += logp3(w3, w2, w1)
        L = pow(2, ((-1 * L) / ngram_count))   

    elif ngram_type == 4:
        for i in range (len(sentence ) - 3):
            if i == 0:
                w1 = sentence[i]
                L += logp1(w1)
            elif i == 1:
                w1 = sentence[i]
                w2 = sentence[i + 1]
                L += logp2(w2, w1)
            elif i == 2:
                w1 = sentence[i]
                w2 = sentence[i + 1]
                w3 = sentence[i + 2]
                L += logp3(w3, w2, w1)
            else:
                w1 = sentence[i]
                w2 = sentence[i + 1]
                w3 = sentence[i + 2]
                w4 = sentence[i + 3]
                L += logp4(w4, w3, w2, w1)
        L = pow(2, ((-1 * L) / ngram_count))

    elif ngram_type == 5:
        for i in range (len(sentence ) - 4):
            if i == 0:
                w1 = sentence[i]
                L += logp1(w1)
            elif i == 1:
                w1 = sentence[i]
                w2 = sentence[i + 1]
                L += logp2(w2, w1)
            elif i == 2:
                w1 = sentence[i]
                w2 = sentence[i + 1]
                w3 = sentence[i + 2]
                L += logp3(w3, w2, w1)
            elif i == 3:
                w1 = sentence[i]
                w2 = sentence[i + 1]
                w3 = sentence[i + 2]
                w4 = sentence[i + 3]
            else:
                w1 = sentence[i]
                w2 = sentence[i + 1]
                w3 = sentence[i + 2]
                w4 = sentence[i + 3]
                w5 = sentence[i + 4]
                L += logp5(w5, w4, w3, w2, w1)
        L = pow(2, ((-1 * L) / ngram_count))
        
 

    return L

def get_random_string(length):
    letters = string.ascii_lowercase +" "
    result_str = ''.join(random.choice(letters) for i in range(length))

    return result_str

#https://www.geeksforgeeks.org/python-creating-multidimensional-dictionary/
#Function for creating multi-dimensional dictionaries.
def multi_dict(K, type):
    if K == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: multi_dict(K-1, type))

#Function that converts file to utf8 format.
def  convert_utf8(file_name,op_name):
    with open(file_name, 'r',encoding="utf-8",errors='ignore') as inp:
        with open(op_name, 'wb') as _file:
            for read in inp:
                _file.write(read.encode("utf-8"))
        _file.close()
    inp.close()

#Function for converting all the characters to lowercase.
def convert_lower_case(x):
    with open(x, "r+b",) as file:
        content = file.read()
        file.seek(0)
        file.write(content.lower())
        file.seek(0)
        file.close()

#Function that reads the file and removes the punct.
def read_and_remove_punct(x):

    file = open(x,  'r', encoding = 'utf_8')

    line = file.read().replace("\n", " ")
    file.close()

    
    removed = line.translate(str.maketrans('', '', string.punctuation))
    #final_username = "".join(u for u in username if u not in ("?", ".", ";", ":", "!"))
    removed = removed.replace("w", "")
    removed = removed.replace("x", "")
    removed = removed.replace("q", "")
    removed = removed.replace("@", "")
    removed = removed.replace("¼", "")
    removed = removed.replace("Ã", "")
    removed = removed.replace("§", "")
    removed = removed.replace("¶", "")
    removed = removed.replace("Ÿ", "")
    removed = removed.replace("±", "")
    removed = removed.replace("Ä", "")




    
    return removed
    


#Function that redirects stdout to file.
def redirect_stdout(x):
    sys.stdout = open(x, 'w',encoding='utf8',errors='ignore')




#Function that fill whole ngram types as letters.
def fill_ngrams(letter_list):
    count = 0
    letter_count = len(letter_list)
    for i in range (letter_count - 4):
        if unigram_dict[letter_list[count]] == 0:
            unigram_dict[letter_list[count]] = 1
        elif unigram_dict[letter_list[count]] >= 0:
            unigram_dict[letter_list[count]] += 1

        if bigram_dict[letter_list[count]][letter_list[count + 1]] == 0:
            bigram_dict[letter_list[count]][letter_list[count + 1]] = 1
        elif bigram_dict[letter_list[count]][letter_list[count + 1]] >= 0:
                bigram_dict[letter_list[count]][letter_list[count + 1]] += 1
        if trigram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]] == 0:
            trigram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]]= 1
        elif trigram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]] >= 0:
            trigram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]] += 1
        
        if fourgram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]][letter_list[count + 3]] == 0:
            fourgram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]][letter_list[count + 3]]= 1
        elif fourgram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]][letter_list[count + 3]] >= 0:
            fourgram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]][letter_list[count + 3]] += 1
        
        if fivegram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]][letter_list[count + 3]][letter_list[count + 4]] == 0:
            fivegram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]][letter_list[count + 3]][letter_list[count + 4]]= 1
        elif fivegram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]][letter_list[count + 3]][letter_list[count + 4]] >= 0:
            fivegram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]][letter_list[count + 3]][letter_list[count + 4]] += 1

        count+= 1

    if unigram_dict[letter_list[count]] == 0:
        unigram_dict[letter_list[count]]= 1
    elif unigram_dict[letter_list[count]] >= 0:
        unigram_dict[letter_list[count]] += 1

    if bigram_dict[letter_list[count]][letter_list[count + 1]] == 0:
        bigram_dict[letter_list[count]][letter_list[count + 1]]= 1
    elif bigram_dict[letter_list[count]][letter_list[count + 1]] >= 0:
        bigram_dict[letter_list[count]][letter_list[count + 1]] += 1

    if trigram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]] == 0:
        trigram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]]= 1
    elif trigram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]] >= 0:
        trigram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]] += 1
        
    if fourgram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]][letter_list[count + 3]] == 0:
        fourgram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]][letter_list[count + 3]]= 1
    elif fourgram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]][letter_list[count + 3]] >= 0:
        fourgram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]][letter_list[count + 3]] += 1

    count+= 1

    if unigram_dict[letter_list[count]] == 0:
        unigram_dict[letter_list[count]]= 1
    elif unigram_dict[letter_list[count]] >= 0:
        unigram_dict[letter_list[count]] += 1

    if bigram_dict[letter_list[count]][letter_list[count + 1]] == 0:
        bigram_dict[letter_list[count]][letter_list[count + 1]]= 1
    elif bigram_dict[letter_list[count]][letter_list[count + 1]] >= 0:
        bigram_dict[letter_list[count]][letter_list[count + 1]] += 1

    if trigram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]] == 0:
        trigram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]]= 1
    elif trigram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]] >= 0:
        trigram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]] += 1

    count+= 1
    if unigram_dict[letter_list[count]] == 0:
        unigram_dict[letter_list[count]]= 1
    elif unigram_dict[letter_list[count]] >= 0:
        unigram_dict[letter_list[count]] += 1

    if bigram_dict[letter_list[count]][letter_list[count + 1]] == 0:
        bigram_dict[letter_list[count]][letter_list[count + 1]]= 1
    elif bigram_dict[letter_list[count]][letter_list[count + 1]] >= 0:
        bigram_dict[letter_list[count]][letter_list[count + 1]] += 1


    count+= 1
    if unigram_dict[letter_list[count]] == 0:
        unigram_dict[letter_list[count]]= 1
    elif unigram_dict[letter_list[count]] >= 0:
        unigram_dict[letter_list[count]] += 1




    

    print ("Count is " + str(count))
    return letter_count

#Function that prints ngram tables.(Same table is printed again and again)
def print_ngram_tables(letter_list):
    

    total_count = len(letter_list)

    for count in range (total_count):
        print("Table[" + letter_list[count] + "]"  + " = "  + str(unigram_dict[letter_list[count]]))
    
    for count in range (total_count - 1):
        print("Table[" + letter_list[count] + "]" + "[" +  letter_list[count + 1] + "]" + " = "  + str(bigram_dict[letter_list[count]][letter_list[count + 1]]))
    
    for count in range (total_count - 2):
        print("Table[" + letter_list[count] + "]" + "[" +  letter_list[count + 1] + "]" + "[" +  letter_list[count + 2] + "]" + " = "  + str(trigram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]]))

    for count in range (total_count - 3):
         print("Table[" + letter_list[count] + "]" + "[" +  letter_list[count + 1] + "]" + "[" +  letter_list[count + 2] + "]" + "[" +  letter_list[count + 3] + "]" + " = "  + str(fourgram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]][letter_list[count + 3]]))
    
    for count in range (total_count - 4):
          print("Table[" + letter_list[count] + "]" + "[" +  letter_list[count + 1] + "]" + "[" +  letter_list[count + 2] + "]" + "[" +  letter_list[count + 3] + "]" + "[" +  letter_list[count + 4] + "]" + " = "  + str(fivegram_dict[letter_list[count]][letter_list[count + 1]][letter_list[count + 2]][letter_list[count + 3]][letter_list[count + 4]]))



#Flattens the nested dictionary. Found this code on SO but can't specify the link.       
def parse(dic):
    for k, v in dic.items():
        if isinstance(v, dict):
            for p in parse(v):
                yield [k] + p
        else:
            yield [k, v]
#N function in formula that gives us count of a specific count.
def N(any_dict, num_occur):
    return any_dict[num_occur]

#All frequencies kept in a dictionary in order to access quickly.
def get_freq(occur_list, any_dict):
    for i in range (len(occur_list)):
        sublist_length = len(occur_list[i])
        
        any_dict[occur_list[i][sublist_length - 1]] += 1
#Function that calculates all perplexity values for whole ngram models.
def calculate_all_perp(sentence_list):
    count = 0
    n = 25
    uni_total = 0
    bi_total = 0
    tri_total = 0
    four_total = 0
    five_total = 0
    chunks = [sentence_list[i:i+n] for i in range(0, len(sentence_list), n)]
    for chunk in chunks:
        uni_perp = perplexity(chunk,ngram_number,1)
        bi_perp = perplexity(chunk,ngram_number,2)
        tri_perp = perplexity(chunk,ngram_number,3) 
        four_perp = perplexity(chunk,ngram_number,4) 
        five_perp = perplexity(chunk,ngram_number,5) 

        uni_total +=  perplexity(chunk,ngram_number,1)
        bi_total +=  perplexity(chunk,ngram_number,2)
        tri_total +=  perplexity(chunk,ngram_number,3) 
        four_total += perplexity(chunk,ngram_number,4) 
        five_total += perplexity(chunk,ngram_number,5) 
        print (chunk + "-uni" + " = " + str(uni_perp))
        print (chunk + "-bi" + " = " + str(bi_perp))
        print (chunk + "-tri" + " = " + str(tri_perp))
        print (chunk + "-four" + " = " + str(four_perp))
        print (chunk + "-five" + " = " + str(five_perp))
        count += 1

    print("Unigram average = " + str(uni_perp / count))
    print("Bigram average = " + str(bi_perp / count))
    print("Trigram average = " + str(tri_perp / count))
    print("Fourgram average = " + str(four_perp / count))
    print("Fivegram average = " + str(five_perp / count))

def create_random_sentences(sentence_list):
    print("\n\n\n\n\n\n\n\n")
    name_list = []
    uni_list = []
    bi_list = []
    tri_list = []
    four_list = []
    five_list = []
    for i in range (100000):
        random_word = get_random_string(15)
        name_list.append(random_word)
        uni_list.append(perplexity(random_word, len(letter_list), 1))
        bi_list.append(perplexity(random_word, len(letter_list), 2))
        tri_list.append(perplexity(random_word, len(letter_list), 3))
        four_list.append(perplexity(random_word, len(letter_list), 4))
        five_list.append(perplexity(random_word, len(letter_list), 5))

    min_value_uni = min(uni_list)
    min_value_bi = min(bi_list)
    min_value_tri = min(tri_list)
    min_value_four = min(four_list)
    min_value_five = min(five_list)

    min_index_uni = uni_list.index(min_value_uni)
    min_index_bi = bi_list.index(min_value_bi)
    min_index_tri = tri_list.index(min_value_tri)
    min_index_four = four_list.index(min_value_four)
    min_index_five = five_list.index(min_value_five)


    print(name_list[min_index_uni] + " = " + str(min_value_uni))
    print(name_list[min_index_bi] + " = " + str(min_value_bi))
    print(name_list[min_index_tri] + " = " + str(min_value_tri))
    print(name_list[min_index_four] + " = " + str(min_value_four))
    print(name_list[min_index_five] + " = " + str(min_value_five))

    

   
sys.stdout = open('terminal_out_', 'w', encoding = 'utf_8') #stdout>file
convert_utf8("raw_file.txt", "utf.txt")

convert_lower_case("utf.txt") #Converting the file to lower case.
letter_list = read_and_remove_punct("utf.txt") #Reading file and keeping all of it in letter_list.

convert_utf8("splitted.txt", "utf_5.txt")

convert_lower_case("utf.txt") #Converting the file to lower case.
letter_list_test = read_and_remove_punct("utf_5.txt") #Reading file and keeping all of it in letter_list.
 


#Defining global ngram dictionaries.
unigram_dict = {}
bigram_dict = {}
trigram_dict = {}
fourgram_dict = {}
fivegram_dict = {}



#Initializing multi dimensional dictionaries for each n-gram type.
unigram_dict = multi_dict(1, int)
bigram_dict = multi_dict(2, int)
trigram_dict = multi_dict(3, int)
fourgram_dict = multi_dict(4, int)
fivegram_dict = multi_dict(5, int)

#Initializing 1D dictionaries for each frequency.
unigram_dict_freq = multi_dict(1, int)
bigram_dict_freq = multi_dict(1, int)
trigram_dict_freq = multi_dict(1, int)
fourgram_dict_freq = multi_dict(1, int)
fivegram_dict_freq = multi_dict(1, int)


#Filling whole ngrams with letters.
ngram_number = fill_ngrams(letter_list)



#Flattening the counts of dictionaries.
list_uni = list(parse(unigram_dict))
list_bi = list(parse(bigram_dict))
list_tri = list(parse(trigram_dict))
list_four = list(parse(fourgram_dict))
list_five = list(parse(fivegram_dict))

#Getting frequencies in a dictionary. 
get_freq(list_uni, unigram_dict_freq)
get_freq(list_bi, bigram_dict_freq)
get_freq(list_tri, trigram_dict_freq)
get_freq(list_four, fourgram_dict_freq)
get_freq(list_five, fivegram_dict_freq)

#print_ngram_tables(letter_list)
calculate_all_perp(letter_list_test)


create_random_sentences(letter_list_test)
