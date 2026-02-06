# Mitmproxy Captor

基于mitmproxy的抓包工具，用于抓取HTTP、HTTPS和Socket等协议的请求和内容，并提供直观的展示界面。

## 功能特性

- **多协议支持**：抓取HTTP、HTTPS等协议
- **实时监控**：实时显示网络流量
- **详细分析**：展示请求和响应的完整内容
- **Web界面**：提供友好的Web操作界面
- **自定义过滤**：支持按域名、路径等过滤请求
- **数据导出**：支持导出为多种格式

## 安装

### 1. 设置虚拟环境 (推荐)

使用虚拟环境可以避免依赖冲突，推荐使用：

```bash
# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
# Windows (命令提示符) (PowerShell)
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
```

### 2. 安装依赖

#### 方法1: 使用 requirements.txt (推荐)

为了避免依赖冲突，推荐使用项目提供的 `requirements.txt` 文件安装：

```bash
pip install -r requirements.txt
```

#### 方法2: 直接安装

如果需要最新版本的 mitmproxy，可以直接安装：

```bash
pip install mitmproxy
```

### 依赖版本说明

由于存在一些依赖兼容性问题，项目指定了以下版本：
- mitmproxy==8.1.1
- passlib==1.7.3
- bcrypt==4.0.1
- werkzeug==2.0.3

这些版本组合可以避免常见的依赖冲突问题。

### 3. 克隆或下载

将本项目下载到本地。

## 使用方法

### 方式1: 命令行界面

```bash
python -m run
```

然后选择选项1启动mitmproxy命令行界面。

### 方式2: Web界面

```bash
python -m run
```

然后选择选项2启动mitmweb Web界面。

### 3. 配置客户端代理

将浏览器或其他客户端的代理设置为：
- 地址：localhost
- 端口：8080

### 4. 安装SSL证书

首次使用时，需要在浏览器中访问 `http://mitm.it` 并下载安装对应平台的SSL证书，以支持HTTPS抓包。

## 界面说明

### 命令行界面 (mitmproxy)

- **按键盘方向键**：浏览请求列表
- **按 Enter**：查看请求详情
- **按 q**：返回上一级
- **按 Ctrl+C**：退出

### Web界面 (mitmweb)

打开浏览器访问 `http://localhost:8081`，可以看到：
- **请求列表**：显示所有捕获的请求
- **详情面板**：显示选中请求的详细信息
- **过滤器**：支持按条件过滤请求

## 配置

修改 `config.py` 文件可以自定义配置：

- `PROXY_PORT`：代理端口
- `WEB_PORT`：Web界面端口
- `MAX_REQUESTS`：最大保存的请求数
- `FILTER_DOMAINS`：过滤的域名
- `IGNORE_PATHS`：忽略的路径

## 扩展开发

### 编写自定义插件

1. 创建新的Python文件，例如 `my_plugin.py`
2. 继承mitmproxy的基类并实现相应方法
3. 在 `run.py` 中修改启动命令，添加 `-s my_plugin.py`

### 示例插件

```python
from mitmproxy import http

class MyPlugin:
    def request(self, flow: http.HTTPFlow) -> None:
        print(f"自定义处理: {flow.request.url}")

addons = [
    MyPlugin()
]
```

## 应用场景

- **API开发调试**：监控和分析API请求和响应
- **网络问题排查**：识别网络延迟、错误和异常
- **安全测试**：检查敏感信息泄露和安全漏洞
- **性能分析**：分析请求时间和响应大小
- **第三方服务集成**：了解第三方服务的API调用

## 注意事项

- 抓包过程中可能会影响网络性能，请在必要时使用
- 不要使用此工具抓取敏感信息或进行未授权的监控
- 定期清理抓包数据，避免占用过多磁盘空间
- 在企业网络环境中使用时，请遵守公司的网络使用政策

## 常见问题

### Q: 无法抓取HTTPS请求
A: 请确保已正确安装并信任mitmproxy的SSL证书

### Q: 抓包速度太慢
A: 可以减少过滤条件，或只抓取必要的请求

### Q: 如何导出抓包数据
A: 在Web界面中，选择请求后点击导出按钮，或使用命令行工具导出

### Q: 支持抓取WebSocket吗
A: 是的，mitmproxy支持抓取WebSocket流量

## 技术原理

本工具基于mitmproxy实现，mitmproxy是一个强大的交互式HTTPS代理，它通过以下步骤工作：

1. 作为中间人拦截客户端和服务器之间的通信
2. 为每个HTTPS连接生成并签名临时SSL证书
3. 解析和分析HTTP/HTTPS请求和响应
4. 提供API接口供开发者扩展功能

## 许可证

本项目采用MIT许可证。
