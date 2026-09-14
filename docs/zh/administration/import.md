# 导入数据

您可以通过上传从其他家谱程序、在线服务或 Gramps Desktop 导出的文件，将现有的家谱导入 Gramps Web。

导入功能位于 [管理设置](settings.md) 的 **数据** 部分（应用程序顶部工具栏中的用户图标 ▸ 管理），可供树的所有者和管理员使用。当树仍然为空时，主页“开始使用”卡片上的 **导入家谱** 按钮也会引导您到此。

## 使用哪个文件

| 来源 | 导出您的家谱为 | 文件扩展名 |
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
3. 文件首先会被解析，随后会显示一个“确认导入”对话框，显示它包含多少个对象（人、家庭、事件、地点等）。此时您的树中尚未添加任何内容。检查计数是否看起来合理，然后点击 **导入** 继续，或点击 **取消** 中止而不更改任何内容。
4. 导入在后台运行，并显示进度指示器。一旦数据导入完成，搜索索引将被更新，对于大型树，这可能需要一些时间。

导入完成后，请检查结果：将主页 **统计** 面板中的人数与您旧程序中的人数进行比较，并打开一个您熟悉的家庭，以查看父母、子女、日期和地点是否如预期那样传递过来。

!!! warning
    常规导入是纯粹的附加操作：它始终创建新对象，而不会更新或删除现有对象，即使这些对象在您的树中已经存在，且具有相同的 Gramps ID 或句柄。重复导入同一文件——或导入与树中已有数据重叠的文件——将导致每个匹配对象重复，而不是合并或跳过它。

    如果您需要将其他地方的更改导入到已经导入的树中，请使用 [从备份恢复](settings.md#restore-from-backup)，它会替换树以匹配上传的文件，而不是添加到其中。这需要一个 Gramps XML 文件。

如果为您的树设置了人数限制（请参见 [使用配额](settings.md#usage-quotas)），则会拒绝超出该限制的导入。

## GEDCOM 文件

可以导入 GEDCOM 5.5.1 和 GEDCOM 7 文件。需要注意以下几点。

### 字符编码

GEDCOM 5.5.1 文件在其头部声明其字符编码。支持 UTF-8、UTF-16、ANSEL 和 Windows（ANSI）编码。如果导入后带有重音或其他特殊字符的名称看起来乱码（例如 `MÃ¼ller` 而不是 `Müller`），则可能是文件以与其声明不同的编码导出的。请从您的旧程序中再次导出文件，如果提供选择，请选择 UTF-8，然后 [重新开始](#starting-over)。

GEDCOM 7 文件必须始终以 UTF-8 编码；其他文件将被拒绝，并显示“无效的 GEDCOM 文件”错误。

### 程序特定数据

许多程序在 GEDCOM 中添加了自己的扩展，其他程序无法理解。Gramps 不会默默丢弃这些数据：它无法解释的行会被收集在附加到其所属的个人、家庭或其他对象的“GEDCOM 导入”类型的注释中。请查看这些注释，以查看是否有任何重要内容未能传递过来。

### 媒体文件

GEDCOM 文件包含对媒体文件（例如照片或扫描文档）的引用，但不包含文件本身。导入后，媒体对象存在于您的树中，但它们的文件缺失，这在 [媒体文件状态](settings.md#media-file-status) 下显示。要添加文件，请参见下面的 [导入媒体文件](#import-media-files)。

## 来自 Gramps Desktop

如果您正在使用 Gramps Desktop，有两个步骤可以准备您的数据库，以确保接下来的操作顺利进行。

1. 检查并修复数据库
    - 可选：通过导出为 Gramps XML 创建数据库备份
    - 运行 [检查和修复数据库工具](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database)。这将修复一些可能导致 Gramps Web 问题的内部不一致性。
2. 将媒体路径转换为相对路径
    - 使用 Gramps 媒体管理器 [将所有媒体路径从绝对路径转换为相对路径](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute)。请注意，即使使用相对路径，任何在您的 Gramps 媒体目录之外的媒体文件在与 Gramps Web 同步时也将无法正常工作。

然后将您的树导出为 Gramps XML (`.gramps`)，按照上述描述进行导入，并按照下一节的描述上传您的媒体文件。要在计算机和网络上继续处理同一棵树，请使用 [Gramps Web 同步插件](sync.md)。

### 为什么不支持 Gramps XML 包？

虽然 Gramps XML (`.gramps`) 是导入数据的首选格式，但 Gramps XML *包* (`.gpkg`) 不被 Gramps Web 支持。这是因为媒体文件的导入和导出例程不适合在 Web 服务器上使用。

## 导入媒体文件

如果您已导入家谱并需要上传相应的媒体文件，请在管理设置的 **数据** 部分使用 **导入媒体文件**。它期望一个包含缺失媒体文件的 ZIP 文件。文件通过以下两种方式之一与您树中的媒体对象匹配：

- **按校验和。** 对于具有校验和的媒体对象——例如从 Gramps Desktop 导入的树——将使用具有匹配校验和的文件，而不管其名称或 ZIP 文件中的文件夹结构。这仅在 Gramps 数据库中的校验和正确时有效，运行检查和修复工具可以确保这一点。
- **按路径。** 没有校验和的媒体对象——在 GEDCOM 导入后通常是这种情况——通过其路径匹配：ZIP 文件必须包含在媒体对象中存储的确切相对路径下的文件。

如果您 GEDCOM 文件中存储的路径是绝对路径（例如 `C:\Users\...\photo.jpg`），按路径匹配将无法工作。在这种情况下，建议首先将所有内容导入 Gramps Desktop，该程序有更多选项将现有媒体文件与导入的树关联，然后按照 [来自 Gramps Desktop](#coming-from-gramps-desktop) 的描述转移到 Gramps Web。

## 常见问题

**“不支持的格式”。** 只有 [上面列出的](#which-file-to-use) 文件扩展名可以被导入。如果您的程序或在线服务给您一个 ZIP 压缩包，请解压并上传其中的 `.ged` 文件。

**所有内容都出现两次。** 同一文件被导入了两次。由于导入从不合并，请 [重新开始](#starting-over)。

**特殊字符乱码。** 请参见 [字符编码](#character-encoding)。

**照片缺失。** 请参见 [导入媒体文件](#import-media-files)。

### 重新开始

如果导入出错，或者您想在旧程序中修复某些内容并重新导入，请首先使用管理设置的危险区域中的 [删除所有对象](settings.md#delete-all-objects) 清空树，然后导入修正后的文件。请注意，这也会删除您自导入以来在 Gramps Web 中所做的任何更改。
