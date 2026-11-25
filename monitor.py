
import urllib.request
import csv
import time
from datetime import datetime
from pathlib import Path

# Arquivo onde serão salvos os resultados
relatorio = Path("relatorio_rede.csv")

# Endereço usado para testar a conexão
site = "https://www.google.com"

print("=== MONITOR DE REDE ===")
print("Monitoramento iniciado.")
print("Pressione CTRL + C para encerrar.")

# Criar o cabeçalho do relatório
if not relatorio.exists():
    with open(relatorio, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Data", "Horario", "Status", "Tempo_ms"])

try:

    while True:

        horario_inicio = time.time()

        try:
            resposta = urllib.request.urlopen(site, timeout=5)

            tempo = (time.time() - horario_inicio) * 1000

            status = "CONECTADO"

            resposta.close()

        except Exception:
            tempo = 0
            status = "SEM CONEXAO"

        agora = datetime.now()

        data = agora.strftime("%d/%m/%Y")
        horario = agora.strftime("%H:%M:%S")

        print(data, horario, status, tempo)

        # Registrar resultado no CSV
        with open(relatorio, "a", newline="", encoding="utf-8") as arquivo:

            escritor = csv.writer(arquivo)

            escritor.writerow([
                data,
                horario,
                status,
                round(tempo, 2)
            ])

        # Esperar 30 segundos
        time.sleep(30)

except KeyboardInterrupt:
    print("\nMonitoramento encerrado.")
