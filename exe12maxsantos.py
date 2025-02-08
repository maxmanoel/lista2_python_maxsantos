#Escreva um programa que pergunta o valor total da conta e em seguida pergunte quantos clientes existem,divida conta pelos clientes e exiba o quaanto cada cliente deve pagar seguida da mensagem "cada cliente deve pagar :" 
n1=float(input("Dgite o valor da fatura:"))
n2=float(input("Digite quantidade de clientes"))
conta = n1/n2
print("cada cliente deve pagar", conta)