import visualgo.flow_control.test_flow_control as vfc 

def test_class_1():
    print("PROGRAM TEST :\n")
    slt = vfc.program()
    slt.k = 2
    print(slt.k)
    slt.f = 1
    slt.f += slt.k
    print(slt.f)
    slt.l = [8, 5, 6]
    slt.l *= slt.f
    print(slt.l)
    print("#=======================================================================================================#")
    return 0

def test_class_2():
    print("PROGRAM2 TEST :\n")
    prog = """
k = 1
j = 2
n = j + k
print(n)
def f(x):
    print(x + 1000)
f(n)
    """
    test = vfc.program2(prog)
    test.run()
    #test.execute_line_by_line()
    print("#=======================================================================================================#")
    return 0

def test_class_4():
    prog = """
x <- 5
k <- x
print(x)"""
    print("PROGRAM4 TEST :", prog, "\n")
    test = vfc.program4(prog)
    test.run()
    prog2="""
def f(x):
    print(x)
    x <- 8
f(x)
    """
    # WARNING : error when calling the following function on x : (g is defined after f)
    # def g(x):
    #     x += 5
    #     f(x)
    # name 'f' is not defined -> why ?
    test2 = vfc.program4(prog2)
    test2.run()
    #need to keep in mind all \t (tabs) for block indent
    print("#=======================================================================================================#")

def test_class_3():
    print("PROGRAM3 TEST :\n")
    test = vfc.program3()
    test.x = 5
    print("access test.x.value :", test.x)
    test.k = 4
    test.k = test.k + test.x
    print("k = k + x :", test.k)
    test.k.debug()
    test.k = test.k * test.x
    print("k = k * x :", test.k)
    test.k.debug()
    test.debug()
    # Breakpoint
    #   python debugger (pdb library) breakpoint
    #   pause() or wait_input()

    # Pseudo-code
    #   compilator -> compile from string to string / blocks are indented

if __name__ == "__main__":
    test_class_1()
    test_class_2()
    test_class_4()
    test_class_3()
