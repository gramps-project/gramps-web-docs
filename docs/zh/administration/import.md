# 导入数据

您可以通过上传从其他家谱程序、在线服务或 Gramps Desktop 导出的文件，将现有的家谱导入 Gramps Web。

导入功能位于 [管理设置](settings.md) 的 **数据** 部分（应用程序顶部工具栏中的用户图标 ▸ 管理），可供树的所有者和管理员使用。当树仍然为空时，主页“开始使用”卡片上的 **导入家谱** 按钮也会引导您到此。

## 使用哪个文件

| 来源 | 将您的树导出为 | 文件扩展名 |
|---|---|---|
| 其他家谱程序或在线服务 | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| 电子表格 | Gramps CSV | `.csv` |
| 地址簿 | vCard | `.vcf` |

GEDCOM 是几乎所有家谱程序和在线服务都可以导出的通用交换格式。在您的程序或网站上查找“导出”或“下载”选项，如果提供多个格式，请选择 GEDCOM。Gramps Wiki 页面 [从其他家谱程序导入](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) 有关于特定程序的说明。

如果您使用 Gramps Desktop，请选择 Gramps XML (`.gramps`)，而不是 GEDCOM。它可以无损地携带所有 Gramps 数据，并且您的在线和离线树保持相同的标识符，因此可以进行 [同步](sync.md)。请参见下面的 [来自 Gramps Desktop](#coming-from-gramps-desktop)。

## 导入家谱文件

1. 打开管理设置的 **数据** 部分。
2. 在“导入家谱”下，选择您的文件并点击 **导入**。
3. 文件首先会被解析，并显示一个“确认导入”对话框，显示它包含多少个对象（人、家庭、事件、地点等）。此时尚未向您的树中添加任何内容。检查计数是否看起来合理，然后点击 **导入** 以继续，或点击 **取消** 以在不更改任何内容的情况下中止。
4. 导入在后台运行，并显示进度指示器。一旦数据导入，搜索索引会更新，对于大型树，这可能需要一些时间。如果导入失败，将显示原因。

导入完成后，检查结果：将主页 **统计** 面板中的人数与您旧程序中的人数进行比较，并打开您熟悉的一个家庭，以查看父母、孩子、日期和地点是否如预期一样传输过来。

!!! warning
    常规导入是纯粹的附加操作：它始终创建新对象，而不会更新或删除现有对象，即使这些对象在您的树中已经存在，并且具有相同的 Gramps ID 或句柄。重复导入相同文件——或导入与树中已有数据重叠的文件——将复制每个匹配对象，而不是合并或跳过它。

    如果您需要将其他地方对已导入树所做的更改带入，请使用 [从备份恢复](settings.md#restore-from-backup)，它会替换树以匹配上传的文件，而不是添加到其中。这需要一个 Gramps XML 文件或 Gramps Web 备份。

如果为您的树设置了人数限制（请参见 [使用配额](settings.md#usage-quotas)），则会拒绝任何超出该限制的导入。

## GEDCOM 文件

可以导入 GEDCOM 5.5.1 和 GEDCOM 7 文件。有一些事项需要注意。

### 字符编码

GEDCOM 5.5.1 文件在其头部声明其字符编码。支持 UTF-8、UTF-16、ANSEL 和 Windows（ANSI）编码。如果导入后带重音或其他特殊字符的名称看起来乱码（例如 `MÃ¼ller` 而不是 `Müller`），则文件可能是用与其声明不同的编码导出的。请从您的旧程序中重新导出文件，如果提供选择，请选择 UTF-8，并 [重新开始](#starting-over)。

GEDCOM 7 文件必须始终编码为 UTF-8；其他文件会被拒绝，并显示“无效的 GEDCOM 文件”错误。

### 程序特定数据

许多程序在 GEDCOM 中添加了自己的扩展，其他程序无法理解。Gramps 不会默默丢弃这些数据：它无法解释的行会被收集在类型为“GEDCOM 导入”的注释中，附加到它们所属的人、家庭或其他对象上。请查看这些注释，以查看是否有任何重要内容未能传输。

### 媒体文件

GEDCOM 文件包含对媒体文件（如照片或扫描文档）的引用，但不包含文件本身。导入后，媒体对象存在于您的树中，但它们的文件缺失，这在 [媒体文件状态](settings.md#media-file-status) 下显示。要添加文件，请参见 [导入媒体文件](import-media.md)。

## 来自 Gramps Desktop

如果您使用 Gramps Desktop，有两个步骤可以准备您的数据库，以确保接下来的操作顺利进行。

1. 检查和修复数据库
    - 可选：通过导出为 Gramps XML 创建数据库备份
    - 运行 [检查和修复数据库工具](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database)。这可以修复一些可能导致 Gramps Web 问题的内部不一致性。
2. 将媒体路径转换为相对路径
    - 使用 Gramps 媒体管理器 [将所有媒体路径从绝对路径转换为相对路径](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute)。请注意，即使使用相对路径，任何位于 Gramps 媒体目录之外的媒体文件在与 Gramps Web 同步时也将无法正常工作。

然后将您的树导出为 Gramps XML (`.gramps`)，按照上述描述导入，并 [上传您的媒体文件](import-media.md)。要在计算机和网络上继续处理同一棵树，请使用 [Gramps Web Sync 附加组件](sync.md)。

### 为什么不支持 Gramps XML 包？

虽然 Gramps XML (`.gramps`) 是导入数据的首选格式，但 Gramps XML *包* (`.gpkg`) 不受 Gramps Web 支持。这是因为媒体文件的导入和导出例程不适合在 Web 服务器上使用。

## 常见问题

**“不支持的格式”。** 只有 [上面列出的](#which-file-to-use) 文件扩展名可以导入。如果您的程序或在线服务给您一个 ZIP 压缩包，请解压并上传其中的 `.ged` 文件。

**所有内容都出现两次。** 相同的文件被导入了两次。由于导入从不合并，请 [重新开始](#starting-over)。

**特殊字符乱码。** 请参见 [字符编码](#character-encoding)。

**照片缺失。** 请参见 [导入媒体文件](import-media.md)。

### 重新开始

如果导入出错，或者您想在旧程序中修复某些内容并重新导入，请首先使用管理设置的危险区中的 [删除所有对象](settings.md#delete-all-objects) 清空树，然后导入修正后的文件。请注意，这也会删除您自导入以来在 Gramps Web 中所做的任何更改。
