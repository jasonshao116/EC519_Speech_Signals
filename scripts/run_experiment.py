from __future__ import annotations

import argparse
from pathlib import Path

from tsm.analysis import save_spectrogram_comparisons, save_waveform_comparisons
from tsm.audio import read_wav_mono, write_wav_mono
from tsm.ola import ola_time_scale


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run OLA time-scale modification experiments on a speech WAV file."
    )
    parser.add_argument("--input", required=True, help="Path to input WAV file")
    parser.add_argument(
        "--factors",
        type=float,
        nargs="+",
        default=[0.5, 1.5, 2.0],
        help="Playback speed factors. Example: 0.5 1.5 2.0",
    )
    parser.add_argument("--frame-length", type=int, default=1024)
    parser.add_argument("--analysis-hop", type=int, default=256)
    parser.add_argument("--output-dir", default="data/output")
    parser.add_argument("--figure-dir", default="figures")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    sample_rate, signal = read_wav_mono(args.input)

    output_dir = Path(args.output_dir)
    figure_dir = Path(args.figure_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    figure_dir.mkdir(parents=True, exist_ok=True)

    input_stem = Path(args.input).stem

    print(f"Loaded {args.input}")
    print(f"Sample rate: {sample_rate} Hz")
    print(f"Samples: {len(signal)}")

    variants = []
    for factor in args.factors:
        modified = ola_time_scale(
            signal,
            speed=factor,
            frame_length=args.frame_length,
            analysis_hop=args.analysis_hop,
        )
        variants.append((factor, modified))

        factor_tag = str(factor).replace(".", "p")
        wav_path = output_dir / f"{input_stem}_ola_{factor_tag}x.wav"

        write_wav_mono(wav_path, sample_rate, modified)
        print(f"Saved {wav_path}")

    waveform_path = figure_dir / f"{input_stem}_waveform_comparison.png"
    spectrogram_path = figure_dir / f"{input_stem}_spectrogram_comparison.png"

    save_waveform_comparisons(
        signal,
        variants,
        sample_rate,
        waveform_path,
        title="OLA waveform comparison",
    )
    save_spectrogram_comparisons(
        signal,
        variants,
        sample_rate,
        spectrogram_path,
        title="OLA spectrogram comparison",
    )

    print(f"Saved {waveform_path}")
    print(f"Saved {spectrogram_path}")


if __name__ == "__main__":
    main()
