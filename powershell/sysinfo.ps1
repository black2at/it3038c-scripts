function getIP{
    (get-netipaddress).IPv4Address | Select-String "192*"
    }
$IP = getIP

Write-Host("This machine's IP is $IP")