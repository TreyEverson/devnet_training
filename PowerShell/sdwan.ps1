# VIPTELLA VMANAGE

$url = 'https://sandboxsdwan.cisco.com:8443/j_security_check'

# When using 'application/x-www-form-urlencoded', you post an object with j_username and j_password
# No conversion to JSON, keep as PS object
$login_body = @{
    j_username = 'devnetuser'
    j_password = 'Cisco123!'
}

# We do want to get a JSON response back
$headers = @{'Accept' = 'application/json' }

#$response = `
Invoke-RestMethod -Uri $url `
    -Method post `
    -Body ($login_body) `
    -ContentType 'application/x-www-form-urlencoded' `
    -Headers $headers `
    -SkipCertificateCheck `
    -SessionVariable s
#$response

$uri = 'https://sandboxsdwan.cisco.com:8443/dataservice/device'
$devs = Invoke-RestMethod -Uri $uri `
    -Method Get `
    -ContentType 'application/json' `
    -Headers $headers `
    -SkipCertificateCheck `
    -Websession $s

Write-Host "Output!!!!!!!" 
$devices = $devs.data
ForEach ($device in $devices) {
    write-host $device
}