# Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. 
# O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para 
# cada exemplar adicional. Qual é o custo total de atacado para 60 cópias.

quantidade = int(input("Quantos livros quer comprar: "))

livro = 24.95
desconto = 40/100

livro_desconto = livro - desconto * livro
preco_total = quantidade * livro_desconto

valor_frete = 3 + 0.75 * (quantidade - 1)

valor_total = preco_total + valor_frete

print(f"O valor total é de R${valor_total} sendo R${preco_total} de livro e R${valor_frete} de transporte.")