# ServerChan推送配置说明

## 功能说明
本程序已集成ServerChan推送功能，当签到发生错误时，会自动通过ServerChan发送推送通知。

## 配置步骤

### 1. 安装依赖
```bash
pip install -r requirements.txt
```
或者单独安装：
```bash
pip install serverchan-sdk
```

### 2. 获取ServerChan发送密钥
1. 访问 [ServerChan官网](https://sct.ftqq.com/)
2. 登录您的账号
3. 在控制台创建新的发送密钥（SendKey）
4. 复制生成的密钥

### 3. 配置环境变量
在运行程序前，设置环境变量：

**Windows (PowerShell):**
```powershell
$env:SERVERCHAN_SENDKEY="你的发送密钥"
```

**Windows (CMD):**
```cmd
set SERVERCHAN_SENDKEY=你的发送密钥
```

**Linux/macOS:**
```bash
export SERVERCHAN_SENDKEY="你的发送密钥"
```

### 4. 运行程序
配置环境变量后，正常运行程序即可：
```bash
python skyland.py
```

## 推送内容
当发生错误时，推送包含：
- **标题**: 森空岛自动签到 - 错误通知
- **内容**: 具体的错误信息
- **标签**: 服务器报警

## 注意事项
- 如果未配置`SERVERCHAN_SENDKEY`环境变量，程序会正常运行但不会发送推送
- 推送功能仅在发生错误时触发，签到成功不会推送
- 请确保serverchan-sdk已正确安装