```
FFFFF FFFFF DDDD  IIIII RRRR  
F     F     D   D   I   R   R 
F     F     D   D   I   R   R 
FFF   FFF   D   D   I   RRRR  
F     F     D   D   I   R R   
F     F     D   D   I   R  R  
F     F     DDDD  IIIII R   R 
                  By: SeagullisLearningToCode
=============================================
NOTE: CODE REQUIRES FFMPEG
Documentation here: https://ffmpeg.org/ffmpeg.html
```

# Optionals (might be needed for some functions to work)
Module/Program | Download |
-------|----------|
Pygame | https://www.pygame.org/news |
MPV | https://mpv.io/ |

## Reuse
The only thing you need to worry about when comes to reusing my code is my framework
all that you need to do is just mention me in your code

## Convert files from directory
This simple script using my framework (Gull Framework), makes it easier to use ffmpeg
in which gets any files from given directory than converts to given output
<br/>
<br/>
Examples (comments like `# ;` is just pseudo-code for a comment in actual python use `#` instead)
```python
# ;                           Don't use filename as output (uses a counter instead)
# ;                                      |
# ;                                      |        Add a new extentsion to the filter list
# ;   Input     Output                   |                   |
ffdir(default, "music/Results", outputNameBeInput=False, addExt=[".wav"]).advancedSettings("-ar 2048", ".wav")
# ;                                                                              |           |   Hz
# ;                                                                              |           |   /        
# ;                                                                              |       audio rate
# ;                                                                              |
# ;                                                              Use commands provided by ffmpeg
```
Note here that if you use this alone that you won't be able to test the file using `ffdir.playinmpv()` unless you give it this...
```python
# Use this
#    |
sampleVar = ffdir(default, "music/Results", outputNameBeInput=False, addExt=[".wav"]).advancedSettings("-ar 2048", ".wav")
sampleVar.playinmpv() # Tries to run mpv from commandline from the output directory, if it can't returns as ProcessError
```
This needs mpv to be installed to use `sampleVar.playinmpv()`

### Global args
These Arguments are optional to use and doesn't require it to be called

Argument-var | Argument | Types | Description |
-------------|----------|-------|-------------|
self.debugPrint | "debugMode" | `bool` | Prints everything that calls `sps(condition=self.debugPrint)` see `GF.py` in `data/frw/` for what it does. (def. `False`)
self.outputFileNameAsOutputFile | "outputNameBeInput" | `bool` | Names the output file name as the original file. (def. `True`)
self.useUserDirectory | "useUserDirectory" | `bool` | Uses the user directory (def. `True`)
self.addExtentsions | "addExt" | `string` or `list of strings` | Takes the value/s from arg and appends (adds) it to the filter list (def. `None`)
self.clearDefaultExtensions | "clearExt" | `bool` or `int` | Clears or Clears part of the list, it safe to use `"addExt`" with this (def. `None`)

### Functions
anything with this `**` contains optional arguments and to find what argument are there look in `main.py`

Function | Arguments | Description |
---------|-----------|-------------|
self.runProc | `**rp` | This is more Advanced way of doing this
self.setResolution | `x`: (int), `y`: (int), `**sargs` | a simplified way of up/down-scaling videos or photos
self.setBitRate | `**sbrargs` | sets the bitrate to a video or audio (use both args if you want to change the video and audio)
self.playinmpv | N/A | plays the output directory (need mpv to be installed)
