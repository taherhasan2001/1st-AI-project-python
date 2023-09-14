import random
from AI.tech import *
from AI.coures import *


courls = []


def readCour(ls):
    f = open("AI/courses.txt", "r")
    templs = []
    for x in f:
        templs.append(x)
    for y in templs:
        y = y.replace(".\n", "")
        subinfo = y.split(",")
        teachls = []
        for u in subinfo[4:]:
            j = u.split("-")
            teach = teacher(j[0], int(j[1]))
            teachls.append(teach)
        temp = coures(subinfo[0], subinfo[1], subinfo[2], int(subinfo[3]), teachls)
        ls.append(temp)


readCour(courls)
all_genes = []


def Genes(ls, course):
    for x in course:
        for i in range(x.numOFsection):
            st = x.code + "-" + str(i + 1)
            ls.append(st)


Genes(all_genes, courls)
print("the number of sections of courses is: ", len(all_genes))
FirCrom = []


def MakeFirCrom(Dictin, all):
    ls_time = []
    s1 = "Mon"
    i = 1
    while i < 6:
        st = s1 + "-" + str(i)
        ls_time.append(st)
        i += 1
    s2 = "Tue"
    i = 1
    while i < 6:
        st = s2 + "-" + str(i)
        ls_time.append(st)
        i += 1
    i = 0
    for x in ls_time:
        if "2" in x:
            j = 0
            ls_temp = []
            while j < 10:
                ls_temp.append(all[i])
                j += 1
                i += 1
            Dictin.append(ls_temp)
        elif x == "Tue-5":
            j = 0
            ls_temp = []
            while j < 4:
                ls_temp.append(all[i])
                j += 1
                i += 1
            Dictin.append(ls_temp)
        elif x == "Mon-5":
            j = 0
            ls_temp = []
            while j < 5:
                ls_temp.append(all[i])
                j += 1
                i += 1
            Dictin.append(ls_temp)
        else:
            j = 0
            ls_temp = []
            while j < 8:
                ls_temp.append(all[i])
                j += 1
                i += 1
            Dictin.append(ls_temp)


MakeFirCrom(FirCrom, all_genes)


def swap(itr, ls1, ls2):
    if itr == "1":
        i = 0
        j = 1
        while j < len(ls2):
            fir_e = ls1.pop(i)
            sec_e = ls2.pop(j)
            ls1.insert(i, sec_e)
            ls2.insert(j, fir_e)
            i += 2
            j += 2

    else:
        i = 1
        j = 0
        while i < len(ls1):
            fir_e = ls1.pop(i)
            sec_e = ls2.pop(j)
            ls1.insert(i, sec_e)
            ls2.insert(j, fir_e)
            i += 2
            j += 2


def Mutation(Fir):
    ls_bit = ["1", "0"]
    i = 0
    j = 5
    while i < 5:
        itr = random.choice(ls_bit)
        swap(itr, Fir[i], Fir[j])
        i += 1
        j += 1


Population = []


def PlusOne(Fir):
    ls = []
    for x in Fir:
        ls_temp = []
        for y in x:
            ls_temp.append(y)
        ls.append(ls_temp)
    return ls


def make_pop(popo, Fir):
    i = 0
    Mutation(Fir)
    popo.append(Fir)
    while i < 9:
        ls_temp = PlusOne(popo[-1])
        Mutation(ls_temp)
        popo.append(ls_temp)
        i += 1


make_pop(Population, FirCrom)


def FitHel(ls):
    res = 0.0
    lsk = []
    for x in ls:
        lsk.append(x)
    i = 0
    while i < len(lsk) - 1:
        j = i + 1
        ls_same = []
        while j < len(lsk):
            if lsk[i][:9] == lsk[j][:9]:
                ls_same.append(lsk[j])
                lsk.pop(j)
                j -= 1
            j += 1
        if len(ls_same) > 0:
            res += 0.5
            lsk.pop(i)
            i -= 1
        i += 1
    i = 0
    while i < len(lsk) - 1:
        j = i + 1
        ls_same = []
        while j < len(lsk):
            if lsk[i][4] == lsk[j][4]:
                ls_same.append(lsk[j])
                lsk.pop(j)
                j -= 1
            j += 1
        if len(ls_same) > 0:
            res += 1.0
            lsk.pop(i)
            i -= 1
        i += 1

    res += len(lsk)
    return res


def Fit(Fir):
    res = 0
    for x in Fir:
        res += FitHel(x)
    return res


lsress = []


def MinPos(ls):
    min = ls[0]
    pos = 0
    j = 1
    while (j < len(ls)):
        if (min > ls[j]):
            min = ls[j]
            pos = j
        j += 1
    return pos


def MinPos2(popo, res):
    pos = 0
    j = 0
    while (j < len(popo)):
        if (Fit(popo[j]) == res):
            return j
        j += 1


def Max(ls):
    max = ls[0]
    pos = 0
    j = 1
    while (j < len(ls)):
        if (max <= ls[j]):
            max = ls[j]
            pos = j
        j += 1
    return pos


def numOfcopy(st, Fir):
    num = 0
    for x in Fir:
        for y in x:
            if (st == y[:8]):
                num += 1
    return num


def CheckInc(Fir, cours):
    lsr = []
    for x in cours:
        lsr.append(numOfcopy(x.code, Fir))
    for i in range(len(lsr)):
        if (not (cours[i].numOFsection == lsr[i])):
            return False
    return True


def Uniated(Fir1, Fir2):
    all = []
    for x in Fir1:
        for y in x:
            all.append(y)
    for x in Fir2:
        for y in x:
            all.append(y)
    return all


def ToForm(itr, ls):
    if (itr == "0"):
        i = 0
        j = len(ls) - 2
        while (i < len(ls) - 1):
            firE = ls.pop(i)
            secE = ls.pop(j)
            ls.insert(i, secE)
            ls.insert(j, firE)
            i += 2
            j -= 2
    elif (itr == "1"):
        i = 0
        j = len(ls) // 2
        while (i < len(ls) // -1):
            firE = ls.pop(i)
            secE = ls.pop(j)
            ls.insert(i, secE)
            ls.insert(j, firE)
            i += 2
            j += 2
    elif (itr == "2"):
        i = 0
        j = len(ls) - 2
        while (i < len(ls) // 2 - 1):
            firE = ls.pop(i)
            secE = ls.pop(j)
            ls.insert(i, secE)
            ls.insert(j, firE)
            i += 2
            j -= 2
    elif (itr == "3"):
        i = 1
        j = len(ls) - 3
        while (i < len(ls) // 2 - 1):
            firE = ls.pop(i)
            secE = ls.pop(j)
            ls.insert(i, secE)
            ls.insert(j, firE)
            i += 2
            j -= 2

    else:
        i = 1
        j = len(ls) // 2 + 1
        while (i < len(ls) // -1):
            firE = ls.pop(i)
            secE = ls.pop(j)
            ls.insert(i, secE)
            ls.insert(j, firE)
            i += 2
            j += 2


def RealCro(Fir1, Fir2, cours):
    uin = Uniated(Fir1, Fir2)
    lsbit = ["0", "1", "2", "3", "4"]
    itr = random.choice(lsbit)
    ToForm(itr, uin)
    Fir1.clear()
    Fir2.clear()
    uin2 = []
    numofsec = []
    readCour(numofsec)
    sum = 1
    while (sum > 0):
        sum = 0
        i = 0
        while (i < len(uin)):
            for y in range(len(cours)):
                if (uin[i][:8] == numofsec[y].code):
                    if (numofsec[y].numOFsection == int(uin[i][9])):
                        uin2.append(uin[i])
                        uin.pop(i)
                        numofsec[y].numOFsection -= 1
                        i -= 1
                        break
            i += 1
        for x in numofsec:
            sum += x.numOFsection
    MakeFirCrom(Fir1, uin2)
    MakeFirCrom(Fir2, uin)


def adba322(s, Fir):
    c = 0
    for x in Fir:
        for y in x:
            if (s == y[:8]):
                c += 1
    return c


def tttt(Cou, Fir):
    for x in Cou:
        o = adba322(x.code, Fir)
        if (o != x.numOFsection):
            return False
    return True


def CroseOver(popo, lsre):
    lsbit = ["1", "0", "2", "3"]
    for x in popo[:10]:
        lsre.append(Fit(x))
    k = 0
    l = 0
    max_pos = Max(lsre)
    while Fit(popo[max_pos]) < 40 or tttt(courls, popo[max_pos]) == False:
        for x in popo[:10]:
            ls_temp = PlusOne(x)
            popo.append(ls_temp)
        i = 10
        while i < len(popo):
            itr = random.choice(lsbit)
            RealCro(popo[i], popo[i + 1], courls)
            i += 2

        for x in popo[10:]:
            lsre.append(Fit(x))
        j = 0
        while (j < 10):
            pos = MinPos(lsre)
            pos2 = MinPos2(popo, lsre[pos])
            lsre.pop(pos)
            popo.pop(pos)
            j += 1
        max_pos = Max(lsre)
        if (l == 100):
            for x in popo:
                Mutation(x)
                l = 0
        l += 1
        k += 1
    print("The number of iterations is: ", k)
    return max_pos


def FindCour(cour, Cours):
    i = 0
    while (i < len(Cours)):
        if (cour[:8] == Cours[i].code):
            return i
        i += 1


def AddTeach(ls, Cours):
    lsk = []
    i = 0
    while (i < len(ls) - 1):
        j = i + 1
        lsSame = []
        while (j < len(ls)):
            if (ls[i][:9] == ls[j][:9]):
                lsSame.append(ls[j])
                ls.pop(j)
                j -= 1
            j += 1
        if (len(lsSame) > 0):
            lsSame.append(ls[i])
            h = ls.pop(i)
            pos = FindCour(lsSame[0], Cours)
            k = 0
            u = 0
            while (k < len(Cours[pos].teacherANDsec) and u < len(lsSame)):
                if (Cours[pos].teacherANDsec[k].numOFsec > 0):
                    str = lsSame[u] + "-" + Cours[pos].teacherANDsec[k].name
                    lsk.append(str)
                    Cours[pos].teacherANDsec[k].numOFsec -= 1
                    u += 1
                    k -= 1
                k += 1
            i -= 1
        i += 1
    for x in ls:
        pos = FindCour(x, Cours)
        k = 0
        while (k < len(Cours[pos].teacherANDsec)):
            if (Cours[pos].teacherANDsec[k].numOFsec > 0):
                str = x + "-" + Cours[pos].teacherANDsec[k].name
                lsk.append(str)
                Cours[pos].teacherANDsec[k].numOFsec -= 1
                break
            k += 1
    ls.clear()
    for x in lsk:
        ls.append(x)


def DistrubTeach(Fir, Cours):
    for x in Fir:
        AddTeach(x, Cours)


def getdub(ls):
    lsSameP = []
    i = 0
    while (i < len(ls) - 1):
        j = i + 1
        while (j < len(ls)):
            if (ls[i][14:] == ls[j][14:]):
                lsSameP.append(j)
            j += 1
        i += 1
    return lsSameP


def Checkcopy(st, ls):
    for x in ls:
        if (st[14:] == x[14:]):
            return False
    return True


def Fix(Fir):
    for x in Fir:
        lsP1 = getdub(x)
        lsP = list(set(lsP1))
        lsV = []
        for o in lsP:
            lsV.append(x[o])
        lsP.sort()
        b = len(lsP) - 1
        while (b >= 0):
            x.pop(lsP[b])
            b -= 1

        if (len(lsP) > 0):
            for k in lsV:
                ch = False
                for i in range(len(Fir)):
                    ch = False
                    if (Checkcopy(k, Fir[i]) == True):
                        if (len(Fir[i]) > 9):
                            continue
                        Fir[i].append(k)
                        ch = True
                        break

                if (ch == False):
                    Fir[0].append(k)


best = CroseOver(Population, lsress)
print("the value of the Fitness function for courses is: ", Fit(Population[best]))

for x in range(len(Population[best])):
    for y in range(len(Population[best][x])):
        if (x < 5):
            if (x % 2 == 0):
                Population[best][x][y] = Population[best][x][y] + ":1:"
            else:
                Population[best][x][y] = Population[best][x][y] + ":2:"
        else:
            if (x % 2 == 1):
                Population[best][x][y] = Population[best][x][y] + ":1:"
            else:
                Population[best][x][y] = Population[best][x][y] + ":2:"

DistrubTeach(Population[best], courls)

p = 0

# -------------------------------------------------------------------------labs


labs = []


def readLabs(ls):
    f = open("AI/labs.txt", "r")
    templs = []
    for x in f:
        templs.append(x)
    for y in templs:
        y = y.replace(".\n", "")
        subinfo = y.split(",")
        teachls = []
        for u in subinfo[4:]:
            j = u.split("-")
            teach = teacher(j[0], int(j[1]))
            teachls.append(teach)
        temp = coures(subinfo[0], subinfo[1], subinfo[2], int(subinfo[3]), teachls)
        ls.append(temp)


readLabs(labs)

AllgensL = []

Genes(AllgensL, labs)

print("the number of secitons of labs: ", len(AllgensL))


def MakeFirCromL(Dictin, all):
    lstime = []
    s1 = "Sat"
    i = 1
    while (i < 4):
        st = s1 + "-" + str(i)
        lstime.append(st)
        i += 1
    s2 = "Mon"
    i = 1
    while (i < 4):
        st = s2 + "-" + str(i)
        lstime.append(st)
        i += 1

    s2 = "Wen"
    i = 1
    while (i < 4):
        st = s2 + "-" + str(i)
        lstime.append(st)
        i += 1

    s2 = "Tue"
    i = 1
    while (i < 4):
        st = s2 + "-" + str(i)
        lstime.append(st)
        i += 1

    s2 = "Thu"
    i = 1
    while (i < 4):
        st = s2 + "-" + str(i)
        lstime.append(st)
        i += 1

    i = 0
    for x in lstime:
        if ("Mon-2" in x):
            j = 0
            lstemp = []
            while (j < 5):
                lstemp.append(all[i])
                j += 1
                i += 1
            Dictin.append(lstemp)
        else:
            j = 0
            lstemp = []
            while (j < 4):
                lstemp.append(all[i])
                j += 1
                i += 1
            Dictin.append(lstemp)


FirCromL = []
MakeFirCromL(FirCromL, AllgensL)


def MutationL(Fir):
    lsbit = ["1", "0"]
    i = 0
    j = 7
    while (i < 7):
        itr = random.choice(lsbit)
        swap(itr, Fir[i], Fir[j])
        i += 1
        j += 1


def MakepopL(popo, Fir):
    i = 0
    MutationL(Fir)
    popo.append(Fir)
    while (i < 9):
        lstemp = PlusOne(popo[-1])
        MutationL(lstemp)
        popo.append(lstemp)
        i += 1


PopultionL = []
MakepopL(PopultionL, FirCromL)
LsresL = []


def RealCroL(Fir1, Fir2, cours):
    uin = Uniated(Fir1, Fir2)
    lsbit = ["0", "1", "2", "3", "4"]
    itr = random.choice(lsbit)
    ToForm(itr, uin)
    Fir1.clear()
    Fir2.clear()
    uin2 = []
    numofsec = []
    readLabs(numofsec)
    sum = 1
    while (sum > 0):
        sum = 0
        i = 0
        while (i < len(uin)):
            for y in range(len(cours)):
                if (uin[i][:8] == numofsec[y].code):
                    if (numofsec[y].numOFsection == int(uin[i][9])):
                        uin2.append(uin[i])
                        uin.pop(i)
                        numofsec[y].numOFsection -= 1
                        i -= 1
                        break
            i += 1
        for x in numofsec:
            sum += x.numOFsection
    MakeFirCromL(Fir1, uin2)
    MakeFirCromL(Fir2, uin)


def CroseOverL(popo, lsre):
    lsbit = ["1", "0", "2", "3"]
    for x in popo[:10]:
        lsre.append(Fit(x))
    k = 0
    l = 0
    maxpos = Max(lsre)
    while (Fit(popo[maxpos]) < 41):
        for x in popo[:10]:
            lstemp = PlusOne(x)
            popo.append(lstemp)

        i = 10
        while (i < len(popo)):
            itr = random.choice(lsbit)
            RealCroL(popo[i], popo[i + 1], labs)
            i += 2

        for x in popo[10:]:
            lsre.append(Fit(x))
        j = 0
        while (j < 10):
            pos = MinPos(lsre)
            pos2 = MinPos2(popo, lsre[pos])
            lsre.pop(pos)
            popo.pop(pos)
            j += 1
        maxpos = Max(lsre)
        if (l == 100):
            for x in popo:
                MutationL(x)
                l = 0
        l += 1
        k += 1
    print("The number of iterations is: ", k)
    return maxpos


def FixL(Fir):
    for x in Fir:
        lsP1 = getdub(x)
        lsP = list(set(lsP1))
        lsV = []
        for o in lsP:
            lsV.append(x[o])
        lsP.sort()
        b = len(lsP) - 1
        while (b >= 0):
            x.pop(lsP[b])
            b -= 1

        if (len(lsP) > 0):
            for k in lsV:
                for i in range(len(Fir)):
                    if (Checkcopy(k, Fir[i]) == True):
                        if (len(Fir[i]) > 7):
                            continue
                        Fir[i].append(k)
                        break


Lbest = CroseOverL(PopultionL, LsresL)

print("the value of the Fitness function for labs is: ", Fit(PopultionL[Lbest]))

for x in range(len(PopultionL[Lbest])):
    for y in range(len(PopultionL[Lbest][x])):
        PopultionL[Lbest][x][y] = PopultionL[Lbest][x][y] + ":1:"

DistrubTeach(PopultionL[Lbest], labs)

for h in range(10):
    FixL(PopultionL[Lbest])
for h in range(10):
    Fix(Population[best])


def Coooon(ls1, ls2):
    lsres = []
    for x in ls1:
        lsres.append(x)
    for x in ls2:
        lsres.append(x)
    return lsres


def CopyLC(FirL, FirC):
    RES = []
    for i in range(len(FirL)):
        if (i < 3):
            x1 = []
            for x in FirL[i]:
                x1.append(x)
            RES.append(x1)
        elif (i < 9):
            if (i % 3 == 0):
                x1 = Coooon(FirL[i], FirC[0])
                x2 = Coooon(x1, FirC[1])
                RES.append(x2)
            elif (i % 3 == 1):
                x1 = Coooon(FirL[i], FirC[2])
                x2 = Coooon(x1, FirC[3])
                RES.append(x2)
            else:
                x1 = Coooon(FirL[i], FirC[4])
                RES.append(x1)
        else:
            if (i % 3 == 0):
                x1 = Coooon(FirL[i], FirC[5])
                x2 = Coooon(x1, FirC[6])
                RES.append(x2)
            elif (i % 3 == 1):
                x1 = Coooon(FirL[i], FirC[7])
                x2 = Coooon(x1, FirC[8])
                RES.append(x2)
            else:
                x1 = Coooon(FirL[i], FirC[9])
                RES.append(x1)
    return RES


def YaaaRabee(Fir):
    for x in Fir:
        lsP1 = getdub(x)
        lsP = list(set(lsP1))
        lsV = []
        for o in lsP:
            lsV.append(x[o])
        lsP.sort()
        b = len(lsP) - 1
        while (b >= 0):
            x.pop(lsP[b])
            b -= 1

        if (len(lsP) > 0):
            for k in lsV:
                i = 0
                while (i < len(Fir)):
                    v = (i + 3) % len(Fir)
                    if (Checkcopy(k, Fir[v]) == True):
                        if (len(Fir[v]) > 14):
                            i += 1
                            continue
                        Fir[v].append(k)
                        break
                    i += 1


def Dub(ls):
    ls2 = []
    for x in ls:
        sli = x.replace("-", "").split(":")
        s = sli[2]
        ls2.append(s)

    lsun = list(set(ls2))
    if (len(ls2) == len(lsun)):
        return True
    else:
        return False


def DubF(Fir):
    for x in Fir:
        if (Dub(x) == False):
            return False
    return True


BGF = CopyLC(PopultionL[Lbest], Population[best])
while (DubF(BGF) == False):
    YaaaRabee(BGF)

cou = 0
for x in BGF:
    for y in x:
        cou += 1


def TimeStr(x, z):
    if (x % 3 == 0 and z == 1):
        return "8:30 -> 9:45 Am"
    elif (x % 3 == 0 and z == 2):
        return "10:00 -> 11:15 Am"
    elif (x % 3 == 1 and z == 1):
        return "11:25 -> 12:40 Am"
    elif (x % 3 == 1 and z == 2):
        return "12:50 -> 2:05 Pm"
    elif (x % 3 == 2):
        return "2:15 -> 3:30 Pm"
    else:
        return "None"


def TimeStr2(x):
    if (x % 3 == 0):
        return "8:00 -> 10:40 Am"
    elif (x % 3 == 1):
        return "11:25 -> 2:05 Pm"
    elif (x % 3 == 2):
        return "2:15 -> 4:55 Pm"
    else:
        return "None"


Finsh = []


def AddTime(Fir, Fin):
    for x in range(len(Fir)):
        if (x < 3):
            for y in Fir[x]:
                if (y[5] == "1"):
                    y = y.replace(":1:", "")
                    y = y + "-" + "Sat" + "-" + TimeStr2(x)
                    Fin.append(y)
                else:
                    if (y[11] == "1"):
                        z = int(y[11])
                        y = y.replace(":1:", "")
                        y = y + "-" + "Sat" + "-" + TimeStr(x, z)
                        Fin.append(y)
                    else:
                        z = int(y[11])
                        y = y.replace(":2:", "")
                        y = y + "-" + "Sat" + "-" + TimeStr(x, z)
                        Fin.append(y)
        elif (x < 6):
            for y in Fir[x]:
                if (y[5] == "1"):
                    y = y.replace(":1:", "")
                    y = y + "-" + "Mon" + "-" + TimeStr2(x)
                    Fin.append(y)
                else:
                    if (y[11] == "1"):
                        z = int(y[11])
                        y = y.replace(":1:", "")
                        y = y + "-" + "Mon" + "-" + TimeStr(x, z)
                        Fin.append(y)
                    else:
                        z = int(y[11])
                        y = y.replace(":2:", "")
                        y = y + "-" + "Mon" + "-" + TimeStr(x, z)
                        Fin.append(y)
        elif (x < 9):
            for y in Fir[x]:
                if (y[5] == "1"):
                    y = y.replace(":1:", "")
                    y = y + "-" + "Wen" + "-" + TimeStr2(x)
                    Fin.append(y)
                else:
                    if (y[11] == "1"):
                        z = int(y[11])
                        y = y.replace(":1:", "")
                        y = y + "-" + "Wen" + "-" + TimeStr(x, z)
                        Fin.append(y)
                    else:
                        z = int(y[11])
                        y = y.replace(":2:", "")
                        y = y + "-" + "Wen" + "-" + TimeStr(x, z)
                        Fin.append(y)
        elif (x < 12):
            for y in Fir[x]:
                if (y[5] == "1"):
                    y = y.replace(":1:", "")
                    y = y + "-" + "Tue" + "-" + TimeStr2(x)
                    Fin.append(y)
                else:
                    if (y[11] == "1"):
                        z = int(y[11])
                        y = y.replace(":1:", "")
                        y = y + "-" + "Tue" + "-" + TimeStr(x, z)
                        Fin.append(y)
                    else:
                        z = int(y[11])
                        y = y.replace(":2:", "")
                        y = y + "-" + "Tue" + "-" + TimeStr(x, z)
                        Fin.append(y)
        else:
            for y in Fir[x]:
                if (y[5] == "1"):
                    y = y.replace(":1:", "")
                    y = y + "-" + "Thu" + "-" + TimeStr2(x)
                    Fin.append(y)
                else:
                    if (y[11] == "1"):
                        z = int(y[11])
                        y = y.replace(":1:", "")
                        y = y + "-" + "Thu" + "-" + TimeStr(x, z)
                        Fin.append(y)
                    else:
                        z = int(y[11])
                        y = y.replace(":2:", "")
                        y = y + "-" + "Thu" + "-" + TimeStr(x, z)
                        Fin.append(y)


AddTime(BGF, Finsh)


def Save(Fin):
    f2 = open("AI/Table.txt", "w")
    for x in Fin:
        f2.write(x)
        f2.write("." + "\n")


Save(Finsh)


def adba3(s, ls):
    c = 0
    for x in ls:
        if (s == x[:8]):
            c += 1


for x in courls:
    adba3(x.code, Finsh)


def adba333(s, ls):
    c = 0
    for x in ls:
        if (s == x[:8]):
            c += 1
    return c


def tttt2(Cou, Fir):
    for x in Cou:
        o = adba333(x.code, Fir)
        if (o != x.numOFsection * 2):
            return False
    return True


def tttt3(Cou, Fir):
    for x in Cou:
        o = adba333(x.code, Fir)
        if (o != x.numOFsection):
            return False
    return True


import AI.interface
