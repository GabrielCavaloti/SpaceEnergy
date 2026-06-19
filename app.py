import random
from datetime import datetime


historico = []


def ler_numero(mensagem, valor_minimo=None, valor_maximo=None):
    while True:
        try:
            valor = float(input(mensagem).replace(",", ".").strip())

            if valor_minimo is not None and valor < valor_minimo:
                print("O valor mínimo permitido é " + str(valor_minimo) + ".")
            elif valor_maximo is not None and valor > valor_maximo:
                print("O valor máximo permitido é " + str(valor_maximo) + ".")
            else:
                return valor
        except ValueError:
            print("Entrada invalida. Digite um numero.")


def ler_comunicacao():
    while True:
        comunicacao = input("Comunicação ativa? Digite 1 para sim ou 0 para não: ")

        if comunicacao == "0" or comunicacao == "1":
            return int(comunicacao)

        print("Opção inválida. Digite somente 1 ou 0.")


def ler_status():
    while True:
        status = input("Status do módulo (operacional, atenção ou falha): ").lower()

        if status == "operacional" or status == "atencao" or status == "falha":
            return status

        print("Status inválido. Digite operacional, atenção ou falha.")


def calcular_risco(dados):
    risco = 0
    alertas = []
    acoes = []

    saldo_potencia = dados["potencia_gerada"] - dados["potencia_consumida"]

    if dados["temperatura"] > 80:
        risco = risco + 30
        alertas.append("Temperatura crítica detectada.")
        acoes.append("Ativar o sistema de resfriamento do módulo.")
    elif dados["temperatura"] > 60:
        risco = risco + 15
        alertas.append("Temperatura acima do ideal.")
        acoes.append("Reduzir a carga de processamento do módulo.")

    if dados["energia"] < 20:
        risco = risco + 30
        alertas.append("Nível da bateria muito baixo.")
        acoes.append("Ativar o modo de economia de energia.")
    elif dados["energia"] < 40:
        risco = risco + 15
        alertas.append("Energia abaixo do recomendado.")
        acoes.append("Priorizar o fornecimento aos módulos essenciais.")

    if dados["comunicacao"] == 0:
        risco = risco + 25
        alertas.append("Falha na comunicação com a base.")
        acoes.append("Tentar a reconexão automática com a central.")

    if saldo_potencia < 0:
        risco = risco + 20
        alertas.append("O consumo é maior que a potência solar gerada.")
        acoes.append("Reduzir cargas não essenciais e redirecionar os painéis solares.")

    if dados["status_modulo"] == "atencao":
        risco = risco + 10
        alertas.append("Módulo operando em estado de atenção.")
        acoes.append("Executar uma verificação preventiva no módulo.")
    elif dados["status_modulo"] == "falha":
        risco = risco + 25
        alertas.append("Falha operacional no módulo.")
        acoes.append("Isolar o módulo e iniciar o protocolo de manutenção.")

    if risco <= 25:
        nivel = "BAIXO"
    elif risco <= 50:
        nivel = "MODERADO"
    elif risco <= 75:
        nivel = "ALTO"
    else:
        nivel = "CRÍTICO"

    return risco, nivel, alertas, acoes


def completar_analise(dados):
    risco, nivel, alertas, acoes = calcular_risco(dados)

    dados["risco"] = risco
    dados["nivel"] = nivel
    dados["alertas"] = alertas
    dados["acoes"] = acoes

    historico.append(dados)
    return dados


def inserir_dados():
    print("\n--- INSERIR DADOS DA MISSÃO ---")

    modulo = input("Nome do modulo: ").strip()
    while modulo == "":
        print("O nome do modulo nao pode ficar vazio.")
        modulo = input("Nome do modulo: ").strip()

    dados = {
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "modulo": modulo,
        "temperatura": ler_numero("Temperatura do módulo em °C: ", -100, 150),
        "energia": ler_numero("Nível da bateria de 0 a 100%: ", 0, 100),
        "comunicacao": ler_comunicacao(),
        "potencia_gerada": ler_numero("Potencia solar gerada em kW: ", 0),
        "potencia_consumida": ler_numero("Potencia consumida em kW: ", 0),
        "status_modulo": ler_status()
    }

    completar_analise(dados)
    print("\nDados cadastrados e analisados com sucesso.")
    exibir_dados(dados)


def gerar_dados_simulados():
    modulos = [
        "Habitação",
        "Comunicacao",
        "Laboratorio",
        "Painéis Solares",
        "Suporte de Vida"
    ]
    status_possiveis = ["operacional", "operacional", "atencao", "falha"]

    dados = {
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "modulo": random.choice(modulos),
        "temperatura": random.randint(10, 100),
        "energia": random.randint(5, 100),
        "comunicacao": random.choice([0, 1, 1]),
        "potencia_gerada": round(random.uniform(2, 15), 2),
        "potencia_consumida": round(random.uniform(3, 18), 2),
        "status_modulo": random.choice(status_possiveis)
    }

    completar_analise(dados)
    print("\nDados simulados gerados e analisados com sucesso.")
    exibir_dados(dados)


def exibir_dados(dados):
    saldo = dados["potencia_gerada"] - dados["potencia_consumida"]

    if dados["potencia_consumida"] > 0:
        cobertura_solar = dados["potencia_gerada"] / dados["potencia_consumida"] * 100
    else:
        cobertura_solar = 100

    if dados["comunicacao"] == 1:
        texto_comunicacao = "ATIVA"
    else:
        texto_comunicacao = "FALHA"

    print("\n" + "=" * 58)
    print("STATUS ENERGÉTICO DA MISSÃO")
    print("=" * 58)
    print("Data e hora: " + dados["data"])
    print("Módulo: " + dados["modulo"])
    print("Temperatura: " + format(dados["temperatura"], ".1f") + " °C")
    print("Bateria: " + format(dados["energia"], ".1f") + "%")
    print("Comunicação: " + texto_comunicacao)
    print("Potência solar gerada: " + format(dados["potencia_gerada"], ".2f") + " kW")
    print("Potência consumida: " + format(dados["potencia_consumida"], ".2f") + " kW")
    print("Saldo de potência: " + format(saldo, ".2f") + " kW")
    print("Cobertura solar da demanda: " + format(cobertura_solar, ".2f") + "%")
    print("Status do módulo: " + dados["status_modulo"].upper())
    print("Nível de risco: " + dados["nivel"] + " (" + str(dados["risco"]) + " pontos)")

    print("\nAlertas:")
    if len(dados["alertas"]) == 0:
        print("- Nenhum alerta. Operação dentro dos limites definidos.")
    else:
        for alerta in dados["alertas"]:
            print("- " + alerta)

    print("\nRespostas automáticas recomendadas:")
    if len(dados["acoes"]) == 0:
        print("- Manter a operação normal e o monitoramento contínuo.")
    else:
        for acao in dados["acoes"]:
            print("- " + acao)


def visualizar_status_atual():
    if len(historico) == 0:
        print("\nNenhum dado foi registrado ainda.")
    else:
        exibir_dados(historico[-1])


def visualizar_historico():
    if len(historico) == 0:
        print("\nNenhum dado foi registrado ainda.")
    else:
        print("\n--- HISTORICO DE MONITORAMENTO ---")

        for i in range(len(historico)):
            dados = historico[i]
            saldo = dados["potencia_gerada"] - dados["potencia_consumida"]

            print("\nRegistro " + str(i + 1))
            print("Data: " + dados["data"])
            print("Modulo: " + dados["modulo"])
            print("Temperatura: " + format(dados["temperatura"], ".1f") + " °C")
            print("Bateria: " + format(dados["energia"], ".1f") + "%")
            print("Saldo de potencia: " + format(saldo, ".2f") + " kW")
            print("Risco: " + dados["nivel"] + " (" + str(dados["risco"]) + " pontos)")


def gerar_relatorio():
    if len(historico) == 0:
        print("\nNenhum dado disponível para o relatório.")
        return

    soma_temperatura = 0
    soma_energia = 0
    soma_geracao = 0
    soma_consumo = 0
    situacoes_graves = 0
    falhas_comunicacao = 0
    registros_autossuficientes = 0

    for dados in historico:
        soma_temperatura = soma_temperatura + dados["temperatura"]
        soma_energia = soma_energia + dados["energia"]
        soma_geracao = soma_geracao + dados["potencia_gerada"]
        soma_consumo = soma_consumo + dados["potencia_consumida"]

        if dados["nivel"] == "ALTO" or dados["nivel"] == "CRITICO":
            situacoes_graves = situacoes_graves + 1

        if dados["comunicacao"] == 0:
            falhas_comunicacao = falhas_comunicacao + 1

        if dados["potencia_gerada"] >= dados["potencia_consumida"]:
            registros_autossuficientes = registros_autossuficientes + 1

    total = len(historico)
    media_temperatura = soma_temperatura / total
    media_energia = soma_energia / total
    media_geracao = soma_geracao / total
    media_consumo = soma_consumo / total
    saldo_medio = media_geracao - media_consumo
    percentual_autossuficiente = registros_autossuficientes / total * 100

    print("\n" + "=" * 58)
    print("RELATÓRIO GERAL DE ENERGIA E SUSTENTABILIDADE")
    print("=" * 58)
    print("Total de registros analisados: " + str(total))
    print("Temperatura média: " + format(media_temperatura, ".2f") + " °C")
    print("Nível médio da bateria: " + format(media_energia, ".2f") + "%")
    print("Potência solar média: " + format(media_geracao, ".2f") + " kW")
    print("Potência consumida média: " + format(media_consumo, ".2f") + " kW")
    print("Saldo médio de potência: " + format(saldo_medio, ".2f") + " kW")
    print("Operações com autossuficiência solar: " + format(percentual_autossuficiente, ".2f") + "%")
    print("Falhas de comunicação: " + str(falhas_comunicacao))
    print("Situações de risco alto ou crítico: " + str(situacoes_graves))

    print("\nConclusão:")
    if situacoes_graves == 0 and saldo_medio >= 0:
        print("A missão apresenta operação segura e geração solar suficiente para a demanda analisada.")
    elif situacoes_graves <= 2:
        print("A missão exige atenção e ajustes para melhorar a segurança e o uso sustentável da energia.")
    else:
        print("A missão apresenta risco elevado e precisa de intervenção imediata nos sistemas críticos.")


def menu():
    while True:
        print("\n" + "=" * 36)
        print("SPACEENERGY MONITOR")
        print("=" * 36)
        print("1 - Inserir dados manualmente")
        print("2 - Gerar dados simulados")
        print("3 - Visualizar status atual")
        print("4 - Visualizar histórico")
        print("5 - Gerar relatório geral")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_dados()
        elif opcao == "2":
            gerar_dados_simulados()
        elif opcao == "3":
            visualizar_status_atual()
        elif opcao == "4":
            visualizar_historico()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "0":
            print("\nSistema de monitoramento encerrado.")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


menu()
