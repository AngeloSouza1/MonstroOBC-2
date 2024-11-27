def criar_monstro(nome, tipo, forca, habilidade):
    """
    Retorna uma descrição formatada do monstro com os dados fornecidos.
    """
    if not nome or not tipo or not habilidade:
        return "Erro: Todos os campos devem ser preenchidos!"
    if not forca.isdigit() or not (1 <= int(forca) <= 100):
        return "Erro: Nível de força deve ser um número entre 1 e 100."
    
    return f"O monstro {nome} é um {tipo} de nível {forca} e possui a habilidade especial: {habilidade}."
