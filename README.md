# Cutting-streaming-video
Capturing frames from streaming video
## What you can do with this app
Receives frames from streaming video of public IP cameras
### What to do for this
- Create a directory for the program
- Clone the repo into it and set the virtual environment
- Create a folder for recording frames and write in the ip_cam.py file instead of 'frame' here: "frame \\
- Search the Internet for the URL of the available video stream, as in the ip_cam.py file, and paste it instead of the existing one
- 15000 in the code is the interval of 15 seconds between sliced frames. Change this value to increase or decrease the spacing. Change the number of required frames as desired    (instead of '12')
- Run 'jupyter notebook' at the command line
- Open the specified page in the browser
- In the window that opens, click on the right 'New' and then 'Python 3'
- Paste the contents of the 'camweb' file (via cp) into the opened line 'input'
- Click 'Start'
- How many frames you specify, as many will be recorded in your folder
