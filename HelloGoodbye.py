import sys 

string1 = sys.argv[1]
string2 = sys.argv[2]

def hello(string1, string2):
    print("Hello", string1, "and",  string2)

def goodbye(string1, string2):
    print("Goodbye", string1,  "and",  string2)

hello(string1, string2)
goodbye(string2, string1)