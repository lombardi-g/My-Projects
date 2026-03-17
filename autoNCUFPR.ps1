$url = "https://servicos.nc.ufpr.br/PortalNC/Concurso?concurso=PS2026"
$arquivo = "$env:USERPROFILE\Downloads\publicacoes.txt"

# ===== CONFIG EMAIL =====
$email = "EMAILAQUIAQUI@gmail.com"
$senha = ConvertTo-SecureString "SENHAAQUIAQUIAQUI" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential ($email, $senha)

try {
    $response = Invoke-WebRequest -Uri $url -UseBasicParsing
    $html = $response.Content

    # Remove HTML
    $texto = $html -replace "<[^>]*>", "`n"

    # Linhas limpas
    $linhas = $texto -split "`n" |
        ForEach-Object { $_.Trim() } |
        Where-Object { $_ -ne "" }

    $publicacoes = @()

    for ($i = 0; $i -lt $linhas.Count; $i++) {

        if ($linhas[$i] -match "Publicado:") {

            $inicio = [Math]::Max(0, $i - 2)
            $fim = [Math]::Min($linhas.Count - 1, $i + 2)

            $bloco = ($linhas[$inicio..$fim] -join " ")

            $publicacoes += $bloco
        }
    }

    $publicacoes = $publicacoes | Sort-Object -Unique

    if ($publicacoes.Count -eq 0) {
        Add-Content "$env:USERPROFILE\Downloads\erro.log" "Nada encontrado - $(Get-Date)"
        return
    }

    if (Test-Path $arquivo) {
        $antigas = Get-Content $arquivo

        $novas = $publicacoes | Where-Object { $_ -notin $antigas }

        if ($novas.Count -gt 0) {

            $mensagem = "Novas publicacoes encontradas:`n`n"
            $mensagem += ($novas -join "`n`n")

            # Email
            Send-MailMessage `
                -To $email `
                -From $email `
                -Subject "Nova publicacao UFPR" `
                -Body $mensagem `
                -SmtpServer "smtp.gmail.com" `
                -Port 587 `
                -UseSsl `
                -Credential $cred
        }

        $publicacoes | Out-File $arquivo

    } else {
        $publicacoes | Out-File $arquivo
    }

} catch {
    Add-Content "$env:USERPROFILE\Downloads\erro.log" $_
}
