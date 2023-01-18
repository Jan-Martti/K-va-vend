#Jan-Martti Olop
#14.12.22
#KT 4



$inputFileName = Read-Host "Sisesta XML faili nimi"
$rows = $inputFileName.customers.customer
foreach ($row in $rows)
{
        
        $nimi = $row.full_name
        
        $pask = "C:\temp\"+$nimi
        $appi = $pask + $nimi + ".txt"
        Get-Host C:\Users\it22\Desktop\ülesanne1.txt

        New-Item -Path $pask -ItemType Directory
        
                
       

       
}
