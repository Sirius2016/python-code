# AD Web Manager

## 项目简介
AD Web Manager 是一个用于管理 Windows Active Directory 用户的工具。通过一个美观的网页界面，用户可以方便地添加、删除单个用户，或批量添加和删除域用户。该项目旨在简化 Active Directory 用户管理的流程，提高工作效率。

## 功能
- **单个用户管理**
  - 添加用户
  - 删除用户
- **批量用户管理**
  - 批量添加用户
  - 批量删除用户

## 技术栈
- Python
- Flask
- Flask-WTF
- SQLite (作为数据库)
- HTML/CSS/JavaScript

## 项目结构
```
ad-web-manager
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── ad_utils.py
│   ├── forms.py
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── add_user.html
│   │   ├── delete_user.html
│   │   ├── batch_add.html
│   │   └── batch_delete.html
│   └── static
│       ├── css
│       │   └── style.css
│       └── js
│           └── main.js
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## 安装与运行
1. 克隆项目到本地：
   ```
   git clone <repository_url>
   cd ad-web-manager
   ```

2. 创建虚拟环境并激活：
   ```
   python -m venv venv
   source venv/bin/activate  # 在Windows上使用 venv\Scripts\activate
   ```

3. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

4. 配置数据库和 Active Directory 信息：
   - 修改 `config.py` 文件，填写相应的数据库和 AD 配置信息。

5. 启动应用：
   ```
   python run.py
   ```

6. 在浏览器中访问 `http://127.0.0.1:5000`。

## 贡献
欢迎任何形式的贡献！请提交问题或拉取请求。

## 许可证
本项目采用 MIT 许可证。