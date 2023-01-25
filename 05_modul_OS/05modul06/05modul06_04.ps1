
$str = $args[1]

# условие проверки первого параметра
if ($args[0] -eq "crypt")
{
    # кодировка в Base64
    $result = [System.Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($str))
    echo($result)
}

else # условие False
{
    if ($args[0] -eq "decrypt") # условие проверки первого параметра
    {
        # расшифровка из Base64
        $decode = [Text.Encoding]::Utf8.GetString([Convert]::FromBase64String($str))
        echo($decode)
    }
}
