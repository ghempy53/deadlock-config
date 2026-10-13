# DeadlockConfig-Update: install this repo's gameinfo.gi into Deadlock.
# Dot-source this file from your PowerShell profile. Setup: docs/UPDATE-COMMAND.md
#
#   DeadlockConfig-Update            stable-config (default)
#   DeadlockConfig-Update -stable    stable-config
#   DeadlockConfig-Update -ex        experimental-config
#   DeadlockConfig-Update -Version 1.0   a frozen stable version (stable-config/v1.0)
#   DeadlockConfig-Update -Branch <name>   install from a branch other than main (to test a PR)
#
# Works in Windows PowerShell 5.1 and PowerShell 7.

function DeadlockConfig-Update {
    [CmdletBinding()]
    param(
        [Alias('ex')][switch]$Experimental,
        [switch]$Stable,
        [string]$Version,
        [string]$Branch = 'main'
    )
    if ($Experimental -and ($Stable -or $Version)) { throw 'Pass -ex or -stable/-Version, not both.' }
    $folder = if ($Experimental) { 'experimental-config' }
              elseif ($Version) { 'stable-config/v' + $Version.TrimStart('v', 'V') }
              else { 'stable-config' }
    $url = "https://raw.githubusercontent.com/ghempy53/deadlock-config/$Branch/$folder/gameinfo.gi"

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

    [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12
    $tmp = [IO.Path]::GetTempFileName()
    try {
        Invoke-WebRequest -Uri $url -OutFile $tmp -UseBasicParsing -ErrorAction Stop
        if (-not (Select-String -Path $tmp -Pattern 'GameInfo' -SimpleMatch -Quiet)) {
            throw "Download is not a gameinfo.gi: $url"
        }
        if ((Get-FileHash $tmp).Hash -eq (Get-FileHash $target).Hash) {
            Write-Host "Already up to date: $folder ($Branch)" -ForegroundColor Green
            return
        }
        Copy-Item $target "$target.bak" -Force   # the previous file, replaced on each update
        Copy-Item $tmp $target -Force            # byte for byte: no BOM or line-ending changes
        Write-Host "Installed $folder ($Branch) -> $target" -ForegroundColor Green
        Write-Host "Previous file saved as $target.bak"
        if (Get-Process deadlock, project8 -ErrorAction SilentlyContinue) {
            Write-Warning 'Deadlock is running. Restart it to load the new config.'
        }
    } finally {
        Remove-Item $tmp -ErrorAction SilentlyContinue
    }
}
