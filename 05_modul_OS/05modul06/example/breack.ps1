$names = Get-ChildItem -Path C:\ -Force


foreach($n in $names)

{
    if($n.Name -eq "test") 
    {
        break
    }
    echo($n.Name)
}
