from __future__ import annotations

import math

import numpy as np


def ola_time_scale(
    signal: np.ndarray,
    speed: float,
    frame_length: int = 1024,
    analysis_hop: int = 256,
) -> np.ndarray:
    """
    Time-scale a 1-D signal with classical overlap-add.

    `speed > 1.0` produces faster playback (shorter output).
    `speed < 1.0` produces slower playback (longer output).
    """
    if speed <= 0:
        raise ValueError("speed must be positive")
    if frame_length <= 0 or analysis_hop <= 0:
        raise ValueError("frame_length and analysis_hop must be positive")
    if analysis_hop >= frame_length:
        raise ValueError("analysis_hop must be smaller than frame_length")

    x = np.asarray(signal, dtype=np.float32).flatten()
    if x.size == 0:
        return x.copy()
    if x.size < frame_length:
        pad_amount = frame_length - x.size
        x = np.pad(x, (0, pad_amount))

    synthesis_hop = max(1, int(round(analysis_hop / speed)))
    window = np.hanning(frame_length).astype(np.float32)

    frame_count = 1 + math.ceil((len(x) - frame_length) / analysis_hop)
    padded_length = (frame_count - 1) * analysis_hop + frame_length
    if padded_length > len(x):
        x = np.pad(x, (0, padded_length - len(x)))

    output_length = (frame_count - 1) * synthesis_hop + frame_length
    output = np.zeros(output_length, dtype=np.float32)
    normalizer = np.zeros(output_length, dtype=np.float32)

    for frame_index in range(frame_count):
        start_in = frame_index * analysis_hop
        start_out = frame_index * synthesis_hop
        frame = x[start_in : start_in + frame_length] * window
        output[start_out : start_out + frame_length] += frame
        normalizer[start_out : start_out + frame_length] += window * window

    valid = normalizer > 1e-8
    output[valid] /= normalizer[valid]

    return output
