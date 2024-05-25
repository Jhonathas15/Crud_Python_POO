from classes import Cliente

# Instanciando um novo cliente

clientes = Cliente()

# Cadastrando novos clientes no banco

clientes.cadastrar_cliente(input('Nome: '), input('Email: '), input('Senha: '))

# Listando clientes cadastrados ou cliente especifico 

clientes.ver_clientes(input('Campo: '))

# Editando cliente

clientes.atualizar_cliente(input('campo: '), input('valor: '), int(input('id: ')))

# Deletando Cliente

clientes.deletar_cliente(int(input('id: ')))