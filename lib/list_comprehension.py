#!/usr/bin/env python3

def return_evens(num_list):
    
    even_number=[n for n in num_list if n%2==0]
    return even_number

print(return_evens(range(20)))
    


  


def make_exclamation(sentence_list):
    return[sentence+"!" for sentence in sentence_list]

