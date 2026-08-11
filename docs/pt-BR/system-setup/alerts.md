---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Alertas

![Alertas](../assets/system-alerts.png)

Quatro avisos válidos para todo o rádio, cada um ativável de forma independente — separados das [funções especiais](../model-setup/special-functions.md) e dos [interruptores lógicos](../model-setup/logical-switches.md) por modelo que você mesmo cria.

- **Modo silencioso** — um alerta falado na inicialização quando esta verificação está ativa e [Geral → Modo de áudio](general.md) está definido como Silencioso, como lembrete de que o rádio está sem som.
- **Tensão principal** — "Bateria do rádio está baixa" quando a bateria principal do rádio cai abaixo do limite de **Tensão baixa** definido em [Bateria](battery.md).
- **Tensão do RTC** — "Bateria do RTC está baixa" quando a bateria tipo moeda do RTC cai abaixo de 2,5 V (o limite padrão). O registro de dados depende do relógio de tempo real; uma hora inválida dificulta a leitura dos logs, especialmente para distinguir as sessões de voo. Isso pode ser silenciado temporariamente enquanto se aguarda a substituição da bateria, mas não deve ficar desativado indefinidamente.
- **Aviso de conflito de sensores** — detecta IDs de sensores de telemetria em conflito. Só vale a pena desativar se você tiver sensores que não atendem à especificação S.Port.
- **Inatividade** — um alerta falado de "Inatividade prolongada" (além de uma vibração háptica, caso o volume esteja baixo) depois que o rádio ficar sem uso por mais tempo que o configurado — 10 minutos por padrão.
