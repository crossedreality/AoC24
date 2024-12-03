$separator = "   "
$lista = @()
$listb = @()
$total = 0

foreach($line in (Get-Content C:\Box\Profile\Scripts\AoC\input.txt)) {
    $parseline = $line.TrimEnd().Split($separator)
    $lista += $parseline[0] #This is going to be super-slow, but doesn't require .Net classes to be loaded.
    $listb += $parseline[1]
}

$lista = $lista | Sort-Object
$listb = $listb | Sort-Object

for ($i = 0; $i -lt $lista.Count; $i++) {
    $total += [Math]::Abs($lista[$i] - $listb[$i])
}

Write-Output $total