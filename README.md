# SpaceEnergy Monitor

Projeto desenvolvido na disciplina "Soluções em Energias Renováveis e Sustentáveis" como parte da Global Solution.

Descrição
--------------------------------------------------------------------------------------------------------------------------------
SpaceEnergy Monitor é uma ferramenta de console em Python para acompanhar o desempenho energético de uma missão experimental. O sistema recebe dados dos módulos (temperatura, bateria, comunicação, geração e consumo), avalia riscos e sugere ações automáticas quando necessário.

Principais recursos
---------------------------------------
- Inserção manual de dados.
- Geração de dados simulados para testes.
- Monitoramento de temperatura e nível de bateria.
- Verificação do estado de comunicação.
- Cálculo de geração vs consumo e saldo de potência.
- Classificação de risco com alertas e recomendações.
- Visualização do status atual, histórico e relatório geral.

Regras básicas de monitoramento
------------------------------------------------------------
- Temperatura: acima de 60 °C → alerta; acima de 80 °C → crítico.
- Bateria: abaixo de 40% → atenção; abaixo de 20% → crítico.
- Comunicação: inativa → alerta e tentativa de reconexão.
- Energia solar: se consumo > geração → alerta e recomendações para reduzir cargas.
- Status do módulo: "atencao" → verificação preventiva; "falha" → isolar e iniciar manutenção.

Classificação de risco
----------------------------------------
- Até 25 pontos: BAIXO
- 26 a 50 pontos: MODERADO
- 51 a 75 pontos: ALTO
- Acima de 75 pontos: CRÍTICO

Como executar
---------------------------------------
1. Abra um terminal na pasta do projeto.
2. Rode:

```bash
python app.py
```


Integrantes
---------------------------
- Gabriel Castilla Cavaloti
