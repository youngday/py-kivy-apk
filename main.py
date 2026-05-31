"""
一个使用 Kivy 构建的 Android 计算器应用
可以在此环境直接预览（桌面窗口），也可用 buildozer 打包为 APK
"""

__version__ = '0.1.0'

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.config import Config

# 配置窗口（仅桌面预览时生效，Android 上自动全屏）
Config.set('graphics', 'resizable', True)
Window.size = (400, 600)


class CalculatorApp(App):
    """主计算器应用类"""

    def build(self):
        """构建 UI 布局"""
        self.title = "计算器"
        self.expression = ""  # 当前表达式字符串

        # 主垂直布局
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # ---------- 显示屏区域 ----------
        display_container = BoxLayout(size_hint_y=0.25)
        with display_container.canvas.before:
            Color(0.95, 0.95, 0.95, 1)  # 浅灰背景
            self.bg_rect = Rectangle(pos=display_container.pos, size=display_container.size)

        # 更新背景矩形位置
        display_container.bind(pos=self._update_rect, size=self._update_rect)

        self.display = Label(
            text="0",
            font_size=48,
            halign='right',
            valign='middle',
            color=(0, 0, 0, 1),
            text_size=(Window.width * 0.9, None),
        )
        display_container.add_widget(self.display)
        main_layout.add_widget(display_container)

        # ---------- 按钮网格 ----------
        buttons_layout = GridLayout(cols=4, spacing=5, size_hint_y=0.75)

        # 各按钮定义：(显示文本, 回调值)
        button_data = [
            ('C', 'clear'), ('←', 'backspace'), ('%', '%'), ('÷', '/'),
            ('7', '7'), ('8', '8'), ('9', '9'), ('×', '×'),
            ('4', '4'), ('5', '5'), ('6', '6'), ('-', '-'),
            ('1', '1'), ('2', '2'), ('3', '3'), ('+', '+'),
            ('±', 'negate'), ('0', '0'), ('.', '.'), ('=', '=')
        ]

        for text, value in button_data:
            btn = Button(
                text=text,
                font_size=28,
                color=(0, 0, 0, 1),
                background_normal='',
                background_color=self._get_button_color(value),
            )
            btn.bind(on_press=lambda _, v=value: self.on_button_press(v))
            buttons_layout.add_widget(btn)

        main_layout.add_widget(buttons_layout)
        return main_layout

    def _update_rect(self, instance, value):
        """更新显示屏容器背景矩形"""
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size

    def _get_button_color(self, value):
        """根据按钮类型返回颜色"""
        if value in ('clear', 'backspace', '%'):
            return (0.85, 0.85, 0.85, 1)  # 浅灰
        elif value in ('+', '-', '×', '/', '='):
            return (0.2, 0.6, 1, 1)  # 蓝色
        elif value in ('negate',):
            return (0.9, 0.9, 0.9, 1)
        else:
            return (0.95, 0.95, 0.95, 1)  # 白色

    def on_button_press(self, value):
        """处理按钮点击"""
        if value == 'clear':
            self.expression = ""
            self.display.text = "0"
            return

        if value == 'backspace':
            self.expression = self.expression[:-1]
            self.display.text = self.expression if self.expression else "0"
            return

        if value == 'negate':
            if self.expression and self.expression[0] == '-':
                self.expression = self.expression[1:]
            else:
                self.expression = '-' + self.expression
            self.display.text = self.expression if self.expression else "0"
            return

        if value == '=':
            try:
                # 替换显示符号为计算符号
                calc_expr = self.expression.replace('×', '*').replace('÷', '/')
                # 安全计算
                result = eval(calc_expr, {"__builtins__": {}}, {})
                # 处理浮点数显示
                if isinstance(result, float):
                    if result == int(result):
                        result = int(result)
                    else:
                        result = round(result, 10)
                self.display.text = str(result)
                self.expression = str(result)
            except Exception:
                self.display.text = "错误"
                self.expression = ""
            return

        # 数字和运算符
        if value in ('+', '-', '×', '/', '%', '.'):
            # 防止连续运算符
            if self.expression and self.expression[-1] in '+-×/.%':
                self.expression = self.expression[:-1]

        self.expression += value
        self.display.text = self.expression


if __name__ == '__main__':
    CalculatorApp().run()