
![Logo](https://forza.pro.br/wp-content/uploads/2019/12/problema-ou-desafio-min.jpg)


# Desafio DIO

## Otimizando o Sistema Bancário 

Utilizando nosso código anterior, iremos deixá-lo mais modularizado criando funções para as operações existentes (sacar, depositar e visualizar extrato) e adicionando duas novas, sendo elas:
- criar usuário (cliente do banco)
- criar conta corrente (vincular com usuário)
Fique a vontade para adicionar mais funções, exemplo: listar contas, inativar contas, etc.

## Separação em funções
Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida como achar melhor.

### Saque
Deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
Sugestão de retorno: saldo e extrato.

### Depósito

A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor e extrato.
Sugestão de retorno: saldo e extrato

### Extrato
A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo. Argumentos nomeados: extrato.

### Criar usuário (cliente)
O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço.
O endereço é uma string com formato de: logradouro, número, bairro, cidade/sigla do estado. 
O CPF é único e deve ser armazenado apenas os números.

### Criar conta corrente (vincular com o usuário)
O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. 
O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário.

### Dica
Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.

## Autor

- [@CruzFabio](https://github.com/CruzFabio)

