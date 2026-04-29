from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def _variant_label(factor: float) -> str:
    return f"{factor:g}x"


def save_waveform_comparisons(
    original: np.ndarray,
    variants: Sequence[tuple[float, np.ndarray]],
    sample_rate: int,
    output_path: str | Path,
    title: str,
) -> None:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    rows = 1 + len(variants)
    fig_height = max(6, 2.2 * rows)
    fig, axes = plt.subplots(rows, 1, figsize=(12, fig_height), sharex=False)
    axes = np.atleast_1d(axes)

    time_original = np.arange(len(original)) / sample_rate
    axes[0].plot(time_original, original, linewidth=0.8)
    axes[0].set_title("Original waveform")
    axes[0].set_xlabel("Time (s)")
    axes[0].set_ylabel("Amplitude")
    axes[0].grid(alpha=0.2)

    for axis, (factor, modified) in zip(axes[1:], variants):
        time_modified = np.arange(len(modified)) / sample_rate
        axis.plot(time_modified, modified, linewidth=0.8, color="tab:orange")
        axis.set_title(f"{_variant_label(factor)} speed waveform")
        axis.set_xlabel("Time (s)")
        axis.set_ylabel("Amplitude")
        axis.grid(alpha=0.2)

    fig.suptitle(title)
    fig.tight_layout()
    fig.savefig(output, dpi=200, bbox_inches="tight")
    plt.close(fig)


def save_spectrogram_comparisons(
    original: np.ndarray,
    variants: Sequence[tuple[float, np.ndarray]],
    sample_rate: int,
    output_path: str | Path,
    title: str,
    nfft: int = 1024,
    overlap: int = 768,
) -> None:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    rows = 1 + len(variants)
    fig_height = max(7, 2.4 * rows)
    fig, axes = plt.subplots(rows, 1, figsize=(12, fig_height), sharex=False)
    axes = np.atleast_1d(axes)

    axes[0].specgram(original, NFFT=nfft, Fs=sample_rate, noverlap=overlap, cmap="magma")
    axes[0].set_title("Original spectrogram")
    axes[0].set_xlabel("Time (s)")
    axes[0].set_ylabel("Frequency (Hz)")

    for axis, (factor, modified) in zip(axes[1:], variants):
        axis.specgram(modified, NFFT=nfft, Fs=sample_rate, noverlap=overlap, cmap="magma")
        axis.set_title(f"{_variant_label(factor)} speed spectrogram")
        axis.set_xlabel("Time (s)")
        axis.set_ylabel("Frequency (Hz)")

    fig.suptitle(title)
    fig.tight_layout()
    fig.savefig(output, dpi=200, bbox_inches="tight")
    plt.close(fig)
