import os


def carregar_partidos_e_coligacoes(nome_do_arquivo):
    coligacoes = []
    arquivo = open(nome_do_arquivo)

    for linha in arquivo:
        dados = linha.strip()
        coligacao = {
            "coligacao": dados,
            "total_votos": 0,
            "qtd_vagas": 0,
            "votos_sobra_total": 0,
        }

        coligacoes.append(coligacao)

    return coligacoes


def carregar_partidos_e_votos(nome_do_arquivo):
    candidatos = []
    arquivo = open(nome_do_arquivo)

    for linha in arquivo:
        dados = linha.strip().split(";")
        candidato = {
            "nome": dados[0].title(),
            "numero": dados[1],
            "partido": dados[2].title(),
            "coligacao": dados[3],
            "total_votos": int(dados[4]),
        }
        candidatos.append(candidato)
        ordenar_caditados = sorted(
            candidatos, key=lambda c: c["total_votos"], reverse=True
        )
        candidatos = ordenar_caditados

    return candidatos


def listar_candidatos(candidatos):
    for i, candidato in enumerate(candidatos, 1):
        resultado = f"""
        {i}. Nome: {candidato['nome']} 
        Número: {candidato['numero']} 
        Partido: {candidato['partido']} 
        Coligação: {candidato['coligacao']} 
        Total de Votos: {candidato['total_votos']}
        """
        print(resultado)


def somatorio(canditados, votos):
    return sum(item[votos] for item in canditados)


def soma(canditados):
    total = 0
    for candidato in canditados:
        total += candidato["total_votos"]
    return total


def quociente_eleitoral(somatorio, qtd_vagas):
    qe = somatorio // qtd_vagas
    return qe


def total_votos_coligacao(coligacoes, candidatos):
    for candidato in candidatos:
        for coligacao in coligacoes:
            if coligacao["coligacao"] == candidato["coligacao"]:
                coligacao["total_votos"] += candidato["total_votos"]


def mostrar_votos_por_coligacao(coligacoes, candidatos):
    total_votos_coligacao(coligacoes, candidatos)

    for coligacao in coligacoes:
        print(
            f"Coligação: {coligacao['coligacao']} \nTotal de Votos: {coligacao['total_votos']}\n"
        )


def quociente_partidario(coligacoes, qe, qtd_vagas):
    qtd_vagas_ocupadas = 0

    for coligacao in coligacoes:
        qp = coligacao["total_votos"] // qe
        coligacao["qtd_vagas"] += qp
        qtd_vagas_ocupadas += qp
        qtd_vagas -= qp
        coligacao["votos_sobra_total"] += coligacao["total_votos"] % qe

    return qtd_vagas_ocupadas, qtd_vagas


def mostrar_quociente_partidario(coligacoes, candidatos, qe, qtd_vagas):

    total_votos_coligacao(coligacoes, candidatos)
    vagas_ocupadas, vagas_restantes = quociente_partidario(coligacoes, qe, qtd_vagas)

    ordenar = sorted(coligacoes, key=lambda c: c["qtd_vagas"], reverse=True)
    for coligacao in ordenar:
        print(
            f"Coligação: {coligacao['coligacao']} \nQtd de Vagas: {coligacao['qtd_vagas']}"
        )
        print(f"Qtd de Votos Sobrando: {coligacao['votos_sobra_total']} \n")

    print(
        f"\nQtd de Vagas Ocupadas: {vagas_ocupadas} \nQtd de Vagas Restantes: {vagas_restantes}"
    )


def distribuir_vaga_por_media(coligacoes, qtd_vagas, mostrar=False):
    contador = 1
    while qtd_vagas != 0:
        if mostrar:
            print(f"{contador}ª MÉDIA".center(60, "="))
            print(f"{'Partido/Coligaçao':<25} {'Cálculo':<25} {'Média':>10}")
            print("-" * 62)

            for coligacao in coligacoes:
                votos = coligacao["total_votos"]
                vagas = coligacao["qtd_vagas"]
                media = votos / (vagas + 1)
                print(
                    f"{coligacao['coligacao']:<25} {f'{votos} / ({vagas}+1)':<25} {media:>10.2f}"
                )
        maior_media = reduzir(coligacoes, obter_max, coligacoes[0])
        media = maior_media["total_votos"] / (maior_media["qtd_vagas"] + 1)

        if mostrar:
            print("-" * 62)
            print(f"==> Maior média: {maior_media['coligacao']} com {media:.2f}")
            print(f"Nova qtd de Vagas: {maior_media['qtd_vagas'] + 1}")
            input("Enter para continuar")
            limpar_tela()

        maior_media["qtd_vagas"] += 1
        qtd_vagas -= 1
        contador += 1
        if mostrar:
            print("TABELA FINAL DE VAGAS POR COLIGAÇÃO".center(62, "="))
            print(f"{'Coligação':<25} {'Total de Vagas':>25}")
            print("-" * 62)
            for coligacao in coligacoes:
             print(f"{coligacao['coligacao']:<30} {coligacao['qtd_vagas']:>30}")

    return coligacoes


def mostrar_vagas_distribuidas_por_media(coligacoes, candidatos, qe, qtd_vagas):
    total_votos_coligacao(coligacoes, candidatos)
    vagas_ocupadas, vagas_restantes = quociente_partidario(coligacoes, qe, qtd_vagas)
    distribuir_vaga_por_media(coligacoes, vagas_restantes, mostrar=True)


def caditados_eleitos(coligacoes, candidatos):

    for coligacao in coligacoes:
        candidato_da_coligacao = filtrar(
            candidatos, lambda c: c["coligacao"] == coligacao["coligacao"]
        )
        print(f"\nColigação: {coligacao['coligacao']}\nEleitos:")
        candidatos_ordenados = sorted(
            candidato_da_coligacao, key=lambda c: c["total_votos"], reverse=True
        )

        houve_eleito = False
        for vagas in range(coligacao["qtd_vagas"]):
            if vagas < len(candidatos_ordenados):
                print(
                    f"- {candidatos_ordenados[vagas]['nome']} ({candidatos_ordenados[vagas]['total_votos']} votos)"
                )
                houve_eleito = True
        if not houve_eleito:
            print("-Nenhum Eleito")


def mostrar_candidatos_eleitos(coligacoes, candidatos, qe, qtd_vagas):
    total_votos_coligacao(coligacoes, candidatos)
    vagas_ocupadas, vagas_restantes = quociente_partidario(coligacoes, qe, qtd_vagas)
    distribuir_vaga_por_media(coligacoes, vagas_restantes, mostrar=False)
    caditados_eleitos(coligacoes, candidatos)


def eleitos_no_sistema_majoritario(candidatos, qtd_vagas):
    for i, candidato in enumerate(candidatos, 1):
        if qtd_vagas != 0:
            print(
                f"{i}. \nCandidato Eleito: {candidato['nome']} \nColigação: {candidato['coligacao']}\nQtd de Votos: {candidato['total_votos']}\n"
            )
            qtd_vagas -= 1


def filtrar(colecao, criterio):
    nova_colecao = []

    for item in colecao:
        if criterio(item):
            nova_colecao.append(item)

    return nova_colecao


def reduzir(colecao, redutora, inicial):
    acumulado = inicial
    for item in colecao:
        acumulado = redutora(acumulado, item)

    return acumulado


def obter_max(v1, v2):
    m1 = v1["total_votos"] / (v1["qtd_vagas"] + 1)
    m2 = v2["total_votos"] / (v2["qtd_vagas"] + 1)
    return v1 if m1 > m2 else v2


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
