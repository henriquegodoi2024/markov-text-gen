# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 16:04:07 2025

@author: henri
"""
import random

def create_dictionary(filename):
    '''returns a dictionary key-value pairs from a text file '''
    file = open(filename, 'r')
    text = file.read()
    file.close()
    words = text.split()
    
    d = {}
    current_word = '$'
    
    for next_word in words:
        if current_word not in d:
            d[current_word] = [next_word]
            
        else:
            d[current_word] += [next_word]
            
        if '.' in next_word:
            current_word = '$'
            
        elif '!' in next_word:
            current_word = '$'
            
        elif'?' in next_word:
            current_word = '$'
            
        else:
            current_word = next_word
            
    return d

    



def generate_text(word_dict, num_words):
    ''' generate and print num_words using word_dict'''
    current_word = '$'         

    for i in range(num_words): 
        
        if current_word in word_dict and word_dict[current_word] != []:
            wordlist = word_dict[current_word]
        else:
            
            current_word = '$'
            wordlist = word_dict[current_word]

        
        next_word = random.choice(wordlist)

        
        print(next_word, end=' ')

        
        char = next_word[-1]
        
        if char == '.' or char == '!' or char == '?':
            current_word = '$'
        else:
            current_word = next_word

    print()   

 

        
            
            
            