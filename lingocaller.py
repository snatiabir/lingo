#!/usr/bin/env python

import random
import codecs

inplay = set([])
called = []
conly = False

place = {"bilabial":set(["b", "p", "m", u"w\u0325", "w"]), "labiodental":set(["f", "v"]), "interdental":set([u"\u03B8", u"\u00F0"]),"alveolar":set(["t", "d", "s", "z", "l", u"\u0279", "n"]), "postalveolar":set([u"\u0283", u"\u0292",u"t\u0283", u"d\u0292"]), "palatal":set(["j"]),"velar":set(["k", "g",u"\u014B"]), "glottal":set([u"\u0294", "h"])}
manner = {"stop":set(["b","p","t","d","k","g",u"\u0294"]),"fricative":set(["f","v",u"\u03B8",u"\u00F0","s","z",u"\u0283",u"\u0292","h"]),"affricate":set([u"t\u0283",u"d\u0292"]),"glide":set(["w","j",u"w\u0325"]), "nasal":set(["m","n",u"\u014B"]) ,"lateral liquid":set(["l"]), "retroflex liquid":set([u"\u0279"])}
voicing = {"voiced":set(["b","m","v",u"\u00F0","d","z","l",u"\u0279","n",u"\u0292","j",u"d\u0292","g",u"\u014B","w"]),"voiceless":set(["t",u"w\u0325","p","f",u"\u03B8","s",u"\u0283",u"t\u0283","k","h",u"\u0294"])}

height = {"high":set(["i","u",u"\u026A",u"\u028A"]), "mid":set(["e",u"\u025B",u"\u028C",u"\u0259","o",u"\u0254"]), "low":set([u"\u00E6",u"\u0251"])}
backness = {"front":set(["i", u"\u026A", "e", u"\u025B", u"\u00E6"]), "central":set([u"\u028C", u"\u0259"]), "back":set(["u",u"\u028A","o", u"\u0254", u"\u0251"])}
tenseness = {"tense":set(["i", "e", "u", "o"]), "lax":set([u"\u026A",u"\u025B",u"\u00E6",u"\u028A",u"\u0254",u"\u0251", u"\u028C", u"\u0259"])}
rounding = {"rounded":set(["u", u"\u028A", "o", u"\u0254"]), "unrounded":set(["i",u"\u026A","e",u"\u025B",u"\u00E6",u"\u028C", u"\u0259",u"\u0251"])}

ordering = dict([[x,"a"] for x in voicing.keys()])
ordering.update(dict([[x,"b"] for x in place.keys()]))
ordering.update(dict([[x,"c"] for x in manner.keys()]))
ordering.update(dict([[x,"d"] for x in height.keys()]))
ordering.update(dict([[x,"e"] for x in backness.keys()]))
ordering.update(dict([[x,"f"] for x in rounding.keys()]))
ordering.update(dict([[x,"g"] for x in tenseness.keys()]))

def test():
    """prints out the full set of sounds for each feature specification"""
    print("************CONSONANTS*************")
    print("************places*************")
    test_print(place)
    print("************manner*************")
    test_print(manner)
    print("************voicing*************")
    test_print(voicing)
    print("***********************************")
    print("\n************VOWELS*************")
    print("************height*************")
    test_print(height)
    print("************backness*************")
    test_print(backness)
    print("************tenseness*************")
    test_print(tenseness)
    print("************rounding*************")
    test_print(rounding)
    print("*********************************")
    return

def test_print(features):
    for x in features.items():
        li = " ".join(list(x[1]))
        print(x[0]+": "+li)
    return

def sint(seq):
    sint = seq[0]
    for x in seq[1:]:
        sint = sint.intersection(x)
    return sint

def cons(n=2):
    """selects n random (consonant) feature specifications, and returns the specification and the respective natural class"""
    n=random.choice([2,3])
    p = random.choice(list(place.items()))
    m = random.choice(list(manner.items()))
    v = random.choice(list(voicing.items()))
    features = random.sample([p,m,v],n)
    #print [x[1] for x in features]
    s = sint([x[1] for x in features])
    if s:
        return [x[0] for x in features], s
    else: return cons(n)

def vowl(n=3):
    """selects n random (vowel) feature specifications, and returns the specification and the respective natural class"""
    n=random.choice([4,3])
    h = random.choice(list(height.items()))
    b = random.choice(list(backness.items()))
    t = random.choice(list(tenseness.items()))
    r = random.choice(list(rounding.items()))
    features = random.sample([h,b,t,r],n)
    s = sint([x[1] for x in features])
    if s:
        return [x[0] for x in features], s
    else: return vowl(n)

def call():
    """makes a call to either the consnant or vowel call functions, and if the result hasn't been made yet, formats it for output"""
    if conly: choice = cons()
    else: choice=random.choice([vowl(), cons(), cons()])
    choice[0].sort(key = lambda x: ordering[x])
    global called, inplay
    if choice[0] not in called:
        called.append(choice[0])
        inplay.update(choice[1])
        print("******************************************")
        print(choice[0])
        print("******************************************\n")
        return
    else: return call()

def inp():
    """prints all called sounds for the current bingo game"""
    global inplay
    print("**************SOUNDS IN PLAY**************")
    for x in list(inplay):
        print(x)
    print("*****************************************\n")
    return

def hist():
    """prints all bingo calls for the curren game"""
    global called
    print("***************PRIOR CALLS***************")
    for x in called:
        print(x)
    print("*****************************************\n")
    return

def ng():
    """clears the game history (both calls and sounds)"""
    global called, inplay
    called = []
    inplay = set([])
    print("Ready for new game!")
    return

def conl(boo):
    """toggle consonants only"""
    global conly
    conly = boo
    if conly == True:
        print("calling consonants only")
        return
    else: print("calling all sounds")
    creturn



print("[l"+u"\u026A"+u"\u014B"+"go"+u"\u028A"+"]!")
print("COMMANDS:\n c = call\n h = game history\n i = sounds in play\n new = reset for a new game\n conly = call only consonants\n allsounds = call consonants and vowels\n quit= quit")
comm = ""
while comm != "quit":
    comm = input()
    if comm == "c": call()
    if comm == "h": hist()
    if comm == "i": inp()
    if comm == "new":ng()
    if comm == "t": test()
    if comm == "conly": conl(True)
    if comm == "allsounds": conl(False)
     







    
