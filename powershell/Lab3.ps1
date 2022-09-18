$From = "airlegohero@gmail.com"
$To = "black2at@mail.uc.edu"
$Subject = "IT3038C Windows SysInfo"
function getIP{
(Get-NetIPAddress).IPAddress | select-string "192.*"
}
function getUser{
(Get-LocalUser) | select-string "Admin*"
}
$IP = getIP
$User = getUser
$Hostname = $Host.Name
$Version = $Host.Version.Major
$Day = (get-date).DayOfWeek
$Date = (get-date).ToShortDateString()
$Body = "This machines IP is $IP, User is $User, Hostname is $Hostname, Powershell version is $Version, Today's Date is $Day, $Date"
$SMTPServer = "smtp.gmail.com"
$SMTPPort = "587"

Send-MailMessage -From $From -To $To -Subject $Subject `
-Body $Body -SmtpServer $SMTPServer -Port $SMTPPort -UseSsl `
-Credential (Get-Credential)
