# Dolphin Freelook Manipulator For Blender 2.8
This is a little tool for Blender 2.8 that allows your freelook camera to be synced up to your active camera in Blender.

## What?
Yeah, you know that dolphin has a feature where can freely look around and stuff. Controlling freelook from Blender can benefit an couple more advanced elements in the tool such as cinematic camera animation, orthographic scale, perspective FOV, switching between orthographic and perspective, etc. 
Here are some examples of what you can do with this:<br>
<img src='https://github.com/John10v10/Dolphin-Freelook-Manipulator-For-Blender-280/blob/master/TutImg/m.gif?raw=true'/>
<img src='https://github.com/John10v10/Dolphin-Freelook-Manipulator-For-Blender-280/blob/master/TutImg/n.gif?raw=true'/>
<img src='https://github.com/John10v10/Dolphin-Freelook-Manipulator-For-Blender-280/blob/master/TutImg/p.gif?raw=true'/>
<img src='https://github.com/John10v10/Dolphin-Freelook-Manipulator-For-Blender-280/blob/master/TutImg/q.gif?raw=true'/>

## How to Install the Script into Blender
First, download this python script of course.
Second, open Blender 2.8.
In Blender, there are multiple tabs on the top. Click the tab that's labeled "Scripting".<br>
<img src='https://github.com/John10v10/Dolphin-Freelook-Manipulator-For-Blender-280/blob/master/TutImg/a.png?raw=true'/>

In the text editor, click "Open".<br>
<img src='https://github.com/John10v10/Dolphin-Freelook-Manipulator-For-Blender-280/blob/master/TutImg/b.jpg?raw=true'/>

So to wherever you downloaded the python script, select it, and then click "Open Text".<br>
<img src='https://github.com/John10v10/Dolphin-Freelook-Manipulator-For-Blender-280/blob/master/TutImg/c.jpg?raw=true'/>

If you see a ton of colorful code, then you did good things. Now click "Run Script".<br>
<img src='https://github.com/John10v10/Dolphin-Freelook-Manipulator-For-Blender-280/blob/master/TutImg/d.jpg?raw=true'/>

Now let's go back to the "Layout" tab.<br>
<img src='https://github.com/John10v10/Dolphin-Freelook-Manipulator-For-Blender-280/blob/master/TutImg/e.jpg?raw=true'/>

And you can see a skinny panel. Stretch it out a bit so you can see the options more clearly.<br>
<img src='https://github.com/John10v10/Dolphin-Freelook-Manipulator-For-Blender-280/blob/master/TutImg/f.jpg?raw=true'/>

There we go. :)<br>
<img src='https://github.com/John10v10/Dolphin-Freelook-Manipulator-For-Blender-280/blob/master/TutImg/g.jpg?raw=true'/>

Now in Dolphin, go to the graphics configuration.<br>
<img src='https://github.com/John10v10/Dolphin-Freelook-Manipulator-For-Blender-280/blob/master/TutImg/o.jpg?raw=true'/>

Inside that window, go into the "Advanced" tab and click "Copy View Matrix Access Code" (These features have not been released, hopefully just not yet). Also be sure to have "Free Look" and "External Control Free Look" checked.
This button copies the access code to your clipboard.<br>
<img src='https://github.com/John10v10/Dolphin-Freelook-Manipulator-For-Blender-280/blob/master/TutImg/h.jpg?raw=true'/>

Back in Blender, paste (Ctrl+V) the access code to the field.<br>
<img src='https://github.com/John10v10/Dolphin-Freelook-Manipulator-For-Blender-280/blob/master/TutImg/i.jpg?raw=true'/>

Finally, press "Go Live!".<br>
<img src='https://github.com/John10v10/Dolphin-Freelook-Manipulator-For-Blender-280/blob/master/TutImg/j.jpg?raw=true'/>

Yay! You should be able to control the "Free Look" view in Dolphin from the camera in Blender... Only now there's one problem... sometimes, the screen may go black. Why is that? Because you're probably looking away from all the objects in the game and just staring into the void.
Select the camera here:<br>
<img src='https://github.com/John10v10/Dolphin-Freelook-Manipulator-For-Blender-280/blob/master/TutImg/k.jpg?raw=true'/>

Reset the position (Alt+G) and rotation (Alt+R) of your camera, then rotate the camera by 90 degrees along the global X axis. You should be seeing the stage if done correctly.
<img src='https://github.com/John10v10/Dolphin-Freelook-Manipulator-For-Blender-280/blob/master/TutImg/l.jpg?raw=true'/>
