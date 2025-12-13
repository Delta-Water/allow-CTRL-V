# 解除粘贴限制 - 智能模拟输入工具

一个专为CQUPT内网代码平台设计的浏览器扩展，通过模拟真实键盘输入的方式绕过粘贴限制，同时保持自然的人工输入效果。

## 🎯 功能特性

- **智能模拟输入**：模拟真实人工输入，带随机延迟和打字错误
- **双模式支持**：
  - 前端模拟（默认）：直接通过JavaScript模拟输入
  - OS键盘模式：通过本地WebSocket服务使用系统级键盘输入
- **自然输入效果**：
  - 可调节的输入速度和随机延迟
  - 模拟打错字和修正过程
  - 间歇性暂停，更贴近真实输入习惯
- **Monaco编辑器集成**：完美支持代码编辑器的特殊字符处理
- **实时演示**：配置界面中可预览输入效果
- **快捷键控制**：ESC暂停/继续，长按ESC强制中断

## 📁 项目结构

```
allow-CTRL-V/
├── allow-CTRL-V.user.js      # Tampermonkey用户脚本
├── os_keyboard_server.py     # OS键盘服务端（Python）
└── README.md                # 说明文档
```

## 🔧 安装与配置

### 第一步：安装用户脚本

1. **安装浏览器扩展**
   - Chrome/Edge：安装 [Tampermonkey](https://www.tampermonkey.net/)
   - Firefox：安装 [Tampermonkey](https://addons.mozilla.org/firefox/addon/tampermonkey/)

2. **安装用户脚本**
   - 打开 `allow-CTRL-V.user.js`
   - Tampermonkey会自动检测并提示安装
   - 点击"安装"按钮

### 第二步：配置OS键盘服务（可选）

如果需要更稳定的系统级键盘输入，请配置OS键盘服务：

#### 对于Windows用户：

1. **安装Python**
   - 下载并安装 [Python 3.8+](https://www.python.org/downloads/)
   - 安装时勾选"Add Python to PATH"

2. **安装依赖包**
   ```bash
   pip install websockets pynput
   ```

3. **启动服务**
   ```bash
   python os_keyboard_server.py
   ```

#### 对于macOS用户：

1. **使用Homebrew安装Python**
   ```bash
   brew install python
   ```

2. **安装依赖包**
   ```bash
   pip3 install websockets pynput
   ```

3. **权限设置**（重要！）
   - 打开"系统设置" → "隐私与安全性"
   - 找到"辅助功能"
   - 添加终端应用（Terminal或iTerm2）到允许列表

4. **启动服务**
   ```bash
   python3 os_keyboard_server.py
   ```

#### 对于Linux用户：

1. **安装Python和依赖**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   pip3 install websockets pynput
   ```

2. **权限设置**
   - 可能需要添加用户到`input`组：
     ```bash
     sudo usermod -a -G input $USER
     ```
   - 重启生效

3. **启动服务**
   ```bash
   python3 os_keyboard_server.py
   ```

### 第三步：在代码平台使用

1. 访问CQUPT内网代码平台（`172.22.181.82/train/*`）
2. 在配置界面中启用"OS键盘输入"（如果已启动本地服务）
3. 正常复制代码，在编辑器中粘贴即可

## ⚙️ 配置说明

在代码平台上点击右下角的配置按钮（⚙️）可调整：

### 输入速度设置
- **基础延迟**：每个字符输入的基本延迟（20-200ms）
- **随机延迟**：增加输入的随机性（0-50ms）
- **错误概率**：模拟打错字的概率（0-20%）

### 间歇性设置
- **字符间隔**：每输入N个字符后暂停
- **暂停时间**：暂停的持续时间（毫秒）

### OS键盘设置
- 启用/禁用OS键盘模式
- 连接状态显示

## 🎮 使用方式

### 基本使用
1. 复制你想要粘贴的代码
2. 在代码平台的编辑器中按 `Ctrl+V`（或右键粘贴）
3. 脚本会自动开始模拟输入

### 控制快捷键
- **ESC**：暂停/继续输入
- **长按ESC**：强制中断输入
- **右下角状态栏**：实时显示输入状态

### 演示功能
在配置界面中点击"开始演示"可以预览当前设置的输入效果。

## 🔒 安全说明

- 脚本仅在 `172.22.181.82/train/*` 域名下运行
- OS键盘服务仅本地运行（127.0.0.1:8765）
- 不会收集或传输任何用户数据
- 所有配置保存在浏览器本地存储中

## ❓ 常见问题

### Q: OS键盘服务无法连接？
- 确保Python脚本正在运行
- 检查防火墙是否允许8765端口
- macOS/Linux用户检查辅助功能权限

### Q: 脚本不生效？
- 确认Tampermonkey已启用该脚本
- 检查是否在正确的网站（CQUPT内网）
- 刷新页面重试

## 🤝 贡献与反馈

欢迎提交Issue和Pull Request！

## 📄 许可证

本项目采用 AGPL-3.0 许可证，请在使用或传播时自觉遵守其内容。
