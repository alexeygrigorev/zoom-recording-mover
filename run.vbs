CreateObject("Wscript.Shell").Run "cmd /c """ & Replace(WScript.ScriptFullName, "run.vbs", "run.bat") & """", 0, False
