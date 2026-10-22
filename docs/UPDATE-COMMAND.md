# The `DeadlockConfig-Update` command

A PowerShell command that downloads a config from this repo's `main` branch and installs it into Deadlock.
It finds the game in any Steam library, overwrites `gameinfo.gi` (or creates it if it was deleted; no backup is kept),
and always replaces the installed file, even when it is already current. Downloads come from the branch's current commit, so a config is installable as soon
as its pull request is merged. The source is [`scripts/DeadlockConfig-Update.ps1`](../scripts/DeadlockConfig-Update.ps1).

```powershell
DeadlockConfig-Update              # current stable config (default)
DeadlockConfig-Update -Ex          # current experimental config
DeadlockConfig-Update -SelfUpdate  # update the command itself
```

Frozen stable versions (`stable-config/v<N>/`) are not installable with the command; copy one
[by hand](INSTALL.md) if you need it.

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
   # Download from main's current commit: the raw.githubusercontent.com branch URL can be 5 minutes stale.
   $sha = (Invoke-RestMethod https://api.github.com/repos/ghempy53/deadlock-config/commits/main -UseBasicParsing).sha
   Invoke-WebRequest https://raw.githubusercontent.com/ghempy53/deadlock-config/$sha/scripts/DeadlockConfig-Update.ps1 `
       -OutFile (Join-Path $dir 'DeadlockConfig-Update.ps1') -UseBasicParsing
   Unblock-File (Join-Path $dir 'DeadlockConfig-Update.ps1')
   if (-not (Test-Path $PROFILE) -or -not (Select-String -Path $PROFILE -SimpleMatch 'DeadlockConfig-Update.ps1' -Quiet)) {
       # Leading newline, in case the profile does not end with one.
       Add-Content $PROFILE ("`r`n" + '. "$PSScriptRoot\DeadlockConfig-Update.ps1"')
   }
   . $PROFILE
   ```

   This saves the script next to your profile and adds one line to the profile that loads it in every new terminal.
3. **Test it.** Run `DeadlockConfig-Update`. It prints `Installed stable-config (main) -> ...\gameinfo.gi`,
   with `(unchanged)` at the end if the same file was already installed.

If step 2 fails with *running scripts is disabled on this system*, allow local scripts for your user, then repeat
step 2:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## Updating the command itself

Run `DeadlockConfig-Update -SelfUpdate`, then open a new terminal. It replaces the script next to your profile with
the latest one from `main`. Running step 2 again does the same thing.

Updating from a copy older than 2026-10-22 removes `-stable`, `-Version` and `-Branch`. Running the command with
one of them then fails with *A parameter cannot be found*; use no option (stable) or `-Ex`.

## Options

| Option | Effect |
| --- | --- |
| *(none)* | Installs the current stable config, `stable-config/gameinfo.gi`. |
| `-Ex` | Installs the current experimental config, `experimental-config/gameinfo.gi`. |
| `-SelfUpdate` | Replaces the command's own script with the latest from `main`. Open a new terminal afterwards. |

Both configs always come from `main`.

## Undo

- The other config from this repo: run the command with or without `-Ex`.
- Valve's stock file: Steam → Deadlock → Properties → Installed Files → *Verify integrity of game files*.

## Errors

| Message | Cause |
| --- | --- |
| `Deadlock (game\citadel folder) not found in any Steam library.` | Steam or Deadlock is not installed for this Windows user. |
| A 404 error | The config file is missing on `main`. |
| `Could not resolve main to a commit` (warning) | The GitHub API was unreachable or rate limited (60 calls an hour). The install still runs from the branch URL, which can be up to 5 minutes old. |
| `A parameter cannot be found that matches parameter name ...` | Your copy of the script is older than the option. Run `DeadlockConfig-Update -SelfUpdate` (or step 2) and open a new terminal. |
| `Download is not a gameinfo.gi` | GitHub returned something else, such as an error page. Nothing was changed. |
| `Deadlock is running` (warning) | The file was installed. Restart the game to load it. |
