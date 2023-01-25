# Первое условие проверки параметра на значение файл
if (Test-Path -Path $args[0] -PathType Leaf)
{
    echo($args[0] + " - file")  # условие True
}
else # первое условие False
{   # второе условие проверки директории (пути директории)
    if (Test-Path $args[0])
    {
        echo($args[0] + " - dir") # условие True
    }
    else {echo($args[0] + " - not exist")} # второе условие False
}
