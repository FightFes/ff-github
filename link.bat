@echo off

rem �J�����g�f�B���N�g���Ɉړ�
cd /d %~dp0

rem if exist ..\.hyper.js (
rem   echo ���łɃt�@�C�������݂��Ă��܂��B
rem ) else (
rem   echo �V���{���b�N�����N���쐬
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