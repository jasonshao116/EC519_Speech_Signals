# Report Outline

This outline follows the proposal and matches the code currently in the repository.

## 1. Introduction

- Explain what time-scale modification is
- Motivate speech playback control, accessibility, and listening-rate adjustment
- State that this project implements classical OLA as a baseline

## 2. Related Work

- Introduce OLA-family methods for speech time-scaling
- Cite WSOLA as an improvement over plain OLA
- Position your implementation as a classical baseline for observing artifacts

Suggested sources:

- [related_work.md](/Users/jshao116/Documents/BU/EC519/EC519_Speech_Signals/report/related_work.md)

## 3. Methods

- Describe framing, windowing, analysis hop, and synthesis hop
- Explain how the speed factor changes the synthesis hop
- Include the OLA reconstruction equation if you want a stronger methods section

## 4. Experimental Setup

- Describe input speech files
- List tested speed factors such as `0.5x`, `1.5x`, and `2.0x`
- State frame length and hop size
- Mention waveform and spectrogram comparisons as evaluation tools

## 5. Results

- Show generated waveforms from `figures/`
- Show generated spectrograms from `figures/`
- Comment on duration changes and obvious artifacts

## 6. Discussion

- Explain where OLA works reasonably well
- Discuss transient smearing, discontinuities, and reduced naturalness at larger factors
- Connect your observations back to lecture topics and related work

## 7. Conclusion

- Summarize what OLA achieves
- Reflect on its limitations
- Mention future work such as WSOLA or phase vocoder comparison
