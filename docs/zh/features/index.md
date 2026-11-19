---
hide:
  - toc
  - navigation
---

# 功能

Gramps Web 是一个用于协作家谱的网络应用程序。它基于 [Gramps](https://gramps-project.org/)，这个开源的家谱程序，并使用相同的数据。您可以在自己的服务器上运行它，或使用托管服务提供商。

[试用演示](#demo){ .md-button .md-button--primary } [开始使用](../install_setup/setup.md){ .md-button }

## 探索您的家谱 { .feature-group }

![显示七代祖先的扇形图](screenshots/fan.png){ align=right width="400"}

### 互动家谱图

以祖先树、后代树、沙漏图、关系图或扇形图的形式浏览您的家谱，提供高质量的互动图形和可配置的代数。

将鼠标悬停在任何人身上，可以查看包含其关键信息的预览卡片，并可以直接从图表跳转到完整详细页面。

<div style="clear:both;"></div>

---

![1940年代到1970年代的家庭事件时间线](screenshots/timeline.png){ align=left width="400"}

### 按时间顺序的时间线

查看您家谱中的每个事件在一个水平、可缩放的时间线上排列。滚动和缩放穿越几个世纪，然后过滤到单个人——或他们所有的祖先或后代——或在一个地方发生的所有事件。

查看 [时间线](../user-guide/timeline.md)。

<div style="clear:both;"></div>

---

![伦敦地图，选定地点，显示其照片和事件](screenshots/map.png){ align=right width="400"}

### 互动地图

在一个互动的可搜索地图上显示您家谱中的所有地点。在创建地点时，可以直接在 OpenStreetMap 上搜索新地点，按地理位置绘制您数据库中的人，并通过在地图上连接他们的事件来追踪单个人的生活。

<div style="clear:both;"></div>

---

![1707年时间滑块设置的 OpenHistoricalMap 层上的伦敦](screenshots/ohm.png){ align=left width="400"}

### 历史地图

将存储为媒体对象的历史地图转换为自定义地图叠加。

您还可以切换到 [OpenHistoricalMap](https://www.openhistoricalmap.org/) 项目的历史矢量地图。使用时间滑块浏览您家族历史中地点的演变，并显示祖先居住或事件发生的地点。

<div style="clear:both;"></div>

---

![“阿尔伯特”的搜索结果，包括人、事件和媒体](screenshots/search.png){ align=right width="400"}

### 查找任何内容

全文搜索引擎覆盖所有 Gramps 对象类型，包括文本注释的内容，并支持通配符和逻辑运算符。

对于精确查询，对象列表视图提供基于 [Gramps 对象查询语言](../user-guide/goql.md) 的高级过滤模式，以及按文本、标签和隐私的快速过滤。

从任何人的页面， [外部搜索](../user-guide/external-search.md) 打开一个预填充的搜索，涵盖 FamilySearch、Ancestry、CompGen 和其他网站——您也可以添加自己的。

<div style="clear:both;"></div>

## 构建和研究 { .feature-group }

![编辑模式下的祖先树，添加家庭成员的对话框](screenshots/tree-edit.png){ align=left width="400"}

### 在图表中直接构建您的家谱

将树视图切换到编辑模式，无需离开图表即可扩展您的家谱。每个人的卡片都有一个 **+** 按钮，可以添加父亲、母亲、孩子或配偶——可以链接数据库中已有的人，或现场创建一个全新的人。每次更改都会立即保存。

查看 [编辑家谱](../user-guide/tree-edit.md)。

<div style="clear:both;"></div>

---

![AI 助手读取出生证明并建议新记录](screenshots/chat.png){ align=right width="400"}

### 集成的 AI 助手

用您自己的语言询问有关您的家谱的问题，并根据您的数据获得答案。

助手不仅仅是搜索：它直接使用一组工具查询您的数据库，过滤人、事件、家庭和地点，并计算个体之间的关系。您可以查看它在构建答案时使用的工具，较长的问题会作为后台任务运行，因此您可以导航离开并返回。

助手是可选的，需要由 [服务器管理员设置](../install_setup/chat.md) 与 AI 模型提供者。

<div style="clear:both;"></div>

---

![显示十一位匹配者共享 DNA 段的染色体浏览器](screenshots/dna.png){ align=left width="400"}

### DNA 匹配、染色体浏览器和 Y-DNA

从您的 DNA 测试提供商上传 DNA 匹配数据，将其与您的家谱存储在一起，并在互动染色体浏览器中查看您的匹配。

原始 Y 染色体 SNP 数据可用于确定一个人最可能的 [Y-DNA 单倍群](../user-guide/y-dna.md)，并在人的 Y 染色体树中显示他们的父系祖先，并提供时间估算。分析完全在您自己的服务器上运行——没有数据发送给任何第三方。

<div style="clear:both;"></div>

---

![带有两个被标记的人和其他检测到的面孔轮廓的画作](screenshots/tag.png){ align=right width="400"}

### 使用自动面部检测在照片中标记人

与您的亲属一起识别旧家庭照片中的祖先。面孔会自动检测，因此标记一个人只需两次点击。

<div style="clear:both;"></div>

---

![带有状态、优先级和标签的研究任务列表](screenshots/tasks.png){ align=left width="400"}

### 集成的任务管理应用

Gramps Web 附带一个集成的任务管理应用，以组织和规划您的家谱研究。为每个任务指定状态、优先级和标签，在丰富的文本描述中记录您的进展，并附上您在此过程中收集的媒体。

这些任务作为来源存储在 Gramps 数据库中，因此它们成为您家谱数据的一部分，并可以在 Gramps Desktop 中访问和编辑。

<div style="clear:both;"></div>

---

![关于识别家庭照片中人物的博客文章](screenshots/blog.png){ align=right width="400"}

### 包含家谱博客

以博客故事的形式总结您的研究，附上图片，并与您的亲属分享。专用编辑器使撰写新帖子变得简单。所有数据存储在 Gramps 数据库中。

<div style="clear:both;"></div>

## 共同协作 { .feature-group }

![家谱中的人物列表](screenshots/list.png){ align=left width="400"}

### 隐私级别和用户访问

您可以 [将记录标记为私有](../user-guide/privacy.md)——甚至是单个姓名、事件链接或 DNA 匹配——并控制哪些用户可以查看私有记录。私有记录在数据库层被过滤，以确保最大安全性。此外，您可以控制用户能够添加和编辑的内容。

用户可以使用密码登录，或通过使用 [OpenID Connect](../install_setup/oidc.md) 的外部身份提供者登录——开箱即用支持 Google 和 Microsoft，以及 Keycloak、Authentik 和 Authelia 等自定义提供者。

<div style="clear:both;"></div>

---

![显示个人记录中更改字段的修订](screenshots/revisions.png){ align=right width="400"}

### 完整的修订历史——带撤销功能

您对家谱的每次编辑都会被记录。浏览按事务分组的完整历史，深入了解任何单独的更改，以查看确切添加、删除或修改了哪些字段，并在发现错误时撤销事务。每个对象的页面也有自己的修订选项卡，显示谁在何时更改了它。

查看 [修订历史](../user-guide/revisions.md)。

<div style="clear:both;"></div>

---

![Gramps Desktop 的工具菜单，包含 Gramps Web 同步条目](screenshots/sync.png){ align=left width="300"}

### 与 Gramps Desktop 的完全集成

Gramps Web 使用与 [Gramps Desktop](https://gramps-project.org/) 相同的数据模型和数据库。您可以浏览和编辑所有相同的 [记录类型](https://gramps-project.org/wiki/index.php/Gramps_Data_Model)：人、家庭、事件、地点、存储库、来源、引用、媒体对象和注释。

通过 [Gramps Web Sync 插件](../administration/sync.md) 与 Gramps Desktop 同步，您可以双向同步数据，因此可以在 Gramps Desktop 和 Gramps Web 中并行工作。

<div style="clear:both;"></div>

## 报告和数据导出 { .feature-group }

![生成的祖先报告，格式为 PDF](screenshots/report.png){ align=right width="400"}

### 生成可打印的报告

Gramps Web 基于与 Gramps Desktop 相同的核心，因此您可以直接从浏览器生成几乎所有 [报告](https://gramps-project.org/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports)，包括关系图或书籍报告，格式为 PDF。

<div style="clear:both;"></div>

---

![导出页面，列出可用的文件格式](screenshots/export.png){ align=left width="300"}

### 无锁定——数据导入和导出

以各种格式导入数据，包括 Gramps XML 和 GEDCOM，并随时下载您的所有数据——家谱数据、媒体文件和用户帐户——以进行备份或迁移到不同的服务器。

导入可以在写入之前预览为干运行，并且可以将完整备份恢复到家谱中。

<div style="clear:both;"></div>

## 随处使用 { .feature-group }

![桌面和手机上相同的个人页面](screenshots/mobile.png){ align=right width="400"}

### 在每个设备上都能使用

在任何带有网络浏览器的设备上使用 Gramps Web：上传照片、创建或编辑记录，或在下次家庭聚会上向亲属展示您的家谱。

Gramps Web 是一个渐进式网络应用：将其安装到您的主屏幕或桌面，它的行为就像一个本地应用。在桌面上， [键盘快捷键](../user-guide/shortcuts.md) 可以让您在几次按键中到达任何地方——按 `?` 查看所有快捷键。

<div style="clear:both;"></div>

---

![语言选择菜单](screenshots/lang.png){ align=left width="300"}

### 完全国际化

使用 Gramps 社区翻译的 50 多种语言中的任何一种来使用界面。

<div style="clear:both;"></div>

## 还有更多

- **通知和后台任务**——导入、导出、报告和索引重建在后台运行，进度和错误集中在一个地方
- **标签、书签和历史**——使用颜色编码的标签组织对象，并返回到您正在处理的内容
- **批量编辑**——在列表视图中选择多个对象以一次性删除它们，或合并重复对象
- **可自定义的列表视图**——选择要显示的列，并按文本、标签或隐私进行过滤
- **文本识别 (OCR)**——从您媒体库中的扫描文档中提取文本
- **数据验证**——检查您的家谱是否存在不合理的日期和其他数据问题
- **日历**——以公历、儒略历、希伯来历、法国共和历、波斯历、伊斯兰历或瑞典历输入日期
- **个性化**——为您的网站命名，设置主题颜色，以及主页文本和图片

## 演示

要登录演示，请使用以下用户名/密码对之一。每个代表 Gramps Web 中的一个用户角色。

`owner / owner` <br>
`editor / editor` <br>
`contributor / contributor` <br>
`member / member`

演示每两小时重置一次，因此您所做的任何更改都是临时的。

[前往演示登录](https://demo.grampsweb.org/){ .md-button .md-button--primary target="_blank"}

### 感谢

演示由 DigitalOcean 友好支持。

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean 推荐徽章" /></a>
