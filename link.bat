@echo off

rem カレントディレクトリに移動
cd /d %~dp0

rem if exist ..\.hyper.js (
rem   echo すでにファイルが存在しています。
rem ) else (
rem   echo シンボリックリンクを作成
rem   mklink ..\.hyper.js .\.hyper.js
rem )

call :MakeLink ..\vimfiles\vimrc %USERPROFILE%\ff-github\vim\vimrc
call :MakeLink ..\AppData\Local\nvim\init.vim %USERPROFILE%\ff-github\vim\init.vim
exit /b

:MakeLink
md %~dp1
del /Q %1
mklink %1 %2
exit /b