# Classificação de áudio com Python

## Representação digital de áudio

O som digital é uma representação numérica discreta do som analógico. Para converter
o som analógico para digital é feita uma amostragem: medir a amplitude do sinal
em intervalos regulares de tempo, é armazenado num vetor como sequência de amostras -> **unidimensional**.

- **período de amostragem (T)**: tempo entre amostras;
- **taxa de amostragem (f_s)** = 1/T em Hz;
- **quantização** = amplitude da representação discreta, quantio maior, mais qualidade. Geralmente 16 bits -> 2^16 = 65535.

Humanos só conseguem ouvir frequências de 20kHz a 22kHz. Quanto maior a frequência, mais aguda.

## Transformada de Fourier

Vai servir pra decompor um sinal em seus componentes de frequência -> desmonta a síntese.

### Short Time FT

Divide o sinal em segmentos menores e calcula a transformada pra cada segmento -> Produz um **esectograma** e permite a visualização de harmonias, etc.

- **tamanho da janela** - Quantas amostras em cada segmento. Os componentes (bins) vão ser metade do número de amostras no segmento.
- O intervalo de frequências vai ser: delta_f = f_s / N
  - O N vai determinar a resolução/qualidade do espectograma

## Teorema de Nynquist

Pra reconstruir um sinal com amostras, é necessário que a frequência de amostragem seja pelo menos o dobro da maior frequência presente no sinal. Ou seja, paracapturar frequências de até 22kHz (limite da audição humana), a f_s tem que ser de 44.1kHz.

Se não for feito assim, pode ocorrer o *aliasing*, onde frequências mais altas são confundidas com frequências mais baixas.

## Análise de espectograma

Sons humanos como um bebê chorando, canto, fala e etc. vão apresentar harmonia (a mesma coisa se repete no eixo da frequências). Sons como chuva e ondas do mar são mais uniformes tanto em faixa quanto em tempo.

[]("imagens/espectograma_ondas.jpg")

Esse sinal pode então ser classificado e rotulado.
