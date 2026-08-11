---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Bateria

![Configurações da bateria do rádio](../assets/system-battery.png)

Calibra a leitura da bateria interna do rádio e define os limites de
alarme — separadamente das configurações da bateria de voo de um modelo
(consulte [Guia prático: Aviso de tensão baixa da
bateria](../how-to/low-battery-warning.md)).

- **Tensão principal** — mostra a leitura atual e também serve como ajuste
  de calibração: informe a tensão real medida com um multímetro. O padrão
  é 8,4 V (uma bateria Li-ion 2S totalmente carregada).
- **Tensão baixa** — o limite de alarme, padrão 7,2 V (7,4 V oferece uma
  margem extra). Quando o [alerta de tensão
  principal](alerts.md) está ativado, cair abaixo desse valor dispara uma
  janela de aviso e um alerta falado "Radio battery is low" a cada minuto,
  esteja a janela aberta ou não.

  !!! warning
      Pouse e recarregue a bateria do rádio assim que esse alerta soar —
      ele se repete a cada minuto de qualquer forma. Em 6,0 V o rádio se
      desliga incondicionalmente para proteger as células Li-ion de
      2×3,0 V.

- **Faixa de tensão exibida** — os valores mín./máx. para a exibição
  gráfica da bateria no canto superior direito: MIN é o ponto em que o
  primeiro segmento da barra se apaga, MAX é o ponto em que o quarto se
  acende. Os padrões são 6,4–8,4 V para a bateria Li-ion integrada; muitos
  pilotos elevam o limite inferior para obter um aviso de tensão baixa
  mais cedo e evitar a descarga excessiva. Ajuste esses valores conforme o
  tipo de bateria efetivamente instalado.
- **Tensão RTC** — a tensão da bateria de moeda do relógio de tempo real.
  3,0 V quando nova; substitua-a abaixo de 2,7 V para manter o relógio
  preciso, e espere o [alerta de tensão RTC](alerts.md) abaixo de 2,5 V.
