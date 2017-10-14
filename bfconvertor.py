from __future__ import print_function
#!/usr/bin/env python
execfile("classaction.py")
execfile("classmisc.py")

import xml.etree.ElementTree as ET

cmds=[]
sBF="C:/SVN/GingerSolutions/Ginger-MetroPCS-OnlineKeying/BusinessFlows/OnlineKeying/testRobot.Ginger.BusinessFlow.xml"
sRobotFile="C:/mypy/RobotFrameworkConvertor/test1.robot"
#def getxmlname():
#    return sBF

tree = ET.parse(sBF)


def writeToRobotScript(cds,sFile):
    f = open(sFile, 'w+')
    f.write("*** Variables ***\n")
    f.write("| ${BROWSER} | ff\n")
    f.write("\n")
    f.write("*** Settings ***\n")
    f.write("| Library | Selenium2Library | 30\n")
    f.write("\n")
    f.write("*** Test Cases ***\n")
    f.write("| Open Browser\n")
    f.write("| | Open Browser | about:blank | ${BROWSER}\n")
    for str in cds:
        #print(repr(str),file=f)
        if str != None:
            f.write(str+"\n")
   # f.writelines(repr(cds))
    f.close


bf=tree.getroot()


def getInputValNFlowCtrl(childnode):
    inputVa=""
    FlowCtrl=""
    for grandchild in childnode:
        if grandchild.tag =='InputValues':
            for ggrandchild in grandchild:
                #print ggrandchild.tag, ggrandchild.attrib
                inputVa=ActInputValue(ggrandchild.get('Param'),ggrandchild.get('Value'))
        elif grandchild.tag =='FlowControls':
            for ggrandchild in grandchild:
                #print ggrandchild.tag, ggrandchild.attrib
                FlowCtrl=FlowControl(ggrandchild.get('Condition'),ggrandchild.get('FlowControlAction'),ggrandchild.get('Value'))
    return [inputVa,FlowCtrl]

for node in bf:
    for activity in node:
        if(activity.get('Active')=='True'):
            acty=Activity(True,activity.get('ActivityName'))            
            cmds.append(acty.convertToRobotCode())
            cmds.append("| | Sleep | 6")
           # print acty.ActivityName
        for child in activity:
            for childnode in child:
                if childnode.tag=='GingerCore.Actions.ActGotoURL':                                       
                    Reslt=getInputValNFlowCtrl(childnode)
                    act=ActGotoURL([Reslt[0]],childnode.get('StatusConverter'))
                elif childnode.tag=='GingerCore.Actions.ActBrowserElement':                    
                    Reslt=getInputValNFlowCtrl(childnode)
                    act=ActBrowserElement(childnode.get('ControlAction'),childnode.get('LocateBy'),childnode.get('LocateValue'),childnode.get('StatusConverter'))
                elif childnode.tag=='GingerCore.Actions.ActButton':                    
                    Reslt=getInputValNFlowCtrl(childnode)
                    act=ActButton(childnode.get('ButtonAction'),childnode.get('LocateBy'),childnode.get('LocateValue'),childnode.get('StatusConverter'))
                elif childnode.tag=='GingerCore.Actions.ActConsoleCommand':                    
                    Reslt=getInputValNFlowCtrl(childnode)
                    act=ActConsoleCommand(childnode.get('ConsoleCommand'),[Reslt[0]])
                elif childnode.tag=='GingerCore.Actions.ActDBValidation':                    
                    Reslt=getInputValNFlowCtrl(childnode)
                    act=ActDBValidation(childnode.get('AppName'),childnode.get('SQL'),childnode.get('StatusConverter'))
                elif childnode.tag=='GingerCore.Actions.ActDropDownList':                    
                    Reslt=getInputValNFlowCtrl(childnode)
                    act=ActDropDownList([Reslt[0]],childnode.get('LocateBy'),childnode.get('LocateValue'),childnode.get('ActDropDownListAction'),childnode.get('StatusConverter'))
                elif childnode.tag=='GingerCore.Actions.ActDummy':                    
                    Reslt=getInputValNFlowCtrl(childnode)
                    act=ActDummy(childnode.get('StatusConverter'))
                elif childnode.tag=='GingerCore.Actions.ActExcel':                    
                    Reslt=getInputValNFlowCtrl(childnode)
                    act=ActExcel(childnode.get('ExcelActionType'),childnode.get('ExcelFileName'),childnode.get('PrimaryKeyColumn'),childnode.get('SelectRowsWhere'),childnode.get('SetDataUsed'),childnode.get('SheetName'),childnode.get('StatusConverter'))
                elif childnode.tag=='GingerCore.Actions.ActFileTransfer':                    
                    Reslt=getInputValNFlowCtrl(childnode)
                    act=ActFileTransfer(childnode.get('PCPath'),childnode.get('UnixPath'),childnode.get('UserName'),childnode.get('Password'),childnode.get('PrivateKey'),childnode.get('PrivateKeyPassPhrase'),childnode.get('Port'),childnode.get('Host'),childnode.get('StatusConverter'))
                elif childnode.tag=='GingerCore.Actions.ActGenElement':                    
                    Reslt=getInputValNFlowCtrl(childnode)
                    act=ActGenElement(childnode.get('GenElementAction'),childnode.get('LocateBy'),childnode.get('LocateValue'),childnode.get('Xoffset'),childnode.get('Yoffset'),[Reslt[0]],childnode.get('StatusConverter'))
                elif childnode.tag=='GingerCore.Actions.ActGotoURL':                    
                    Reslt=getInputValNFlowCtrl(childnode)
                    act=ActGotoURL([Reslt[0]],childnode.get('StatusConverter'))
                elif childnode.tag=='GingerCore.Actions.ActLink':                    
                    Reslt=getInputValNFlowCtrl(childnode)
                    act=ActLink(childnode.get('LinkAction'),childnode.get('LocateBy'),childnode.get('LocateValue'),childnode.get('StatusConverter'))
                elif childnode.tag=='GingerCore.Actions.ActScript':                    
                    Reslt=getInputValNFlowCtrl(childnode)
                    act=ActScript(childnode.get('ScriptInterpreterType'),childnode.get('ScriptName'),childnode.get('ScriptPath'),[Reslt[0]],childnode.get('StatusConverter'))
                elif childnode.tag=='GingerCore.Actions.ActSetVariableValue':                    
                    Reslt=getInputValNFlowCtrl(childnode)
                    act=ActSetVariableValue(childnode.get('VariableName'),[Reslt[0]])
                elif childnode.tag=='GingerCore.Actions.ActSmartSync':                    
                    Reslt=getInputValNFlowCtrl(childnode)
                    act=ActSmartSync(childnode.get('SmartSyncAction'),childnode.get('LocateBy'),childnode.get('LocateValue'),childnode.get('StatusConverter'))
                elif childnode.tag=='GingerCore.Actions.ActTextBox':                    
                    Reslt=getInputValNFlowCtrl(childnode)
                    act=ActTextBox(childnode.get('TextBoxAction'),childnode.get('LocateBy'),childnode.get('LocateValue'),[Reslt[0]],childnode.get('StatusConverter'))
                elif childnode.tag=='GingerCore.Actions.ActValidation':                    
                    Reslt=getInputValNFlowCtrl(childnode)
                    act=ActValidation(childnode.get('Condition'),FlowControl,childnode.get('StatusConverter'))
                
                if act.__class__.__name__ in ['ActTextBox','ActLink','ActGotoURL','ActGenElement'] and act.convertToRobotCode()!=None and getattr(act, 'LocateValue')!="":
                    cmds.append("| | Wait Until Element Is Visible | "+getattr(act, 'LocateValue'))
                    
                cmds.append(act.convertToRobotCode())
writeToRobotScript(cmds,sRobotFile)                