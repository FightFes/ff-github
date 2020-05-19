@echo off

rem カレントディレクトリに移動
cd /d %~dp0
echo %~dp0

call :MakeDirLink %USERPROFILE%\AppData\Local\nvim %~dp0nvim
call :MakeLink %USERPROFILE%\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json %~dp0config\settings.json
pause
exit /b

:MakeLink
rem ファイルを消す
echo %1
echo %2
del /q %1
rem ないならフォルダを作成する
md %~dp1
rem リンクを貼る
mklink %1 %2
exit /b

:MakeDirLink
rem ファイルを消す
rd /q /s %1
rem ないならフォルダを作成する
md %~dp1
rem リンクを貼る
mklink /d %1 %2
exit /b