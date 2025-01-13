### SinoJazzy

> Transform any jazz piece into a Chinese-influenced jazz track by mapping all notes to a pentatonic scale!

---

## Overview

SinoJazzy is a Python-based project that takes any jazz song—whether MIDI or single-melody MP3—and remaps its notes to a Chinese-style pentatonic scale, creating a unique “Eastern jazz” experience. By combining the characteristic improvisational flair of jazz with the distinctive tonal flavor of the Chinese pentatonic scale, SinoJazzy delivers a fresh cross-cultural fusion.

The project primarily works with MIDI files for precise note-by-note remapping. For monophonic MP3s, it relies on pitch-tracking libraries (e.g., `librosa`) to convert waveforms into musical notes, then applies the same “pentatonization” process.

---

## Features

- **Pentatonic Remapping for MIDI**  
  Automatically snaps every note in a MIDI file to the closest pentatonic pitch, then saves a brand-new `.mid` file.

- **Basic Pitch-Tracking**  
  An experimental module that uses pitch detection (e.g., `librosa.pyin`) for monophonic MP3 tracks and then applies the pentatonic conversion.

- **Customizable Pentatonic Scales**  
  By default, SinoJazzy uses the C pentatonic scale (C, D, E, G, A). Feel free to specify any other pentatonic scale (e.g., G pentatonic).

- **Extensible Architecture**  
  The open-source code is easy to modify or enhance, supporting advanced features like chord recognition, multi-part separation, and beyond.

---

## Getting Started

1. **Clone the repository**  
   ```bash
   git clone https://github.com/YourGitHubName/SinoJazzy.git
   cd SinoJazzy
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
   - You’ll likely need [mido](https://mido.readthedocs.io/) for MIDI processing.  
   - For pitch tracking on MP3 files (single melody), consider installing [librosa](https://librosa.org/).

3. **Run the example**  
   ```bash
   python main.py --input examples/example_in.mid --output examples/example_out.mid
   ```
   This will snap the MIDI notes from `example_in.mid` to a pentatonic scale and save the output as `example_out.mid`.

4. **Audio/Pitch-Tracking (Experimental)**  
   - Use `audio_utils.py` to detect pitch in monophonic MP3 files and remap them to the pentatonic scale. You’ll need libraries like `librosa` for this functionality.

---

## Usage Example

If you have a MIDI file `my_jazz.mid` and you want the SinoJazzy output `my_chinese_jazz.mid`, simply run:

```bash
python main.py --input my_jazz.mid --output my_chinese_jazz.mid
```

To change to a different pentatonic scale—say G major pentatonic (G, A, B, D, E, which corresponds to `[7, 9, 11, 2, 4]`)—use:

```bash
python main.py --input my_jazz.mid --output my_chinese_jazz.mid --scale 7,9,11,2,4
```

---

## Roadmap

- **Polyphonic Support**  
  Implement deep learning-based multi-pitch detection and source separation to handle chordal or multi-instrument jazz pieces.

- **AI Melody Generation**  
  Beyond simply snapping existing notes to pentatonic scales, explore AI approaches to rearrange melodies and create new motifs.

- **Real-time Processing**  
  Integrate with MIDI devices or audio input to enable live “pentatonic auto-correction” for on-the-fly performances.

Contributions via issues or pull requests are greatly appreciated!

---

## License & Disclaimer

- **Music Copyright**  
  Please ensure you have the rights to use any uploaded audio or MIDI files. This project does not assume responsibility for copyrighted material.

- **Project License**  
  SinoJazzy is released under the [MIT License](./LICENSE). Feel free to use and modify as you see fit.

- **Disclaimer**  
  This software’s pentatonic conversion is intended for educational and entertainment purposes only.

- **Acknowledgments**  
  Many thanks to all contributors who helped make SinoJazzy possible.

---

**Try it out now**: Upload any jazz tune, snap it to the Chinese pentatonic scale, and experience the rich flavor of “Eastern jazz!”  

> *“Jazz meets China—unleash the Sino groove!”*