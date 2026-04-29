# EC519 Speech Signals Project

This repository is a starter implementation for the EC519 project on time-scale modification (TSM) of speech signals. It follows the proposal scope by implementing a classical Overlap-Add (OLA) pipeline, generating waveform and spectrogram comparisons, and documenting related work for the final report.

## Project Goal

Change speech playback speed while preserving intelligibility and naturalness as much as possible. The current implementation focuses on OLA and supports experiments with factors such as `0.5x`, `1.5x`, and `2.0x`.

## Repository Layout

- `src/tsm/ola.py`: OLA time-scale modification implementation
- `src/tsm/audio.py`: WAV loading and saving helpers
- `src/tsm/analysis.py`: waveform and spectrogram plotting utilities
- `scripts/run_experiment.py`: main experiment runner
- `scripts/generate_demo_signal.py`: creates a simple synthetic speech-like demo file
- `report/related_work.md`: related work notes and citations for the report
- `report/report_outline.md`: report structure mapped to the proposal

## Setup

Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Quick Start

1. Generate a demo file if you do not yet have a speech WAV:

```bash
python3 scripts/generate_demo_signal.py
```

2. Run the OLA experiment:

```bash
PYTHONPATH=src python3 scripts/run_experiment.py \
  --input data/input/demo_signal.wav \
  --factors 0.5 1.5 2.0
```

3. Check:

- `data/output/` for time-scaled WAV files
- `figures/` for combined waveform and spectrogram comparison figures

## Using Your Own Audio

- Put a mono or stereo PCM WAV file in `data/input/`
- Pass it with `--input`
- Stereo files are mixed to mono for analysis

Example:

```bash
PYTHONPATH=src python3 scripts/run_experiment.py \
  --input data/input/my_speech.wav \
  --factors 0.5 1.5 2.0 \
  --frame-length 1024 \
  --analysis-hop 256
```

## Notes on the Current Baseline

- OLA is simple and a good first baseline, but it may introduce transient smearing and reverberant artifacts for larger scaling changes.
- The report can compare these artifacts in both waveform and spectrogram views.
- An obvious extension is WSOLA or a phase-vocoder baseline.

## Related Work

The repository already includes a report-ready note in [report/related_work.md](/Users/jshao116/Documents/BU/EC519/EC519_Speech_Signals/report/related_work.md).

Two useful references to cite are:

1. W. Verhelst and M. Roelands, "An overlap-add technique based on waveform similarity (WSOLA) for high quality time-scale modification of speech," 1993 IEEE International Conference on Acoustics, Speech, and Signal Processing, 1993.
2. W. Verhelst, "Overlap-add methods for time-scaling of speech," *Speech Communication*, 30(2-3), 207-221, 2000.
