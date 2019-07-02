@echo off

rem カレントディレクトリに移動
cd /d %~dp0

rem if exist ..\.hyper.js (
rem   echo すでにファイルが存在しています。
rem ) else (
rem   echo シンボリックリンクを作成
rem   mklink ..\.hyper.js .\.hyper.js
rem )

call :makelink ..\.hyper.js %USERPROFILE%\ff-github\.hyper.js
call :makelink ..\vimfiles\vimrc %USERPROFILE%\ff-github\vimrc
call :makelink ..\vimfiles\gvimrc %USERPROFILE%\ff-github\gvimrc
call :makelink ..\AppData\Local\nvim\init.vim %USERPROFILE%\ff-github\init.vim
exit /b

:makelink
del /Q %1
mklink %1 %2
exit /b
