# gkærxseufn svar for den første opgave dog er det forkert fordi der bliver brugt 28 bogstaver vi manger W  såå det 29 mennn ud fra beksrivelsen bliver det gkærxseufn
ALPHABET ="abcdefghijklmnopqrstuvwxyzæøå"

L = len(ALPHABET)
TO_NUM = {ch: i+1 for i, ch in enumerate(ALPHABET)}
TO_CHAR = {i+1: ch for i, ch in enumerate(ALPHABET)}
TO_CHAR[0] = ""


def decryptonize(id,cryptizedtext):
    uncryptizedtyext=[]
    crypttextlower = cryptizedtext.lower().replace(" ","")
    idlower = id.lower().replace(" ","")
    for i,(ch,p) in enumerate(zip(crypttextlower,idlower)):

        ct = TO_NUM[ch]

        ids = TO_NUM[p]
        løst = (ct - ids) % L
        print(løst)
        uncryptizedtyext.append(TO_CHAR[løst])
    return "".join(uncryptizedtyext)


def cryptonize(id,text):
    cryptedtext=[]
    textlower = text.lower().replace(" ","")
    idlower = id.lower().replace(" ","")
    for i,(ch,p) in enumerate(zip(textlower,idlower)):

        t = TO_NUM[ch]

        ids = TO_NUM[p]
        # print(t,ch)
        # print(ids,p)
        # print("bugga")
        crypttext = (t + ids) % L
        cryptedtext.append(TO_CHAR[crypttext])


    return "".join(cryptedtext)



ot = cryptonize("programmerin","sukkertoppen")
print(ot)
ot2=decryptonize("programmerin",ot)
print(ot2)

