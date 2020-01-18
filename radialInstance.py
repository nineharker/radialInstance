# -*- coding: utf-8 -*-
from maya import cmds

#円柱のようなモデルを作るとき一つの面だけ作ってインスタンスコピーしながら回転する
def radialInstance(*args):
    nodes = cmds.ls(sl=True)
    cmds.FreezeTransformations()
    number = cmds.textField( "number", q=True, tx=True )
    number = int(number)
    angle = 360.0/number
    angleRotate = 360.0/number
    radioSelect = cmds.radioCollection('rcName',q=True,select=True)
    for i in range(number-1):
        ins = cmds.instance(nodes)
        cmds.setAttr(ins[0]+".rotate"+radioSelect,angle)
        angle += angleRotate  


def createWindow():
    if cmds.window('radialmenu', exists=True):
        cmds.deleteUI('radialmenu')

    window = cmds.window('radialmenu', title='Radial Instance')
    cmds.columnLayout()
    cmds.text(label = u'中心軸')
    cmds.radioCollection('rcName')
    cmds.radioButton('X',l='X')
    cmds.radioButton('Y',l='Y',select = True)
    cmds.radioButton('Z',l='Z')
    cmds.text(label = u'複製する回数を入力')
    cmds.textField( "number" )
    cmds.button(label='Instance', command=radialInstance) 
    cmds.showWindow(window)


def main():
    createWindow()



