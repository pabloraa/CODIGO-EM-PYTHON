def cubo(num):
    for i in vetor:
        print(i**3)
vetor = []
for i in range(0,3):
    x = int(input("Digite três elementos"))
    vetor.append(x)
print(vetor)
print(cubo(vetor))
