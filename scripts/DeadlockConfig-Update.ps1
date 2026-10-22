# DeadlockConfig-Update: install this repo's gameinfo.gi into Deadlock. Always overwrites the installed file.
# Dot-source this file from your PowerShell profile. Setup: docs/UPDATE-COMMAND.md
#
#   DeadlockConfig-Update              stable-config (default)
#   DeadlockConfig-Update -Ex          experimental-config
#   DeadlockConfig-Update -SelfUpdate  replace this script with the latest one from main
#
# Works in Windows PowerShell 5.1 and PowerShell 7.

function DeadlockConfig-Update {
    [CmdletBinding()]
    param(
        [switch]$Ex,
        [switch]$SelfUpdate
    )
    $repo = 'ghempy53/deadlock-config'
    $Branch = 'main'
    [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12

    # raw.githubusercontent.com caches branch URLs for about 5 minutes after a push, so download from the branch's
    # current commit instead. If the GitHub API is unreachable (or rate limited), fall back to the branch URL.
    try {
        $ref = (Invoke-RestMethod "https://api.github.com/repos/$repo/commits/$Branch" -UseBasicParsing -ErrorAction Stop).sha
        $label = "$Branch @ $($ref.Substring(0, 7))"
    } catch {
        Write-Warning "Could not resolve $Branch to a commit; the download may be up to 5 minutes old."
        $ref = $Branch
        $label = $Branch
    }
    $raw = "https://raw.githubusercontent.com/$repo/$ref"

    if ($SelfUpdate) {
        $self = $MyInvocation.MyCommand.ScriptBlock.File
        if (-not $self) { throw 'This function was not loaded from a file, so there is nothing to update.' }
        $tmp = [IO.Path]::GetTempFileName()
        try {
            Invoke-WebRequest -Uri "$raw/scripts/DeadlockConfig-Update.ps1" -OutFile $tmp -UseBasicParsing -ErrorAction Stop
            if (-not (Select-String -Path $tmp -Pattern 'function DeadlockConfig-Update' -SimpleMatch -Quiet)) {
                throw 'Download is not the DeadlockConfig-Update script.'
            }
            Copy-Item $tmp $self -Force
            Write-Host "Updated $self ($label). Open a new terminal to use it." -ForegroundColor Green
        } finally {
            Remove-Item $tmp -ErrorAction SilentlyContinue
        }
        return
    }

    $folder = if ($Ex) { 'experimental-config' } else { 'stable-config' }

    # Find Deadlock (Steam app 1422450) in any Steam library. Look for the game folder, not gameinfo.gi, so an install
    # still works after the file was deleted.
    $steam = (Get-ItemProperty 'HKCU:\Software\Valve\Steam' -ErrorAction Stop).SteamPath
    $vdf = Join-Path $steam 'steamapps\libraryfolders.vdf'
    $libs = @($steam)
    if (Test-Path $vdf) {
        $libs += Select-String -Path $vdf -Pattern '"path"\s+"(.+?)"' |
            ForEach-Object { $_.Matches[0].Groups[1].Value -replace '\\\\', '\' }
    }
    $citadel = $libs |
        ForEach-Object { Join-Path $_ 'steamapps\common\Deadlock\game\citadel' } |
        Where-Object { Test-Path $_ -PathType Container } | Select-Object -First 1
    if (-not $citadel) { throw 'Deadlock (game\citadel folder) not found in any Steam library.' }
    $target = Join-Path $citadel 'gameinfo.gi'

    $tmp = [IO.Path]::GetTempFileName()
    try {
        Invoke-WebRequest -Uri "$raw/$folder/gameinfo.gi" -OutFile $tmp -UseBasicParsing -ErrorAction Stop
        if (-not (Select-String -Path $tmp -Pattern 'GameInfo' -SimpleMatch -Quiet)) {
            throw "Download is not a gameinfo.gi: $raw/$folder/gameinfo.gi"
        }
        # Always replace the installed file, even when it matches the download.
        $same = (Test-Path $target) -and (Get-FileHash $tmp).Hash -eq (Get-FileHash $target).Hash
        Copy-Item $tmp $target -Force   # byte for byte: no BOM or line-ending changes
        $note = if ($same) { ' (unchanged)' } else { '' }
        Write-Host "Installed $folder ($label) -> $target$note" -ForegroundColor Green
        if (Get-Process deadlock, project8 -ErrorAction SilentlyContinue) {
            Write-Warning 'Deadlock is running. Restart it to load the new config.'
        }
    } finally {
        Remove-Item $tmp -ErrorAction SilentlyContinue
    }
}
