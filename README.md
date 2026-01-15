# 森空岛自动签到工具（支持ServerChan推送）

自用裁剪版，只保留了 Actions部署，且加入了报错推送。

## 功能特性

- ✅ 自动签到多个账号
- ✅ 支持多种登录方式（密码、验证码、手动输入token）
- ✅ 错误日志记录
- ✅ **ServerChan错误推送**（新增功能）
- ✅ GitHub Actions支持

## 快速开始

### 方法一：GitHub Actions自动签到（推荐）

1. **Fork本仓库**
2. **配置GitHub Secrets**（详见 [SECRETS_CONFIG.md](SECRETS_CONFIG.md)）

   必需的Secrets：
   - `TOKEN`：森空岛登录token

   可选的Secrets（用于推送）：
   - `SERVERCHAN_SENDKEY`：ServerChan推送密钥

3. **启用Actions**
   - 在GitHub仓库的 Actions 标签页中启用工作流
   - 默认每天凌晨1点自动执行，也可手动触发

### 方法二：本地运行

1. **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```

2. **配置环境变量**：
   
   **Windows (PowerShell)**：
   ```powershell
   $env:SERVERCHAN_SENDKEY="你的发送密钥"
   $env:TOKEN="你的token"
   ```
   
   **Linux/macOS**：
   ```bash
   export SERVERCHAN_SENDKEY="你的发送密钥"
   export TOKEN="你的token"
   ```

3. **运行程序**：
   ```bash
   python skyland.py
   ```

## ServerChan推送功能

### 功能说明
当签到发生错误时，程序会自动通过ServerChan发送推送通知到您的手机。

### 配置步骤

1. **获取ServerChan发送密钥**：
   - 访问 [ServerChan官网](https://sct.ftqq.com/)
   - 使用GitHub账号登录
   - 创建新的SendKey并复制

2. **配置环境变量**：
   - 本地运行：设置 `SERVERCHAN_SENDKEY` 环境变量
   - GitHub Actions：在Secrets中添加 `SERVERCHAN_SENDKEY`

3. **测试推送**（可选）：
   ```bash
   python test_push.py
   ```

### 推送内容
- **标题**：森空岛自动签到 - 错误通知
- **内容**：具体的错误信息和建议
- **标签**：服务器报警

### 注意事项
- 推送功能是可选的，未配置不影响基本签到
- 仅在发生错误时推送，签到成功不推送
- 请确保已安装 `serverchan-sdk`：`pip install serverchan-sdk`

## 环境变量说明

| 变量名 | 说明 | 示例 | 是否必需 |
|--------|------|------|----------|
| `TOKEN` | 森空岛登录token | `token1,token2` | ✅ 是 |
| `SERVERCHAN_SENDKEY` | ServerChan推送密钥 | `SCT123456...` | ❌ 否 |
| `SKYLAND_TYPE` | 运行模式 | `add_account` | ❌ 否 |

## GitHub Actions配置

### 工作流文件
- `.github/workflows/auto_sign.yaml`：自动签到工作流

### 触发方式
- **定时触发**：每天凌晨1点（UTC时间）
- **手动触发**：在GitHub仓库的Actions页面手动运行

### Secrets配置
详见 [SECRETS_CONFIG.md](SECRETS_CONFIG.md)

## 文件说明

- `skyland.py`：主程序
- `SecuritySm.py`：安全模块
- `requirements.txt`：依赖包
- `test_push.py`：推送测试脚本
- `PUSH_CONFIG.md`：推送功能详细配置
- `SECRETS_CONFIG.md`：GitHub Secrets配置说明

## 常见问题

### Q: 如何获取token？
A: 运行程序后选择第3种登录方式，按照提示操作即可。

### Q: 推送不工作怎么办？
A: 1) 检查SERVERCHAN_SENDKEY是否正确配置 2) 确保已安装serverchan-sdk 3) 运行test_push.py测试

### Q: 如何添加多个账号？
A: 在TOKEN环境变量中用逗号分隔多个token。

## 免责声明

本工具仅供学习交流使用，请勿用于商业用途。使用过程中请遵守相关平台的用户协议。
