import sys

def showTxt(txt, typeTxt, shouldAnalyze):
    if(shouldAnalyze):
        print('\n---------BEGIN---------\n')
    print(typeTxt+"\n")
    print(txt);
    if(shouldAnalyze):
        letters = [{'letter':'a','freq':0},{'letter':'b','freq':0},{'letter':'c','freq':0},{'letter':'d','freq':0},{'letter':'e','freq':0},{'letter':'f','freq':0},{'letter':'g','freq':0},{'letter':'h','freq':0},{'letter':'i','freq':0},{'letter':'j','freq':0},{'letter':'k','freq':0},{'letter':'l','freq':0},{'letter':'m','freq':0},{'letter':'n','freq':0},{'letter':'o','freq':0},{'letter':'p','freq':0},{'letter':'q','freq':0},{'letter':'r','freq':0},{'letter':'s','freq':0},{'letter':'t','freq':0},{'letter':'u','freq':0},{'letter':'v','freq':0},{'letter':'w','freq':0},{'letter':'x','freq':0},{'letter':'y','freq':0},{'letter':'z','freq':0}]
        print('\nAnalysis:')
        for eachLetter in letters:
            letters[letters.index(eachLetter)]['freq'] = wholeTxt.count(eachLetter['letter'].upper())
            print(eachLetter['letter'].upper()+'->'+str(letters[letters.index(eachLetter)]['freq'])+', ', end="" )

def takeReplacement(wholeTxt, wholeTxtTemp2):
    wholeTxtTemp = wholeTxtTemp2;
    print('\n---------BEGIN---------\n')
    replacement = input("\nEnter replacement rule-> ").split(",");
    print('\n\n----------END-----------')
    for eachLetter in replacement:
        firstreplace, secondreplace = eachLetter.split(":")
        wholeTxtTemp = wholeTxtTemp.replace(firstreplace, secondreplace);
    showTxt(wholeTxt, "Cipher Text:", True)
    showTxt(wholeTxtTemp, "Plain Text:", False);
    return wholeTxtTemp

if(len(sys.argv)<2):
    print("File Argument must be specified...\nTerminating");
    exit(1)



f = open(sys.argv[1])
if f.closed:
    print("File not opened...\nTerminating");
    exit(1)
wholeTxt = f.read();
wholeTxtTemp = wholeTxt
f.close();
showTxt(wholeTxt, "Cipher Text:", True)
print('\n----------END-----------\n')

while(True):
    option= int(input("\n\nOption:\n1)Take replace rule\n2)Exit\nOption> "));
    if option ==1:
        wholeTxtTemp = takeReplacement(wholeTxt, wholeTxtTemp);
    else:
        exit(0)
    print('\n----------END-----------\n')




