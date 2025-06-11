import requests
import time

def verificar_conexao(url='https://www.google.com'):
    print("🌐 Verificando conexão com a internet...")
    
    try:
        inicio = time.time()
        resposta = requests.get(url, timeout=5)
        fim = time.time()

        tempo_resposta = fim - inicio
        tamanho_kb = len(resposta.content) / 1024
        status = resposta.status_code

        print("✅ Conexão estabelecida com sucesso!")
        print(f"🔁 Status HTTP: {status}")
        print(f"⏱️ Tempo de resposta: {tempo_resposta:.2f} segundos")
        print(f"📦 Tamanho do conteúdo recebido: {tamanho_kb:.2f} KB")

        if tempo_resposta < 0.5:
            qualidade = "🚀 Ótima"
        elif tempo_resposta < 1.5:
            qualidade = "👍 Boa"
        elif tempo_resposta < 3:
            qualidade = "⚠️ Lenta"
        else:
            qualidade = "🐢 Muito lenta"

        print(f"📶 Qualidade da conexão: {qualidade}")
        return {
            "status": status,
            "tempo_resposta": tempo_resposta,
            "tamanho_kb": tamanho_kb,
            "qualidade": qualidade
        }

    except requests.ConnectionError:
        print("❌ Sem conexão com a internet.")
    except requests.Timeout:
        print("⏱️ Tempo limite excedido. Conexão muito lenta.")
    except Exception as e:
        print(f"⚠️ Erro inesperado: {e}")

if __name__ == "__main__":
    verificar_conexao()
