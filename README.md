<p align="center">
  <img src="https://github.com/ArturMaia/Internauta/blob/main/TecnicoNet.png" alt="Net" style="width: 200px; border-radius: 10px;">
</p>

# 🌐 Internauta

**Internauta** é uma ferramenta em Python para diagnóstico rápido da conexão com a internet. Realiza uma requisição HTTP e fornece métricas objetivas como tempo de resposta, status HTTP e tamanho do conteúdo, com classificação da qualidade da rede.

---

## Funcionalidades

- Teste de conectividade via `requests.get()`
- Medição de tempo de resposta (em segundos)
- Status HTTP e tamanho da resposta (KB)
- Classificação da conexão:
 · 🚀 Ótima
 · 👍 Boa
 · ⚠️ Lenta
 · 🐢 Muito lenta
- Tratamento de erros: `ConnectionError`, `Timeout`, exceções genéricas

---

## Exemplo de resultado

```bash
🌐 Verificando conexão com a internet...
✅ Conexão estabelecida com sucesso!
🔁 Status HTTP: 200
⏱️ Tempo de resposta: 0.42 segundos
📦 Tamanho do conteúdo recebido: 11.87 KB
📶 Qualidade da conexão: 👍 Boa
````

---

## Exemplo de falha

```bash
❌ Sem conexão com a internet.
⏱️ Tempo limite excedido. Conexão muito lenta.
⚠️ Erro inesperado: <mensagem da exceção>
```

---

## Modificações futuras

* Suporte a múltiplas URLs
* Exportação em JSON/CSV
* Interface gráfica básica

---

## Contribuições

Contribuições são encorajadas e bem-vindas.
