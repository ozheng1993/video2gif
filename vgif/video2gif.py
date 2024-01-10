#!/usr/bin/env python
#ou zheng
#2020/1.2
import os

import cv2
import imageio
import click

scale=0.25
skipRate=30
gifFps=10


@click.command(name='A script that converts video to GIF.', help='Converts video to GIF.')
@click.option('-i', '--input', type=click.Path(exists=True), default='../video/demo.mov', help='input video file', prompt='Enter path of the video file to convert to GIF.')
@click.option('-o', '--output', type=click.Path(exists=True), help='output gif file path and name.')
def main(input: str, output: str):
    videoName = input
    if output:
        outName = output
    else:
        out_dir = os.path.dirname(videoName)
        outName = os.path.join(out_dir, videoName[:-3] + 'gif')
    cap = cv2.VideoCapture(videoName)
    videoWidth = cap.get(3)
    videoHeight = cap.get(4)
    videoFps = cap.get(5)
    frameTotal = cap.get(7)
    frameForOutput = frameTotal / skipRate

    with imageio.get_writer(outName, duration=1 / gifFps, mode='I') as writer:
        framerCounter = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                print("finished")
                break
            framerCounter += 1
            if framerCounter % 10 == 0:
                frame = cv2.resize(frame, (0, 0), fx=scale, fy=scale)
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