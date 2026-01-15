# 快速开始指南

## 5分钟配置GitHub Actions自动签到 + 错误推送

### 第1步：Fork仓库
点击右上角的 "Fork" 按钮，将本仓库fork到您的GitHub账号下。

### 第2步：配置Secrets

访问您的fork仓库：
```
https://github.com/你的用户名/skyland-auto-sign/settings/secrets/actions
```

点击 "New repository secret"，添加以下Secrets：

#### 必需配置：
1. **TOKEN**
   - 值：你的森空岛登录token
   - 如何获取：运行程序，选择第3种登录方式

#### 可选配置（用于错误推送）：
2. **SERVERCHAN_SENDKEY**
   - 值：ServerChan发送密钥
   - 如何获取：访问 https://sct.ftqq.com/ ，创建SendKey

### 第3步：启用Actions

1. 访问您的仓库的 "Actions" 标签页
2. 点击 "I understand my workflows, go ahead and enable them"
3. 找到 "Auto Sign" 工作流，点击 "Run workflow" 手动测试

### 第4步：完成！

- ✅ 每天凌晨1点自动签到
- ✅ 发生错误时推送通知（如果配置了SERVERCHAN_SENDKEY）
- ✅ 可以在Actions页面手动触发

## 本地测试（可选）

如果您想先在本地测试：

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置环境变量（Windows）
$env:SERVERCHAN_SENDKEY="你的密钥"
$env:TOKEN="你的token"

# 3. 运行测试
python skyland.py

# 4. 测试推送（可选）
python test_push.py
```

## 推送功能说明

当配置了 `SERVERCHAN_SENDKEY` 后：

- ✅ 签到失败 → 自动推送错误信息到手机
- ❌ 签到成功 → 不推送（保持安静）

推送内容示例：
```
标题：森空岛自动签到 - 错误通知
内容：签到过程中发生错误：
      角XXX签到失败了！原因：网络错误
      
      请检查日志或重新运行程序。
标签：服务器报警
```

## 常见问题

**Q: 如何获取token？**
A: 运行程序，选择第3种登录方式，按照提示操作。

**Q: 如何获取ServerChan密钥？**
A: 访问 https://sct.ftqq.com/ ，登录后创建SendKey。

**Q: 想要多个账号怎么办？**
A: 在TOKEN中用逗号分隔：`token1,token2,token3`

**Q: 推送不工作？**
A: 检查SERVERCHAN_SENDKEY是否正确，确保已安装serverchan-sdk。

## 下一步

- 详细配置：查看 [SECRETS_CONFIG.md](SECRETS_CONFIG.md)
- 推送配置：查看 [PUSH_CONFIG.md](PUSH_CONFIG.md)
- 完整说明：查看 [README.md](README.md)