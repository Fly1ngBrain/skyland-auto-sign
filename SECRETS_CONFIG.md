# GitHub Secrets 配置说明

## 必需的环境变量

### TOKEN（必需）
- **说明**：森空岛登录token，支持多个账号（用逗号分隔）
- **配置方法**：
  1. 在GitHub仓库的 Settings → Secrets and variables → Actions → New repository secret
  2. 名称填写：`TOKEN`
  3. 值填写：你的token（多个用逗号分隔）

### SERVERCHAN_SENDKEY（可选）
- **说明**：ServerChan推送密钥，用于错误推送通知
- **配置方法**：
  1. 在GitHub仓库的 Settings → Secrets and variables → Actions → New repository secret
  2. 名称填写：`SERVERCHAN_SENDKEY`
  3. 值填写：你的ServerChan发送密钥

## 如何获取ServerChan发送密钥

1. 访问 [ServerChan官网](https://sct.ftqq.com/)
2. 使用GitHub账号登录
3. 点击"发送消息" → "创建新的SendKey"
4. 复制生成的密钥

## 配置步骤

### 1. 配置GitHub Secrets

访问您的GitHub仓库：
```
https://github.com/你的用户名/你的仓库名/settings/secrets/actions
```

点击"New repository secret"，添加以下Secrets：

| Secret名称 | 说明 | 是否必需 |
|-----------|------|----------|
| TOKEN | 森空岛登录token | ✅ 是 |
| SERVERCHAN_SENDKEY | ServerChan推送密钥 | ❌ 否 |

### 2. 推送功能说明

- 当配置了 `SERVERCHAN_SENDKEY` 后，签到发生错误时会自动推送通知
- 推送内容包含具体的错误信息
- 未配置则不会推送，程序正常运行

### 3. 多账号配置示例

如果需要签到多个账号，可以在 `TOKEN` 中配置多个token：

```
token1,token2,token3
```

## 注意事项

1. **安全性**：所有Secrets都是加密存储的，只有您和GitHub Actions可以访问
2. **隐私**：不要将Secrets提交到代码仓库中
3. **测试**：建议先在本地测试成功后再配置到GitHub Actions
4. **推送**：ServerChan推送是可选功能，不影响基本签到功能