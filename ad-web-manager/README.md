# AD Web Manager

## 项目简介
AD Web Manager 是一个用于管理 Windows Active Directory 的网页工具。该工具允许用户通过网页界面批量添加和删除域用户，简化了用户管理的流程。

## 文件结构
```
ad-web-manager
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── ad_utils.py
│   ├── routes.py
│   └── templates
│       ├── index.html
│       └── users.html
├── requirements.txt
├── config.py
└── README.md
```

## 安装
1. 克隆该项目到本地：
   ```
   git clone https://github.com/your-repo/ad-web-manager.git
   ```
2. 进入项目目录：
   ```
   cd ad-web-manager
   ```
3. 安装所需的 Python 包：
   ```
   pip install -r requirements.txt
   ```

## 配置
在 `config.py` 文件中，您可以设置 Active Directory 的相关配置，例如域名、管理员凭据等。

## 使用
1. 启动 Flask 服务器：
   ```
   python app/main.py
   ```
2. 打开浏览器，访问 `http://127.0.0.1:5000` 以访问应用程序。

## 功能
- **用户管理**：通过用户管理页面批量添加或删除域用户。
- **界面友好**：提供简洁的用户界面，方便用户操作。

## 贡献
欢迎任何形式的贡献！请提交问题或拉取请求。

## 许可证
该项目遵循 MIT 许可证。