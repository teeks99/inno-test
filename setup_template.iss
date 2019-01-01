; This is a template for an installer

[Setup]
AppName=Installer-Test
AppVerName=1.0-${Config}
AppPublisher=Boost Org
DefaultDirName=C:\local\test_1.0-${Config}
DefaultGroupName=none
DirExistsWarning=no
DisableStartupPrompt=yes
DisableProgramGroupPage=yes
DisableReadyMemo=yes
DisableReadyPage=yes
Compression=lzma2/ultra64
${SetupVariables}
OutputDir=.
OutputBaseFilename=test_1.0-${Config}
Uninstallable=no
PrivilegesRequired=lowest
VersionInfoTextVersion=test_1.0-${Config}
VersionInfoVersion=1.0

[Files]
Source: "${SourceDir}/*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs ignoreversion

[Messages]
SelectDirLabel3=Installed Test Files
