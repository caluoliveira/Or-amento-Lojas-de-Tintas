# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 5 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
area=float(input("Informe a metragem da área a ser pintada: \n"))
qtd_litros=float(area/3)
preço_tinta=float(qtd_litros*4.44)
qtd_lata=float(area/54)
print ("Ao final, você utilizará " "%.2f" % qtd_litros, "litros de tinta ou", "%.2f" % qtd_lata, "latas de 18 litros. Cada litro lhe custará R$", "%.2f" % preço_tinta,"reais.")