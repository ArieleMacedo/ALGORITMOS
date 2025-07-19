def carregar_arquivo(nome_do_arquivo):
    escolas = []
    arquivo = open(nome_do_arquivo, encoding="utf-8-sig")

    for linha in arquivo:
        linha = linha.replace("M�dio", "Médio")
        linha = linha.replace("informa��o", "Informação")
        dados = linha.strip().split(";")
        escola = {}
        escola["nome"] = dados[1]
        escola["municipio"] = dados[2]
        escola["uf"] = dados[3]
        escola["rede"] = dados[4]
        escola["permanencia"] = dados[5]
        escola["nivel_socio_economico"] = dados[6].strip().capitalize()
        escola["media_objetivas"] = float(dados[7].replace(",", "."))
        escola["matematica"] = float(dados[8].replace(",", "."))
        escola["linguagens"] = float(dados[9].replace(",", "."))
        escola["ciencias_natureza"] = float(dados[10].replace(",", "."))
        escola["humanas"] = float(dados[11].replace(",", "."))
        escola["redacao"] = float(dados[12].replace(",", "."))

        escolas.append(escola)

    return escolas


def listar_dados(escolas):

    for escola in escolas:
        resultado = f"""
        Nome: {escola['nome']} - Municipio: {escola['municipio']} - UF: {escola['uf']} -
        Rede: {escola['rede']} - Permanência: {escola['permanencia']} - Nível Sócio Econômico: {escola['nivel_socio_economico']} -
        Média(Objetivas): {escola['media_objetivas']} - Matemática: {escola['matematica']} - Linguagens: {escola['linguagens']} -
        Ciências da natureza: {escola['ciencias_natureza']} - Humanas: {escola['humanas']} - Redação: {escola['redacao']}
        """
        print(resultado)

    print(100 * "=")


def n_todas_as_areas(escolas, nota1, nota2, n):

    ordenar = sorted(escolas, key=lambda e: media(e[nota1], e[nota2]), reverse=True)

    top = ordenar[:n]

    for i, escola in enumerate(top):
        media_escola = media(escola[nota1], escola[nota2])
        print(f"{i+1}º - {escola['nome']} ({escola['uf']}) - Média: {media_escola:.2f}")


def top_n_escolas(escolas, area, n):
    ordenadas = sorted(escolas, key=lambda escola: escola[area], reverse=True)

    top_escolas = ordenadas[:n]

    for i, escola in enumerate(top_escolas):
        print(f"{i+1}º - {escola['nome']} ({escola['uf']}) - Nota: {escola[area]}")


def ordenar_estado_por_nota(escolas, area, uf, n):

    estado = filtrar(escolas, lambda e: e["uf"] == uf)

    ordenar = sorted(estado, key=lambda escola: escola[area], reverse=True)
    top_escolas = ordenar[:n]

    for i, escola in enumerate(top_escolas):
        print(f"{i+1}º - {escola['nome']} ({escola['uf']}) - Nota: {escola[area]}")


def media_por_area(escolas, area):
    qtd = qtd_notas(escolas)
    if qtd == 0:
        print("Não é possivel calcular a média.")
        return 0.0

    soma = somatorio_por_area(escolas, area)
    media = soma / qtd

    return media


def melhor_escola(escolas, area, uf):

    melhor_estado = filtrar(escolas, lambda e: e["uf"] == uf)
    melhor = reduzir(
        melhor_estado[1:], lambda e1, e2: obter_max(e1, e2, area), melhor_estado[0]
    )
    print(f"A melhor escola do estado {uf} é o {melhor['nome']}, com média de {melhor[area]} em {area}")


def ordenar_renda(escolas):
    ordem_nivel = {
        "Sem informação": 1,
        "Muito baixo": 2,
        "Baixo": 3,
        "Médio baixo": 4,
        "Médio": 5,
        "Médio alto": 6,
        "Alto": 7,
        "Muito alto": 8,
    }

    ordenar = sorted(
        escolas, key=lambda e: ordem_nivel[e["nivel_socio_economico"]], reverse=True
    )

    return ordenar


def ordenar_por_renda_estado(escolas, uf):
    por_renda_estado = filtrar(escolas, lambda e: e["uf"] == uf)
    ordenar = ordenar_renda(por_renda_estado)
    lista_ordenada = listar_dados(ordenar)

    return lista_ordenada


def estado_com_maior_media(escolas, area):
    ufs_unicas = []
    for escola in escolas:
        if escola["uf"] in ufs_unicas:
            continue
        else:
            ufs_unicas.append(escola["uf"])
    media_estado = []
    for uf in ufs_unicas:
        agrupar_escola = filtrar(escolas, lambda e: e["uf"] == uf)
        filtrar_media = media_por_area(agrupar_escola, area)
        media_estado.append({"uf": uf, "media": filtrar_media})

    maior_media = reduzir(
        media_estado, lambda e1, e2: obter_max(e1, e2, "media"), media_estado[0]
    )

    return maior_media["uf"], maior_media["media"]


def media_maior_que(escolas, valor, area):
    for escola in escolas:
        if escola[area] >= valor:
            print(f"{escola['nome']}, tem média {escola[area]}")


def escola_com_maior_nota_nivel(escolas, area):
    nivel = []
    for escola in escolas:
        if escola["nivel_socio_economico"] in nivel:
            continue
        else:
            nivel.append(escola["nivel_socio_economico"])
    nota = []
    for nivel_socio_economico in nivel:
        agrupar = filtrar(
            escolas, lambda e: e["nivel_socio_economico"] == nivel_socio_economico
        )
        maior_nota = reduzir(
            agrupar, lambda e1, e2: obter_max(e1, e2, area), agrupar[0]
        )
        nota.append(
            {
                "escola": maior_nota["nome"],
                "nivel_socio_economico": nivel_socio_economico,
                "nota": maior_nota[area],
            }
        )

    return nota


def contem_caracter(escolas, caracter):
    contador = 1
    encontrou = False
    
    for escola in escolas:
        if escola["nome"][0].upper() == caracter.upper():
            print(f"{contador}°: {escola['nome']}")
            contador +=1
            encontrou = True
            
    if not encontrou:
        print("Escola não encontrada")


def mapear(escolas, funcao_transformadora):
    nova_escolas = []

    for item in escolas:
        item_transformado = funcao_transformadora(item)
        nova_escolas.append(item_transformado)

    return nova_escolas


def filtrar(escolas, criterio):
    nova_escolas = []

    for item in escolas:
        if criterio(item):
            nova_escolas.append(item)

    return nova_escolas


def reduzir(escolas, redutora, inicial):
    acumulado = inicial

    for item in escolas:
        acumulado = redutora(acumulado, item)

    return acumulado


def por_estado(escolas, uf):
    nova_escolas = []

    for escola in escolas:
        if escola["uf"] == uf:
            nova_escolas.append(escola)

    return nova_escolas


def por_municipio(escolas, municipio):
    nova_escolas = []

    for escola in escolas:
        if escola["municipio"] == municipio:
            nova_escolas.append(escola)

    return nova_escolas


def por_rede(escolas, rede):
    nova_escolas = []

    for escola in escolas:
        if escola["rede"] == rede:
            nova_escolas.append(escola)

    return nova_escolas


def somatorio_por_area(escolas, area):
    return sum(item[area] for item in escolas)


def qtd_notas(escolas):
    return len(escolas)


def obter_max(v1, v2, variavel):
    return v1 if v1[variavel] > v2[variavel] else v2


def media(n1, n2):
    return (somar(n1, n2)) / 2


def somar(a1, a2):
    return a1 + a2
