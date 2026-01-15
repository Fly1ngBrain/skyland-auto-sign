#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试ServerChan推送功能的脚本
"""

import os
import sys

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from skyland import send_serverchan_notification

def test_push():
    """测试推送功能"""
    print("=== ServerChan推送测试 ===")
    
    # 检查环境变量
    sendkey = os.environ.get('SERVERCHAN_SENDKEY')
    if not sendkey:
        print("❌ 未配置 SERVERCHAN_SENDKEY 环境变量")
        print("请先设置环境变量：")
        print("Windows: $env:SERVERCHAN_SENDKEY='你的密钥'")
        print("Linux/macOS: export SERVERCHAN_SENDKEY='你的密钥'")
        return False
    
    print(f"✓ 检测到 SERVERCHAN_SENDKEY: {sendkey[:8]}...{sendkey[-4:]}")
    
    # 测试推送
    print("\n正在发送测试推送...")
    try:
        result = send_serverchan_notification(
            title="森空岛签到 - 测试推送",
            desp="这是一条测试推送消息，如果收到说明推送功能配置正确。",
            tags="测试"
        )
        print("✓ 推送发送完成！")
        print(f"结果: {result}")
        return True
    except Exception as e:
        print(f"❌ 推送失败: {e}")
        return False

if __name__ == '__main__':
    test_push()