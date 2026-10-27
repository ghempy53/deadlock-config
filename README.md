# Deadlock configuration

A performance-focused `gameinfo.gi` config for Deadlock, installed with the `DeadlockConfig-Update` PowerShell command.

## 1. Set up the command (once)

Open PowerShell and paste:

```powershell
$dir = Split-Path $PROFILE
New-Item -ItemType Directory -Force $dir -ErrorAction Stop | Out-Null
[Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12
# Resolve one revision before downloading.
$sha = (Invoke-RestMethod https://api.github.com/repos/ghempy53/deadlock-config/commits/main -UseBasicParsing -ErrorAction Stop).sha
if ($sha -notmatch '^[0-9a-f]{40}$') { throw 'Could not resolve main to a commit.' }
Invoke-WebRequest https://raw.githubusercontent.com/ghempy53/deadlock-config/$sha/scripts/DeadlockConfig-Update.ps1 `
    -OutFile (Join-Path $dir 'DeadlockConfig-Update.ps1') -UseBasicParsing -ErrorAction Stop
Unblock-File (Join-Path $dir 'DeadlockConfig-Update.ps1') -ErrorAction Stop
if (-not (Test-Path $PROFILE) -or -not (Select-String -Path $PROFILE -SimpleMatch 'DeadlockConfig-Update.ps1' -Quiet)) {
    # Leading newline, in case the profile does not end with one.
    Add-Content $PROFILE ("`r`n" + '. "$PSScriptRoot\DeadlockConfig-Update.ps1"') -ErrorAction Stop
}
. $PROFILE
```

This saves the script next to your PowerShell profile and loads it in every new terminal. Windows PowerShell and
PowerShell 7 have separate profiles; run it in each one you use.

If it fails with *running scripts is disabled on this system*, run
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` and paste the block again.

## 2. Install the config

Close Deadlock, then run:

```powershell
DeadlockConfig-Update
```

It finds Deadlock in any Steam library, replaces `game\citadel\gameinfo.gi` and prints a green *Installed* line.
It keeps **no backup**; to go back to Valve's file, use Steam → Deadlock → Properties → Installed Files →
*Verify integrity of game files*.

## 3. Update later

- **New config:** close Deadlock and run `DeadlockConfig-Update` again. It always installs the latest version.
  After a Deadlock patch, Steam may replace `gameinfo.gi`; run it again once this repository has been updated for
  that patch.
- **New version of the command:** run `DeadlockConfig-Update -SelfUpdate`, then open a new terminal.

Error messages: [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md#update-command-errors). Manual install:
[INSTALL.md](docs/INSTALL.md).
