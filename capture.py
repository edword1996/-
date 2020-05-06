
import argparse

a = open('data.txt')

X = a.readline().split()
X = [float(x) for x in X]

Y = a.readline().split()
Y = [float(y) for y in Y]

print(X)
print(Y)
a.close()

parser = argparse.ArgumentParser()
parser.add_argument('x', metavar='x', type=float, nargs='+',
                    help='input number')
i = 0
K = []#пустые массивы
B = []# K и В это то что я буду искать по формуле

while i != len(X) - 1:
    k = (Y[i] - Y[i + 1]) / (X[i] - X[i + 1])# этот блок считает уравнение и добавлет K и В после каждого уравнения, находим зависимость
    b = Y[i] - k * X[i]
    i = i + 1
    K.append(k)
    B.append(b)


n = 0
m = 0
i = 0

while i != len(K) - 1:
    if K[i] == K[i + 1]:
        n = 1
    else:
        n = 0
    if B[i] == B[i + 1]:#делаем равеньство всех элементов
        m = 1           # коеф K и В были равны
    else:
        m = 0
    i = i + 1


if n == 1 and m == 1:
    print("Введите х:")
    x = float(input("\tx = "))
    y = lambda x:K[0] * x + B[0]
    zap=y(x)
    print(" otvet = %.2f" % (zap))
else:
    print("Shos ne to")


args = parser.parse_args()
answer = args[(input("\tx = "))]
print (args)

x = args.x
print (" otvet = %.2f" % (zap))



parser = argparse.ArgumentParser()
parser.add_argument("-f", type=argparse.FileType())
args = parser.parse_args(["-f", "data.txt"])


#print (args.f.read())


