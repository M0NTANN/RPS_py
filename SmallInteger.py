from xmlrpc.server import SimpleXMLRPCServer
import re


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


def check(x):
    xx = x
    if xx > 10000 or xx < -10000:
        if (xx > 0):
            schet_povt = int(xx / 10000)
            if (schet_povt % 2 == 0):
                xx = sub_cycle(xx, schet_povt)
                xx = (10000 - xx)
                return xx
            elif (schet_povt % 2 != 0):
                xx = sub_cycle(xx, schet_povt)
                xx = (10000 - xx) * -1
            return xx
        if xx < 0:
            schet_povt = int((xx * -1) / 10000)
            if (schet_povt % 2 == 0):
                xx = sub_cycle_2(xx, schet_povt)
                xx = (10000 + xx) * -1
                return xx
            elif (schet_povt % 2 != 0):
                xx = sub_cycle_2(xx, schet_povt);
                xx = (10000 + xx)
                return xx
    return xx


def sum(x, y):
    print(x)
    print(y)
    xx = check(int(x))
    yy = check(int(y))
    s = xx + yy
    return s


def sub(x, y):
    xx = check(int(x))
    yy = check(int(y))
    s = xx - yy
    return s


def mul(x, y):
    xx = check(int(x))
    yy = check(int(y))
    s = xx / yy
    return s


def div(x, y):
    xx = check(int(x))
    yy = check(int(y))
    s = xx % yy
    return s




server = SimpleXMLRPCServer(("localhost", 8000))
print("Listen on port 8000...")
server.register_function(sum, "sum")
server.register_function(sub, "sub")
server.register_function(div, "div")
server.register_function(mul, "mul")

server.serve_forever()
