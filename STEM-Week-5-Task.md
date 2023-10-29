# STEM 4 Creatives Week 5 Task

## MusicAnalyser.py (and Animator.py again)

We are going to use the things we now know about audio waves and analysis, and the things we already know about drawing shapes to do two tasks. 

In combination with ``Animator.py``, we will use ``MusicAnalyser.py``. This will load in an audio file, complete some analysis (including FFT!) and start playing the audio back. 

In realtime, the current audio analysis information is available in sync with the music playback. This allows us to do some cool audio visuals!

## Task 1 Draw a waveform 

The first task is a static one so we will be staying in ``def setup(self):``. 

Your task is to draw a waveform. Thats it! Whilst this might seem easy, there is loads of creative and stylised ways to do this beyond just drawing the waveform sample by sample.

The audio data for the file you have loaded in is stored in `mus.y`. It contains **all the samples**. However, we might want squish some of the samples together and for this we can use ``windowing``. 

```
window_size = 1024
num_buffers = len(mus.y)//window_size
#Do this code to every buffer
for i in range(num_buffers):
    start = i*window_size
    end = (i+1)*window_size
    buffer = mus.y[start:end]
    mean = np.abs(buffer.mean())
```

Here are some examples to inspire! 

* [Open Processing](https://openprocessing.org/browse/?time=anytime&type=all&q=waveform#)

Some starter code can be found in ``seed_audio.py``. Copy this and starting working on your own!

### New Drawing Tip: Use alpha (transparency)

Instead of drawing to ``an.canvas``, you can draw to ``an.to_alpha(0.4)`` to make your shapes have transparency (or alpha)!

The ``to_alpha()`` function returns a new canvas that gets rendered and blended appropriately, accepting one argument from 0 (invisible) to 1 (fully opaque).

```
rectangle(an.to_alpha(0.3), (0,0), (100,100) (255,0,0), -1)
```

## Task 2 Make an FFT visualiser 

You can also get access to the current FFT information in the `def draw(self):` function. The `mus.fft_vals` variable is updated as the music plays. It is an array with 1024 values, each showing the power of a particular frequency bin. Low values at the bottom, high at the top.

So, we can use a `for loop` to iterate through that list, and visualise the spectrum. If we do this in the `def draw(self):` function, and use `an.background()` to overwrite at the start each time, we will have an animation that changes in time to the music!

```
def draw(self):
    an.background(0)
    for i,val in enumerate(mus.fft_vals):
        x = i*2
        y = an.height-int(val*100)
        line(an.canvas, (x, an.height), (x,y), (0,255,0), 1)
```

Maybe consider using `an.frame` to make is change further over time, or using a `if statement`, so your visualiser changes when a particular threshold is passed.

Here are some examples to inspire! 

* [Open Processing](https://openprocessing.org/browse/?time=anytime&type=all&q=fft#)

Some starter code can be found in ``seed_fft.py``. Copy this and starting working on your own!

### New Drawing Tip: Class Variables 

Currently, all the variables we declare are only either in the ``setup()`` function **or** the ``draw()`` function. And they only exist for **one loop of the draw function**. 

We can add variables that belong to the ``MySketch`` class and can be accessed and overwritten from **any function within it**. This might be useful if we want to know what happened in a previous frame to effect what we draw in the current frame!

We define them at the top of the class and refer to them in the functions using the `self.` prefix. The example below makes a class variable called ``show_beat``, which can then be accessed and changed in the ``draw()`` function using ``self.show_beat``

```
class MySketch:

    show_beat = 0

    def __init__(self):
        an.start_loop(self.setup, self.draw)           
        
    def setup(self):
        print("setup")
        
    def draw(self):
        col = (0,0,0)
        if mus.is_beat():
            self.show_beat = 10
        
        if self.show_beat > 0:
            col = (255,255,255)
        
        an.background(col)
        self.show_beat -= 1

MySketch()  
```