# DeadlockConfig-Update: install this repo's gameinfo.gi into Deadlock. Always overwrites the installed file.
# Dot-source this file from your PowerShell profile. Setup: docs/UPDATE-COMMAND.md
#
#   DeadlockConfig-Update              stable-config (default)
#   DeadlockConfig-Update -Ex          experimental-config
#   DeadlockConfig-Update -SelfUpdate  replace this script with the latest one from main
#
# Targets Windows PowerShell 5.1 and PowerShell 7.

function DeadlockConfig-Update {
    [CmdletBinding(DefaultParameterSetName = 'Install')]
    param(
        [Parameter(ParameterSetName = 'Install')]
        [switch]$Ex,
        [Parameter(Mandatory = $true, ParameterSetName = 'SelfUpdate')]
        [switch]$SelfUpdate
    )
    $repo = 'ghempy53/deadlock-config'
    $Branch = 'main'
    [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12

    # Pin the branch tip once so the download has an identifiable revision. If the API is unreachable,
    # fall back to the branch URL, whose cache age is unknown.
    try {
        $ref = (Invoke-RestMethod "https://api.github.com/repos/$repo/commits/$Branch" -UseBasicParsing -ErrorAction Stop).sha
        if ($ref -notmatch '^[0-9a-f]{40}$') { throw 'GitHub returned an invalid commit SHA.' }
        $label = "$Branch @ $($ref.Substring(0, 7))"
    } catch {
        Write-Warning "Could not resolve $Branch to a commit; using the branch URL, whose cache age is unknown."
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
            $tokens = $null
            $parseErrors = $null
            $ast = [System.Management.Automation.Language.Parser]::ParseFile($tmp, [ref]$tokens, [ref]$parseErrors)
            $function = $ast.Find({ param($node)
                $node -is [System.Management.Automation.Language.FunctionDefinitionAst] -and
                $node.Name -eq 'DeadlockConfig-Update'
            }, $true)
            if ($parseErrors.Count -gt 0 -or -not $function) {
                throw 'Download is not a valid DeadlockConfig-Update PowerShell script.'
            }
            Copy-Item $tmp $self -Force -ErrorAction Stop
            if ((Get-FileHash $tmp -ErrorAction Stop).Hash -ne (Get-FileHash $self -ErrorAction Stop).Hash) {
                throw 'Script copy verification failed.'
            }
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
        $download = [IO.File]::ReadAllText($tmp)
        if ($download -notmatch '(?s)^\s*(?://[^\r\n]*[\r\n]+\s*)*(?:"GameInfo"|GameInfo)\s*\{' -or
            $download -notmatch '(?m)^\s*ConVars\s*$' -or $download -notmatch '\}\s*$') {
            throw "Download is not a gameinfo.gi: $raw/$folder/gameinfo.gi"
        }
        # Always replace the installed file, even when it matches the download.
        $same = (Test-Path $target) -and (Get-FileHash $tmp -ErrorAction Stop).Hash -eq (Get-FileHash $target -ErrorAction Stop).Hash
        Copy-Item $tmp $target -Force -ErrorAction Stop   # byte for byte: no BOM or line-ending changes
        if ((Get-FileHash $tmp -ErrorAction Stop).Hash -ne (Get-FileHash $target -ErrorAction Stop).Hash) {
            throw 'Installed config copy verification failed.'
        }
        $note = if ($same) { ' (unchanged)' } else { '' }
        Write-Host "Installed $folder ($label) -> $target$note" -ForegroundColor Green
        if (Get-Process deadlock, project8, citadel -ErrorAction SilentlyContinue) {
            Write-Warning 'Deadlock is running. Restart it to load the new config.'
        }
    } finally {
        Remove-Item $tmp -ErrorAction SilentlyContinue
    }
}
