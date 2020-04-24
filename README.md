# Real-Time-Multiple-Face-Detection-of-Pedestrian

Object Detection using Haar feature-based cascade classifiers is an effective object detection method proposed by Paul Viola and Michael Jones in their paper, “Rapid Object Detection using a Boosted Cascade of Simple Features” in 2001. It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images.

## Real time detection can be use via command prompt or GUI.

<table>
  <tbody>
	<tr align="center">
		<th><strong>A USA Real-Time Road Detection</strong></th>
	</tr>
	<tr align="center">
		<td><img src="https://github.com/muhammadshiraz/YOLO-Real-Time-Object-Detection/blob/master/doc/detector1.gif"></td>		
	</tr>
	<tr align="center">
		<th><strong>A UK Real-Time Road Detection</strong></th>
	</tr>
	<tr align="center">
		<td><img src="https://github.com/muhammadshiraz/YOLO-Real-Time-Object-Detection/blob/master/doc/detector2.gif"></td>
	</tr>
	<tr align="center">
		<th><strong>A Real-Time Webcam Detection</strong></th>
	</tr>
	<tr align="center">
		<td style="width: 100%;"><img src="https://github.com/muhammadshiraz/YOLO-Real-Time-Object-Detection/blob/master/doc/webcam_detector.jpg"></td>
	</tr>
</tbody>
</table>

Yolo is a deep learning algorythm which came out on may 2016 and it became quickly so popular because it’s so fast compared with the previous deep learning algorythm.
With yolo we can detect real time objects at a relatively high speed. With a GPU we would be able to process over 45 frames/second while with a CPU around a frame per second.

OpenCV dnn module supports running inference on pre-trained deep learning models from popular frameworks like Caffe, Torch and TensorFlow.

## Requirement
<ul>
<li>OpenCV 4.2.0</li>
<li>Python 3.6</li>
</ul>

## Quick start
<ul>
  <li>Download official <a href="https://pjreddie.com/media/files/yolov3.weights" rel="nofollow">yolov3.weights</a> and place it under a folder called weight.</li>
  <li>Download official <a href="https://pjreddie.com/media/files/yolov3-tiny.weights" rel="nofollow">yolov3-tiny.weights</a> and place it under a folder called weight.</li>
  <li>Download <a href="https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg">yolov3.cfg</a> and place it under a folder called cfg.</li>
  <li>Download <a href="https://github.com/pjreddie/darknet/blob/master/cfg/yolov3-tiny.cfg">yolov3-tiny.cfg</a> and place it under a folder called cfg.</li>
</ul>

## Dependencies
<ul>
<li>opencv</li>
<li>numpy</li>
</ul>

## Install dependencies
<p><code>pip install numpy opencv-python</code></p>

## How to use?
<ol>
  <li>Clone the repository</li>
  <p><code>git clone https://github.com/muhammadshiraz/YOLO-Real-Time-Object-Detection.git</code></p>
</ol>
<ol start="2">
  <li>Move to the directory</li>
  <p><code>cd YOLO-Real-Time-Object-Detection</code></p>
</ol>
<ol start="3">
  <li>To view the UK Real-Time Road Detection</li>
  <p><code>python real_time_yolo_detector1.py</code></p>
</ol>
<ol start="4">
  <li>To view the USA Real-Time Road Detection</li>
  <p><code>python real_time_yolo_detector2.py</code></p>
</ol>
<ol start="5">
  <li>To use in real-time on webcam</li>
  <p><code>python real_time_yolo_webcam.py</code></p>
</ol>

## Graphical User Interface:
#### A USA Real-Time Road Detection
<img src="https://user-images.githubusercontent.com/45601530/79018190-a4dff500-7b8c-11ea-8866-119735d7c8fc.jpg">

#### A UK Real-Time Road Detection
<img src="https://user-images.githubusercontent.com/45601530/79018201-aad5d600-7b8c-11ea-9844-b93a98fd0e00.jpg">

#### A Real-Time Webcam Detection
<img src="https://github.com/muhammadshiraz/YOLO-Real-Time-Object-Detection/blob/master/doc/webcam_detector.jpg">
