# The `DeadlockConfig-Update` command

A PowerShell command that downloads a config from this repo's `main` branch and installs it into Deadlock.
It finds the game in any Steam library, overwrites `gameinfo.gi` (or creates it if it was deleted; no backup is kept),
and always replaces the installed file, even when it is already current. It normally resolves `main` to a commit before downloading, prints that revision, and verifies the copied bytes.
If the API lookup fails it warns and uses the branch URL; its cache age is unknown. The source is [`scripts/DeadlockConfig-Update.ps1`](../scripts/DeadlockConfig-Update.ps1).

```powershell
DeadlockConfig-Update              # current stable config (default)
DeadlockConfig-Update -Ex          # current experimental config
DeadlockConfig-Update -SelfUpdate  # update the command itself
```

Frozen stable versions (`stable-config/v<N>/`) are not installable with the command; copy one
[by hand](INSTALL.md) if you need it.

Type `DeadlockC` and press Tab to complete the name.

## Setup (once)

Targets Windows PowerShell 5.1 and PowerShell 7, including Windows Terminal. The 2026-10-22 audit reviewed the
script statically; Windows/PowerShell execution still needs testing. If you use both, run the setup in each:
they have separate profiles.

Close Deadlock and make a manual backup before the first install. The downloaded script is executable code from
this repository; inspect the source if needed before loading it.

1. **Remove the old command, if you have one.** `(Get-Command Update-DeadlockConfig -ErrorAction SilentlyContinue).ScriptBlock.File` prints the
   file that defines it (usually `$PROFILE`). Open that file in Notepad, delete the whole
   `function Update-DeadlockConfig { ... }` block, and save.
2. **Install the command.** Paste this into the terminal:

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

   This saves the script next to your profile and adds one line to the profile that loads it in every new terminal.
3. **Test it.** Run `DeadlockConfig-Update`. It prints `Installed stable-config (main @ <sha>) -> ...\gameinfo.gi`,
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

Both configs always come from `main`. `-Ex` and `-SelfUpdate` are separate operations and cannot be combined.
The content checks reject obvious wrong downloads; they are not a full Valve parser or a runtime compatibility test.
`-SelfUpdate` additionally parses the downloaded PowerShell before replacing the script. Copy/hash failures stop
the command before it prints success. No automatic rollback copy is retained.

## Undo

- The other config from this repo: run the command with or without `-Ex`.
- A known local backup: close the game and restore it manually; use a backup from the current game build.
- Valve's current stock file: Steam → Deadlock → Properties → Installed Files → *Verify integrity of game files*.

Switching to experimental is not a guaranteed matchmaking fix: both current files differ from stock engine sections.

## Errors

| Message | Cause |
| --- | --- |
| `Deadlock (game\citadel folder) not found in any Steam library.` | Steam or Deadlock is not installed for this Windows user. |
| A 404 error | The config file is missing on `main`. |
| `Could not resolve main to a commit` (warning) | The API was unreachable, rate limited, or returned an invalid SHA. The install uses the branch URL with unknown cache age. |
| `A parameter cannot be found that matches parameter name ...` | The option is unavailable in this copy, or was removed. Use the options above. To refresh the command, run `DeadlockConfig-Update -SelfUpdate` (or step 2) and open a new terminal. |
| `Download is not a gameinfo.gi` | The download failed the basic content checks. The installed file was not copied over. |
| Access denied or copy verification failed | The copy did not complete successfully. Check permissions, file attributes and available space, then restore your backup if needed. |
| `Deadlock is running` (warning) | The file was installed. Restart the game to load it. |
