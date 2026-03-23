## Move Zoom Recording

A simple script that automatically moves Zoom podcast recordings
to a Dropbox folder. It finds the most recent recording in
`~/Documents/zoom`, extracts the guest name from the audio files,
and moves the audio to `~/Dropbox/podcast/<date>-<guest>`.

Folders that have already been processed or that are too small
(under 90 MB) are skipped.

Windows only. For Linux/macOS you'll need to replace the Windows
message box calls.

### Clone the repo

```bash
git clone git@github.com:alexeygrigorev/zoom-recording-mover.git
```

### Configure

Edit `run.py` to set the source and destination paths:

* `zoom_videos` - where Zoom saves recordings (default: `~/Documents/zoom`)
* `dropbox_dest` - where to move audio files (default: `~/Dropbox/podcast`)

### Schedule it

From the repo directory, schedule it to run hourly using `run.vbs`
(a wrapper that runs `run.bat` without showing a terminal window):

```batch
schtasks /create ^
    /tn zoom-move-recording ^
    /sc hourly ^
    /st 00:05 ^
    /tr "%CD%\run.vbs"
```

Or run it daily at a specific time:

```batch
schtasks /create ^
    /tn zoom-move-recording ^
    /sc daily ^
    /st 09:30 ^
    /tr "%CD%\run.vbs"
```

To delete the scheduled task:

```batch
schtasks /delete /tn zoom-move-recording /f
```

To check if it's scheduled:

```batch
schtasks /query /tn zoom-move-recording
```

### Tips

* If you use `run.bat` directly instead of `run.vbs`, a terminal window
  will briefly appear each time the task runs. Use `run.vbs` to avoid this.
