
$str = $args[1]

#if ($args[0] -eq "decrypt")
#{
#    $decode = [Text.Encoding]::Utf8.GetString([Convert]::FromBase64String($result))
#    echo($decode)
#}



if ($args[0] -eq "crypt")
{
    $result = [System.Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($str))
    echo($result)
}

else
{
    if ($args[0] -eq "decrypt")
    {
        $decode = [Text.Encoding]::Utf8.GetString([Convert]::FromBase64String($str))
        echo($decode)
    }
}