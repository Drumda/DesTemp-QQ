import sys
import os
import shutil
import zipfile
import win32com.client  # 需要安装pywin32库用于创建快捷方式
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QCheckBox, QFileDialog, QMessageBox, QProgressBar
)
from PyQt5.QtGui import QFont
import time

liteloader0x44e = ""


def button1_clicked():
    path = QFileDialog.getExistingDirectory(None, "请选择安装目录")
    if path:
        edit_box_file_path.setText(path)
        print("edit_box_file_path是否可见:", edit_box_file_path.isVisible())  # 调试语句，查看控件可见性
        return path
    return ""


def button2_clicked():
    resource_path = os.path.join(GetRunPath(), "Resourse", "LiteLoaderHelp.docx")
    if os.path.exists(resource_path):
        os.startfile(resource_path)
    else:
        PopCatch("System.Read.IO.File.FilePath", "帮助文档文件不存在", "打开帮助文档操作", "帮助文档文件缺失", True)


def button3_clicked(file_path, plugin_install_path):
    if file_path and plugin_install_path:
        if MkDir(os.path.join(GetRunPath(), "temp")):
            installthread(file_path)
        else:
            PopCatch("System.Write.IO.File.FilePath", "创建临时目录失败", "MkDir", "创建临时目录时出错", True)
    else:
        PopCatch("System.Write.IO.File.FilePath", "在操作文件时提供的目录发生了错误", "WriteFile | ZipToFolder.ZipLinker", "目录错误", True)


def button4_clicked():
    reply = QMessageBox.question(None, "安装", "是否要取消安装", QMessageBox.Yes | QMessageBox.No)
    if reply == QMessageBox.Yes:
        app.quit()


def button5_clicked():
    path = QFileDialog.getExistingDirectory(None, "请选择插件的安装目录")
    if path:
        edit_box_plugin_install_path.setText(os.path.join(path, "LiteLoaderQQNT"))
        print("edit_box_plugin_install_path是否可见:", edit_box_plugin_install_path.isVisible())  # 调试语句，查看控件可见性
        return path + "/LiteLodaerQQNT"
    return ""

def check_box1_clicked():
    if not check_box1.isChecked():
        check_box2.setEnabled(False)
    else:
        check_box2.setEnabled(True)


def installthread(file_path):
    window.hide()
    window1.show()
    SetEffect("准备就绪")
    if MkDir("C:\\DesTempQQImage"):
        ntqq_zipfile_bin = ReadFile(os.path.join(GetRunPath(), "Resourse", "%~QT"))
        liteloader_zipfile_bin_0x7d = ReadFile(os.path.join(GetRunPath(), "Resourse", "%~lr"))
        telegramtheme_background_image_bin = ReadFile(os.path.join(GetRunPath(), "Resourse", "%~IA"))
        if ntqq_zipfile_bin and liteloader_zipfile_bin_0x7d and telegramtheme_background_image_bin:
            if WriteFile(os.path.join(GetRunPath(), "temp", "qp.zip"), ntqq_zipfile_bin) and \
                    WriteFile(os.path.join(GetRunPath(), "temp", "lt.zip"), liteloader_zipfile_bin_0x7d) and \
                    WriteFile(os.path.join(GetRunPath(), "temp", "ia.zip"), telegramtheme_background_image_bin):
                SetEffect("解压NTQQ主体")
                if ZipToFolder(os.path.join(GetRunPath(), "temp", "qp.zip"), file_path):
                    SetEffect("注入QQ NT Lite Loader & Plugins")
                    if ZipToFolder(os.path.join(GetRunPath(), "temp", "lt.zip"), liteloader0x44e):
                        if ZipToFolder(os.path.join(GetRunPath(), "temp", "ia.zip"), "C:\\DesTempQQImage"):
                            SetEffect("完成清理...")
                            if Kill(os.path.join(GetRunPath(), "temp", "qp.zip")) and \
                                    Kill(os.path.join(GetRunPath(), "temp", "lt.zip")) and \
                                    Kill(os.path.join(GetRunPath(), "temp", "ia.zip")):
                                time.sleep(2.5)
                                SetEffect("写入插件目录...")
                                content = f'require(String.raw`{liteloader0x44e}\\LiteLoaderQQNT`);'
                                if WriteFile(os.path.join(file_path, "versions", "9.9.16-28971", "resources", "app", "app_launcher", "liteloader.h.js"), content.encode('utf-8')):
                                    if check_box1.isChecked():
                                        SetEffect("正在创建快捷方式")
                                        if check_box2.isChecked():
                                            shortcut_path = os.path.join(os.path.expanduser("~\\Desktop"), "DesTemp QQ.lnk")
                                            target_path = os.path.join(file_path, "Launcher.exe")
                                            if CreateShortCut(shortcut_path, target_path, "DesTemp QQ Enjoy!"):
                                                SetEffect("完成")
                                                QMessageBox.information(None, "提示", "安装Destemp QQ成功!")
                                            else:
                                                PopCatch("System.Create.ShortCut", "在创建快捷方式时发生了未知的错误", "CreateShortCut, #Desktop, Target, Note", "Null", True)
                                        else:
                                            shortcut_path = os.path.join(os.path.expanduser("~\\Desktop"), "DesTemp QQ.lnk")
                                            target_path = os.path.join(file_path, "QQ.exe")
                                            if CreateShortCut(shortcut_path, target_path, "DesTemp QQ Enjoy!"):
                                                SetEffect("完成")
                                                QMessageBox.information(None, "提示", "安装Destemp QQ成功!")
                                            else:
                                                PopCatch("System.Create.ShortCut", "在创建快捷方式时发生了未知的错误", "CreateShortCut, #Desktop, Target, Note", "Null", True)
                                    else:
                                        SetEffect("完成")
                                        QMessageBox.information(None, "提示", "安装Destemp QQ成功!")
                                else:
                                    PopCatch("System.Write.IO.File.FilePath", "写入插件目录文件失败", "WriteFile", "写入插件相关文件时出错", True)
                            else:
                                PopCatch("System.Write.IO.File.FilePath", "解压纸飞机主题配置文件到指定目录失败", "ZipToFolder", "解压相关文件操作失败", True)
                        else:
                            PopCatch("System.Write.IO.File.FilePath", "解压LiteLoader到指定目录失败", "ZipToFolder", "解压相关文件操作失败", True)
                    else:
                        PopCatch("System.Write.IO.File.FilePath", "解压NTQQ主体到指定目录失败", "ZipToFolder", "解压相关文件操作失败", True)
                else:
                    PopCatch("System.Write.IO.File.FilePath", "将NTQQ主体转换为zip并解压失败", "ZipToFolder", "解压相关文件操作失败", True)
            else:
                PopCatch("System.Write.IO.File.FilePath", "写入临时文件失败", "WriteFile", "写入临时文件时出错", True)
        else:
            PopCatch("System.Write.IO.File.FilePath", "读取资源文件失败", "ReadFile", "读取安装所需资源文件出错", True)
    else:
        PopCatch("System.Write.IO.File.FilePath", "创建DesTempQQImage目录失败", "MkDir", "创建相关目录时出错", True)
    app.quit()


def PopCatch(error_type, error_reason, error_function, description, use_error_msg):
    detailed_error_msg = ""
    if use_error_msg:
        detailed_error_msg += f"运行时发生错误\n错误类型-------------------------\n{error_type}\n错误原因-------------------------\n{error_reason}\n出错指令-------------------------\n{error_function}\n出错描述-------------------------\n描述：{description}"
    else:
        detailed_error_msg += f"运行时发生错误\n-------------------------\n{error_type}\n-------------------------\n{error_reason}\n-------------------------\n{error_function}\n-------------------------\n描述：{description}"

    try:
        # 获取最近一次的异常信息
        import traceback
        detailed_error_msg += "\n详细异常信息:\n" + "".join(traceback.format_exc())
    except:
        pass

    if use_error_msg:
        QMessageBox.critical(None, "Error", detailed_error_msg)
    else:
        QMessageBox.information(None, "Error", detailed_error_msg)


def CreateShortCut(shortcut_path, target_path, description, icon_path="", window_style=""):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = target_path
    shortcut.Description = description
    if icon_path:
        shortcut.IconLocation = icon_path
    if window_style:
        shortcut.WindowStyle = window_style
    try:
        shortcut.Save()
        return True
    except:
        return False


def IsFileExist(file_path):
    return os.path.exists(file_path)


def WriteFile(file_path, content):
    try:
        with open(file_path, 'wb') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"写入文件 {file_path} 出现错误: {str(e)}")
        return False


def ReadFile(file_path):
    try:
        with open(file_path, 'rb') as f:
            return f.read()
    except FileNotFoundError as e:
        print(f"读取文件 {file_path} 时出现文件不存在的错误: {str(e)}")
        return None
    except Exception as e:
        print(f"读取文件 {file_path} 时出现其他未知错误: {str(e)}")
        return None


def GetRunPath():
    return os.path.dirname(os.path.abspath(__file__))


def SetEffect(message):
    print(message)
    # 可以在这里根据实际情况添加更多逻辑，比如更新界面上的提示标签等内容


def MkDir(dir_path):
    try:
        os.makedirs(dir_path, exist_ok=True)
        return True
    except Exception as e:
        print(f"创建目录 {dir_path} 出现错误: {str(e)}")
        return False


def Kill(file_path):
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            return True
        except Exception as e:
            print(f"删除文件 {file_path} 出现错误: {str(e)}")
            return False
    return False


def SetKeyText(config_file_path, section, key, value):
    try:
        with open(config_file_path, 'a') as f:
            f.write(f"{section} {key} {value}\n")
        return True
    except Exception as e:
        print(f"写入配置文件 {config_file_path} 时出现错误: {str(e)}")
        return False


def ZipToFolder(zip_file_path, extract_dir):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            total_files = len(zip_ref.namelist())
            extracted_count = 0
            for file in zip_ref.namelist():
                zip_ref.extract(file, extract_dir)
                extracted_count += 1
                progress = int(extracted_count / total_files * 100)
                SetEffect(f"解压进度: {progress}%")  # 显示解压进度
            return True
    except zipfile.BadZipFile as e:
        print(f"解压文件 {zip_file_path} 出现错误，可能是损坏的ZIP文件: {str(e)}")
    except Exception as e:
        print(f"解压文件 {zip_file_path} 出现其他未知错误: {str(e)}")
    return False


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 设置全局字体为微软雅黑
    font = QFont("微软雅黑", 9)
    app.setFont(font)

    # 主窗口
    window = QWidget()
    window.setWindowTitle("安装程序")
    window.resize(800, 600)  # 设置一个合适的初始大小，避免窗口过小看不到控件

    layout = QVBoxLayout()

    # 安装目录相关
    layout_file_path = QHBoxLayout()
    label_file_path = QLabel("安装目录:")
    edit_box_file_path = QLineEdit()
    button_file_path = QPushButton("选择")
    button_file_path.clicked.connect(button1_clicked)
    layout_file_path.addWidget(label_file_path)
    layout_file_path.addWidget(edit_box_file_path)
    layout_file_path.addWidget(button_file_path)
    layout.addLayout(layout_file_path)

    # 插件安装目录相关
    layout_plugin_path = QHBoxLayout()
    label_plugin_path = QLabel("插件安装目录:")
    edit_box_plugin_install_path = QLineEdit()
    button_plugin_path = QPushButton("选择")
    button_plugin_path.clicked.connect(button5_clicked)
    layout_plugin_path.addWidget(label_plugin_path)
    layout_plugin_path.addWidget(edit_box_plugin_install_path)
    layout_plugin_path.addWidget(button_plugin_path)
    layout.addLayout(layout_plugin_path)

    # 选择框相关
    check_box1 = QCheckBox("创建快捷方式")
    check_box1.clicked.connect(check_box1_clicked)
    check_box2 = QCheckBox("使用Launcher.exe创建")
    check_box2.setEnabled(False)
    layout_check_boxes = QHBoxLayout()
    layout_check_boxes.addWidget(check_box1)
    layout_check_boxes.addWidget(check_box2)
    layout.addLayout(layout_check_boxes)

    # 按钮相关
    button_help = QPushButton("帮助")
    button_help.clicked.connect(button2_clicked)
    button_cancel = QPushButton("取消安装")
    button_cancel.clicked.connect(button4_clicked)
    button_install = QPushButton("开始安装")
    button_install.clicked.connect(lambda: button3_clicked(edit_box_file_path.text(), edit_box_plugin_install_path.text()))
    layout_buttons = QHBoxLayout()
    layout_buttons.addWidget(button_help)
    layout_buttons.addWidget(button_cancel)
    layout_buttons.addWidget(button_install)
    layout.addLayout(layout_buttons)

    # 模拟窗口1相关控件（进度条和标签）
    window1 = QWidget()
    window1.hide()
    layout_window1 = QVBoxLayout()
    progress_bar = QProgressBar()
    label_progress = QLabel("")
    layout_window1.addWidget(progress_bar)
    layout_window1.addWidget(label_progress)
    window1.setLayout(layout_window1)

    window.setLayout(layout)  # 确保布局设置给窗口
    window.show()
    sys.exit(app.exec_())