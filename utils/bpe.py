import numpy as np
from copy import deepcopy
# adapted from: https://github.com/karpathy/minbpe/tree/master

def merge(ids, pair, idx):
    """
    In the list of integers (ids), replace all consecutive occurrences
    of pair with the new integer token idx
    Example: ids=[1, 2, 3, 1, 2], pair=(1, 2), idx=4 -> [4, 3, 4]
    """
    newids = []
    i = 0
    while i < len(ids):
        # if not at the very last position AND the pair matches, replace it
        if ids[i] == pair[0] and i < len(ids) - 1 and ids[i+1] == pair[1]:
            newids.append(idx)
            i += 2
        else:
            newids.append(ids[i])
            i += 1
    return newids

def get_stats(ids, counts=None):
    """
    Given a list of integers, return a dictionary of counts of consecutive pairs
    Example: [1, 2, 3, 1, 2] -> {(1, 2): 2, (2, 3): 1, (3, 1): 1}
    Optionally allows to update an existing dictionary of counts
    """
    counts = {} if counts is None else counts
    for pair in zip(ids, ids[1:]): # iterate consecutive elements
        counts[pair] = counts.get(pair, 0) + 1
    return counts

# single step of BPE
def one_step_of_bpe(
        ids: np.array,
        merges: dict,
        alphabet_size: int 
        ):
    # count up the number of times every consecutive pair appears
    stats = get_stats(ids=ids)
    # find the pair with the highest count
    pair = max(stats, key=stats.get)
    # mint a new token: assign it the next available id
    idx = alphabet_size + 1
    # replace all occurrences of pair in ids with idx
    ids = merge(ids, pair, idx)
    # save the merge
    merges[pair] = idx

    return deepcopy(ids), deepcopy(merges), idx
