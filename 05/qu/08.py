# Change the lookup procedure
# to now work with dictionaries.

def lookup(index, keyword):
    if keyword not in index:
        return None
    return index[keyword]

