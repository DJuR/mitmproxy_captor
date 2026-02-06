"""配置文件"""

class Config:
    """抓包工具配置"""
    
    # 代理端口
    PROXY_PORT = 8080
    
    # Web界面端口 (mitmweb)
    WEB_PORT = 8081
    
    # 最大保存的请求数
    MAX_REQUESTS = 1000
    
    # 是否启用详细日志
    DEBUG = False
    
    # 过滤规则
    # 格式: ["域名1", "域名2", ...]
    FILTER_DOMAINS = []
    
    # 忽略的路径
    # 格式: ["路径1", "路径2", ...]
    IGNORE_PATHS = [
        "/api/health",
        "/favicon.ico"
    ]
    
    # 导出格式
    # 可选: "json", "har", "text"
    EXPORT_FORMAT = "json"
