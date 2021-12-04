def mostralinha():  # Função sem parâmetro
    print('-' * 30)


def mensagem(msg):  # Função com parâmetro
    print('-' * 30)
    print(msg)
    print('-' * 30)


mostralinha()
print(f'{"CURSO EM VÍDEO":^30}')
mostralinha()
print(f'{"APRENDA PYTHON":^30}')
mostralinha()
print(f'{"GUSTAVO GUANABARA":^30}')
mostralinha()

mensagem(f'{"CURSO EM VÍDEO":^30}')
mensagem(f'{"APRENDA PYTHON":^30}')
mensagem(f'{"GUSTAVO GUANABARA":^30}')
