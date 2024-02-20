video2gif ~ vgif
============================

Programmatically generate animated GIF from video in Python

With this video2gif converter you can upload any format of video and rich media files to turn them into high quality animated GIFs.

Getting Started
------------------------------
1. Install
------------------------------
* pip Install
   ``pip install vgif -U``
* source Install
   1. Clone this repository
   2. Run setup from the repository root directory
        ``python3 setup.py install``
2. Start UP
------------------------------
🅶 GUI
------------------------------
.. image:: https://github.com/Haoke98/video2gif/raw/master/assets/interface.png
        :width: 600px

1. Start interface::

       vgif-gui



2. Select video file
3. Set options
#. Click button "Start" to start
#. Once started converter will save the output under the same folder ad source video
#. Click button "ReStart" to re-start this process
#. Click button "Exit" to end this program.

The options includes:

* Video Sample Rate : (default sample every 10 frame)
* Output GIF FPS: Set output GIF fps(default 10 fps)
* Video Resize Rate: Shrink video n times smaller (default 2 times smaller)

🅲 CMD
------------------------------
* Usage ::

         vgif [OPTIONS]::

            Converts video to GIF.

         Options:
            -i, --input PATH         input video file
            -o, --output TEXT        output gif file path and name.
            -s, --scale INTEGER      Scale the factor for frame_x and frame_y.
            -r, --resolution TEXT    The resolution factor for factor ( For Compress ),
                              like 1920x1080.

            -fps, --gif-fps INTEGER  The fps of the GIF.
            --help                   Show this message and exit.

*  Just Give the Input::

        vgif -i /myLocalDir/myVideo.mov

      This will generate the GIF with the same name to the same directory as the original file.


* Give the file path for out.::

          vgif -i /myLocalDir/myVideo.mov -o /some_dir/out.gif

