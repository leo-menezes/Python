print('Digite os valores solicitados para saber se poderá ou não, pegar o empréstimo para compra da casa')
vi = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Informe o salário do comprador: R$'))
anos = int(input('Em quantos anos deseja pagar o empréstimo? '))
meses = anos * 12
mensalidade = vi / meses
print('A mensalidade ficará no valor de: {:.2f}R$'.format(mensalidade))
if mensalidade <= salario * 0.3:
    print('Empréstimo Aprovado!')
elif mensalidade > salario * 0.3 and mensalidade <= salario * 0.35:
    print('Em análise!!! Envie o comprovativo de rendimento.')
else:
    print('Empréstimo Negado!!!')