# STEM WEEK 8 Task 

## Exploring Audio

We're going to try and adapt the code you have been given in the lecture to explore and prepare a new audio dataset that you can find online. 

[Kaggle](https://www.kaggle.com/search?q=audio+in%3Adatasets) (make sure you get one that has .wav files, not already pre-processed audio features)

[DSAI Audio Sample Repo](https://git.arts.ac.uk/lmccallum/samples)

Once you have found your dataset, you will need to:

1. Split out the classes (are there multiple labels? Are the different classes in different folders or is there something in the file name that tells us? You can work on the ``glob`` to automatically read in the right files). If there is no clear way to split your dataset, you can compare two separate datasets (e.g. two of the folders from the [DSAI Audio Sample Repo](https://git.arts.ac.uk/lmccallum/samples)).

2. Load in the files 

3. Visualise a sub set. Are they similar in length? Are they the same number of channels?

4. What features in librosa are available to highlight differences between the audio files in your dataset?

5. How does the dataset change if you compare different statistics to compressing of the features of each set of frames (where previously we had done the `mean()`)? Consider `standard deviation`, `max` and `min` etc..

## Animating datasets

We're also going to look at different ways we can display and animate an image dataset in an interesting way. Take one of the example sketches as a starting point and develop into a new visualisation / animation. There are a bunch of possible approaches (non exhaustive!) listed below.

I've provided some code which uses the same `get_images` function from `mosaic.py` to load in all the images in a given file. It then shows a new random image very frame, which is quite intense. 

Here, we use the `paste()` function from the `PIL` Image library to copy the image we have randomly selected from the `self.dataset` into a given position `coords` on the canvas. 

```
new_canvas = Image.new('RGB', (an.width, an.height))
to_paste = self.dataset[np.random.randint(len(self.dataset))]
coords = (0,0)
new_canvas.paste(Image.fromarray(to_paste), coords)
an.canvas = np.array(new_canvas)
```
[Basic Image Cycle Example](seed_many_images.py)

Things you could try:

* Different datasets (obsv)

* Having the position of the image being drawn follow the mouse (`an.mouse_x` and `an.mouse_y`). If you don't overwrite the background (`an.background(0)`) at the top of your `draw()` loop, you will get a paint-brush style trail 

* When and how often to change the picture being drawn. Is it random, is it a sequence, is when the mouse passes over it? Is it not every frame? Is it when something else happens? `if` statements are your friend here

* Draw multiple pictures at once 
  
    * In a grid (using a nested for loop like in the mosaic from week 6)

        [Basic Image Cycle Example](seed_many_images_click_greed.py)

    * Or arranged another pattern (a circle?)

* Pictures in different sizes over time (use `an.frame` to be the driver here, remember to use `%` or `sin` to keep within a range)

[Bouncing Size Example](seed_many_images_resize.py)

* Pictures moving in certain directions over time (use `an.frame` to be the driver here, remember to use `%` or `sin` to keep within a range). Do they move in a straight line? Do they move in random directions? What happens when they reach the edge?

[Random Walk Example](seed_many_images_random_walk.py)




