from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QWidget, QStackedWidget
from Ui_tipesFrom import Ui_tipesFrom
from Ui_guideFrom import Ui_guideFrom
from Ui_oneForm import Ui_oneForm
from Ui_twoForm import Ui_twoForm

class tipesWindows(QWidget, Ui_tipesFrom):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.guidesWindows = guidesWindows()
        self.starbtn.clicked.connect(lambda : self.clickGobtn())

    def clickGobtn(self):
        self.guidesWindows.show()
        self.close()

class guidesWindows(QWidget, Ui_guideFrom):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.starOneWindows()
        self.starTwoWindows()
        self.starFourWindows()
        self.starFiveWindows()
        self.starSixWindows()

    def starOneWindows(self):
        self.oneWindows = oneWindows()
        self.onebtn.clicked.connect(lambda : self.oneWindows.show())
        self.onebtn.clicked.connect(lambda : self.close())

    def starTwoWindows(self):
        self.twoWindows = twoWindows()
        self.twobtn.clicked.connect(lambda : self.twoWindows.show())
        self.twobtn.clicked.connect(lambda : self.close())

    def starFourWindows(self):
        self.fourWindows = fourWindows()
        self.fourbtn.clicked.connect(lambda : self.fourWindows.show())
        self.fourbtn.clicked.connect(lambda : self.close())

    def starFiveWindows(self):
        self.fiveWindows = fiveWindows()
        self.fivebtn.clicked.connect(lambda : self.fiveWindows.show())
        self.fivebtn.clicked.connect(lambda : self.close())

    def starSixWindows(self):
        self.sixWindows = sixWindows()
        self.sixbtn.clicked.connect(lambda : self.sixWindows.show())
        self.sixbtn.clicked.connect(lambda : self.close())

class oneWindows(QWidget, Ui_oneForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.one()


    def one(self):
        self.pix = QtGui.QPixmap('pic/1.png')
        self.piclab.setScaledContents(True)
        self.piclab.setPixmap(self.pix)

        self.lab.setText('看呀，这有一个连接孔，让我们用螺栓连接它')

        self.btn.clicked.connect(lambda : self.two())

    def two(self):
        self.pix = QtGui.QPixmap('pic/2.png')
        self.piclab.setScaledContents(True)
        self.piclab.setPixmap(self.pix)

        self.lab.setText('很好已经连接完成了过几年我们再来看看吧')

        self.btn.setText('等待几年')

        self.btn.clicked.connect(lambda : self.three())

    def three(self):
        self.pix = QtGui.QPixmap('pic/3.png')
        self.piclab.setScaledContents(True)
        self.piclab.setPixmap(self.pix)

        self.lab.setText('哎呀连接孔已经被破坏了')

        self.btn.setText('有什么办法能强化连接孔呢？')

        self.btn.clicked.connect(lambda : self.four())

    def four(self):
        self.piclab.clear()
        self.lab.setText('想要强化连接孔就要先明白连接孔为什么被破坏')
        self.btn.setText('为什么呢？')

        self.btn.clicked.connect(lambda : self.five())


    def five(self):
        self.pix = QtGui.QPixmap('pic/4.png')
        self.piclab.setScaledContents(True)
        self.piclab.setPixmap(self.pix)

        self.lab.setText('这是连接孔的应力分布图，可以看到连接孔受到很大的应力')

        self.btn.setText('使用冷挤压强化技术')

        self.btn.clicked.connect(lambda : self.six())

    def six(self):
        self.pix = QtGui.QPixmap('pic/5.png')
        self.piclab.setScaledContents(True)
        self.piclab.setPixmap(self.pix)

        self.lab.setText('对于连接孔的冷挤压强化技术使用芯棒挤压连接孔')

        self.btn.setText('分析')
        self.btn.clicked.connect(lambda : self.seven())

    def seven(self):
        self.pix = QtGui.QPixmap('pic/6.png')
        self.piclab.setScaledContents(True)
        self.piclab.setPixmap(self.pix)

        self.lab.setText('强化机理如图，从宏观角度来讲挤压使孔壁表层金属发生塑性变形距孔壁较远的深层金属发生弹性变形')

        self.btn.clicked.connect(lambda : self.eight())

    def eight(self):
        self.lab.setText('挤压使孔壁表层金属发生塑性变形距孔壁较远的深层金属发生弹性变形')
        self.btn.clicked.connect(lambda: self.nine())

    def nine(self):
        self.lab.setText('深层金属层由于弹性变形的作用会有恢复原样的趋势会对表层已发生塑性变形的金属层进行反向加载从而在孔壁一定范围内形成残余压应力层')
        self.btn.clicked.connect(lambda : self.ten())

    def ten(self):
        self.pix = QtGui.QPixmap('pic/7.png')
        self.piclab.setScaledContents(True)
        self.piclab.setPixmap(self.pix)

        self.lab.setText('可以看到，连接孔所受的最大应力大大减小')

        self.btn.setText('了解了')

        self.btn.clicked.connect(lambda : self.close())
        self.btn.clicked.connect(lambda : self.one())
        self.guidesWindows = guidesWindows()
        self.btn.clicked.connect(lambda : self.guidesWindows.show())

class twoWindows(QWidget, Ui_twoForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.one()


    def one(self):
        self.btn.setText('了解开封衬套')

        self.pix = QtGui.QPixmap('pic/8.png')
        self.piclab.setScaledContents(True)
        self.piclab.setPixmap(self.pix)

        self.lab.setText('      带开缝衬套的孔冷挤压强化阻止孔周围细小裂纹扩展；无需增加重量或改变刚体的结构；可以单侧操作，用于铝合金、钛合金和高强度钢的航空金属的强化；经济效益好，强化时间短等')

        self.btn.clicked.connect(lambda : self.two())

    def two(self):
        self.pix = QtGui.QPixmap('pic/9.png')
        self.piclab.setScaledContents(True)
        self.piclab.setPixmap(self.pix)

        self.lab.setText('      这是开缝衬套，开缝衬套仅作为一次性工艺件，挤压完成后失去作用，具有很好的回弹效果，方便取下')

        self.btn.setText('查看结构图')

        self.btn.clicked.connect(lambda : self.three())

    def three(self):
        self.pix = QtGui.QPixmap('pic/10.png')
        self.piclab.setScaledContents(True)
        self.piclab.setPixmap(self.pix)

        self.lab.setText('      这是开缝衬套的结构图，衬套的翻边处理不容小觑，它可以在冷挤压过程中，对衬套有一个约束作用，使衬套在芯棒的轴向运动下能和孔内壁保持静止，并让孔壁充分得到挤压。为了能使芯棒平稳均匀的通过开缝衬套，要对衬套内表面喷涂润滑剂，这种润滑剂应该满足能够一次性为芯棒顺利通过开缝衬套提供润滑作用')

        self.btn.setText('了解芯棒')

        self.btn.clicked.connect(lambda : self.four())

    def four(self):
        self.pix = QtGui.QPixmap('pic/11.png')
        self.piclab.setScaledContents(True)
        self.piclab.setPixmap(self.pix)

        self.lab.setText('      这是安装开缝衬套所用的芯棒，它的大小直接影响了对初孔的挤压量，连接段的作用是实现和拉枪相连，为芯棒提供拉力。前锥段的角度是保证整个冷挤压过程能够挤压顺利且不发生紧楔的重要条件，后锥段的角度可以对挤压部位的回弹起稳定缓冲作用。')

        self.btn.setText('了解冷挤压拉枪及动力台')

        self.btn.clicked.connect(lambda : self.five())

    def five(self):
        self.pix = QtGui.QPixmap('pic/12.png')
        self.piclab.setScaledContents(True)
        self.piclab.setPixmap(self.pix)

        self.lab.setText('      拉枪及动力台式为整个挤压过程提供动力的装置，两者的平稳运行是完成挤压过程的保障。利用动力台为拉枪输油，对活塞施加压强带动活塞杆运动，实现芯棒的轴向运动。挤压完成后油缸卸油压，气缸充气压使活塞恢复到原位，完成卸压过程。挤压过程中，动力台仪表盘会输出油压的压强值，通过记录的最大峰值，结合油液与活塞杆的作用面积可以估算出芯棒在挤压过程中所需要的轴向拉力值。')

        self.btn.setText('了解试验板')

        self.btn.clicked.connect(lambda : self.six())

    def six(self):
        self.pix = QtGui.QPixmap('pic/13.png')
        self.piclab.setScaledContents(True)
        self.piclab.setPixmap(self.pix)

        self.lab.setText('      试验板进行挤压工艺试验及疲劳试验在制备，过程中要保证孔壁表面的粗糙度及精度，以防在挤压强化时就萌生裂纹影响效果，同时制造完成后进行去应力退火，用以提高试验的精度。')

        self.btn.setText('了解了')

        self.guidesWindows = guidesWindows()
        self.btn.clicked.connect(lambda : self.close())
        self.btn.clicked.connect(lambda : self.guidesWindows.show())

class fourWindows(QWidget, Ui_twoForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('开缝衬套的制备技术')
        self.one()
    def one(self):
        self.piclab.hide()
        self.lab.setText('      开缝衬套的制备技术在一定程度上也影响着强化效果，有一些开缝衬套的制备方法在开缝衬套制备之初就产生了一定的应力，降低了开缝衬套的强度。目前可实现的成型工艺主要有冲压，滚弯，自由卷曲等，本节对比了这几种制备方法的优劣。')

        self.btn.setText('了解冲压成形工艺')
        self.btn.clicked.connect(lambda : self.two())

    def two(self):
        self.piclab.show()
        self.piclab.setText('画个图')

        self.lab.setText('      冲压连续折弯成形采用冲压模具对样件连续折弯，虽具有成本低等优势。但多次对带材的连续折弯，虽成形后内眼不能看出有任何质量缺陷，但通过显微镜观察衬套外表面会形成明显的竖状条纹，这些条纹是加工过程中由于发生冷作硬化而产生的，这使材料弹性大大下降，挤压完成后开缝衬套回弹效果不佳，可能会出现衬套卡在孔壁内，多次折弯也会降低开缝衬套的整体强度。')

        self.btn.setText('了解上下合模式一次成形原理')
        self.btn.clicked.connect(lambda : self.three())

    def three(self):
        self.pix = QtGui.QPixmap('pic/14.png')
        self.piclab.setScaledContents(True)
        self.piclab.setPixmap(self.pix)

        self.lab.setText('      上下合模式成形原理主要组成为上、下半模、支撑轴，通过将切好的块状带材放入模具内，经过一次性模具压制而成。该成型技术采用圆柱面模具和芯轴包裹带材完成一次成形技术。')

        self.btn.setText('了解滚弯成形工艺')
        self.btn.clicked.connect(lambda : self.four())

    def four(self):
        self.pix = QtGui.QPixmap('pic/15.png')
        self.piclab.setScaledContents(True)
        self.piclab.setPixmap(self.pix)

        self.lab.setText('      双轴柔性滚弯成形技术是国内研究最为深入且实现了大规格开缝衬套生产。它基于车床和钢性轴支撑滚弯成形原理，但是受钢性轴限制，只能成形直径20mm以上衬套且不易于实现大批量自动化生产，其制备工具也容易受到磨损。')

        self.btn.setText('了解三轴滚弯成形技术')
        self.btn.clicked.connect(lambda : self.five())

    def five(self):
        self.pix = QtGui.QPixmap('pic/16.png')
        self.piclab.setScaledContents(True)
        self.piclab.setPixmap(self.pix)

        self.lab.setText('      为解决双轴滚弯刚性轴的刚度问题，研制了三轴手动卷制原理机，对小规格开缝衬套进行了试制。试制结果表明对刚性轴的变形和断裂得不到有效的改善，且制造效率低，也会发生橡胶辊磨损情况。')

        self.btn.setText('了解了')
        self.btn.clicked.connect(lambda : self.close())
        self.guidesWindows = guidesWindows()
        self.btn.clicked.connect(lambda : self.guidesWindows.show())

class fiveWindows(QWidget, Ui_twoForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('开缝衬套的制备技术')
        self.one()

    def one(self):
        self.piclab.hide()
        self.lab.setText('      挤压量是影响冷挤压强化效果最直接的因素之一。挤压量大小的选取是影响整个冷挤压强化效果的关键因素，过大的挤压量会导致孔周微观金属粒子发生剪切滑移从而产生裂纹，成为发生疲劳断裂的疲劳源，也会使孔壁轴向金属流动增大，挤出面孔端金属堆积对结构造成损伤，过大的芯棒拉力同样会给挤压过程带来安全隐患。\n采用下面公式进行设计挤压量的计算：')
        self.setWindowTitle('开缝衬套冷挤压强化工艺参数')
        self.btn.setText('继续了解挤压量')
        self.btn.clicked.connect(lambda : self.two())

    def two(self):
        self.piclab.show()
        self.pix = QtGui.QPixmap('pic/17.png')
        self.piclab.setScaledContents(True)
        self.piclab.setPixmap(self.pix)

        self.lab.hide()
        self.btn.clicked.connect(lambda : self.three())

    def three(self):
        self.piclab.hide()
        self.lab.show()
        self.lab.setText('      与设计挤压量相对的是工程挤压量，同设计挤压量一样分为工程绝对挤压量和工程相对挤压量，工程绝对挤压量就是挤压后的孔径与初孔直径的差，工程相对挤压量是在工程绝对挤压量的基础上除以初孔直径再乘百分函数。由于材料回弹等因素方面的影响，工程绝对挤压量往往要小于设计时的绝对挤压量，一般说的挤压量大小都是指设计挤压量。')

        self.btn.setText('了解孔距和孔边距')
        self.btn.clicked.connect(lambda : self.four())

    def four(self):
        self.piclab.show()
        self.pix = QtGui.QPixmap('pic/18.png')
        self.piclab.setScaledContents(True)
        self.piclab.setPixmap(self.pix)

        self.lab.setText('      孔距和孔边距也同样影响着冷挤压强化效果，孔距指两孔中心点距离，孔距较小挤压时，可能会有孔壁变形产生裂纹的现象，所以一般设置孔距值至少为三倍孔的直径。')

        self.btn.setText('了解铰削量')
        self.btn.clicked.connect(lambda : self.five())

    def five(self):
        self.piclab.hide()
        self.lab.setText('      在开缝衬套挤压后，会在孔壁产生一条沿孔轴向的凸脊，在凸脊的根部会因挤压而产生裂纹，若不进行处理很有可能成为疲劳裂纹萌生的位置，故需要在挤压之后进行一次铰削')

        self.btn.setText('了解了')
        self.btn.clicked.connect(lambda: self.close())
        self.guidesWindows = guidesWindows()
        self.btn.clicked.connect(lambda: self.guidesWindows.show())

class sixWindows(QWidget, Ui_twoForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('开缝衬套应力应变情况分析')
        self.one()

    def one(self):
        self.lab.hide()
        self.pix = QtGui.QPixmap('pic/20.png')
        self.piclab.setScaledContents(False)
        self.piclab.setPixmap(self.pix)

        self.btn.setText('查看应变分析')
        self.btn.clicked.connect(lambda : self.two())

    def two(self):
        self.lab.hide()
        self.pix = QtGui.QPixmap('pic/21.png')
        self.piclab.setScaledContents(False)
        self.piclab.setPixmap(self.pix)

        self.btn.setText('了解了')
        self.btn.clicked.connect(lambda: self.close())
        self.guidesWindows = guidesWindows()
        self.btn.clicked.connect(lambda: self.guidesWindows.show())



if __name__ =="__main__":
    app = QApplication([])
    window = tipesWindows()
    window.show()
    app.exec()
