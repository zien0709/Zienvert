import sys
from cli import parse_and_run
from ui.app import launch_gui

if __name__ == "__main__":
    # 路由邏輯：有給予參數則進入 CLI 模式，否則啟動 GUI 模式
    if len(sys.argv) > 1:
        parse_and_run(sys.argv[1:])
    else:
        launch_gui()