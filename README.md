# IP-OpenCVPython
Image Processing using open souce OpenCV python library. Python version used 3.7

> # GETTING STARTED

## Installing OpenCV 4.0.0

There are two ways of installing OpenCV
| SNO  | TYPE  |  LEVEL |
|---|---|---|
| 1 | Installing using `pip`  | EASY  |
| 2 | Building from source  | INTERMEDIATE  |

> ## #1.1 Installing OpenCV using pip to work with python3

| Commands  |
|---|
| `sudo apt update`  |
| `sudo apt upgrade`  |
| `sudo apt install python3-pip`  |

>## #1.2 Installing OpenCV using default debian package manager `apt`

| Commands  |
|---|
| `sudo apt update`  |
| `sudo apt upgrade`  |
| `sudo apt install libopencv-dev`  |


> ## #2 Building OpenCV from source to use with python3

| Commands - STAGE #1  |
|---|
| `cd`  |
| `sudo apt update`  |
| `sudo apt upgrade`  |
| `sudo apt-get install build-essential cmake unzip pkg-config`  |
| `sudo apt-get install libjpeg-dev libpng-dev libtiff-dev`  |
| `sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev`  |
| `sudo apt-get install libxvidcore-dev libx264-dev`  |
| `sudo apt-get install libgtk-3-dev`  |
|  `sudo apt-get install libatlas-base-dev gfortran` |
| `sudo apt-get install python3-dev`  |

> ----------------------

| Commands - STAGE #2  |
|---|
| `cd`  |
| `wget -O opencv.zip https://github.com/opencv/opencv/archive/4.0.0.zip`  |
| `wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.0.0.zip`  |
|  `unzip opencv.zip` |
| `unzip opencv_contrib.zip`  |
| `mv opencv-4.0.0 opencv`  |
| `mv opencv_contrib-4.0.0 opencv_contrib`  |

| Commands - STAGE #3  |
|---|
| `wget https://bootstrap.pypa.io/get-pip.py`  |
| `sudo python3 get-pip.py`  |
| `sudo pip install virtualenv virtualenvwrapper`  |
| `sudo rm -rf ~/get-pip.py ~/.cache/pip`  |

> V IMP : step

`cd`
`sudo apt install nano`
`nano ~/.bashrc`

```sh
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

Add these lines at the `end` of the file .bashrc

press `ctrl + X` and then `Shift + Y` to save and exit.

IMP command:

 > `source ~/.bashrc`

 | Commands - STAGE #4  |
|---|
| `mkvirtualenv cv -p python3`  |
| `workon cv`  |
| `pip install numpy`  |
| `cd ~/opencv`  |
| `mkdir build`  |
| `cd build`  |

> V IMP OBSERVE THE USE OF CMAKE
 This command should be executed inside the build folder.

 ```sh
 cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D INSTALL_C_EXAMPLES=OFF \
	-D OPENCV_ENABLE_NONFREE=ON \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	-D PYTHON_EXECUTABLE=~/.virtualenvs/cv/bin/python \
	-D BUILD_EXAMPLES=ON ..
 ```

 > EPIC Command - wait till I say

 `make -j4`

| Command - #LAST STAGE  |
|---|
| `sudo make install`  |
| `sudo ldconfig`  |


> ### V IMPORTANT STEP

` cd /usr/local/python/cv2/python-3.5`
` sudo mv cv2.cpython-35m-x86_64-linux-gnu.so cv2.so`
`cd ~/.virtualenvs/cv/lib/python3.5/site-packages/`
`ln -s /usr/local/python/cv2/python-3.5/cv2.so cv2.so`

> ### Verifying our installation

$  `workon cv`

$ `python`

` >>> import cv2`

` >>> cv2.__version`

