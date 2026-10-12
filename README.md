# Code Art Video Player

An interactive Python application that converts videos into high-resolution, colorized ASCII-style **Code Art** rendered in real-time. The visual sequence uses programming keywords and symbols (`def`, `if`, `class`, `import`, etc.) mapped to video pixels, maintaining synchronization with background MP3 audio.

---

##  Features

* **High-Definition Code Art**: Renders frames at high character density for crisp visual details.
* **Color Accuracy**: Samples background RGB colors directly from the original video frames.
* **Audio-Video Synchronization**: Plays MP3 audio in sync with the visual rendering loop.
* **Interactive Track Selection**: Dynamic console menu to easily switch between tracks/animations.
* **Looping Support**: Smooth replay capabilities for continuous visualizer playback.

---

##  Prerequisites & Tech Stack

* **Language**: Python 3.12+
* **Libraries**:
  * `pygame` – Window management and audio playback.
  * `opencv-python` (`cv2`) – Video frame decoding.
  * `numpy` – Fast matrix manipulation for pixel-to-character mapping.

---
