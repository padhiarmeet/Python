from prettytable import PrettyTable 

n = int(input("Enter number of rows- "));
method = int(input("Enter number of what method you want to do \n1]Direct Method\n2]Assumed Mean Method\n3]Step Division Method\n"))
xi = []
fi = []
fixi = []
di = []
fidi = []
fiui = []
ui = []
clas = []
Sfi = 0
Sfidi = 0
parts = []

if method == 1:
    
    for i in range(0,n):
        xi.append(int(input(f"Enter xi for {i} element - ")))
        fi.append(int(input(f"Enter fi for {i} element - ")))
        fixi.append(xi[i] * fi[i])

        print("\n");


    Sxi = sum(xi)
    Sfi = sum(fi)
    Sfixi = sum(fixi)

    myTable = PrettyTable(['Xi','Fi','FiXi'])

    for i in range(0,n):
        myTable.add_row([xi[i],fi[i],fixi[i]])

    myTable.add_row([" ",f"\u03A3Fi = {Sfi}",f"\u03A3FiXi = {Sfixi}"])
    print(myTable)

    print("\nMean(x\u0304) = \u03A3FiXi / \u03A3Fi")

    print(f"        = {Sfixi} / {Sfi}")
    print(f"        = {Sfixi / Sfi}")


elif method == 2:

    for i in range(0,n):
        clas.append(input(f"Enter xi for {i} element - "))
        fi.append(int(input(f"Enter fi for {i} element - ")))
        parts = clas[i].split('-');
        xi.append((int(parts[0]) + int(parts[1])) / 2)
        print("\n")

    a = xi[int((n/2)-1)];

    for i in range(0,n):
        di.append(int(xi[i] - a));
        fidi.append(fi[i] * di[i])
    
    Sfidi = sum(fidi)
    Sfi = sum(fi)

    myTable = PrettyTable(['class','Fi','Xi','di','Fidi'])

    for i in range(0,n):

        if i == a:
            myTable.add_row([clas[i],fi[i],f"{xi[i]} = A",di[i],fidi[i]])
        else:
            myTable.add_row([clas[i],fi[i],xi[i],di[i],fidi[i]])

    myTable.add_row([" ",f"\u03A3Fi = {Sfi}"," "," ",f"\u03A3Fidi = {Sfidi}"])
    print(myTable)

    print("\nMean(x\u0304) = A + \u03A3Fidi / \u03A3Fi")

    print(f"        = A + {Sfidi} / {Sfi}")
    print(f"        = {a + (Sfidi / Sfi)}")
    
elif method == 3:

    for i in range(0,n):
        clas.append(input(f"Enter xi for {i} element - "))
        fi.append(int(input(f"Enter fi for {i} element - ")))
        parts = clas[i].split('-');
        xi.append((int(parts[0]) + int(parts[1])) / 2)
        print("\n")

    a = xi[int((n/2)-1)]
    c = int(parts[0]) + int(parts[1])

    for i in range(0,n):
        ui.append((xi[i] - a) / c);
        fiui.append(fi[i] * ui[i])
    
    Sfiui = sum(fiui)
    Sfi = sum(fi)

    myTable = PrettyTable(['class','Fi','Xi','ui','Fiui'])

    for i in range(0,n):

        if i == a:
            myTable.add_row([clas[i],fi[i],f"{xi[i]} = A",ui[i],fiui[i]])
        else:
            myTable.add_row([clas[i],fi[i],xi[i],ui[i],fiui[i]])

    myTable.add_row([" ",f"\u03A3Fi = {Sfi}"," "," ",f"\u03A3fiui = {Sfiui}"])
    print(myTable)

    print("\nMean(x\u0304) = A + (\u03A3fiui / \u03A3Fi) * C")

    print(f"        = A + ({Sfiui} / {Sfi}) * {c}")
    print(f"        = {a + (Sfiui / Sfi) * c}")