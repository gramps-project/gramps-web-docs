---
hide:
  - toc
  - navigation
---

# 功能


![图片标题](screenshots/sync.png){ align=left width="300"}

## 与 Gramps Desktop 的完全集成

Gramps Web 使用与 [Gramps Desktop](https://gramps-project.org/) 相同的 **模型 / 数据库** 结构来存储家谱数据。您可以浏览与 Gramps Desktop 中相同的 [记录类型](https://gramps-project.org/wiki/index.php/Gramps_Data_Model)：***人、家庭、事件、地点、档案馆、来源、引用、媒体对象和笔记。***

通过 [Gramps Web Sync 插件](../administration/sync.md) 与 Gramps Desktop 之间可以双向同步数据！尽管使用 Gramps Web 或您熟悉的 Gramps Desktop 应用程序编辑数据，它们可以无缝协作！

<div style="clear:both;"></div>

---

![图片标题](screenshots/fan.png){ align=right width="400"}

## 互动家谱图

以祖先树、后代树、沙漏图、关系图或扇形图的形式浏览您的家谱，提供高质量的互动图形和可配置的世代数量。

将鼠标悬停在任何人身上，可以查看包含其关键信息的预览卡片，并可以直接从图表跳转到完整详细页面。

<div style="clear:both;"></div>

---

![图片标题](screenshots/tree-edit.png){ align=left width="400"}

## 直接在图表中构建您的家谱

将树视图切换到编辑模式，无需离开图表即可扩展您的家谱。每个人的卡片上都有一个 **+** 按钮，可以添加父亲、母亲、孩子或配偶——可以链接数据库中已有的人，或现场创建一个全新的人。每次更改都会立即保存。

请参见 [编辑家谱](../user-guide/tree-edit.md)。

<div style="clear:both;"></div>

---

![图片标题](screenshots/timeline.png){ align=right width="400"}

## 按时间顺序的时间线

查看您家谱中的每个事件在水平、可缩放的时间线上的布局。滚动和缩放穿越几个世纪，然后过滤到单个个人——或所有他们的祖先或后代——或在一个地方发生的所有事件。

请参见 [时间线](../user-guide/timeline.md)。

<div style="clear:both;"></div>

---

![图片标题](screenshots/map.png){ align=left width="400"}

## 强大的地图

在互动的可搜索地图上显示您家谱中的所有地点。在创建地点时，可以直接在 OpenStreetMap 上搜索新地点，地理位置标记您数据库中的人物，并通过在地图上连接他们的事件来追踪单个人的生活。

<div style="clear:both;"></div>

---

![图片标题](screenshots/ohm.png){ align=right width="400"}

## 历史地图

将存储为 Gramps 媒体对象的历史地图转换为自定义地图覆盖。

此外，由 [OpenHistoricalMap](https://www.openhistoricalmap.org/) 项目创建的历史矢量地图是家谱映射的完美补充。使用时间滑块浏览您家族历史中地点的演变，并显示祖先居住或事件发生的地点。

<div style="clear:both;"></div>

---

![图片标题](screenshots/search.png){ align=left width="400"}

## 查找任何内容

全文搜索引擎覆盖所有 Gramps 对象类型，包括文本笔记的内容，并支持通配符和逻辑运算符。

如果您的服务器启用了此功能，**语义搜索** 可以通过意义而非确切词语回答自然语言查询，例如“19 世纪巴伐利亚的农民”。对于精确查询，对象列表视图提供基于 [Gramps 查询语言](../user-guide/gql.md) 的高级过滤模式，以及按文本、标签和隐私的快速过滤。

从任何个人页面，[外部搜索](../user-guide/external-search.md) 可以打开在 FamilySearch、Ancestry、CompGen 和其他网站上的预填充搜索——您也可以添加自己的搜索。

<div style="clear:both;"></div>

---

![图片标题](screenshots/chat.png){ align=right width="400"}

## 集成的 AI 助手

由 AI 驱动，Gramps Web 允许您以母语与您的家谱聊天！

助手不仅仅是搜索：它直接使用一组工具查询您的数据库，过滤人物、事件、家庭和地点，并计算个体之间的关系。您可以看到它在构建答案时使用的工具，较长的问题作为后台任务运行，因此您可以导航离开并再回来。

<div style="clear:both;"></div>

---

![图片标题](screenshots/dna.png){ align=left width="400"}

## DNA 匹配、染色体浏览器和 Y-DNA

如果您有来自某个 DNA 家谱提供商的 DNA 匹配数据，可以上传并以未来-proof 的方式存储它，并在互动染色体浏览器中查看您的匹配。

原始 Y 染色体 SNP 数据可以用来确定一个人最可能的 [Y-DNA 单倍群](../user-guide/y-dna.md)，并在人体 Y 染色体树中显示他们的父系祖先，并提供时间估计。分析完全在您自己的服务器上运行——没有数据发送给任何第三方。

<div style="clear:both;"></div>

---

![图片标题](screenshots/tag.png){ align=right width="400"}

## 使用自动面部检测标记照片中的人物

与您的亲属合作，识别旧家庭照片中的祖先。得益于自动面部检测，标记人物只需两次点击。

<div style="clear:both;"></div>

---

![图片标题](screenshots/revisions.png){ align=left width="400"}

## 完整的修订历史 - 可撤销

对您家谱的每次编辑都会被记录。浏览按事务分组的完整历史，深入了解任何单独的更改，以查看具体添加、删除或修改了哪些字段，并在发现错误时撤销事务。每个对象的页面也有自己的修订选项卡，显示谁在何时更改了它。

请参见 [修订历史](../user-guide/revisions.md)。

<div style="clear:both;"></div>

---

![图片标题](screenshots/list.png){ align=right width="400"}

## 隐私级别和用户访问

许多人希望保留某些细节的私密性，我们对此表示尊重！您可以将记录标记为私密，并控制哪些用户可以查看私密记录。私密记录在数据库层被过滤，以确保最大安全性。此外，您可以控制用户能够添加和编辑的内容。

用户可以使用密码登录，或通过使用 [OpenID Connect](../install_setup/oidc.md) 的外部身份提供者登录——Google 和 Microsoft 默认支持，以及 Keycloak、Authentik 和 Authelia 等自定义提供者。

<div style="clear:both;"></div>

---

![图片标题](screenshots/blog.png){ align=left width="400"}

## 包含家谱博客

以博客故事的形式总结您的研究，并与您的亲属分享。专用编辑器使撰写新帖子变得简单。所有数据都存储在 Gramps 数据库中。

<div style="clear:both;"></div>

---

![图片标题](screenshots/tasks.png){ align=right width="400"}

## 集成的任务管理应用

Gramps Web 附带一个集成的任务管理应用，以组织和计划您的家谱研究。为每个任务设置状态、优先级和标签，在丰富的文本描述中记录您的进展，并附上您在此过程中收集的媒体。

这些任务作为来源存储在 Gramps 数据库中，因此它们成为您家谱数据的一部分，并可以在 Gramps Desktop 中访问和编辑。

<div style="clear:both;"></div>

---

![图片标题](screenshots/report.png){ align=left width="400"}

## 生成可打印报告

由于它直接建立在支持 Gramps Desktop 的核心之上，您可以直接从浏览器生成几乎所有桌面应用支持的 [报告](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Reports)，包括关系图或书籍报告的 PDF。

<div style="clear:both;"></div>

---

![图片标题](screenshots/export.png){ align=right width="300"}

## 无锁定 - 数据导入和导出

除了能够以各种格式导入数据，包括 Gramps XML 和 GEDCOM，Gramps Web 使用户可以随时下载他们的所有数据（家谱数据、媒体文件、用户帐户），以备份或迁移到其他服务器。您的数据仅属于您！

导入可以在写入任何内容之前预览为干运行，并且可以将完整备份恢复到树中。

<div style="clear:both;"></div>

---

![图片标题](screenshots/mobile.png){ align=left width="400"}

## 在每个设备上均可使用

从任何支持网络的设备访问 Gramps Web。您可以上传照片、创建或编辑记录、向他人展示您的家谱，或者在下次家庭聚会上查找您记不起来的家庭成员姓名！

Gramps Web 是一个渐进式网络应用：将其安装到您的主屏幕或桌面，它的行为就像本地应用。在桌面上，[键盘快捷键](../user-guide/shortcuts.md) 让您在几次按键中到达任何地方——按 `?` 查看所有快捷键。

<div style="clear:both;"></div>

---

![图片标题](screenshots/lang.png){ align=right width="300"}

## 完全国际化

在 Gramps 社区翻译的 50 多种语言之间切换界面的语言。

<div style="clear:both;"></div>

---

## 还有更多

- **通知和后台任务** - 导入、导出、报告和索引重建在后台运行，进度和错误集中在一个地方
- **标签、书签和历史** - 使用颜色编码的标签组织对象，并返回到您正在处理的内容
- **批量编辑** - 在列表视图中选择多个对象以一次性删除，或合并重复对象
- **可自定义的列表视图** - 选择要显示的列，并按文本、标签或隐私进行过滤
- **文本识别 (OCR)** - 从您的媒体库中的扫描文档中提取文本
- **数据验证** - 检查您的家谱是否存在不合理的日期和其他数据问题
- **日历** - 输入公历、儒略历、希伯来历、法国共和历、波斯历、伊斯兰历或瑞典历中的日期
- **个性化设置** - 为您的网站命名、选择主题颜色，以及设置主页文本和图像

<p>&nbsp;</p>

## 演示

要登录演示，请使用以下任一 ***用户 / 密码*** 登录凭据。每个凭据代表 Gramps Web 用户可能被分配的用户类型。

`owner / owner` <br>
`editor / editor` <br>
`contributor / contributor` <br>
`member / member`


[前往演示登录](https://demo.grampsweb.org/){ .md-button .md-button--primary target="_blank"}


### 感谢

该演示得到了 DigitalOcean 的大力支持。

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean 推荐徽章" /></a>
