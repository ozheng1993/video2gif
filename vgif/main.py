#!/usr/bin/env python
import PySimpleGUI as sg
from PIL import Image
import cv2
import io
import imageio
def loadVideo():
	filename = sg.popup_get_file('Filename to gif')
	return filename
def main():
	
	# ---===--- Get the filename --- #
	skipRate=3
	gifFps=10
	videoFile=loadVideo()
	# scale=0.5
	try:
		outFile=videoFile[:-3] + 'gif'
		cap = cv2.VideoCapture(videoFile)
		videoWidth=cap.get(3)
		videoHeight=cap.get(4)
		videoFps=cap.get(5)
		frameTotal = cap.get(7)
	except:
		print("cannot play")
		return

	sg.theme('Black')

	# ---===--- define the window layout --- #
	layout = [[sg.Text('OpenCV Demo', size=(40, 1), font='Helvetica 20',key='-text-')],
			  [sg.Image(filename='', key='-image-')],

			  [sg.Text('Video Sample Rate'),sg.Slider(range=(skipRate, 300),
						size=(60, 10), orientation='h', key='-slider-')],
			  [sg.Text('Output Gif FPS'),sg.Slider(range=(10, 60),
						size=(60, 10), orientation='h', key='-slider2-')],
			  [sg.Text('Video Resize Rate'),sg.Slider(range=(2, 10),
						size=(60, 10),orientation='h', key='-slider3-')],
			  [sg.Button('Start', size=(7, 1), pad=((600, 0), 3), font='Helvetica 14')],
			  [sg.Button('Restart', size=(7, 1), pad=((600, 0), 3), font='Helvetica 14')],
			  [sg.Button('Exit', size=(7, 1), pad=((600, 0), 3), font='Helvetica 14')]]

	# create the window and show it without the plot
	window = sg.Window('Demo Application - video2gif', layout, no_titlebar=False, location=(0, 0))

	# locate the elements we'll be updating. Does the search only 1 time
	image_elem = window['-image-']
	text_elem = window['-text-']
	slider_elem = window['-slider-']
	gifSliderElem = window['-slider2-']
	sizeSliderElem = window['-slider3-']
	
	# ---===--- LOOP through video file by frame --- #
	cur_frame = 0
	startProcess=False
	ret, firstFrame = cap.read()

	while True:
		event, values = window.read(timeout=0)
		if event in ('Start', None):
			startProcess=True
		if event in ('Exit', None):
			break
		if(startProcess==False):
			skipRate = int(values['-slider-'])
			gifFps = int(values['-slider2-'])
			scale = int(values['-slider3-'])
			slider_elem.update(skipRate)
			gifSliderElem.update(gifFps)
			sizeSliderElem.update(scale)
			firstFrameDisplay=cv2.resize(firstFrame,(0,0),fx=1/scale,fy=1/scale)
			framerCounter=0
			cap.set(cv2.CAP_PROP_POS_FRAMES, framerCounter)
			gifEstLenght="EST out put GIF length:"+ str(round((frameTotal/skipRate)/gifFps,2))+" s"
			text_elem.update(gifEstLenght)
			imgbytes = cv2.imencode('.png', firstFrameDisplay)[1].tobytes()  # ditto
			image_elem.update(data=imgbytes)
		else:
			eta="strating...."
			text_elem.update(eta)
			with imageio.get_writer(outFile, duration=1/gifFps, mode='I') as writer:

				while True:
					event, values = window.read(timeout=0)
					if event in ('Restart', None):
						break
					cap.set(cv2.CAP_PROP_POS_FRAMES, framerCounter)
					ret, frame = cap.read()
					if not ret:  # if out of data stop looping
						break
					framerCounter+=skipRate
					frame=cv2.resize(frame,(0,0),fx=1/scale,fy=1/scale)		
					imgbytes = cv2.imencode('.png', frame)[1].tobytes()  # ditto
					image_elem.update(data=imgbytes)
					frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
					writer.append_data(frame)
					eta="ETA-"+str(round((framerCounter/frameTotal)*100,2))+"%"
					text_elem.update(eta)
					slider_elem.update(skipRate)
					gifSliderElem.update(gifFps)
					if cv2.waitKey(1) == ord('q'):
						cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
						startProcess=False
						break
			# 
			startProcess=False
	cap.release()













	
main()