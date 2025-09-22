# gkærxseufn svar for den første opgave dog er det forkert fordi der bliver brugt 28 bogstaver vi manger W  såå det 29 mennn ud fra beksrivelsen bliver det gkærxseufn
ALPHABET ="abcdefghijklmnopqrstuvwxyzæøå"

L = len(ALPHABET)
TO_NUM = {ch: i+1 for i, ch in enumerate(ALPHABET)}
print(TO_NUM)
TO_CHAR = {i+1: ch for i, ch in enumerate(ALPHABET)}
TO_CHAR[0] = ""
#Vi bruger enumerate til at give hvert bogstav et tal. 
#Normalt starter det på 0, men vi lægger 1 til, så det starter på 1. TO_CHAR[0] = "" er for at undgå fejl.

def decryptonize(id,cryptizedtext):
    uncryptizedtyext=[]
    # slut uncryptizedtyext
    crypttextlower = cryptizedtext.lower().replace(" ","")
    idlower = id.lower().replace(" ","")
    # vi sætter begge af dem til .lower().replace så vi både fjerne mellemrum og .lower så sortebogstaver ikke effecter kryptering 
    for i,(ch,p) in enumerate(zip(crypttextlower,idlower)):

        ct = TO_NUM[ch]

        ids = TO_NUM[p]
        løst = (ct - ids) % L
        print(løst)
        uncryptizedtyext.append(TO_CHAR[løst])
    return "".join(uncryptizedtyext)
    # den returner den sidste løst uncryptizedtyext

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

# det sammen basic som dekryptering men i stedet for et krypterede tekst kryptere vi teksten 
ot = cryptonize("programmerin","sukkertoppen")
print(ot)
ot2=decryptonize("programmerin",ot)
print(ot2)
# her printes bare den dektryperede tekst og krypteret tekst :D

#DER ER STAVE FEJL I TEKSTEN "uncryptizedtYext"
