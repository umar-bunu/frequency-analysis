from operator import indexOf
import sys

print('---------BEGIN---------')
f = open(sys.argv[1])
if f.closed:
    print("File not opened...\nTerminating");
    exit(1)
wholeTxt = f.read();
f.close();
letters = [{'letter':'a','freq':0},{'letter':'b','freq':0},{'letter':'c','freq':0},{'letter':'d','freq':0},{'letter':'e','freq':0},{'letter':'f','freq':0},{'letter':'g','freq':0},{'letter':'h','freq':0},{'letter':'i','freq':0},{'letter':'j','freq':0},{'letter':'k','freq':0},{'letter':'l','freq':0},{'letter':'m','freq':0},{'letter':'n','freq':0},{'letter':'o','freq':0},{'letter':'p','freq':0},{'letter':'q','freq':0},{'letter':'r','freq':0},{'letter':'s','freq':0},{'letter':'t','freq':0},{'letter':'u','freq':0},{'letter':'v','freq':0},{'letter':'w','freq':0},{'letter':'x','freq':0},{'letter':'y','freq':0},{'letter':'z','freq':0}]
for eachLetter in letters:
    letters[letters.index(eachLetter)]['freq'] = wholeTxt.count(eachLetter['letter'].upper())
    print("letter count: "+str(letters[letters.index(eachLetter)]['freq']) )




print('----------END-----------')