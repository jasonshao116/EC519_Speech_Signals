from __future__ import annotations

import wave
from pathlib import Path

import numpy as np


def read_wav_mono(path: str | Path) -> tuple[int, np.ndarray]:
    """Read a PCM WAV file and return (sample_rate, mono_float_signal)."""
    wav_path = Path(path)
    with wave.open(str(wav_path), "rb") as wav_file:
        channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        sample_rate = wav_file.getframerate()
        frame_count = wav_file.getnframes()
        raw = wav_file.readframes(frame_count)

    if sample_width == 1:
        signal = np.frombuffer(raw, dtype=np.uint8).astype(np.float32)
        signal = (signal - 128.0) / 128.0
    elif sample_width == 2:
        signal = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    elif sample_width == 4:
        signal = np.frombuffer(raw, dtype=np.int32).astype(np.float32) / 2147483648.0
    else:
        raise ValueError(f"Unsupported sample width: {sample_width} bytes")

    if channels > 1:
        signal = signal.reshape(-1, channels).mean(axis=1)

    return sample_rate, signal.astype(np.float32, copy=False)


def write_wav_mono(path: str | Path, sample_rate: int, signal: np.ndarray) -> None:
    """Write a mono float signal in [-1, 1] to 16-bit PCM WAV."""
    wav_path = Path(path)
    wav_path.parent.mkdir(parents=True, exist_ok=True)

    clipped = np.clip(np.asarray(signal, dtype=np.float32), -1.0, 1.0)
    int_signal = (clipped * 32767.0).astype(np.int16)

    with wave.open(str(wav_path), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(int_signal.tobytes())
