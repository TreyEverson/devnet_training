$url = "https://dashboard.meraki.com/api/v0/organizations"
$headers = @{
    'Accept'                 = 'application/json' 
    'X-Cisco-Meraki-API-Key' = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

$orgs = Invoke-RestMethod -Uri $url `
    -Method get `
    -ContentType 'application/json' `
    -Headers $headers 

# Get OrgID of DevNet Sandbox
ForEach ($org in $orgs) {
    If ($org.name -eq 'DevNet Sandbox') {
        $orgId = $org.id
    }
}

# Get networks from organization
$orgId
$net_url = "https://dashboard.meraki.com/api/v0/organizations/$($orgId)/networks"
$networks = Invoke-RestMethod -Uri $net_url `
    -Method get `
    -ContentType 'application/json' `
    -Headers $headers 

# Get network ID of DNSMB5
ForEach ($network in $networks) {
    #Write-Host $network.name
    If ($network.name -eq 'DNSMB5') {
        $netId = $network.id
    }
}

# Get all devices on DNSMB5 network
$devices_url = "https://dashboard.meraki.com/api/v0/networks/$($netId)/devices"
$devices = Invoke-RestMethod -Uri $devices_url `
    -Method get `
    -ContentType 'application/json' `
    -Headers $headers 

$devices | ConvertTo-Json | Write-Output