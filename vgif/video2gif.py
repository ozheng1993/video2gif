#!/usr/bin/env python
# ou zheng
# 2020/1.2
import os

import cv2
import imageio
import click

skipRate = 30


@click.command(name='A script that converts video to GIF.', help='Converts video to GIF.')
@click.option('-i', '--input', type=click.Path(exists=True), default='../video/demo.mov', help='input video file',
              prompt='Enter path of the video file to convert to GIF.')
@click.option('-o', '--output', help='output gif file path and name.')
@click.option('-s', '--scale', type=click.INT, default=1, help="Scale the factor for frame_x and frame_y.")
@click.option('-r', '--resolution', help="The resolution factor for factor ( For Compress ), like 1920x1080.",
              default="0x0")
@click.option('-fps', '--gif-fps', type=click.INT, default=10, help="The fps of the GIF.",
              prompt="Enter the fps of the GIF.")
def main(input: str, output: str, scale: int, resolution: str, gif_fps: int):
    videoName = input
    if output:
        outName = output
    else:
        out_dir = os.path.dirname(videoName)
        outName = os.path.join(out_dir, videoName[:-3] + 'gif')
    print("out:", outName)
    d_size = (0, 0)
    if resolution:
        r_x, r_y = resolution.split("x")
        d_size = (int(r_x), int(r_y))

    print("resolution:", d_size)
    cap = cv2.VideoCapture(videoName)
    videoWidth = cap.get(3)
    videoHeight = cap.get(4)
    videoFps = cap.get(5)
    print("video original fps:", videoFps)
    frameTotal = cap.get(7)
    frameForOutput = frameTotal / skipRate

    with imageio.get_writer(outName, duration=1 / gif_fps, mode='I') as writer:
        framerCounter = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                print("finished")
                break
            framerCounter += 1
            if framerCounter % 10 == 0:
                frame = cv2.resize(frame, d_size, fx=scale, fy=scale)
                cv2.imshow('frame', frame)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                writer.append_data(frame)
                print("ETA-", round((framerCounter / frameTotal) * 100, 2), "%")
            else:
                continue

            if cv2.waitKey(1) == ord('q'):
                break
    cap.release()


if __name__ == '__main__':
    main()
