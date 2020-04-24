X = [0, 1,5, 10, 100]
Y = [32, 33.8, 41, 50, 212]

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
    print(" zap = %.2f" % (zap))
else:
    print("Shos ne to")
"lambda"
