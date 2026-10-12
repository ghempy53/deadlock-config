# The `DeadlockConfig-Update` command

A PowerShell command that downloads a config from this repo's `main` branch and installs it into Deadlock.
It finds the game in any Steam library, keeps the previous file as `gameinfo.gi.bak`, and does nothing if the
installed file is already current. The source is [`scripts/DeadlockConfig-Update.ps1`](../scripts/DeadlockConfig-Update.ps1).

```powershell
DeadlockConfig-Update            # stable config (default)
DeadlockConfig-Update -stable    # same thing, explicit
DeadlockConfig-Update -ex        # experimental config
```

Type `DeadlockC` and press Tab to complete the name.

## Setup (once)

Works in Windows PowerShell 5.1 and PowerShell 7, including in Windows Terminal. If you use both, run the setup in each:
they have separate profiles.

1. **Remove the old command, if you have one.** `(Get-Command Update-DeadlockConfig).ScriptBlock.File` prints the
   file that defines it (usually `$PROFILE`). Open that file in Notepad, delete the whole
   `function Update-DeadlockConfig { ... }` block, and save.
2. **Install the command.** Paste this into the terminal:

   ```powershell
   $dir = Split-Path $PROFILE
   New-Item -ItemType Directory -Force $dir | Out-Null
   Invoke-WebRequest https://raw.githubusercontent.com/ghempy53/deadlock-config/main/scripts/DeadlockConfig-Update.ps1 `
       -OutFile (Join-Path $dir 'DeadlockConfig-Update.ps1') -UseBasicParsing
   Unblock-File (Join-Path $dir 'DeadlockConfig-Update.ps1')
   if (-not (Test-Path $PROFILE) -or -not (Select-String -Path $PROFILE -SimpleMatch 'DeadlockConfig-Update.ps1' -Quiet)) {
       Add-Content $PROFILE '. "$PSScriptRoot\DeadlockConfig-Update.ps1"'
   }
   . $PROFILE
   ```

   This saves the script next to your profile and adds one line to the profile that loads it in every new terminal.
3. **Test it.** Run `DeadlockConfig-Update`. It prints `Installed stable-config (main) -> ...\gameinfo.gi`,
   or `Already up to date` if that file is already installed.

If step 2 fails with *running scripts is disabled on this system*, allow local scripts for your user, then repeat
step 2:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## Updating the command itself

Run step 2 again. It overwrites the script and does not add a second line to your profile.

## Options

| Option | Effect |
| --- | --- |
| *(none)* or `-stable` | Installs `stable-config/gameinfo.gi`. |
| `-ex` | Installs `experimental-config/gameinfo.gi`. |
| `-Branch <name>` | Installs from another branch, for example to try a pull request before merging it. |

## Undo

- Previous file: in `<Steam library>\steamapps\common\Deadlock\game\citadel\`, delete `gameinfo.gi` and rename
  `gameinfo.gi.bak` to `gameinfo.gi`.
- Valve's stock file: Steam → Deadlock → Properties → Installed Files → *Verify integrity of game files*.

## Errors

| Message | Cause |
| --- | --- |
| `Deadlock gameinfo.gi not found in any Steam library.` | Steam or Deadlock is not installed for this Windows user. |
| A 404 error | The branch or config folder does not exist (check the `-Branch` name). |
| `Download is not a gameinfo.gi` | GitHub returned something else, such as an error page. Nothing was changed. |
| `Deadlock is running` (warning) | The file was installed. Restart the game to load it. |
