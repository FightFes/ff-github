@echo off

rem �J�����g�f�B���N�g���Ɉړ�
cd /d %~dp0
echo %~dp0

call :MakeDirLink %USERPROFILE%\AppData\Local\nvim %~dp0nvim
exit /b

:MakeLink
rem �t�@�C��������
echo %1
rd /q %1
rem �Ȃ��Ȃ�t�H���_���쐬����
md %~dp1
rem �����N��\��
mklink %1 %2
exit /b

:MakeDirLink
rem �t�@�C��������
echo %1
echo %2
rd /q /s %1
rem �Ȃ��Ȃ�t�H���_���쐬����
md %~dp1
rem �����N��\��
mklink /d %1 %2
exit /b