## 使用方法

下载DLL后就可以调用dll了

## 这里面都有什么命令?

`ClearInstallationPackageBuffer() #1 is a success and 0 is a failure，This command is used to empty the buffer folder of the installation package, leaving some disk space`

`CreatePackageBuffer() #1 is a success and 0 is a failure1，This command is used to create a buffer folder for the installation package, which is mainly used to store some temporary files for the installation package`

`CopyFile (str FilePath, str CopyPath, str CopyName) #FilePath is the path of the file to be copied, CopyPath is the path of the file to be copied, and Copyname is the name of the copied file`

`CheckFile() #Returns true if successful, and false if fails， Used to check the integrity of the file`

`StartInstall(str Path, str Plugin Path, bool Check) #Path is the installation path of the main program, PluginPath is the installation path of Liteloader, and Check is the detection file`
