# music-majors
Project 2: Music bot to play Discord YouTube requests through user's microphone.  

---
Contributors:
- Warren Lee (Team Lead)
- Matthew Emsak (Scrum Master)
- Esther Parson
- Jonathan Barajas
- Ying Fan

---
## Required Software
- [Python 3.10+](https://www.python.org/downloads/)
- [VLC media player](https://www.videolan.org/vlc/): Used for audio playback.
- [VoiceMeeter Banana](https://vb-audio.com/Voicemeeter/banana.htm): Virtual mixer to route audio.
- [Virtual Audio Cable](https://vb-audio.com/Cable/index.htm): Creates an audio bridge to assist with audio routing between applications.

### Audio Routing Setup
**It is strongly recommended to enable the `Run on Windows Startup` option in VoiceMeeter Banana since your computer's audio will be routed through the application.**
1. In VoiceMeeter Banana, set up routing as shown below. Replace `Hardware Input 1` with your primary microphone and `Hardware Out A1` with your primary playback device. The WDM driver is recommended for better latency.  
![Voicemeeter Banana Screenshot](https://i.imgur.com/fkT0gis.png)
2. In Windows Sound settings, navigate to the Playback tab. Set `VoiceMeeter Input` as `Default Device` and `VoiceMeeter Aux Input` as `Defaul Communication Device`.  
![Windows Sound Playback Screenshot](https://i.imgur.com/hSPTDgF.png)
3. Switch over to the Recording tab. Set `VoiceMeeter Output` as `Default Device` and `VoiceMeeter Aux Output` as `Default Communication Device`.  
![Windows Sound Recording Screenshot](https://i.imgur.com/TbbztDm.png)
4. Set input and output devices in your communication applications to either `Default Device` or `VoiceMeeter Aux Input/Output`.