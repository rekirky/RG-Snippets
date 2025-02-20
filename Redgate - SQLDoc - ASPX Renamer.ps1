$folderPath = "C:\Temp\(local)__documentation"

#Get all .html files recursively
Get-ChildItem -Path $folderPath -Filter "*.html" -Recurse | ForEach-Object {
    $newName = $_.FullName -replace "\.html$", ".aspx"

    #Read file content, replace "html" with "aspx", and save
    (Get-Content $_.FullName) -replace "html", "aspx" | Set-Content $newName

    # Display modified file name - used for debugging, remove if process running smoothly
    Write-Host "Modified: $($_.FullName) -> $newName"

    # Remove the original .html file
    Remove-Item $_.FullName
}