import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

sampleVector, sampleRate = librosa.load(librosa.example("brahms"), sr=None)

print(f"Taxa de amostragem: {sampleRate} Hz")
print(f"Número de amostras: {len(sampleVector)}")
print(f"Número de amostras: {len(sampleVector) / sampleRate:.2f} segundos")

# Plotar os primeiros 5ms após 10s
plt.figure(figsize=(10, 5))
librosa.display.waveshow(
    sampleVector[10 * sampleRate : 10 * sampleRate + int(sampleRate * 0.005)],
    sr=sampleRate,
)

plt.title("Trecho de 5ms de áudio")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.show()
