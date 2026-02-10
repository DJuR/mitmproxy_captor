"""启动脚本 - 运行mitmproxy抓包工具"""

import subprocess
import sys
import os


def run_mitmproxy():
    """运行mitmproxy"""
    print("启动mitmproxy抓包工具...")
    print("使用说明:")
    print("1. 浏览器设置代理: localhost:8080")
    print("2. 访问 http://mitm.it 安装SSL证书")
    print("3. 开始浏览网页，查看抓包结果")
    print("\n按 Ctrl+C 停止")
    
    # 获取capture.py的路径
    capture_script = os.path.join(os.path.dirname(__file__), "capture.py")
    
    # 构建命令，添加上游代理支持
    cmd = [
        sys.executable, "-m", "mitmproxy",
        "--mode", "upstream:http://127.0.0.1:10808",
        "-s", capture_script,
        "-p", "8080"
    ]
    
    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\n抓包工具已停止")
    except Exception as e:
        print(f"错误: {e}")
        print("请确保已安装mitmproxy: pip install mitmproxy")


def run_mitmweb():
    """运行mitmweb (Web界面)"""
    print("启动mitmweb (Web界面)...")
    print("使用说明:")
    print("1. 浏览器设置代理: localhost:8080")
    print("2. 访问 http://mitm.it 安装SSL证书")
    print("3. 打开浏览器访问: http://localhost:8081")
    print("4. 在Web界面查看抓包结果")
    print("\n按 Ctrl+C 停止")
    
    # 获取capture.py的路径
    capture_script = os.path.join(os.path.dirname(__file__), "capture.py")
    
    # 构建命令，使用直接调用mitmweb可执行文件的方式，添加上游代理支持
    cmd = [
        "mitmweb",
        "--mode", "upstream:http://127.0.0.1:10808",
        "-s", capture_script,
        "-p", "8080",
        "--web-port", "8081"
    ]
    
    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\n抓包工具已停止")
    except Exception as e:
        print(f"错误: {e}")
        print("请确保已安装mitmproxy: pip install mitmproxy")


if __name__ == "__main__":
    print("Mitmproxy Captor - 基于mitmproxy的抓包工具")
    print("=====================================")
    print("1. 启动 mitmproxy (命令行界面)")
    print("2. 启动 mitmweb (Web界面)")
    print("3. 安装依赖")
    
    choice = input("请选择: ")
    
    if choice == "1":
        run_mitmproxy()
    elif choice == "2":
        run_mitmweb()
    elif choice == "3":
        print("安装mitmproxy...")
        subprocess.run([sys.executable, "-m", "pip", "install", "mitmproxy"], check=True)
        print("安装完成！")
    else:
        print("无效选择")
