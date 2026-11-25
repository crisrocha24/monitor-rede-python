# Monitor de Rede

Projeto desenvolvido em Python para monitorar a conectividade com um site, registrar o status da conexão e medir o tempo de resposta.

## Objetivo

Praticar conceitos de Python aplicados à infraestrutura de TI, monitoramento de conectividade e registro de informações.

## Funcionalidades

- Verificação periódica de conexão
- Identificação de conexão bem-sucedida ou falha
- Medição do tempo de resposta em milissegundos
- Registro dos resultados em arquivo CSV
- Encerramento do monitoramento pelo teclado

## Tecnologias utilizadas

- Python
- Biblioteca urllib
- Biblioteca csv
- Biblioteca time
- Biblioteca datetime
- Biblioteca pathlib

## Como executar

1. Instale o Python.
2. Faça o download ou clone este repositório.
3. Abra a pasta do projeto no VS Code.
4. Execute no terminal:

```bash
python monitor.py
```

Para encerrar o monitoramento, pressione `Ctrl + C`.

## Relatório

Os resultados são registrados automaticamente no arquivo `relatorio_rede.csv`, criado na pasta em que o programa é executado.

## Aprendizados

Este projeto foi desenvolvido como parte dos meus estudos em Ciência da Computação, com foco em Python, redes e infraestrutura de TI.

O desenvolvimento permitiu praticar tratamento de exceções, manipulação de arquivos, monitoramento de conectividade e organização de dados.

## Próximas melhorias

- Permitir configurar o endereço monitorado
- Registrar falhas com mais detalhes
- Criar um resumo de disponibilidade
- Desenvolver uma interface gráfica para visualizar os resultados