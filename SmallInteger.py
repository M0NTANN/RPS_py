def sub_cycle(xx, schet_povt):
    while schet_povt >= 1:
        xx = xx - 10000
        schet_povt = schet_povt - 1
    return xx



def sub_cycle_2(xx, schet_povt):
    while schet_povt >= 1:
        xx = xx + 10000
        schet_povt = schet_povt - 1
    return xx




class SmallInteger:


    def check(x):
        xx = x
        if xx > 10000 or xx < -10000:
            if (xx > 0):
                schet_povt = int(xx/ 10000)
                if (schet_povt % 2  == 0):
                    xx = sub_cycle(xx, schet_povt)
                    xx = (10000 - xx)
                    return xx
                elif (schet_povt % 2 != 0):
                    xx = sub_cycle(xx, schet_povt)
                    xx = (10000 - xx) * -1
                return xx
            if xx < 0:
                schet_povt = int((xx * -1) / 10000)
                if (schet_povt % 2  == 0):
                    xx = sub_cycle_2(xx, schet_povt)
                    xx = (10000 + xx) * -1
                    return xx
                elif (schet_povt % 2 != 0):
                    xx = sub_cycle_2(xx, schet_povt);
                    xx = (10000 + xx)
                    return xx
        return xx

def sum(x, y):
    xx = SmallInteger.check(int(x))
    yy = SmallInteger.check(int(y))
    s = xx + yy
    return s

def sub(x, y):
    xx = SmallInteger.check(int(x))
    yy = SmallInteger.check(int(y))
    s = xx - yy
    return s

def mul(x, y):
    xx = SmallInteger.check(int(x))
    yy = SmallInteger.check(int(y))
    s = xx / yy
    return s

def div(x, y):
    xx = SmallInteger.check(int(x))
    yy = SmallInteger.check(int(y))
    s = xx % yy
    return s

