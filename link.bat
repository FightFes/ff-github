@echo off

rem �J�����g�f�B���N�g���Ɉړ�
cd /d %~dp0
echo %~dp0

call :MakeDirLink %USERPROFILE%\AppData\Local\nvim %~dp0nvim
call :MakeLink %USERPROFILE%\AppData\Local\Microsoft\Windows Terminal\settings.json %~dp0winterm\settings.json
call :MakeLink %USERPROFILE%\afxw64_163\AFXW.KEY %~dp0afxw\AFXW.KEY
call :MakeLink %USERPROFILE%\afxw64_163\AFXW.KEY.TXT %~dp0afxw\AFXW.KEY.TXT
call :MakeLink %USERPROFILE%\afxw64_163\AFXW.INI %~dp0afxw\AFXW.INI
call :MakeLink %USERPROFILE%\afxw64_163\AFXW.DEF %~dp0afxw\AFXW.DEF
pause
exit /b

:MakeLink
echo �t�@�C���̃V���{���b�N�����N���쐬
echo %1 %2
rem �t�@�C��������
del /q %1
rem �Ȃ��Ȃ�t�H���_���쐬����
md %~dp1
rem �����N��\��
mklink %1 %2
echo;
exit /b

:MakeDirLink
echo �f�B���N�g���̃V���{���b�N�����N���쐬
echo %1 %2
rem �t�H���_������
rd /q /s %1
rem �Ȃ��Ȃ�t�H���_���쐬����
md %~dp1
rem �����N��\��
mklink /d %1 %2
echo;
exit /b