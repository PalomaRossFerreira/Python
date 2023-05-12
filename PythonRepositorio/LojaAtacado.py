print('Seja bem vindo(a) a loja de atacado')
#Entrada do valor do produto
valor_produto = float(input('Entre com o valor do produto: '))
#Entrada da quantidade do produto
qntd_produto = int(input('Entre com a quantidade de produtos: '))

#5% de desconto
if qntd_produto >= 10 and qntd_produto <=99:
  desconto = 5
  valor_subtotal = valor_produto * qntd_produto
  valor_final = valor_subtotal - (valor_subtotal * (desconto/100))

#10% de desconto
elif qntd_produto >= 100 and qntd_produto <= 999:
  desconto = 10
  valor_subtotal = valor_produto * qntd_produto
  valor_final = valor_subtotal - (valor_subtotal * (desconto/100))

#15% de desconto
elif qntd_produto >= 1000:
  desconto = 15
  valor_subtotal = valor_produto * qntd_produto
  valor_final = valor_subtotal - (valor_subtotal * (desconto/100))

#Sem desconto (apenas quantidades menores que 10)
else:
  desconto = 0
  valor_subtotal = valor_produto * qntd_produto
  valor_final = valor_subtotal

print('O valor sem desconto foi: R$ {:.2f}'.format(valor_subtotal))
print('O valor com desconto foi: R$ {:.2f}. O desconto foi de {}%'.format(valor_final, desconto))