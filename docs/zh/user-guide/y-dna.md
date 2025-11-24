# 使用 Gramps Web 进行 Y-DNA 分析

!!! note "注意"
    此功能需要 Gramps Web API 版本 3.3.0 或更高版本，以及 Gramps Web 前端版本 25.9.0 或更高版本。

Gramps Web 中的 Y-DNA 视图可以使用原始 Y 染色体单核苷酸多态性 (SNP) 数据来确定一个人最可能的 Y-DNA 单倍群，并在人体 Y 染色体树中显示派生的祖先及其时间估计。

## 如何获取和存储 Y-DNA SNP 数据

要获取 Y-DNA SNP 数据，您需要通过基因检测服务进行 Y-DNA 测试。结果以一组突变 (SNP) 表示，每个突变由一个字符串标识（例如 `R-BY44535`）和一个 `+` 或 `-` 符号，指示该突变是存在还是缺失。Gramps Web 期望将所有测试过的 SNP 字符串以格式 `SNP1+, SNP2-, SNP3+,...` 存储在自定义类型为 `Y-DNA` 的个人属性中（区分大小写）。您可以在 Gramps Web 或 Gramps Desktop 中手动创建此属性，或者导航到 Gramps Web 中的 Y-DNA 视图，点击蓝色的“添加”按钮，选择要添加数据的个人，然后粘贴 SNP 字符串。在任何情况下，数据将作为个人属性存储在您的 Gramps 数据库中。

[请参见下面](#instructions-for-obtaining-snp-data-from-testing-services) 获取有关如何从各种检测服务获取 SNP 数据的说明。

## 工作原理

一旦一个人拥有包含 SNP 数据的 `Y-DNA` 属性，Gramps Web 将使用开源的 [yclade](https://github.com/DavidMStraub/yclade) Python 库来确定该人在人体 Y 染色体树上的最可能位置。该树是由 [YFull](https://www.yfull.com/) 项目基于数万个 Y-DNA 测试创建的。请注意，Gramps Web 使用 YFull 树的本地副本，因此不会将任何数据发送给第三方。

树从根部遍历到叶子，在每个节点上，与该节点相关的 SNP 与该人的阳性和阴性测试 SNP 进行比较，并遵循适当的分支。

最终结果是从树的根部（[Y 染色体“亚当”](https://en.wikipedia.org/wiki/Y-chromosomal_Adam)）到与该人 SNP 数据一致的最派生的分支的一系列谱系。每个谱系都有一个基于属于该谱系的 YFull 数据库中样本的年龄的估计年龄。

由于 Y 染色体是从父亲遗传给儿子的，因此这一系列谱系对应于该人的父系祖先的摘录。

## 如何解读结果

最重要的信息是该人最可能的单倍群，显示在页面顶部。该名称链接到 [YFull](https://www.yfull.com/) 网站上相应的页面，其中包含更多信息，例如属于该单倍群的测试样本的原产国。

在 Gramps Web 中显示的父系祖先树中，测试人员正上方的框是所有属于该人单倍群的测试样本的最近共同祖先 (MRCA)。该祖先显示的日期是他的估计出生日期。位于他上方的祖先是定义该单倍群的突变首次出现的祖先。

由于 Y 染色体的突变率较慢，MRCA 可能在几百年前。对于稀有单倍群（即目前测试人数较少的单倍群），甚至可能是数千年前。

## 从检测服务获取 SNP 数据的说明

### [YSEQ](https://www.yseq.net/)

登录到“我的账户”后，转到“我的结果 / 查看我的等位基因”，并导航到页面底部。文本字段“紧凑的等位基因列表”是专门为 Gramps Web 添加的，格式正好适合粘贴到 `Y-DNA` 属性中。
