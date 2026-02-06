"""核心抓包模块"""

from mitmproxy import http, ctx
from typing import List, Dict, Any
import json
import time

class CaptureAddon:
    """mitmproxy抓包插件"""
    
    def __init__(self):
        self.requests: List[Dict[str, Any]] = []
        self.max_requests = 1000
    
    def request(self, flow: http.HTTPFlow) -> None:
        """处理请求"""
        request_data = {
            "id": id(flow),
            "timestamp": time.time(),
            "method": flow.request.method,
            "url": flow.request.url,
            "headers": dict(flow.request.headers),
            "content": flow.request.content.decode('utf-8', errors='ignore') if flow.request.content else "",
            "response": None
        }
        
        # 添加到请求列表
        self.requests.append(request_data)
        
        # 限制请求列表大小
        if len(self.requests) > self.max_requests:
            self.requests.pop(0)
        
        # 打印请求信息
        ctx.log.info(f"[请求] {flow.request.method} {flow.request.url}")
    
    def response(self, flow: http.HTTPFlow) -> None:
        """处理响应"""
        # 查找对应的请求
        for request_data in self.requests:
            if request_data["id"] == id(flow):
                request_data["response"] = {
                    "status_code": flow.response.status_code,
                    "headers": dict(flow.response.headers),
                    "content": flow.response.content.decode('utf-8', errors='ignore') if flow.response.content else "",
                    "timestamp": time.time()
                }
                break
        
        # 打印响应信息
        ctx.log.info(f"[响应] {flow.request.url} - {flow.response.status_code}")
    
    def get_requests(self) -> List[Dict[str, Any]]:
        """获取所有请求"""
        return self.requests
    
    def clear_requests(self) -> None:
        """清空请求列表"""
        self.requests.clear()

addons = [
    CaptureAddon()
]
