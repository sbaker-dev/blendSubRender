# blendSubRender
Sub processing multiple instances of blender for rendering. When rending the general principle is applying more 
resources and completely the current frame is faster approach to getting the end result. Most of the time this works, 
but there are a few, additively niece cases, when it can be faster to subprocess an animation. 

For example, lets say you have a 10 seconds shot of 60 frames per second of a room that, apart from a television, is 
static. The television is showing an animated texture, cast as an emission texture which means it can quite effectively
be rendered at a single sample. In this case, you can render the whole scene once, and then use a lower poly scene and
a light capture the changes in light from the television. Now instead of render 600 frames at say 5000 samples, you 
instead render 1 shot at 5000 samples and then just capture the television at 1 sample. 

# Example

In this case a scene with image texture with a video taking up 100% of the scene was used in the cycles render. This 
used a single sample at 720p for 600 frames at 60 frames a second. All other settings where set their default values.
Each process was only run a single time though, and clearly timings are hardware specific so the raw numbers are less
important than the ratio's between them.

| Subprocess   | Time  | Relative to previous  |
|--------------|-------|-----------------------|
| 1            | 8.04  |      -                |
| 2            | 4.93  | 1.63                  |
| 3            | 3.26  | 1.51                  |
| 4            | 3.11  | 1.04                  |
| 5            | 2.77  | 1.12                  |
| 6            | 2.64  | 1.04                  |
| 7            | 2.51  | 1.05                  |
| 8            | 2.27  | 1.10                  |

As you can see adding even a single extra subprocess can speed these sort of tasks up significantly, and running three 
subprocess also brought a large return but then the relative benefit (on my system) reduces. But compared to running the
same process with just a single subprocess adding in at least 1 addition subprocess has been useful in my experience, so
i have made this available so you can use it as well if you want.

## blendSubRender
blendSubRender is available via Pypi so you can just pip install it, if your a windows user the following command can
be used from the terminal. Alternatively just download the files 

```shell script
python -m pip install blendSubRender
```

# How to use blendSubRender

Very simple, although you may need to dig through your directories. You need to find the path to the actual executable,
not the short cut, of your blender install so that this path can be used for sub-processing. You then also need to have
a path to the blend file that you are going to use. Set the blender_path, the blend_path and the end frame and your 
good to go. You may however, set the start frame, but it defaults to 1 and set the number of subprocess you want to use,
it defaults to 2. 

```python

from blendSubRender import BlendSubRender

if __name__ == '__main__':
    blender_path = r"path_to_blender\blender-2.82-windows64\blender"
    blend_path = r"path_to_your_blend_file\BLEND_FILE.blend"
    BlendSubRender(blender_path, blend_path, 700, start_frame=100, subproccess=8).sub_render()

```

This is it basically! Everything else, like the samples you want to use, the output directory and anything else should
be set within the .blend file itself. 

## License
Distributed under the MIT License. See `LICENSE` for more information.
