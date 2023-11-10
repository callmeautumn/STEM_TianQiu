# Week 7 Working With Video

This week we are going look at 

* While loops


* OpenCV


* Background Subtraction 


* Thresholding 


* Circular Buffers


* Running Averages 


* Face and Eye Tracking + Making our own filters!
 
### Getting the webcam feed

[Video Capture Example](STEM-Week-7-Video-Capture.py)

#### ```cv2.VideoCapture()```, ```.read()```

We can use the ``VideoCapture`` object to pull in new frames from the webcam. The ``.read()`` function returns us a new image (which we store in the variable ``camera_feed``), and a **boolean** value telling us whether it worked or not (which we store in the variable ``success``). We convert back to RGB colour space, resize to the size of the ``an.canvas`` and overwrite it so it gets displayed in the window.


#### A note on frame rate

There is a time cost to grabbing a frame from the webcam. 

There is also some time introduced by use analysing the frame, or editting it somehow.

All of this introducing latency until we can go back to the top of the ``def draw():`` function to get another frame. Depending on how complicated the calculations we are doing are, depends on how quickly we can get a new frame. 

The amount of new frames we can grab in a second is known as the **Frame rate**. 

### Background Subtraction

[Background Subtract Example](STEM-Week-7-Video-Background-Subtract.py)

To detect movement, or new objects or people in a frame, one technique we can use is **Background Subtraction**. 

Here, we subtract all of the pixel values from the current frame from all of the pixel values from a background frame. 

Whats left is anything that has changed! We can save the the first frame in the ``background`` variable and use this to compare to the new frame next time around.

We can use the ``cv2.absdiff()`` function to do this. 

![alt text](images/background_subtract.png)

#### Absolute Difference 

When subtract one thing from another, there are 3 possible outcomes 

1. 0 (if they are the same)


2. A positive number (if the first number is bigger than the second)


3. A negative number (if the first number is bigger than the second)


If all we care about is **how much things are different**, not which direction, we use the ``absolute difference``. The result of this calculation is **always positive**

You will see that this doesnt actually work that well, we more see an imprint of the background image over the new video frames. How do we know that the person in the foreground in the new thing thats moving at the background is remaining constant?

### Thesholding

[Threshhold Example](STEM-Week-7-Video-Threshhold.py)

If what we intend to do is eventually identify whole objects automatically, often it helps to move into a binary world. Things are either **old / part of the background** (0) or they are **new** (255). 

Small changes are often not new objects, just small differences caused by noise in the camera, shadows, changes in lights. We can set a **threshold** where any changes larger than this become 255, and anything lower than this are set to 0.

![alt text](images/background_subtract_noise.png)


We can do this in OpenCV using the ``cv2.threshold()`` function. We lose all the small changes, and keep the big ones (over the threshold).

![alt text](images/threshold.png)

### Experiment

Try the code below and change the ``threshold`` value. See it effects what gets filtered out. What happens when you set it 0? What about 255?

## Using a Model 

What do we mean when we say **background**?

Previously, this has just been how the world when we turned on the camera (the first frame). Often, we want to avoid small changes to the background when doing our subtraction, and even incorporate new things that have changed (and become the background) over time. 

In this case, we want to build some kind of model of our background over time. One approach is to take **an average of the camera feed over a given window**. Anything that hangs around long enough becomes part of the background!

### Circular Buffer

[Circular Buffer Example](STEM-Week-7-Video-Circular-buffer.py)

The approach towards this we'll see is by collecting all the frames into a new list as they come in. Then each time, we'll get the ``mean`` of these frames and us that to subtract the new camera data against. 

The data structure we'll use is a ``Circular Buffer``. This just means we have a list of a pre-defined length and each time we get new data, we are adding it into a point in the list that contains the oldest piece of data. 

This means we always have a list / buffer of the most recent frames and are constantly overwriting old data as it becomes less relevant.


![alt text](images/circularbuffer.png)

In the code, we have a pointer that moves forward each time telling us where the new data goes. We use the ``modulo (%)`` function to wrap back round to the beginning when we go off the end.

### Experiment

Try the code below and change the ``window_size`` value. See how it effects what gets filtered out. What happens when its 2 (very short memory). What happens when its 100 (long memory)?

Change the ``an.canvas = `` part of the code to display ``self.model`` instead of the thresholded image. Watch it gradually update over time.

### Running Average

[Running Average Example](STEM-Week-7-Video-Running-Average.py)

The circular buffer works fine but is **not very efficient**. Depending on our ``window_size``, we might be holding any number of frames in memory and calculating a new average from all of them **every frame**!

There is a way we can estimate this without having to literally store a history of previous frames, this is known as a ``Running Average``

Here, we subtract a **small percentage** of the model from itself (removing some history) and add a small percentage of the new data to the model. This means we are always **forgetting old data and adding some new data**. 

You will see that video runs smoother. This is because the computation done with each frame is more effcient, so we get back to top of the while loop sooner. This means we are grabbing frames more regularly (a higher frame rate).

### Experiment

Try the code below and change the ``window_size`` value. See how it effects what gets filtered out. What happens when its 2 (very short memory). What happens when its 100 (long memory)?

Change the ``an.canvas = `` part of the code to display ``self.model`` instead of the thresholded image. Watch it gradually update over time.

How is it different to the circular buffer approach?

### Task 1 (complete in pairs)

Run through the ``Experiments`` in the above code

### Task 2 (complete in pairs)

Check out these 3 camera based sensing methods. They all run in the browser (Try Firefox or Chrome!)

* How well do they work?

* What parts / actions / conditions are they good at tracking?

* What makes them fail? Obscuring things with objects, different lights, multiple people / faces/ hands, moving quickly?


1. [MoveNet](https://mimicproject.com/code/8a60a7b7-6277-2b4f-8aae-389f7b49ca1c?embed=true)


2. [FaceMesh](https://mimicproject.com/code/8aa114c7-3e87-5ef6-e81e-151c5cd9a38a?embed=true)


3. [HandTrack](https://mimicproject.com/code/d1c15d10-1071-a6a2-ac9c-82447150d771?embed=true)


## Make your own filter

[Face Filter Example](STEM-Week-7-Video-Face-Filter.py)

Here we have some Python code to get the ``bounding boxes`` (x and y coordinates, width and height of object) for faces

We can use this information, and the drawing functions of OpenCV, to add some face based animations to our camera!

As we are using the ``Animator.py`` we can use the openCV drawing functions we have used before

``cv2.rectangle()``, ``cv2.line()``,``cv2.circle()``,``cv2.polygon()``,``cv.putText()``


### Task 3 

Use the shape functions in OpenCV to draw some accessories to your camera feed 


* Sunglasses?


* A Crown?


* A halo?


* New hair?


* Alien Attena?


* Cartoon eyes?

