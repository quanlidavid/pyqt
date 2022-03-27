# PYQT

### 安装pyenv-win管理多版本python

```shell
pip install pyenv-win --target %USERPROFILE%\.pyenv

[System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('PYENV_ROOT',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")

[System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('path', "User"),"User")

pyenv --version
pyenv rehash

pyenv install -l
pyenv install 3.9.6
```

pycharm 里选择安装的3.9.6环境：C:\Users\quan\.pyenv\pyenv-win\versions\3.9.6

## 安装PYQT6

💔必须命令行安装，在package管理里面装不上。

`pip install PyQt6`

### 安装QT Designer

🖤在python 3.10环境下装不上

`pip install pyqt6-tools`

### 打开Designer和.ui文件转.py文件 - 方式一

```shell
pyqt6-tools designer #打开Designer
pyuic6 -x ./PartOne/WindowUI.ui -o windowui.py	#-x表示输出的py文件包含__main__段
```

### 打开Designer和.ui文件转.py文件 - 方式二

配置Pycharm里面的外部工具：

- QtDesigner
  - Program：C:\Users\quan\PycharmProjects\pyqt\venv\Scripts\pyqt6-tools.exe
  - Arguments：designer
  - Working directory：$FileDir$

- pyuic
  - Program：C:\Users\quan\PycharmProjects\pyqt\venv\Scripts\pyuic6.exe
  - Arguments：-x $FileName$ -o $FileNameWithoutExtension$.py
  - Working directory：$FileDir$