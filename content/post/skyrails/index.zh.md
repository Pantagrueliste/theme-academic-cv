---
title: "从截图重建Skyrails"
subtitle: 数字考古、人工智能与软件的过时

summary: >
  Skyrails是约塞·维贾亚打造的一款出色的三维网络浏览工具，多年前便从网上消失了。凭着寥寥几张截图，
  Claude一夜之间把它重建了出来。后来原版在GitHub上现身，我们才得以衡量这次重建究竟有多接近。

date: "2026-10-01T00:00:00Z"
lastmod: "2026-10-01T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: '重建版Skyrails中的《悲惨世界》人物，焦点落在珂赛特身上'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- 可持续性
- 人工智能
- 数据可视化

categories:
- 札记
---

2007年前后，时为新南威尔士大学学生的约塞·维贾亚（Yose Widjaja）写出了Skyrails——一个在三维空间中探索网络的非凡程序。用户穿行于网络本身之中，沿着发光的轨道从一个节点走到另一个节点，仿佛置身数据内部。在那个研究工具大多扁平灰暗的年代，它看上去像一款电子游戏。炫目的画面背后，是实打实的深度：Skyrails有自己的脚本语言，用来设定图的样式、分析图的结构；菜单也用这门语言写成，不会编程的人照样能用。这一切，都是一个学生单枪匹马完成的。多年前我在YouTube上看过一段演示，至今念念不忘。


## 消失的程序

Skyrails从未得到维护。它运行在Windows上，大学网站上的主页已不复存在，我顺着找到的每一个链接都已失效。留存下来的只有痕迹：Flickr上的[一组截图](https://www.flickr.com/photos/14933315@N05/albums/72157602730584157/)，以及2007年的寥寥几篇博文，分别发在[FlowingData](https://flowingdata.com/?p=947)、蒂姆·兰伯特（Tim Lambert）的[*Deltoid*](https://scienceblogs.com/deltoid/2007/10/22/skyrails-graph-visualizations)和[InfoVis Wiki](https://infovis-wiki.net/wiki/2007-10-27:_Skyrails:_Social_Network_Visualisation_System)上。

这些截图透露的信息多得出人意料。画面上有飘着缕缕云丝的深蓝夜空，以动态V形箭头绘出的边，形如图标或饼图的节点，还有按住鼠标右键时在节点周围展开的环形菜单。截图里还能看到驱动各个演示的脚本名称（`labs.van`、`macaque.van`、`worldtrade.van`），这些脚本生成的菜单，以及名为*normal*、*desert*、*valley*和*openspace*的四套主题。其中一张甚至留下了一行脚本语言，就敲在屏幕顶端的控制台里：

```
with all nodes do nodeplane x 1 -1 end
```


## 凭证据重建

Claude根据这些证据，一夜之间重建了Skyrails。新版本借助[Three.js](https://threejs.org/)在网页浏览器中运行，按理说也应当能在虚拟现实头显上使用。它复刻了天空、V形箭头轨道、带着图标、饼图和圆环的发光节点、指针所指节点上的大号标签、环形菜单，以及四套主题。它还有一门小小的脚本语言，围绕截图中留存的那一行搭建而成，用`with … do … end`语句来设定图的样式、定义菜单。

为了检验，我载入了三个经典数据集：约翰·帕吉特（John Padgett）的佛罗伦萨家族网络，记录各家族之间的联姻与商业往来；韦恩·扎卡里（Wayne Zachary）的空手道俱乐部；以及高德纳（Donald Knuth）的《悲惨世界》人物网络——两个人物若在同一章中出场，便连在一起。下面的视频在最后这个网络中穿行，从冉阿让到沙威、芳汀、珂赛特和马吕斯。镜头沿着哪条轨道行进，哪条轨道便亮起来。

<video controls playsinline preload="metadata" poster="/post/skyrails/poster.jpg" style="width:100%; height:auto; border-radius:4px;">
  <source src="/post/skyrails/skyrails-les-miserables.mp4" type="video/mp4">
  您的浏览器无法播放此视频，您可以改为<a href="/post/skyrails/skyrails-les-miserables.mp4">下载</a>观看。
</video>

结果与截图如此相像，我当即怀疑，原版代码的某些痕迹在训练过程中被模型吸收了。


## 原版现身

接着，事情出现了转折。重建完成之后，我在GitHub上找到了原版程序。2015年，一位研究者征得约塞·维贾亚的同意，把它连同ShmooCon安全会议上一场数据可视化报告的代码一并公开（[RITHoneynet/DataVisualization](https://github.com/RITHoneynet/DataVisualization)，另有副本见[Light0617/3D_UIUX](https://github.com/Light0617/3D_UIUX/tree/master/skyrails/skyrailsdist)）。其中有Windows可执行文件、数据、着色器和原始脚本，唯独没有主引擎的源代码。

于是，两者可以对照了。重建版在外观和手感上与原版相当接近，脚本语言和着色器却大相径庭。原版脚本是这样的：

```
with all edges do (
   if(#marriage == 1) then (
      linkorigin <- marriage -> linktarget;
   ) end;
) end;
```

它们用`sub`定义子程序，用`menudef`和`menulink`定义菜单，用`rgb: 130 0 0`定义颜色，用箭头定义连接类型。这些在重建版里一概没有；两者共有的，只是截图中可见的`with … do … end`句式。原版着色器名为`BloomFX`、`RetinalBurnFX`之类，与新的着色器也毫无共同之处。

这并不能了结模型是否“记住”了原作的问题。原版脚本自2015年起便已公开，完全可能进入了模型的训练数据；而模型究竟见过什么，谁也无法确知，模型自己也不例外。但如果模型真的记住了Skyrails，我想它至少会把那门语言复现出来。从这些差异来看，Claude依据的应是截图中的证据。


## 数字考古与软件的可持续性

我把这次实验看作一种数字考古：根据一件失物留下的痕迹将它重建，再找到原物，量一量我们离它有多近。与任何复原一样，新的Skyrails是一种诠释。它的外观与行为以证据为本，底下的一切则全是新的。

这也关乎可持续性。软件过时，比它当初要读取的数据快得多。一个程序死去，用它做出的文件、脚本和可视化即便留存下来，也难以再打开。2000年代的许多软件，如今只以截图、视频和旧二进制文件的形式存在，而能运行这些文件的机器越来越少。原版Skyrails或许还能在Windows电脑上或模拟器里启动，但源代码既已失传，它便再也无法维护、改编或移植。

正如我几年前所预言的，人工智能正在成为对抗这类过时的实用工具。它能根据痕迹重建失传的工具，也能重新打造让旧数据保持可用的读取程序。这个项目显而易见的下一步，是教新引擎读懂原版的`.van`脚本和数据文件，让约塞·维贾亚在2007年写下的演示重新运行起来。对每一个关心数据可持续性的人来说，无论身在科研、档案还是数字人文领域，这都值得关注。

Skyrails走在了时代前面，近二十年后依然令人惊艳。这一构想与设计的全部功劳，都属于约塞·维贾亚；但愿这篇文字能传到他那里。
