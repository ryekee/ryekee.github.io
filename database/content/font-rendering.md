Title: 字体渲染背后不得不说的故事  
Author: Ryekee  
Date: 2013-11-4 20:43
Tags: fonts, translation, geek  
Category: geek  
Slug: font-rendering  
Summary: 放大网页字体的截图，边缘竟出现五彩的颜色，圆滑纯黑并优美的字体放大之后为何会出现诡异的形状和颜色？这背后又有什么神奇的秘密？一起来到本期「走进科学」——字体渲染背后不得不说的故事。

*最近在看关于字体渲染技术的时候看到了[这篇文章](http://www.smashingmagazine.com/2012/04/24/a-closer-look-at-font-rendering/)，觉得算是对 Windows、MacOS 以及 iOS上渲染技术说的比较详细的了，就翻译成了中文，同步更新于[Ryekee_Blog](http://ryekee.com/2013/font-rendering)。有任何错误或者不当的翻译欢迎指出。:-)下面开始正文内容：*

>两年多（原文写于2012年）以前开始的Web字体革命，引出了一个我们忽视了多年的问题：**字体渲染**，新被发明出来的Web字体给我们带来了新的挑战。选择使用一个字体不再仅仅是样式问题，它已值得我们去探寻其背后是如何实现的了。

虽然我们无法改变网站访客的浏览器和操作系统，但了解字体渲染的原理，有助于我们搭建一个对所有人都友好易读的网站。直到最近，我们可以使用的「Web零风险」字体屈指可数。但它们为屏幕显示进行了精心的设计以及优化，因此不必太担心这些字体的显示效果。

如今，当我们为网站选择字体时已经有了更大的灵活性，可以清楚的看到，字体设计的渲染技术已经悄然发生了改变。操作系统厂商采用不同的字体渲染策略，这一情况还将随时间继续演化。随着对屏幕上的字体更加深入的了解，我们已经意识到，这些字型的渲染会因为操作系统和字体格式而存在着明显的差异。蛋疼的是，即便是精心设计的字体可能看上去都不适合`Windows`，只因为它们缺少了很重要的要素：字体微调（hinting）。

本文将介绍字体渲染的原理，它们被开发出来的历程，以及它们是怎么被应用在不同的操作系统和浏览器中的。因此当你为你下一个项目挑选字体时，你就知道要怎么样才可以确保排版的效果了。

#渲染策略

![Ideal shape, black-and-white and grayscale rendering](http://farm3.staticflickr.com/2849/10605654775_4ddb0df0bb_o.jpg)<!--1-->    
*理想的形状（左），黑白渲染（中），灰度渲染（右）*
&nbsp;

##栅格化（Rasterization）

在数字形态（digital type）中，字体被设计成矢量的图像。当文本在屏幕上显示时，需要将图形栅格化，理想的显示效果是需要不同的大小的一个个像素网格来共同组成字体的。你可以看到理想的形状中e的边缘并没有占满整个像素，但由于我们所能控制的最小元素就是像素了，也就造成了现实与理想的差距。  
因此，工业界发明出了越来越先进的渲染策略，以确保屏幕显示的字体友好易读。

##黑白渲染（Black and white rendering）

最早的字体渲染技术是使用黑白两色来填充像素，有时这种方法也被称作二值渲染（bi-level rendering）。目前打印机仍在使用这种方法，但由于打印机的高分辨率，打印的效果可以很好地还原原始的设计。  
然而当这一技术应用于屏幕时，早期屏幕的低分辨率的局限性使得字体的呈现效果并不好。虽然肉眼无法分辨每个像素，但是难看的锯齿边缘却很明显。  

##灰度渲染（Grayscale rendering）

从上世纪九十年代中期开始，我们的前人开始采用了一种很聪明方式，虽然当时的分辨率依旧很低，但可以控制每个像素的灰度，这就可以在栅格化的图像中存储更多的信息，以使字体边缘变得更加平滑。这就是灰度渲染。

在灰度渲染中，边缘的像素不再是纯黑的，它的灰度值取决于理想的字型在此像素所覆盖的面积比例。这样，字体的轮廓看起来更加平滑，设计的细节也更加丰富。屏幕上的字体不再仅仅满足于清晰可辨，它们甚至还可以体现字体本身的特征和风格。

这一方法也被称作抗锯齿渲染，与照片重新采样（resampled）到一个较低分辨率时的原理是相同的。我们的眼睛和大脑在理解灰色像素所包含的信息时，会将它转换为字型的轮廓，这就让我们可以获得与原始设计极为接近的渲染效果。  
类似的效果出现在当我们离报纸上糟糕的图片保持足够远的距离时（Chuck Close艺术）。最近，Gary Andrew Clarke就在他的「[Art Remixed](http://www.someprints.com/Spots-Prints-Posters/mona-lisa-remix-print-by-graphic-nothing.html)」系列作品中将这一原理运用到了极致。

##亚像素渲染（Subpixel rendering）

![Apparently colored pixels increase the resolution](http://farm3.staticflickr.com/2891/10605714756_92b772a266_o.jpg)<!--2-->   
*彩色像素提高了分辨率*

第三代渲染技术的特点是加入了颜色信息，如果我们把屏幕截图不断放大，可以看到字体边缘有红蓝两色出现，这就是亚像素渲染了。

在LCD屏中，一个像素是由红绿蓝三个紧密排列的亚像素构成的，它们决定了这一像素的颜色和亮度。由于它们是如此之小，以至于肉眼不会把它们看作是一个个独立的色点。如果我们仔细看看上图中被白点标记的「红色」像素，就可以发现它所采用的渲染策略：所有的亚像素都可以单独控制开或关的；若「空白」像素最右侧的亚像素是红色的话，则此像素都将填满红色。

![Subpixel rendering on an LCD screen.](http://farm8.staticflickr.com/7402/10605909993_7ec05e9264_o.jpg)<!--3-->   
*LCD屏中的亚像素渲染*

如果我们需要降低图片的饱和度，采用该技术的好处就显而易见了。相比于单纯的灰度渲染，水平方向的分辨率是其三倍。垂直方向的位置和粗细也更加的精确，文本也呈现得更加清晰。

#当前的应用情况

浏览器中文本的显示完全依赖于系统的渲染技术，因此当我们讨论Web字体渲染时，关键还是操作系统所采用的渲染技术。然而，由于每个浏览器所采用的技术都不相同，字间距（kerning）、连字（ligatures）、下划线位置甚至它们的粗细都不一样，因此我们无法在这些不同的浏览器中获得完全相同的渲染 效果（即便是在同一个操作系统下）。   
更蛋疼的是，在`Windows`下还可能采用两种技术来渲染——`GDI`或者`DirectWrite`。

在我们探寻背后的细节之前，让我们先了解一下每个浏览器所采用的渲染技术：  
![Rendering modes used by Windows browsers.](http://farm8.staticflickr.com/7308/10605681796_a770209e69_o.jpg)<!--4-->   
*各种Windows浏览器所采用渲染模型*

##Windows

在`Windows`系统下，字体格式对其渲染效果有很显著的影响，比如`PostScript`字体和`TrueType`字体之间就存在着巨大的差别。但这种差别并不是由浏览器所引起的，只要底层的字体一样，我们就可以看到完全相同的渲染效果。

尽管这种方法并不十分可靠，但从字体的命名中我们可以大致推断该字体所采用的渲染技术，比如，`EOT`和`.ttf`格式一定是`TrueType`技术，反之`.otf`通常是`PostScript`技术。但是还有一中封装的字体格式`WOFF`，它可以包含其中任意一种字体格式。因此光看文件名是不可能清楚它所采用的渲染技术的。除了`EOT`和`.ttf`格式文件可以断定是`TrueType`渲染技术外，其他文件格式所包含的是哪种字体都无法确定。因此在你购买字体时，你最好对想要购买的字体做一番了解。（[@Ryekee](http://ryekee.com): 我觉得这一句根本不用翻译，中国还有人会买字体么？）

`TrueType`和`PostScript`的区别在于描绘曲线时所采用的数学方法不同，但这一差异对栅格器并不会造成太大的影响，只有字型设计人员才需要考虑着两者的差别。另一个重要的区别就是所采用的字体微调的方法。`PostScript`只包含了组成字体的各种元素的抽象位置信息，而`TrueType`则包含了非常详细的底层命令，直接接管了渲染的进程。然而造成两种渲染技术的差异并不是它们的设计理念上的差别，而是源于Micro$oft采对`TrueType`采用了新的渲染引擎。

##Windows: TrueType字体

![TrueType font rendering with Windows grayscale](http://farm6.staticflickr.com/5540/10605912683_e8ba4d5298_o.jpg)<!--5-->  
![TrueType font rendering with Windows grayscale-zoom](http://farm6.staticflickr.com/5471/10605913893_6340f46696_o.jpg)<!--6-->  
*Windows灰度渲染下的TrueType字体渲染效果*  

在`Windows XP`中，许多浏览器都是采用灰度渲染来渲染文本的。尽管效果比不上`Mac OS`所采用的亚像素渲染，但字体在大尺寸下的效果依旧出众，字体的边缘很平滑。  

![TrueType font rendering with Windows GDI ClearType](http://farm8.staticflickr.com/7379/10605915553_c5b85799f7_o.jpg)<!--7-->  
![TrueType font rendering with Windows GDI ClearType-zoom](http://farm8.staticflickr.com/7417/10605687356_e582884384_o.jpg)<!--8-->  
*Windows GDI ClearType渲染下的TrueType字体渲染效果*  

`ClearType`渲染技术是Micro$oft对亚像素渲染的「借鉴」。它最早供`GDI`使用——经典的`Windows API`。尽管从`Windows XP`系统开始就可以使用该技术，但是所有的浏览器都并没有采用该技术。在`Windows 7`和`Vista`中，`ClearType`是默认开启的，从而使得其成为了应用最广泛的渲染技术（如果算上所有的互联网用户的话）。但需要注意的是，`ClearType`只适用于`TrueType`类Web字体，并不适用于`PostScript`类字体。

奇怪的是，Micro$oft吸纳了水平方向上亚像素渲染技术的优点，却全然抛弃了垂直方向上平滑度的改进。因此`ClearType`实际上是亚像素渲染和黑白渲染的杂交，结果使得字体在轮廓线上出现了锯齿，在大尺寸字体下更扎眼。即便是最精细的字体微调也无法消除曲线上难看的锯齿。

对于大尺寸的字体，`ClearType`表现得十分糟糕，水平方向上精确度带来的好处非但并不明显，粗糙的轮廓甚至毁了整体的渲染效果，技术仿佛退回了解放前。

![TrueType font rendering with DirectWrite](http://farm4.staticflickr.com/3742/10605675744_9a6323eb68_o.jpg)<!--9-->  
![TrueType font rendering with DirectWrite-zoom](http://farm8.staticflickr.com/7353/10605919193_111bba3c5f_o.jpg)<!--10-->  
*DirectWrite模式下的TrueType字体渲染效果*  

至少对`Windows`字体渲染技术来说，未来是光明的。在`GDI`的接班人`DirectWrite`中，Micro$oft为`ClearType`增加了垂直方向上的平滑度。新的渲染模型（目前应用于IE9）在所有尺寸下都提供了平滑而精确的渲染效果。与`Mac OS`不同的是，Micro$oft仍试图将轮廓与全像素高度（full pixel heights）对齐，如果字体微调得当的话，此举将可以获得更好的渲染效果。更牛逼的是，`DirectWrite`可以进行亚像素定位（subpixel positioning），让字符间的间隙与设计的完全相同，还改善了字体纹理的匀称度。

##Windows: PostScript字体

![PostScript font rendering with GDI grayscale](http://farm8.staticflickr.com/7460/10605691046_03c4a4ca5a_o.jpg)<!--11-->    
![PostScript font rendering with GDI grayscale-zoom](http://farm6.staticflickr.com/5491/10605921583_d18eb2ce10_o.jpg)<!--12-->    
*GDI灰度渲染模式下的PostScript字体渲染效果*  

在使用`GDI`渲染模式的浏览器中，`PostScript`类型的字体是通过灰度渲染呈现的。不同于流行的`GDI-ClearType`渲染模式，这种渲染模式可以使得字体轮廓更加平滑；与`TrueType`字体微调不同，`PostScript`字体微调更为简单，甚至可以自动完成。

![PostScript font rendering with DirectWrite](http://farm8.staticflickr.com/7375/10605668985_fef8b2b734_o.jpg)<!--13-->   
![PostScript font rendering with DirectWrite-zoom](http://farm4.staticflickr.com/3742/10605681674_a5f6b0372c_o.jpg)<!--14-->   
*DirectWrite下的PostScript字体渲染效果*  

`DirectWrite`不仅可以使字体的边缘更加平滑，它也可以运用亚像素渲染技术来渲染`PostScript`类字体。但与`TrueType`渲染不同的是，为了能够更加真实的反应笔画的粗细，它使用了更多的灰色像素。经过优化的渲染效果更加接近`Mac OS`的渲染了。

未来的某个时候（浏览器厂商并不会像我们期望的那样快的采用新技术），`DirectWrite`将取代`Windows`过时的渲染技术，到那时我们就不必再纠结于选择`TrueType`类字体还是`PostScript`类字体了。

##Windows: 无微调字体

![Unhinted font rendered with grayscale](http://farm8.staticflickr.com/7316/10605682714_e30f771aff_o.jpg)<!--15-->  
![Unhinted font rendered with grayscale-zoom](http://farm8.staticflickr.com/7355/10605696636_55ba6828d2_o.jpg)<!--16-->    
*灰度渲染下的无微调字体渲染效果*  

在`Windows`老式的灰度渲染模式下，无微调字体的渲染效果出奇的好。因为字体并没有通过微调与全像素对齐，栅格器也没有对其进行强制处理，其效果很接近`iOS`上的字体渲染。遗憾的是，目前来看，无微调字体还不适合使用，我们可以看看下图：

![Unhinted TrueType font in GDI-ClearType rendering](http://farm6.staticflickr.com/5506/10605685674_0f4cee6bbc_o.jpg)<!--17-->  
![Unhinted TrueType font in GDI-ClearType rendering-zoom](http://farm3.staticflickr.com/2843/10605675325_290729f4d9_o.jpg)<!--18-->  
*GDI-ClearType下的无微调TrueType字体的渲染效果*  

在许多有关Web字体渲染的讨论文章中都指出，`GDI-ClearType`极度依赖良好的字体微调。水平方向上的笔画需要通过微调来精确定义，否则笔画的粗细可能会不恰当。在大尺寸字体下，微调也极为重要。无微调字体在轮廓线在没有对齐像素网格的地方会出现一些「疤」，正如上图所示。

![Unhinted font rendered with DirectWrite](http://farm3.staticflickr.com/2824/10605700356_b703733581_o.jpg)<!--19-->  
![Unhinted font rendered with DirectWrite-zoom](http://farm4.staticflickr.com/3666/10605701786_6b20422d98_o.jpg)<!--20-->  
*DirectWrite下的无微调字体的渲染效果*  

在`DirectWrite`模式下，无微调的`PostScript`和`TrueType`两种Web字体的渲染效果几乎完全相同。这两种格式的文本字体仍需要良好的微调才可以保证笔画的清晰度和一致性。屏幕显示的字体可能可以侥幸避免无微调带来的不良效果，因为在大尺寸下，微调与否区别并不大。

##Mac OS X

![Font rendering in Mac OS X](http://farm4.staticflickr.com/3665/10605691064_381040aea5_o.jpg)<!--21-->  
![Font rendering in Mac OS X-zoom](http://farm8.staticflickr.com/7460/10605692204_b598f94bbc_o.jpg)<!--22-->  
*Mac OS X下的字体渲染*  

在`Mac OS`中，所有的浏览器都使用`Quartz`渲染引擎。`TrueType`和`PostScript`字体采用完全一样的渲染方式，所以字体微调可以完全无视了卧槽，这正是两种字体的核心区别啊！所以`Mac OS`的亚像素渲染简直是屌爆了，我们可以放一百万个心。栅格器不会试图解读构成字体的笔画和特征，因为所有东西都可以通过暗像素来呈现。字体形状不会被解读，因此也就不会被曲解。`Quartz`渲染引擎十分可靠，因为它不会自作聪明瞎搞瞎弄。另外，Apple似乎也会采用一些很美妙的智能方案去增强渲染效果，但是这种技术没有说明文档，也完全超出我们的控制范围。

不过在某些情况下，这种技术也会导致一些不理想的效果。比如在上图所示的例子中，由于大「T」的高度不是全像素值，而`Mac OS`不会强制字母对齐，因此在字母的顶端会有一条灰线。可惜这个蛋疼的情况不是设计者所能改变的。不过，这种模糊的现象只有在特定的字号下才会出现，因此一般只需要改一改字号就可以解决这一问题。体会一下修改字号带来的阵痛，我们就可以获得一个非常棒的渲染效果啦。

在`Mac`上另一个比较蛋疼的是，字体会渲染得更重一些。在文本字体的大小下会更明显，同样地字体在`Mac OS`下会「黏乎」一些，而在`Windows`下则比较清淡。

##iOS

![Font rendering in iOS](http://farm6.staticflickr.com/5540/10605681615_f21ae75117_o.jpg)<!--23-->  
![Font rendering in iOS-zoom](http://farm6.staticflickr.com/5518/10605706996_7837aa9047_o.jpg)<!--24-->  
*iOS上的字体渲染*  

`iOS`上的渲染遵循与`Mac OS`一样的原理，两者主要的区别就是`iOS`不采用亚像素渲染。主要的原因就是当设备旋转之后，系统需要重新计算并更新渲染，因为亚像素的排列方向发生了变化。Apple竭尽全力想要减少CPU的使用。

#结论

网站访客所使用的浏览器和操作系统差异很大，有些是没有及时更新，有些是公司的政策所规定，不是用户的错。我个人的建议是尽可能的为用户提供最佳的渲染效果，而不是指责操作系统厂商，或者要求用户更换更好的操作系统（[@Ryekee](http://ryekee.com)：比如Mac OS？:-P）。

在`Mac OS`和`iOS`上，我们对渲染没有控制权，但这完全可以接受，因为渲染引擎简直太棒了。除了字体渲染得太过黏乎之外。或许有一天，Web字体服务可以根据不同的平台提供稍浓或稍淡的字体来改善字体的一致性。

在`Windows`上，字体微调极为重要，尤其是对`TrueType`类字体而言（这是万恶的IE6到IE8唯一接受的Web字体格式）。除此之外，选择`TrueType`还是`PostScript`字体格式也会对渲染的结果造成重大的影响。除了小号字体的微调外，`PostScript`的渲染效果完全不逊色于`TrueType`。尽管	`DirectWrite`为`Windows`提供了令人身心愉快的渲染效果，但是良好的字体微调依旧很重要。

#实际应用：改善屏显字体的渲染效果

一些Web字体的提供商，比如Typekit和Just Another Foundry，已经开始提供`PostScript`类字体了。

![JAF Domus Titling Web rendered with GDI ClearType](http://farm4.staticflickr.com/3724/10605708266_7b660499bc_o.jpg)<!--25-->   
![JAF Domus Titling Web rendered with DirectWrite](http://farm6.staticflickr.com/5518/10605685505_ea9cf1755b_o.jpg)<!--26-->  
![JAF Domus Titling Web rendered with Windows grayscale](http://farm4.staticflickr.com/3665/10605939913_4db51114e8_o.jpg)<!--27-->  
![JAF Domus Titling Web rendered in Mac OS X](http://farm3.staticflickr.com/2830/10605688375_9605a7257b_o.jpg)<!--28-->  
*JAF Domus Titling字体在不同的环境下的渲染效果*  

在IE6到IE8中，`GDI ClearType`渲染效果的锯齿无法避免，但在其他环境下都可以得到平滑的渲染效果。这就意味着我们还是需要使用带有微调的`TrueType`字体，因为操蛋的IE6 - 8还是有着巨大的市场份额。

![Bello by Underware on Typekit](http://farm3.staticflickr.com/2869/10605689535_f79c4e1b56_o.jpg)<!--29-->    
*Typekit上的Underware设计室设计的Bello字体就是PostScript格式的Web字体（右侧），它比左边的TrueType字体轮廓要更顺滑一些*

Typekit也开始采用混合策略，提供`PostScript`格式的屏显字体，为`Windows GDI`提供更平滑的渲染效果。但这需要为制定一些视觉效果的评判标准。

你们可能会问我，「你大爷的究竟要如何定义屏显字体（display font）啊？」  
事实上确实很难画一条清晰的线来定义屏显字体。有些字体供应商提供人工微调的`TrueType`字体，用作正文显示非常不错（可惜的是转换成`PostScript`格式可能会丢失微调信息）。一些文本字体在大尺寸的情况下表现也相当不俗，因此理想的情况是同一字体提供两套不同的格式。不过这会增加UI以及后端的复杂度，目前来看并不现实。

#未来发展

越来越多的字体设计师都开始注意到Web字体所带来的技术问题，尤其是`TrueType`字体的微调。随着Web字体产业的崛起，他们愿意付出精力为屏幕显示而优化字体。在不远的将来，我们将看到大量精心设计的字体问世（或者至少是对现有字体的更新）。

随着屏幕分辨率的增加（以及对栅格器的重大改进），我们慢慢地不再担心字体渲染的技术细节。采用`GDI`渲染模式的浏览器必将拖后腿，正因为此，未来数年内，我们都还无法放心的使用无微调的`TrueType`字体。只有当这一类浏览器用户比例降到足够低的程度的时候，`TrueType`字体微调（耗时又需要高超的技巧）才可以被扔到一边。尽管目前市面上几乎所有Web字体都是`TrueType`格式的，我仍希望字体行业能够大规模转向`PostScript`格式，因为这种字体能为设计师减少绝大部分的工作。

##相关资源

* [《Firefox6 中的 DirectWrite 字体渲染》](http://blog.mozilla.com/nattokirai/2011/08/11/directwrite-text-rendering-in-firefox-6/)，Mozilla官方博客
*  [《JAF Domus Titling 字体》](http://justanotherfoundry.com/domus-titling-web)，Just Another Foundry
*  [《Typekit 更新：为 Windows 改善字体渲染》](http://blog.typekit.com/2011/07/26/new-from-typekit-improved-font-rendering-on-windows/)，Typekit 官方博客
*  [《OpenType/CFF 相对于 TrueType 的优势》](http://blogs.adobe.com/typblography/2010/12/the-benefits-of-opentypecff-over-truetype.html)，Typblography