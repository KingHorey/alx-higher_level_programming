#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        hghst = max(a_dictionary)
        if not hghst:
            return None
        else:
            return hghst
