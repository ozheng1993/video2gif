# video2gif

Programmatically generate animated GIF from video in Python

With this video2gif converter you can upload any format of video and rich media files to turn them into high quality animated GIFs. 
keyword:gif video gifmaker video2gif
## Requirements

Python 3.6+, pysimplegui,opencv-python and other common packages listed in `requirements.txt`.

## Installation

1. Clone this repository
2. Install dependencies
   ```bash
   pip3 install -r requirements.txt
   ```
3. Run setup from the repository root directory
    ```bash
    python3 setup.py install
    ``` 

## Getting Started

1. Start interface
   ```bash
   python3 vgif/main.py
     ```
2. Select video file
3. Set options
4. Click button "Start" to start
5. Once started converter will save the output under the same folder ad source video
6. Click button "ReStart" to re-start this process
7. Click button "Exit" to end this program.

## Interface
![Instance Segmentation Sample](assets/interface.png)
The options includes:
* Video Sample Rate:Set sample rate for the source video (defult sample every 10 frame)
* Output GIF FPS: Set output GIF fps(defult 10 fps)
* Video Resize Rate: Shrink video n times samller (defult 2 times smaller)

## Citation
Use this bibtex to cite this repository:
```
@misc{ouzheng1993,
  title={video2gif},
  author={ou zheng},
  year={2020},
  publisher={Github},
  journal={GitHub repository},
  howpublished={\url{https://github.com/ozheng1993/video2gif}},
}
```

## Contributing
Contributions to this repository are welcome. Examples of things you can contribute:
* update README
* update user interface
