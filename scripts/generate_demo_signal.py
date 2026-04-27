from __future__ import annotations

from pathlib import Path

import numpy as np

from tsm.audio import write_wav_mono


def synthetic_vowel_like_signal(sample_rate: int = 16000, duration: float = 2.0) -> np.ndarray:
    t = np.linspace(0.0, duration, int(sample_rate * duration), endpoint=False)

    f0 = 140.0
    excitation = (
        0.5 * np.sin(2.0 * np.pi * f0 * t)
        + 0.25 * np.sin(2.0 * np.pi * 2.0 * f0 * t)
        + 0.15 * np.sin(2.0 * np.pi * 3.0 * f0 * t)
    )

    formant_1 = 0.4 * np.sin(2.0 * np.pi * 700.0 * t)
    formant_2 = 0.25 * np.sin(2.0 * np.pi * 1220.0 * t)
    envelope = 0.5 * (1.0 - np.cos(2.0 * np.pi * np.minimum(t / duration, 1.0)))
    syllable_modulation = 0.55 + 0.45 * np.sin(2.0 * np.pi * 2.2 * t) ** 2

    signal = (excitation + formant_1 + formant_2) * envelope * syllable_modulation
    signal /= np.max(np.abs(signal)) + 1e-8
    return signal.astype(np.float32)


def main() -> None:
    sample_rate = 16000
    signal = synthetic_vowel_like_signal(sample_rate=sample_rate, duration=2.0)
    output_path = Path("data/input/demo_signal.wav")
    write_wav_mono(output_path, sample_rate, signal)
    print(f"Saved demo signal to {output_path}")


if __name__ == "__main__":
    main()
