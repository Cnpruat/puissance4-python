# ✈️ XPlane-Haptic-Interface

Spatial disorientation is a common issue in aviation, often leading to poor decisions and accidents. To address this, this project focus on enhancing situational awareness through intuitive haptic feedback.
This repository gathers two projects developed during my engineering internship. Both interact with the X-Plane flight simulator :

- A **Python program** that retrieves real-time flight data from X-Plane and triggers haptic feedback using the **bHaptics TactSuit X40**.
- A **C++ plugin** for X-Plane that displays an interactive window with buttons to trigger failures, adjust weather, or test control surfaces.
---

# 🏁 How to use

## Softwares
- Windows 10/11
- Python 3.13.5 (tested)
- Visual studio code (recommended)
- Microsoft visual studio (recommended)
- [bHaptics player](https://www.bhaptics.com/software/player/) 2.6.3.86 (86) (at least)
- XPlane 11/12 (tested)

## Requirements

All the librairies needed are listed in [requirements.txt](/python_interface/requirements.txt).
```bash
keyboard==0.13.5
pybind11==3.0.0
pygame==2.6.1
pygame_widgets==1.2.2
setuptools==80.8.0
websocket_client==0.57.0

tactcombine==0.1
```
### Standard librairies
You can install all the standard python libraries with :

```bash
pip install keyboard==0.13.5 pybind11==3.0.0 pygame==2.6.1 pygame_widgets==1.2.2 setuptools==80.8.0 websocket_client==0.57.0
```
### Custom librairy
Since `tactcombine` is a custom library, you will need to build it manually from the `python_interface/combine/` directory using pybind11 :

```bash
pip install ./python_interface/combine
```
The library will be added to your python PATH.

(A [precompiled version of the tactcombine library](/python_interface/combine/tactcombine.cp313-win_amd64.pyd) is also included for Windows. This allows immediate use without requiring compilation)

### Local SDK/plugin
You will also need the following dependencies :
#### Python
- [bHaptics python SDK](https://github.com/bhaptics/tact-python/) included [here](/python_interface/libs/bhaptics/)
- [XPlane connect Plugin](https://github.com/nasa/XPlaneConnect) included [here](/python_interface/libs/xpc) (Python)

#### XPlane
- [XPlane connect Plugin](https://github.com/nasa/XPlaneConnect) included [here](/Control_panel_XP/XPlaneConnect/) (XPlane plugin)

   Copy the [folder](/Control_panel_XP/XPlaneConnect/) into :

   ```
    C:\X-Plane 12\Resources\plugins
   ```

## Python Program
### Run the application
1. The bHaptics player needs to be launched first
2. Connect the TactSuit and launch XPlane
3. Run the [main program](/python_interface/main.py)

   ```bash
   python main.py
   ```

### Usage
- The GUI will automatically opens at launch
- Real-time flight data displayed
- Real-time haptic cues displayed


<p align="center">
   <img src="images/GUI_py.png" alt="Python GUI" width="850"/>
</p>

You can use the buttons to switch between the different operating logics. Three sliders allows you tu adjust the intensity of the vibrations as well as the roll and pitch activation threshold.

### Operating logics
The differents vibrating logics are implemented and can be modified through the `logic1.py`, `logic2.py`, `logic3.py` and `logic4.py` files.


## X-Plane Plugin
### Setup
You can either use the [pre-compiled plugin](/Control_panel_XP/plugin_output/plugin/control_panel/) and put it into :
  ```
   C:\X-Plane 12\Resources\plugins
  ```

  Or you can edit the [source code](/Control_panel_XP/control_panel.cpp) and compile it yourself :
1. Build the plugin using a C++ compiler with the [XPlane SDK](https://developer.x-plane.com/sdk/) included [here](/Control_panel_XP/SDK/)
2. Copy the compiled folder with the `.xpl` and `.pdb`files into :

   ```
    C:\X-Plane 12\Resources\plugins
   ```
3. Launch X-Plane and use the plugin

### Usage
- The control panel will automatically opens in XPlane
- Provides buttons to:
  - Trigger and reset failures (engine, bird strike, control surfaces)
  - Change weather conditions


<p align="center">
   <img src="images/controlpanel_xp.png" alt="XPlane control panel" width="250"/>
</p>


If you close the control panel, you can still re-open on the upper menu :
<p align="center">
   <img src="images/menu_xp.png" alt="XPlane control panel" width="400"/>
</p>

---
# 📁 Repository Structure

```
XPlane-Haptic-Interface/
│
├── python_interface/
    ├── assets/
    ├── combine/
    ├── libs/
    ├── patterns/
    └── main.py
├── control_panel_xp/
    ├── SDK/
    ├── XPlaneConnect/
    ├── plugin_output/
    └── control_panel.cpp
├── images/
├── .gitignore
└── README.md
```

---
# 👨‍🏭 Author


**Pierre Bourrandy**, 4th year Mechatronics Engineering student - **ENSIL-ENSCI**
This project was part of my internship at **IISRI**.

Thanks to **Mr. Houshyar Asadi** for the inspiring topic, support, and trust throughout the internship.

## Contact detail
pierre.bourrandy@etu.unilim.fr *(ENSIL-ENSCI)*

https://github.com/Cnpruat/XPlane-Haptic-Interface *(GitHub)*

