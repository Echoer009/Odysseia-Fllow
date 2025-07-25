# Odysseia-Fllow

Odysseia-Fllow 一个大部分哈基米代打，后续有待更新。专为 Discord 论坛类脑设计的关注机器人。它允许服务器成员关注他们感兴趣的内容创作者，并在创作者发布新帖子时，通过一种非侵入性的方式（ghost ping）获得即时通知。

## ✨ 核心功能

-   **👤 作者关注**: 关注创作者，在新帖发布时获得通知。
-   **🔔 频道关注**: 订阅特定频道，并使用关键词过滤感兴趣的帖子。
-   **📜 帖子收藏夹**: 收藏您喜欢的帖子，并进行批量管理。
-   **🏆 杯赛关注**: 关注杯赛，在新作品提交时获得私信提醒。
-   **⚙️ 统一管理面板**: 通过 `/我的关注` 命令，提供一个统一的、交互式的界面来管理您的所有关注项。
-   **🚀 丰富的操作方式**: 广泛支持斜杠命令和右键菜单，操作方便快捷。
-   **⚡ 高性能设计**: 核心功能采用缓存与异步处理，确保流畅的用户体验和机器人稳定性。

## ⚙️ 安装与设置

1.  **克隆仓库**
    ```sh
    git clone https://github.com/Echoer009/Odysseia-Fllow.git
    cd Odysseia-Fllow
    ```

2.  **创建并激活虚拟环境 (推荐)**
    ```sh
    # 创建虚拟环境
    python -m venv venv
    # 激活虚拟环境
    # Windows
    .\venv\Scripts\activate
    # Linux / macOS
    source venv/bin/activate
    ```

3.  **安装依赖**
    确保您已在虚拟环境中，然后运行：
    ```sh
    pip install -r requirements.txt
    ```

4.  **配置环境变量**
    将 `.env.example` 文件复制一份并重命名为 `.env`。
    ```sh
    # 在 Windows 上
    copy .env.example .env
    # 在 Linux/macOS 上
    cp .env.example .env
    ```
    然后，编辑 `.env` 文件并填入您的信息：
    -   `DISCORD_TOKEN`: 您的 Discord 机器人令牌。
    -   `RESOURCE_CHANNEL_IDS`: 需要监控的论坛频道的ID，多个ID之间用英文逗号分隔。
    -   `DB_NAME`: 数据库文件名，默认为 `database.db` 即可。
    -   `TEST_GUILD_ID`: 您的测试服务器ID。在开发期间，这可以使斜杠命令立即同步。

5.  **运行机器人**
    ```sh
    python -m src.bot
    ```

## 🚀 使用教程

> 本教程详细介绍了机器人的四大核心功能：**作者关注**、**频道关注**、**帖子收藏**和**杯赛关注**。

### 1. 统一管理入口
这是最推荐的使用方式，可以管理您所有的关注项。
*   **命令**: `/我的关注`
*   **功能**: 在任意频道的聊天框输入此命令，机器人会给您发送一条**临时信息**。在这条临时信息里，您可以看到一个管理面板。
*   **面板选项**:
    *   **👤 管理关注的作者**: 查看您关注的所有作者，并可以进行取关操作。
    *   **🔔 管理关注的频道**: 管理您对特定频道的订阅规则。
    *   **📜 管理我的收藏夹**: 查看您收藏的帖子，并执行批量收藏、取消收藏或退出子区的操作。
    *   **🔒 管理黑名单(待更新)**: 管理您的黑名单

### 2. 作者关注功能
当您关注一位作者后，每当TA在服务器的指定频道发布新帖子时，您都会收到ghost ping通知。它会在子区**提及**您并删除这条消息,这样这个新帖子就会直接放入您的子区列表
*   **如何关注？**
    *   **方法一 (推荐)**: 在服务器里，右键点击您想关注的人发送的任意**消息**，在菜单中选择 `APP` -> `⭐ 关注此消息作者`。
    *   **方法二**: 进入您想关注的人发布的**帖子**中，输入斜杠命令 `/关注本贴作者`。
*   **如何取关？**
    *   **方法一 (推荐)**: 使用 `/我的关注` 命令，在管理面板中进行取关。
    *   **方法二**: 右键点击该作者的**消息**，选择 `APP` -> `:➖: 取关此消息作者`。
    *   **方法三**: 进入该作者的**帖子**，输入 `/取关本贴作者`。

### 3. 频道关注功能
您可以关注服务器的指定频道，并设置关键词来过滤您感兴趣的内容。
*   **如何使用？**
    1.  使用 `/我的关注` 命令，在私信面板中点击 `🔔 管理关注的频道`。
    2.  **关注新频道**: 点击 `➕ 关注新频道` 按钮，从列表中选择您想关注的频道。
    3.  **管理已关注的频道**: 从下拉菜单中选择一个您已关注的频道，进入管理界面。
*   **关键词规则**:
    *   **全量接收**: 不设置任何“关注词”，您会收到该频道的所有新帖通知。
    *   **精准过滤**: 设置“关注词”后，只有新帖标题或标签匹配时，您才会收到通知。
    *   **屏蔽**: 设置“屏蔽词”，任何匹配屏蔽词的帖子都**不会**通知您。

### 4. 帖子收藏夹功能
您可以收藏感兴趣的帖子，方便日后查找，并对已加入的帖子进行批量管理。
*   **如何收藏？**
    *   在任意帖子内，右键点击帖子**主楼的任意消息**，在菜单中选择 `APP` -> `⭐ 收藏此帖`。
*   **如何管理收藏？**
    1.  使用 `/我的关注` 命令，在面板中点击 `📜 管理我的收藏夹`。
    2.  在这里，您可以看到一个分页列表，展示了所有您收藏的帖子。
*   **批量操作**:
    *   `📥 批量收藏`: 自动扫描并收藏所有您已加入、但尚未收藏的活跃帖子。一键同步，非常方便。
    *   `🗑️ 批量取消收藏`: 进入一个多选界面，让您可以一次性选择多个帖子并从收藏夹中移除。
    *   `🚪 批量退出子区`: 进入一个多选界面，让您可以批量退出当前已加入的活跃帖子，快速清理您的帖子列表。
    *   `🔄 刷新列表`: 手动刷新收藏夹或可退出帖子列表。当您刚加入或退出一个帖子，而列表未更新时，可以使用此功能强制刷新缓存。

### 5. 杯赛关注功能
当您关注一个杯赛后，每当该杯赛有新作品提交时，机器人都会私信通知您。
*   **如何关注？**
    *   **方法一 (推荐)**: 在发布杯赛信息的频道，右键点击 `最近投稿作品`展示的**消息**，选择 `APP` -> `⭐ 关注此杯赛`。
    *   **方法二**: 复制杯赛消息`最近投稿作品`的链接，使用斜杠命令 `/关注杯赛` 并粘贴链接。
*   **如何取关？**
    *   **方法一 (推荐)**: 右键点击您当初关注的杯赛`最近投稿作品`**消息**，选择 `APP` -> `➖ 取关此杯赛`。
    *   **方法二**: 复制杯赛消息`最近投稿作品`的链接，使用斜杠命令 `/取关杯赛` 并粘贴链接。

## 🎯 未来计划
本项目正在持续开发中，旨在完善更多与创作者和关注者互动相关的功能。欢迎提出建议和反馈！

## 📄 许可证
本项目采用 [GNU AGPLv3 许可证](LICENSE)。
