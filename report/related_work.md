# Related Work Notes

This project studies classical time-scale modification for speech, so the most natural related work is the overlap-add family of methods.

## Suggested Related Work Paragraph

A strong related-work reference for this project is Verhelst and Roelands' WSOLA paper, which improved basic overlap-add by aligning adjacent waveform segments before overlap and synthesis. That idea matters here because it shows why plain OLA is a useful baseline but not always the highest-quality solution for speech. A second foundational reference is Verhelst's 2000 overview of overlap-add methods for speech time-scaling, which discusses the main design trade-offs of OLA-style techniques and provides context for artifacts such as discontinuities, reverberant smearing, and reduced naturalness at larger scaling factors.

## Report-Ready Citations

1. Verhelst, W., and Roelands, M. "An overlap-add technique based on waveform similarity (WSOLA) for high quality time-scale modification of speech." *Proceedings of ICASSP 1993*, 1993.
   Source: https://ieeexplore.ieee.org/document/319360

2. Verhelst, W. "Overlap-add methods for time-scaling of speech." *Speech Communication*, 30(2-3), 207-221, 2000.
   Source: https://www.sciencedirect.com/science/article/pii/S016763939900064X

## Example BibTeX

```bibtex
@inproceedings{verhelst1993wsola,
  author = {Verhelst, Werner and Roelands, Marc},
  title = {An overlap-add technique based on waveform similarity (WSOLA) for high quality time-scale modification of speech},
  booktitle = {Proceedings of IEEE International Conference on Acoustics, Speech, and Signal Processing},
  year = {1993},
  pages = {554--557}
}

@article{verhelst2000ola,
  author = {Verhelst, Werner},
  title = {Overlap-add methods for time-scaling of speech},
  journal = {Speech Communication},
  volume = {30},
  number = {2-3},
  pages = {207--221},
  year = {2000}
}
```

## How To Use This In Your Report

- Cite the WSOLA paper in the introduction or methods section when motivating why OLA is a baseline rather than the final state of the art.
- Cite the 2000 paper in the methods or discussion section when explaining the overlap-add family and expected artifacts.
- In your discussion, compare your observed artifacts against the trade-offs these papers describe.
