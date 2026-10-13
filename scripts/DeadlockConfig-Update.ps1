# DeadlockConfig-Update: install this repo's gameinfo.gi into Deadlock.
# Dot-source this file from your PowerShell profile. Setup: docs/UPDATE-COMMAND.md
#
#   DeadlockConfig-Update            stable-config (default)
#   DeadlockConfig-Update -stable    stable-config
#   DeadlockConfig-Update -ex        experimental-config
#   DeadlockConfig-Update -Version 1.0   a frozen stable version (stable-config/v1.0)
#   DeadlockConfig-Update -Branch <name>   install from a branch other than main (to test a PR)
#   DeadlockConfig-Update -SelfUpdate      replace this script with the latest one from the branch
#
# Works in Windows PowerShell 5.1 and PowerShell 7.

function DeadlockConfig-Update {
    [CmdletBinding()]
    param(
        [Alias('ex')][switch]$Experimental,
        [switch]$Stable,
        [string]$Version,
        [string]$Branch = 'main',
        [switch]$SelfUpdate
    )
    if ($Experimental -and ($Stable -or $Version)) { throw 'Pass -ex or -stable/-Version, not both.' }
    $repo = 'ghempy53/deadlock-config'
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

    $folder = if ($Experimental) { 'experimental-config' }
              elseif ($Version) { 'stable-config/v' + $Version.TrimStart('v', 'V') }
              else { 'stable-config' }

    # Find Deadlock (Steam app 1422450) in any Steam library.
    $steam = (Get-ItemProperty 'HKCU:\Software\Valve\Steam' -ErrorAction Stop).SteamPath
    $vdf = Join-Path $steam 'steamapps\libraryfolders.vdf'
    $libs = @($steam)
    if (Test-Path $vdf) {
        $libs += Select-String -Path $vdf -Pattern '"path"\s+"(.+?)"' |
            ForEach-Object { $_.Matches[0].Groups[1].Value -replace '\\\\', '\' }
    }
    $target = $libs |
        ForEach-Object { Join-Path $_ 'steamapps\common\Deadlock\game\citadel\gameinfo.gi' } |
        Where-Object { Test-Path $_ } | Select-Object -First 1
    if (-not $target) { throw 'Deadlock gameinfo.gi not found in any Steam library.' }

    $tmp = [IO.Path]::GetTempFileName()
    try {
        Invoke-WebRequest -Uri "$raw/$folder/gameinfo.gi" -OutFile $tmp -UseBasicParsing -ErrorAction Stop
        if (-not (Select-String -Path $tmp -Pattern 'GameInfo' -SimpleMatch -Quiet)) {
            throw "Download is not a gameinfo.gi: $raw/$folder/gameinfo.gi"
        }
        if ((Get-FileHash $tmp).Hash -eq (Get-FileHash $target).Hash) {
            Write-Host "Already up to date: $folder ($label)" -ForegroundColor Green
            return
        }
        Copy-Item $target "$target.bak" -Force   # the previous file, replaced on each update
        Copy-Item $tmp $target -Force            # byte for byte: no BOM or line-ending changes
        Write-Host "Installed $folder ($label) -> $target" -ForegroundColor Green
        Write-Host "Previous file saved as $target.bak"
        if (Get-Process deadlock, project8 -ErrorAction SilentlyContinue) {
            Write-Warning 'Deadlock is running. Restart it to load the new config.'
        }
    } finally {
        Remove-Item $tmp -ErrorAction SilentlyContinue
    }
}
