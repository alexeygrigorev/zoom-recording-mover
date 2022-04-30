## Move Zoom Recording

I was tired manually moving the recording of the podcast to Dropbox
so I decided to automate it

It works for Windows only. For Linux / MacOS you'll need 
to modify the code for showing messages

### Clone the repo

```bash
git clone git@gist.github.com:bdedd854cf6df69879fb153543f1a5c9.git move_zoom_recording
```

### Schedule it

Modidy `run.bat`:

* Set full path to your Python interpreter
* Set full path to `pun.py`

Next, schedule it:

```batch
Set RUN_PATH=%CD%\run.bat

schtasks /create ^
    /tn zoom-move-recording ^
    /sc daily ^
    /st 09:30 ^
    /tr %RUN_PATH%
```

Running it hourly:

```batch
Set RUN_PATH=%CD%\run.bat

schtasks /create ^
    /tn zoom-move-recording ^
    /sc hourly ^
    /st 00:05 ^
    /tr %RUN_PATH%
```

Some other useful stuff: 

* https://pureinfotech.com/prevent-command-window-appearing-scheduled-tasks-windows-10/


That's all!
