---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Testar uma Configuração de Receptor Redundante

A redundância só vale a pena se for realmente testada antes de voar —
isto pressupõe que um [receptor redundante](../model-setup/rf-system.md#redundant-receivers)
já esteja configurado.

!!! note "Capturas de tela pendentes"
    Esta página ainda não possui capturas de tela do simulador — consulte [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

## A. Teste em campo

Com o receptor principal em 2.4GHz e o redundante em 900MHz, inicie uma
[Verificação de alcance](../model-setup/rf-system.md#range-check) e afaste-se do
modelo até que o sinal de 2.4GHz seja perdido (além do alerta de RSSI Crítico). O
receptor redundante de 900MHz deve assumir o controle nesse momento.

## B. Teste de bancada

1. **Confirme a configuração normal** — ambos os receptores vinculados, ambos os LEDs verdes acesos,
   controles respondendo normalmente.
2. **Vincule o receptor principal a outro Model ID** — crie um modelo de
   teste descartável (por exemplo, "TestRx") com um Model ID diferente e vincule o
   receptor *principal* a ele. Volte ao modelo em teste: o LED do receptor
   principal deve agora estar **vermelho** (vinculado a outro modelo), o LED do
   receptor redundante permanece **verde** — e os controles ainda devem funcionar,
   comprovando que o receptor redundante, por si só, mantém o modelo em condições de voo.
3. **Revincule o receptor principal** ao seu Model ID normal. Confirme que ambos
   os LEDs estão verdes novamente e que os controles estão funcionando antes de considerar
   o teste concluído.
