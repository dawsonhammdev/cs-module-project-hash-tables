# Your code here
fname = input("Enter file name: ")
def histo(fname):
    
    
    d = {}
    
    with open(fname, 'r') as f:
        for line in f:
            for char in '":;,.-+=/\\|[]{}()*^&':
                line = line.replace(char, '')
                line = line.lower()
                words = line.split()
                for word in words:
                    # if it is a key in our dictionary we will return the value if not we will add it.
                    d[word] = d.get(word, 0) + 1
    return d

def print_sorted(fname):
    d = histo(fname)

    items = list(d.items())

    items.sort(key=lambda e: e[1], reverse=True)

    for i in items:
        print(f'{i[0]}: {"#" * i[1]}')

print(print_sorted(fname))




        


    


