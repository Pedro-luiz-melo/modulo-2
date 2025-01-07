comprimento=int(input("Digite o comprimento:"))
largura =int(input("Digite a largura:"))
preco_m2 = float(input("valor do m2:"))

area = comprimento * largura #m2
preco_total= area * preco_m2

print(f"O terreno possui {area}m2 e custa RS{preco_total}")
