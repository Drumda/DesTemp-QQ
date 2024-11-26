import sys
import os

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit,
                             QCheckBox, QMessageBox, QProgressBar, QLabel, QFileDialog, QSizePolicy, QSpacerItem)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

import zipfile
import tempfile
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        #隐藏最大化按钮
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint)
        self.resize(350, 200)
        self.setFixedSize(self.size())
        # 设置窗口标题和字体（微软雅黑字体）
        self.setWindowTitle("DesTemp QQ Installer")
        font = QFont("Microsoft YaHei", 10)
        self.setFont(font)
        # 设置窗口图标
        self.setWindowIcon(QIcon(os.getcwd() + "\\Resources\\Icon.ico"))

        # 整体布局
        main_layout = QVBoxLayout()

        # 安装目录选择相关布局
        install_path_layout = QHBoxLayout()
        self.edit_box_file_path = QLineEdit()
        select_install_path_button = QPushButton("选择安装目录")
        select_install_path_button.clicked.connect(self.select_install_path)
        install_path_layout.addWidget(self.edit_box_file_path)
        install_path_layout.addWidget(select_install_path_button)

        # 插件安装目录选择相关布局
        plugin_path_layout = QHBoxLayout()
        self.edit_box_plugin_install_path = QLineEdit()
        select_plugin_path_button = QPushButton("选择插件安装目录")
        select_plugin_path_button.clicked.connect(self.select_plugin_path)
        plugin_path_layout.addWidget(self.edit_box_plugin_install_path)
        plugin_path_layout.addWidget(select_plugin_path_button)

        # 按钮布局
        button_layout = QHBoxLayout()
        self.button2 = QPushButton("打开帮助文档")
        self.button2.clicked.connect(self.open_help_doc)
        self.button3 = QPushButton("开始安装")
        self.button3.clicked.connect(self.start_install)
        self.button4 = QPushButton("取消安装")
        self.button4.clicked.connect(self.cancel_install)
        button_layout.addWidget(self.button2)
        button_layout.addWidget(self.button3)
        button_layout.addWidget(self.button4)

        # 其他选项相关布局（复选框等）
        option_layout = QHBoxLayout()
        self.check_box1 = QCheckBox("创建快捷方式")
        self.check_box1.stateChanged.connect(self.toggle_check_box2)
        self.check_box2 = QCheckBox("特定快捷方式选项")
        option_layout.addWidget(self.check_box1)
        option_layout.addWidget(self.check_box2)

        # 进度条和提示信息布局
        progress_layout = QVBoxLayout()
        self.progress_bar = QProgressBar()
        # 增加进度条的宽度
        self.progress_bar.setFixedSize(370, 15)
        self.label_info = QLabel("准备安装...")
        #将label_info设为左对齐
        self.label_info.setAlignment(Qt.AlignLeft)
        progress_layout.addWidget(self.label_info)
        progress_layout.addWidget(self.progress_bar)
        # 添加垂直间距
        spacer_item = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        progress_layout.addItem(spacer_item)
        main_layout.addLayout(install_path_layout)
        main_layout.addLayout(plugin_path_layout)
        main_layout.addLayout(button_layout)
        main_layout.addLayout(option_layout)
        main_layout.addLayout(progress_layout)

        self.setLayout(main_layout)

    def select_install_path(self):
        path = QFileDialog.getExistingDirectory(self, "请选择安装目录")
        if path:
            self.edit_box_file_path.setText(path)

    def select_plugin_path(self):
        path = QFileDialog.getExistingDirectory(self, "请选择插件的安装目录")
        if path:
            self.edit_box_plugin_install_path.setText(path + "/LiteLoaderQQNT")

    def open_help_doc(self):
        doc_path = os.path.join(self.get_run_path(), "Resourse", "LiteLoaderHelp.docx")
        if os.path.exists(doc_path):
            if sys.platform.startswith('win'):
                os.startfile(doc_path)  # 在Windows系统下使用os.startfile打开文件
        else:
            self.show_error_message("帮助文档不存在", "文件缺失错误", "打开帮助文档时找不到对应文件")

    def cancel_install(self):
        reply = QMessageBox.question(self, "安装", "是否要取消安装", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
    def disable_all_controls(self):
        # 获取窗口中的所有控件
         all_widgets = self.findChildren(QWidget)
    
        # 遍历所有控件，禁用按钮和编辑框
         for widget in all_widgets:
             if isinstance(widget, QPushButton) or isinstance(widget, QLineEdit):
               widget.setEnabled(False)
    def start_install(self):

        install_path = self.edit_box_file_path.text()
        plugin_install_path = self.edit_box_plugin_install_path.text()
        if install_path and plugin_install_path:
            self.install_thread(install_path, plugin_install_path)
        else:
            self.show_error_message("文件路径错误", "在操作文件时提供的目录发生了错误",
                                    "安装时提供的安装目录或插件安装目录不正确")
    def set_effect(self, text):
        self.label_info.setText(text)  # 假设界面上有个self.label_info用于显示提示信息
    def install_thread(self, install_path, plugin_install_path):
        # 禁用所有控件
        self.disable_all_controls()
        #self.setVisible(False) 鸡巴代码，用了会导致进度条无法正常显示，隔壁豆包的代码
        temp_dir = tempfile.mkdtemp()
        
        # 模拟读取文件等操作（以下文件名等按原代码示例，实际可能需要调整）
        ntqq_zipfile_bin = self.read_file(os.path.join(self.get_run_path(), "Resourse", "%~QT"))
        liteloader_zipfile_bin_0x7d = self.read_file(os.path.join(self.get_run_path(), "Resourse", "%~lr"))
        telegramtheme_background_image_bin = self.read_file(os.path.join(self.get_run_path(), "Resourse", "%~IA"))

        self.write_file(os.path.join(temp_dir, "qp.zip"), ntqq_zipfile_bin)
        self.write_file(os.path.join(temp_dir, "lt.zip"), liteloader_zipfile_bin_0x7d)
        self.write_file(os.path.join(temp_dir, "ia.zip"), telegramtheme_background_image_bin)

        self.set_effect("解压NTQQ主体")
        self.unzip_file(os.path.join(temp_dir, "qp.zip"), install_path)
        self.set_effect("注入QQ NT Lite Loader & Plugins")
        self.unzip_file(os.path.join(temp_dir, "lt.zip"), plugin_install_path)
        self.unzip_file(os.path.join(temp_dir, "ia.zip"), "C:/DesTempQQImage")

        self.set_effect("完成清理...")
        os.remove(os.path.join(temp_dir, "qp.zip"))
        os.remove(os.path.join(temp_dir, "lt.zip"))
        os.remove(os.path.join(temp_dir, "ia.zip"))

        # 以下部分原代码功能涉及更复杂操作，需进一步完善，这里简单示意
        self.set_effect("写入插件目录...")
        with open(os.path.join(install_path, "versions", "9.9.16-29927", "resources", "app", "app_launcher", # 更改版本到9.9.16-29927
                               "liteloader.h.js"), 'w') as f:
            f.write('require(String.raw`' + plugin_install_path + '\\LiteLoaderQQNT`);')

        if self.check_box1.isChecked():
            self.set_effect("正在创建快捷方式")
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            if self.check_box2.isChecked():
                target_path = os.path.join(install_path, "Launcher.exe")
            else:
                target_path = os.path.join(install_path, "QQ.exe")
            shortcut_created = self.create_shortcut(os.path.join(desktop_path, "DesTemp QQ"), target_path,
                                                    "DesTemp QQ Enjoy!")
            if not shortcut_created:
                self.show_error_message("创建快捷方式失败", "在创建快捷方式时发生了未知的错误",
                                        "创建快捷方式操作出现问题")
            else:
                QMessageBox.information(self, "提示", "安装Destemp QQ成功!")
        else:
            QMessageBox.information(self, "提示", "安装Destemp QQ成功!")

        self.close()

    def toggle_check_box2(self, state):
        if state == Qt.Checked:
            self.check_box2.setEnabled(True)
        else:
            self.check_box2.setEnabled(False)

    def show_error_message(self, error_type, error_reason, error_function):
        msg = f"运行时发生错误\n错误类型-------------------------\n{error_type}\n错误原因-------------------------\n{error_reason}\n出错指令-------------------------\n{error_function}"
        QMessageBox.critical(self, "Error", msg)

    def get_run_path(self):
        return os.path.dirname(sys.argv[0])

    def read_file(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                return f.read()
        return b''

    def write_file(self, file_path, data):
        dir_path = os.path.dirname(file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        with open(file_path, 'wb') as f:
            f.write(data)

    def unzip_file(self, zip_file_path, extract_to_path):
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            total_files = len(zip_ref.infolist())
            for i, file_info in enumerate(zip_ref.infolist()):
                zip_ref.extract(file_info, extract_to_path)
                progress_percentage = int((i + 1) / total_files * 100)
                self.progress_bar.setValue(progress_percentage)
                self.label_info.setText(f"安装中...({progress_percentage}%)")

    def create_shortcut(self, shortcut_path, target_path, description):
        try:
            from win32com.client import Dispatch
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(shortcut_path + ".lnk")
            shortcut.TargetPath = target_path
            shortcut.Description = description
            shortcut.Save()
            return True
        except:
            return False

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())