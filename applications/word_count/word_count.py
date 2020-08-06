def word_count(s):
    # Your code here
    # cleaning all the words from symbols and uppercase
    for char in '":;,.-+=/\\|[]{}()*^&':
        s=s.replace(char, '')
    s = s.lower()

    word_list = s.split()
    
    # initialize a dict
    d = {}

    for word in word_list:
        # if it is a key in our dictionary we will return the value if not we will add it.
        d[word] = d.get(word, 0) + 1

    return d






if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))