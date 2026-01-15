# 更新日志

## 2026-01-15 - 添加ServerChan推送功能

### 新增功能
- ✅ **ServerChan错误推送**：当签到发生错误时，自动通过ServerChan发送推送通知
- ✅ **GitHub Actions环境变量支持**：在YAML配置中添加了SERVERCHAN_SENDKEY支持
- ✅ **推送测试脚本**：新增 `test_push.py` 用于测试推送功能
- ✅ **详细配置文档**：新增多个配置说明文件

### 修改的文件

#### 1. `skyland.py`
- 添加ServerChan推送配置导入
- 新增 `send_serverchan_notification()` 函数
- 修改 `start()` 函数，添加错误收集和推送逻辑

#### 2. `requirements.txt`
- 添加 `serverchan-sdk` 依赖

#### 3. `.github/workflows/auto_sign.yaml`
- 在环境变量中添加 `SERVERCHAN_SENDKEY: ${{ secrets.SERVERCHAN_SENDKEY }}`

#### 4. `README.md`
- 更新为完整的使用说明
- 添加ServerChan推送功能详细说明
- 添加GitHub Actions配置指南

### 新增文件

- `test_push.py` - 推送功能测试脚本
- `PUSH_CONFIG.md` - 推送功能详细配置说明
- `SECRETS_CONFIG.md` - GitHub Secrets配置说明
- `QUICK_START.md` - 快速开始指南
- `.env.example` - 环境变量配置示例
- `CHANGELOG.md` - 更新日志

### 使用方法

#### GitHub Actions（推荐）
1. Fork仓库
2. 配置Secrets：
   - `TOKEN`：森空岛登录token（必需）
   - `SERVERCHAN_SENDKEY`：ServerChan推送密钥（可选）
3. 启用Actions

#### 本地运行
```bash
# 安装依赖
pip install -r requirements.txt

# 配置环境变量
export SERVERCHAN_SENDKEY="你的密钥"
export TOKEN="你的token"

# 运行
python skyland.py

# 测试推送
python test_push.py
```

### 推送功能说明

**触发条件**：签到过程中发生任何错误
**推送内容**：
- 标题：森空岛自动签到 - 错误通知
- 内容：具体错误信息
- 标签：服务器报警

**配置要求**：
- 安装 `serverchan-sdk`
- 配置 `SERVERCHAN_SENDKEY` 环境变量

### 注意事项
- 推送功能是可选的，未配置不影响基本签到
- 仅在错误时推送，成功签到不推送
- 请妥善保管您的token和推送密钥

### 兼容性
- ✅ 完全向后兼容，原有功能不变
- ✅ 新增功能不影响现有配置
- ✅ 支持多账号签到