## 准备您的 Gramps 数据库

如果您正在使用 Gramps Desktop，有两个步骤可以准备您的数据库，以确保接下来的操作顺利进行。如果您是从其他家谱程序迁移，可以跳过此步骤。

1. 检查并修复数据库
    - 可选：通过导出为 Gramps XML 创建数据库备份
    - 运行 [检查和修复数据库工具](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database)。这将修复一些可能导致 Gramps Web 问题的内部不一致性。
2. 将媒体路径转换为相对路径
    - 使用 Gramps 媒体管理器 [将所有媒体路径从绝对路径转换为相对路径](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute)。请注意，即使使用相对路径，任何位于 Gramps 媒体目录之外的媒体文件在与 Gramps Web 同步时也将无法正常工作。

## 导入家谱数据

要导入现有的家谱树，请使用“导入”页面并上传任何 Gramps 支持的文件格式的文件 &ndash; 请参见 Gramps Wiki 中的 [从其他家谱程序导入](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program)。

如果您已经在使用 Gramps Desktop，强烈建议使用 Gramps XML (`.gramps`) 格式，以确保您的在线和离线家谱使用相同的标识符并可以 [同步](sync.md)。

点击“导入”后，文件首先会被解析，随后会显示一个“确认导入”对话框，预览文件包含的对象（人员、家庭、事件、地点等），在将任何内容添加到您的家谱之前。检查计数，然后在对话框中点击“导入”以继续，或点击“取消”以在不更改任何内容的情况下中止。

!!! warning
    常规导入是纯粹的添加：它始终创建新对象，而不会更新或删除现有对象，即使是那些在您的家谱中已存在的对象，且具有相同的 Gramps ID 或句柄。重复导入同一文件 &ndash; 或导入与家谱中已有数据重叠的文件 &ndash; 将复制每个匹配的对象，而不是合并或跳过它。

    如果您需要将其他地方的更改带入已导入的家谱，请使用 [从备份恢复](settings.md#restore-from-backup)，它将替换树以匹配上传的文件，而不是向其添加内容。

## 为什么不支持 Gramps XML 包？

虽然 Gramps XML (`.gramps`) 是导入数据的首选格式，但 Gramps XML *包* (`.gpkg`) 不受 Gramps Web 支持。这是因为媒体文件的导入和导出例程不适合在 Web 服务器上使用。

要导入属于已导入的 `.gramps` 文件的媒体文件，请参见下一部分。

## 导入媒体文件

如果您已上传家谱树并需要上传相应的媒体文件，可以在“导入”页面上使用“导入媒体档案”按钮。

它需要一个包含缺失媒体文件的 ZIP 文件。ZIP 文件中的文件夹结构不必与 Gramps 媒体文件夹中的文件夹结构相同，因为文件是通过其校验和与媒体对象匹配的。

请注意，此功能仅适用于在 Gramps 数据库中具有正确校验和的文件（这应通过在第一步中运行检查和修复工具来确保）。

当从其他家谱程序迁移到 Gramps Web 时，包括媒体文件，建议首先将所有内容导入 Gramps Desktop，因为它有更多选项将现有媒体文件与导入的家谱树关联。
