import sys
import os
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QCheckBox, QMessageBox, QFileDialog
import zipfile
import pyshortcuts
import time

class InstallWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("DesTemp QQ Setup")

        # 整体布局
        layout = QVBoxLayout()

        # 选择安装目录按钮和文本框
        h_layout1 = QHBoxLayout()
        self.button1 = QPushButton("选择安装目录")
        self.button1.clicked.connect(self.select_install_path)
        self.edit_box_file_path = QLineEdit()
        h_layout1.addWidget(self.button1)
        h_layout1.addWidget(self.edit_box_file_path)

        # 选择插件安装目录按钮和文本框
        h_layout2 = QHBoxLayout()
        self.button5 = QPushButton("选择插件安装目录")
        self.button5.clicked.connect(self.select_plugin_install_path)
        self.edit_box_plugin_install_path = QLineEdit()
        h_layout2.addWidget(self.button5)
        h_layout2.addWidget(self.edit_box_plugin_install_path)

        # 创建快捷方式相关的复选框
        self.check_box1 = QCheckBox("创建快捷方式")
        self.check_box1.stateChanged.connect(self.toggle_check_box2)
        self.check_box2 = QCheckBox("使用特定启动文件创建快捷方式")
        self.check_box2.setEnabled(False)
        h_layout3 = QHBoxLayout()
        h_layout3.addWidget(self.check_box1)
        h_layout3.addWidget(self.check_box2)

        # 安装、取消等按钮
        h_layout4 = QHBoxLayout()
        self.button2 = QPushButton("查看帮助文档")
        self.button2.clicked.connect(self.open_help_doc)
        self.button3 = QPushButton("开始安装")
        self.button3.clicked.connect(self.start_install)
        self.button4 = QPushButton("取消安装")
        self.button4.clicked.connect(self.cancel_install)
        h_layout4.addWidget(self.button2)
        h_layout4.addWidget(self.button3)
        h_layout4.addWidget(self.button4)

        layout.addLayout(h_layout1)
        layout.addLayout(h_layout2)
        layout.addLayout(h_layout3)
        layout.addLayout(h_layout4)

        self.setLayout(layout)

    def select_install_path(self):
        path = QFileDialog.getExistingDirectory(self, "请选择安装目录")
        if path:
            self.edit_box_file_path.setText(path)

    def select_plugin_install_path(self):
        path = QFileDialog.getExistingDirectory(self, "请选择插件的安装目录")
        if path:
            path_W = path + "/LiteLoaderQQNT"
            self.edit_box_plugin_install_path.setText(os.path.join(path_W.replace("/", "\\")))

    def toggle_check_box2(self):
        if self.check_box1.isChecked():
            self.check_box2.setEnabled(True)
        else:
            self.check_box2.setEnabled(False)

    def open_help_doc(self):
        # 这里假设帮助文档在指定的相对路径下，需要根据实际情况调整
        help_doc_path = os.path.join(os.getcwd(), "Resourse", "LiteLoaderHelp.docx")
        if os.path.exists(help_doc_path):
            os.startfile(help_doc_path)
        else:
            QMessageBox.critical(self, "错误", "帮助文档不存在")

    def cancel_install(self):
        reply = QMessageBox.question(self, "安装", "是否要取消安装", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit(0)

    def start_install(self):
        install_path = self.edit_box_file_path.text()
        plugin_install_path = self.edit_box_plugin_install_path.text()
        if install_path and plugin_install_path:
            try:
                os.makedirs(os.path.join(os.getcwd(), "temp"), exist_ok=True)
                # 以下模拟原代码中的一些文件读取、写入、解压等操作，需要根据实际文件情况调整具体逻辑
                # 读取文件（示例，原代码中ReadFile功能）
                def read_file(file_path):
                    with open(file_path, 'rb') as f:
                        return f.read()
                ntqq_zipfile_bin = read_file(os.path.join(os.getcwd(), "Resourse", "%~QT"))
                liteloader_zipfile_bin = read_file(os.path.join(os.getcwd(), "Resourse", "%~lr"))
                telegramtheme_background_image_bin = read_file(os.path.join(os.getcwd(), "Resourse", "%~IA"))
                # 写入文件（示例，原代码中WriteFile功能）
                def write_file(file_path, data):
                    with open(file_path, 'wb') as f:
                        f.write(data)
                write_file(os.path.join(os.getcwd(), "temp", "qp.zip"), ntqq_zipfile_bin)
                write_file(os.path.join(os.getcwd(), "temp", "lt.zip"), liteloader_zipfile_bin)
                write_file(os.path.join(os.getcwd(), "temp", "ia.zip"), telegramtheme_background_image_bin)
                # 解压文件（示例，原代码中ZipToFolder功能）
                def unzip_file(zip_path, extract_dir):
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(extract_dir)
                unzip_file(os.path.join(os.getcwd(), "temp", "qp.zip"), install_path)
                unzip_file(os.path.join(os.getcwd(), "temp", "lt.zip"), plugin_install_path)
                unzip_file(os.path.join(os.getcwd(), "temp", "ia.zip"), "C:\\DesTempQQImage")
                # 清理临时文件
                os.remove(os.path.join(os.getcwd(), "temp", "qp.zip"))
                os.remove(os.path.join(os.getcwd(), "temp", "lt.zip"))
                os.remove(os.path.join(os.getcwd(), "temp", "ia.zip"))
                # 写入插件目录相关文件（示例，原代码中WriteFile相关功能）
                with open(os.path.join(install_path, "versions", "9.9.16-28971", "resources", "app", "app_launcher", "liteloader.h.js"), 'w') as f:
                    f.write("require(String.raw`" + str(self.edit_box_plugin_install_path.text()) + "\\LiteLoaderQQNT" + "`);")
                # 创建快捷方式（示例，原代码中CreateShortCut功能）
                if self.check_box1.isChecked():
                    target_file = os.path.join(install_path, "Launcher.exe") if self.check_box2.isChecked() else os.path.join(install_path, "QQ.exe")
                    try:
                        pyshortcuts.make_shortcut(target_file, name="DesTemp QQ", desktop=True, description="DesTemp QQ Enjoy!")
                    except Exception as e:
                        QMessageBox.critical(self, "错误", f"创建快捷方式时出错: {str(e)}")
                QMessageBox.information(self, "提示", "安装Destemp QQ成功!")
                app.exit()
            except Exception as e:
                QMessageBox.critical(self, "错误", f"安装过程中出现错误: {str(e)}")
        else:
            QMessageBox.critical(self, "错误", "安装目录或插件安装目录不能为空")
app = QApplication(sys.argv)
window = InstallWindow()
time.sleep(1.5)
window.show()
sys.exit(app.exec_())