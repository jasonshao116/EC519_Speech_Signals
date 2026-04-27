from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def save_waveform_comparison(
    original: np.ndarray,
    modified: np.ndarray,
    sample_rate: int,
    output_path: str | Path,
    title: str,
) -> None:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    time_original = np.arange(len(original)) / sample_rate
    time_modified = np.arange(len(modified)) / sample_rate

    fig, axes = plt.subplots(2, 1, figsize=(12, 6), sharex=False)
    axes[0].plot(time_original, original, linewidth=0.8)
    axes[0].set_title("Original waveform")
    axes[0].set_xlabel("Time (s)")
    axes[0].set_ylabel("Amplitude")
    axes[0].grid(alpha=0.2)

    axes[1].plot(time_modified, modified, linewidth=0.8, color="tab:orange")
    axes[1].set_title("Time-scaled waveform")
    axes[1].set_xlabel("Time (s)")
    axes[1].set_ylabel("Amplitude")
    axes[1].grid(alpha=0.2)

    fig.suptitle(title)
    fig.tight_layout()
    fig.savefig(output, dpi=200, bbox_inches="tight")
    plt.close(fig)


def save_spectrogram_comparison(
    original: np.ndarray,
    modified: np.ndarray,
    sample_rate: int,
    output_path: str | Path,
    title: str,
    nfft: int = 1024,
    overlap: int = 768,
) -> None:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(2, 1, figsize=(12, 7), sharex=False)

    axes[0].specgram(original, NFFT=nfft, Fs=sample_rate, noverlap=overlap, cmap="magma")
    axes[0].set_title("Original spectrogram")
    axes[0].set_xlabel("Time (s)")
    axes[0].set_ylabel("Frequency (Hz)")

    axes[1].specgram(modified, NFFT=nfft, Fs=sample_rate, noverlap=overlap, cmap="magma")
    axes[1].set_title("Time-scaled spectrogram")
    axes[1].set_xlabel("Time (s)")
    axes[1].set_ylabel("Frequency (Hz)")

    fig.suptitle(title)
    fig.tight_layout()
    fig.savefig(output, dpi=200, bbox_inches="tight")
    plt.close(fig)
