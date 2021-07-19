#Justin Baraniuk
#February 25, 2021

def histogram(s):
    """Takes a string and creates a dictionary that maps 
    letters to frequencies.
    s: str
    returns: dict
    """
    
    d = {}
    
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
            
    return d


def most_frequent(s):
     """Takes a string and prints the letters in decreasing order of frequency.
    s: str
    """
    hist = histogram(s)
    
    t = []
    for key, value in hist.items():
        t.append((value, key))
   
    t.sort(reverse=True)

    letters = []
    for key, value in t:
        if value != ' ':
            print(value)