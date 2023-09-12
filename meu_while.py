termina = 30
comeca = 0

def condicao_while():
    # coloque a condição do seu while aqui

    # minha ideia de iteração em um while

    global comeca
    return comeca < termina  # retorna um bool


def corpo_while():
    # coloque o código do seu while aqui

    global comeca

    # iterando
    comeca += 1
    print(comeca)


def while_sem_while(corpo_while, condicao_while):
    
    if condicao_while():  # enquanto ela for True

        corpo_while()
        while_sem_while(corpo_while, condicao_while)
    
    
while_sem_while(corpo_while, condicao_while)
