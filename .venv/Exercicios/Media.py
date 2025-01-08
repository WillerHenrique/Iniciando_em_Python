notaA = float(input("Informe a primeira nota: "))
notaB = float(input("Informe a segunda nota: "))

mediaFinal = (notaA + notaB) / 2

if mediaFinal >= 7.0:
    print("A Média: %.1f - Aprovado" % mediaFinal)
else:
    print("A Média: %.1f - Reprovado" % mediaFinal)