$names = Get-ChildItem -Path C:\ -Force

#echo($arg)
foreach($n in $names)

{
    if($n.Name -eq "test") {continue}
    echo($n.Name)
}
