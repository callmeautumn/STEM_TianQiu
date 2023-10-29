# Drawing Task Instructions 

## Make your own sketch 

Use the file explorer on the left to copy and paste a new version of the file ``seed.py``. Give it a new name! You can do this by right clicking and selecting ``Rename``.

### Install `openCV`

In the terminal (bottom window), run

```
pip install opencv-python
```

### Run the file

Click the play button in the top right when your new `.py` file is open, it should open a separate window with a rectangle in it. 

Press `q` whilst the window is in focus to quit. You should kill the window **before** you re-run the code to see changes. 

## Task 1 - Pictionary 

This task is adapted from [Angi Chau](https://teach.angichau.com/starter-kit-for-teaching-with-p5-js/drawing-colors-collapsible/). 

The task here is to draw the prompt you are given by this [generator](https://mimicproject.com/code/c16ba573-f345-f03a-f5fe-1f603d16b262?embed=true&showCode=false) using the shapes available in the openCV [drawing functions](https://docs.opencv.org/4.x/dc/da5/tutorial_py_drawing_functions.html). 

The main ones to try are 

* ```rectangle(an.canvas, (top_left_x, top_left_y), (bottom_right_x, bottom_), color, border_weight (-1 for fill))```

* ```line(an.canvas, (x1,y1), (x2, y2), color, line_weight)```

* ``circle(an.canvas, (centre_x, centre_y), radius, color, border_weight (-1 for fill))``

* ```polylines(an.canvas, [[[x1, y1],[x2,y2],...[xn, yn]]], True, color, border_weight (-1 for fill))```

You should put all your code under the `def setup(self):` function

Happy Drawing! 

Make a screen shot and add your picture to the padlet when you are done!

Take a look at others pictures on the padlet, can you guess the prompt? Remember it must be from the original [list]([https://artslondon-my.sharepoint.com/:x:/g/personal/l_mccallum_arts_ac_uk/Efa_G4cWLndMlYHtDsgqhccBjH-g6yYHbweHHCvwE8PW3w?e=0U2xDk]). Add in a comment with your guess!

## Task 2 - Make it move

We are now going to add some movement into our sketches! You can choose to either animate part of your existing Pictionary sketch, or start from scratch. 

There are two main ways we can add some animation to our sketches, and in both cases we will be able to test out our skills with ``if statements``

In both cases, we will also be adding our drawing into the `def draw(self):` function. This gets called repeatedly on a loop, so our drawing can keeping get refreshed. Below we detail two approaches for how to update the shapes positions or colours.

### `an.background(colour)`

As we are drawing new things every frames, we might want to overwrite the old stuff! We can do this by calling `an.background()` and passing in the colour we want the background to be

```
def draw(self):
    an.background((255,0,0))
```

### Time

The ``Animator`` object (stored in the `an` variable), has two properties that we can use to determine how much time has passed from the start of the sketch. Think of these are `variables` that belong to the object.

`an.millis` tells us how many milliseconds have passed. `an.frame` tells us how many frames have passed (e.g. how many times the ``draw()`` function has been called). 

This code changes the colour of the circle drawn every 30 frames. It makes use of the `%` (modulo) operator which returns the remainder of the division between the two operators. 

This is useful when we have a number that is always rising (e.g `an.frame`) and we want it to loop back to zero after a given maximum.

```
def draw(self):
    an.background((0,0,0))
    colour = (255,0,0)
    if an.frame % 60 > 30 :
        colour = (255,0,255)
    circle(an.canvas, (an.width//2, an.height//2), 100, colour, -1)
```

### Mouse position 

We also can use `an.mouse_x` and `an.mouse_y` to get the current mouse coordinates

Here we change the colour of the circle depending on which half of the screen the `mouse_x` is in.

```
def draw(self):
    an.background((0,0,0))
    colour = (255,0,0)
    if an.mouse_x < an.width/2:
        colour = (255,0,255)
    circle(an.canvas, (an.width//2, an.height//2), 100, colour, -1)
```

### TRY ADDING SOME MOVEMENT TO YOUR OWN SKETCH!
