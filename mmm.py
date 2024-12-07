from prettytable import PrettyTable 

n = int(input("Enter number of rows- "));
method = input("Enter what method you want t o")
xi = [];
fi = [];
fixi = [];

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

print("\nMean(x\u0304) = \u03A3FiXi/\u03A3Fi")

print(f"        = {Sfixi} / {Sxi}")
print(f"        = {Sfixi / Sxi}")



