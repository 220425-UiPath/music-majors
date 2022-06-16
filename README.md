# music-majors
A music bot to play Discord YouTube requests through a user's microphone.  

---
## Technologies Used
- [UiPath Studio 2020.10.7+](https://www.uipath.com/product/studio): Development environment.
- [UiPath Orchestrator](https://cloud.uipath.com/): Automation deployment.
- [Python 3.10+](https://www.python.org/downloads/): Language used to build bot for Discord.
- [VLC media player](https://www.videolan.org/vlc/): Application used for audio playback.
- [VoiceMeeter Banana](https://vb-audio.com/Voicemeeter/banana.htm): Virtual mixer to route audio.
- [Virtual Audio Cable](https://vb-audio.com/Cable/index.htm): Creates an audio bridge to assist with audio routing between applications.

---
## Features
- Takes video requests from Discord chat in the form of a YouTube link or a search string.
- Adds the request to a queue.
- Plays the requests retrieved from the queue using VLC media player.
- Accepts commands to control playback including pause/resume, skip, and change volume.

---
## Getting Started
### Building Automations
1. Use `git clone https://github.com/220425-UiPath/music-majors.git` to clone repository.
2. Open project.json for both dispatcher and performer and publish to Orchestrator.
4. Set up one robot to run the dispatcher process.
5. Set up a second robot to run the performer process, initially triggered by an item being added to the queue.
6. Update the config.xlsx for the performer process with the directory of VLC player on the machine.

### Audio Routing Setup
**It is strongly recommended to enable the `Run on Windows Startup` option in VoiceMeeter Banana since your computer's audio will be routed through the application.**
1. In VoiceMeeter Banana, set up routing as shown below. Replace `Hardware Input 1` with your primary microphone and `Hardware Out A1` with your primary playback device. The WDM driver is recommended for better latency.  
![Voicemeeter Banana Screenshot](https://i.imgur.com/fkT0gis.png)
2. In Windows Sound settings, navigate to the Playback tab. Set `VoiceMeeter Input` as `Default Device` and `VoiceMeeter Aux Input` as `Defaul Communication Device`.  
![Windows Sound Playback Screenshot](https://i.imgur.com/hSPTDgF.png)
3. Switch over to the Recording tab. Set `VoiceMeeter Output` as `Default Device` and `VoiceMeeter Aux Output` as `Default Communication Device`.  
![Windows Sound Recording Screenshot](https://i.imgur.com/TbbztDm.png)
4. Set input and output devices in your communication applications to either `Default Device` or `VoiceMeeter Aux Input/Output`.

---
## Contributors
- Warren Lee (Team Lead)
- Matthew Emsak (Scrum Master)
- Esther Parson
- Jonathan Barajas
- Ying Fan

---
## License
This project uses the following license: MIT.
