@echo off

rem カレントディレクトリに移動
cd /d %~dp0
echo %~dp0

call :MakeDirLink %USERPROFILE%\AppData\Local\nvim %~dp0nvim /d
call :MakeLink %USERPROFILE%\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json %~dp0config\winterm\settings.json
call :MakeLink %USERPROFILE%\afxw64_163\AFXW.KEY %~dp0config\afxw\AFXW.KEY
call :MakeLink %USERPROFILE%\afxw64_163\AFXW.KEY.TXT %~dp0config\afxw\AFXW.KEY.TXT
call :MakeLink %USERPROFILE%\afxw64_163\AFXW.INI %~dp0config\afxw\AFXW.INI
call :MakeLink %USERPROFILE%\afxw64_163\AFXW.DEF %~dp0config\afxw\AFXW.DEF
pause
exit /b

:MakeLink
echo ファイルのシンボリックリンクを作成
echo %1 %2
rem ファイルを消す
del /q %1
rem ないならフォルダを作成する
md %~dp1
rem リンクを貼る
mklink %1 %2
echo;
exit /b

:MakeDirLink
echo ディレクトリのシンボリックリンクを作成
echo %1 %2
rem フォルダを消す
rd /q /s %1
rem ないならフォルダを作成する
md %~dp1
rem リンクを貼る
mklink /d %1 %2
echo;
exit /b