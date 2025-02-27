#entrada de dados
#genero
#idade
#tempo de serviço
genero = input()
idade = int(input())
tempo = int(input())
           
#processamento
#A: para mulheres ter mais de 60 anos. Para homens, 65.
#B: ou ter trabalhado mais de 30 anos 
#C: ou ter 60 anos e trabalhado 60

A = (genero == 'f' and idade >= 60) or \
    (genero == 'm' and idade >= 65)
B = tempo > 30
C = idade >= 60 and tempo >= 25

pode_aposentar = A or B or C

#saida
print(A, B, C, pode_aposentar)
