import numpy as np
from tqdm import tqdm

# 
def increment_dict(dictionary: dict, key: str):
    try:
        dictionary[key] += 1
    except KeyError:
        dictionary[key] = 1

# 
def sort_dictionary(dictionary: dict):
    return {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}

# 
# increment frequency for a given item (sentence) and a given tokenizer
def increment_frequency(dictionary:dict, item: str):
    for count, word in enumerate(item.split()):
        increment_dict(dictionary=dictionary, key=word)
    return count+1

# 
def normalize_dictionary(dictionary: dict, denominator: int):
    return_dictionary = {}
    for key, value in dictionary.items():
        return_dictionary[key] = value/denominator
    
    return return_dictionary

# takes array and 
def freq(arr: np.array):
    raw_freq_dict = {}
    count = 0

    # prog_bar = tqdm(arr)
    for raw_item in arr:
        item = str(raw_item)
        count += increment_frequency(dictionary=raw_freq_dict, item=item)

    # 
    sorted_freq_dict = sort_dictionary(dictionary=raw_freq_dict)
    frequencies = normalize_dictionary(dictionary=sorted_freq_dict, denominator=count)

    return frequencies