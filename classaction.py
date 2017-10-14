#!/usr/bin/env python
"""
    Action classes to mimic every each of Ginger action after extraction info from the BF,
    Later, will use it to convert them to Robotframework key words
"""
class Action(object):
    Active=True
    Description=""
    EnableRetryMechanism=False
    MaxNumberOfRetries=0
    RetryMechanismInterval=""
    Wait=0
    key=""
    aid=""
    robotparam=""
    LocateBy=""
    LocateValue=""
    StatusConverter=""
    InputValues=[]
    ReturnValues=[]
    FlowControls=[]
    def __init__(self, Active, Description, EnableRetryMechanism, MaxNumberOfRetries, RetryMechanismInterval, Wait,key,aid,robotparam):
       
        self.Active = Active
        self.Description = Description
        self.EnableRetryMechanism = EnableRetryMechanism
        self.MaxNumberOfRetries = MaxNumberOfRetries
        self.RetryMechanismInterval = RetryMechanismInterval
        self.Wait = Wait
        self.key=key
        self.aid=aid
        self.robotparam=robotparam
    def convertToRobotCode(self):
        return "rawaction"
        
class ActSetVariableValueOption(Action):
    VariableName=""
    InputValues=""
    def __init__(self, VariableName,InputValues):                   
        self.VariableName = VariableName
        self.InputValues = InputValues
               
    def convertToRobotCode(self):
        return
    
class ActBrowserElement(Action):
    ControlAction=""
    def __init__(self,ControlAction,LocateBy,LocateValue,StatusConverter):
        self.ControlAction=ControlAction
        self.LocateBy=LocateBy
        self.LocateValue=LocateValue
        self.StatusConverter=StatusConverter
    def convertToRobotCode(self):
        return
    
class ActButton(Action):
    ButtonAction=""
    def __init__(self,ButtonAction,LocateBy,LocateValue,StatusConverter):
        self.ButtonAction=ButtonAction
        self.LocateBy=LocateBy
        self.LocateValue=LocateValue
        self.StatusConverter=StatusConverter
    def convertToRobotCode(self):
        return "| | Click Button | "+self.LocateValue
    
class ActConsoleCommand(Action):
    ConsoleCommand=""
    def __init__(self,ConsoleCommand,InputValues):
        self.ConsoleCommand=ConsoleCommand
        self.InputValues=InputValues
    def convertToRobotCode(self):
        return

class ActDBValidation(Action):
    AppName=""
    SQL=""
    def __init__(self,AppName,SQL,StatusConverter):
        self.AppName=AppName
        self.SQL=SQL
        self.StatusConverter=StatusConverter
    def convertToRobotCode(self):
        return
    
class ActDropDownList(Action):    
    def __init__(self,InputValues,LocateBy,LocateValue,ActDropDownListAction,StatusConverter):
        self.InputValues=InputValues
        self.LocateBy=LocateBy
        self.LocateValue=LocateValue
        self.ActDropDownListAction=ActDropDownListAction
        self.StatusConverter=StatusConverter
    def convertToRobotCode(self):
        if self.ActDropDownListAction=='SetSelectedValueByText' or self.ActDropDownListAction=='SetSelectedValueByItem':
            return "| | Select From List | "+self.LocateValue + " | "+self.InputValues[0].convertToRobotCode()
        elif self.ActDropDownListAction=='SetSelectedValueByIndex':
            return "| | Select From List By Index | "+self.LocateValue + " | "+self.InputValues[0].convertToRobotCode()

class ActDummy(Action):
    def __init__(self,StatusConverter):        
        self.StatusConverter=StatusConverter
    def convertToRobotCode(self):
        return

class ActExcel(Action):
    ExcelActionType=""
    ExcelFileName=""
    PrimaryKeyColumn=""
    SelectRowsWhere=""
    SetDataUsed=""
    SheetName=""
    def __init__(self,ExcelActionType,ExcelFileName,PrimaryKeyColumn,SelectRowsWhere,SetDataUsed,SheetName,StatusConverter):
        self.ExcelActionType=ExcelActionType
        self.ExcelFileName=ExcelFileName
        self.PrimaryKeyColumn=PrimaryKeyColumn
        self.SelectRowsWhere=SelectRowsWhere
        self.SetDataUsed=SetDataUsed
        self.SheetName=SheetName
        self.StatusConverter=StatusConverter
    def convertToRobotCode(self):
        return

class ActFileTransfer(Action):
    PCPath=""
    UnixPath=""
    UserName=""
    Password=""
    PrivateKey=""
    PrivateKeyPassPhrase=""
    Port=""
    Host=""
    def __init__(self,PCPath,UnixPath,UserName,Password,PrivateKey,PrivateKeyPassPhrase,Port,Host,StatusConverter):
        self.PCPath=PCPath
        self.UnixPath=UnixPath
        self.UserName=UserName
        self.Password=Password
        self.UnixPath=UnixPath
        self.PrivateKey=PrivateKey
        self.PrivateKeyPassPhrase=PrivateKeyPassPhrase
        self.Port=Port
        self.Host=Host
        self.StatusConverter=StatusConverter
    def convertToRobotCode(self):
        return
    
class ActGenElement(Action):
    GenElementAction=""
    Xoffset=""
    Yoffset=""
    def __init__(self,GenElementAction,LocateBy,LocateValue,InputValues,Xoffset,Yoffset,StatusConverter):
        self.GenElementAction=GenElementAction
        self.LocateBy=LocateBy
        self.LocateValue=LocateValue
        self.Xoffset=Xoffset
        self.Yoffset=Yoffset
        self.StatusConverter=StatusConverter
        self.InputValues=InputValues
    def convertToRobotCode(self):
        if self.GenElementAction=='Click' or self.GenElementAction=='ClickAt' or self.GenElementAction=='AsyncClick':
            return "| | Click Element | "+self.LocateValue
        elif self.GenElementAction=='GotoURL':
            return "| | Go TO | "+self.InputValues[0].convertToRobotCode()                   
        elif self.GenElementAction=='SetValue':
            return "| | Input Text | "+self.LocateValue+" | "+self.InputValues[0].convertToRobotCode()
        elif self.GenElementAction=='GetValue':
            return "| | Get Value | "+self.LocateValue
        elif self.GenElementAction=='GetWindowTitle':
            return "| | Get Title | "+self.LocateValue
        elif self.GenElementAction=='SelectFromDropDown':
            return "| | Select From List | "+self.LocateValue + " | "+self.InputValues[0].convertToRobotCode()
        elif self.GenElementAction=='CloseBrowser':
            return "| | Close Browser"
#        elif self.GenElementAction=='Visible':
#            return "| | Element Should Be Visible | "+self.LocateValue

class ActGotoURL(Action):   
    def __init__(self,InputValues,StatusConverter):
        self.InputValues=InputValues
        self.StatusConverter=StatusConverter
    def convertToRobotCode(self):
        return "| | Go TO | "+self.InputValues[0].convertToRobotCode()
        return
    
class ActLink(Action):
    LinkAction=""
    def __init__(self,LinkAction,LocateBy,LocateValue,StatusConverter):
        self.LinkAction=LinkAction
        self.LocateBy=LocateBy
        self.LocateValue=LocateValue
        self.StatusConverter=StatusConverter
    def convertToRobotCode(self):
        return
    
class ActScript(Action):
    ScriptInterpreterType=""
    ScriptName=""
    ScriptPath=""
    def __init__(self,ScriptInterpreterType,ScriptName,ScriptPath,InputValues,StatusConverter):
        self.ScriptInterpreterType=ScriptInterpreterType
        self.ScriptName=ScriptName
        self.ScriptPath=ScriptPath
        self.InputValues=InputValues
    def convertToRobotCode(self):
        return
    
class ActSmartSync(Action):
    SmartSyncAction=""
    def __init__(self,SmartSyncAction,LocateBy,LocateValue,StatusConverter):
        self.SmartSyncAction=SmartSyncAction
        self.LocateBy=LocateBy
        self.LocateValue=LocateValue
        self.StatusConverter=StatusConverter
    def convertToRobotCode(self):
        return
    
class ActTextBox(Action):
    TextBoxAction=""
    def __init__(self,TextBoxAction,LocateBy,LocateValue,InputValues,StatusConverter):
        self.TextBoxAction=TextBoxAction
        self.LocateBy=LocateBy
        self.LocateValue=LocateValue
        self.InputValues=InputValues
        self.StatusConverter=StatusConverter
    def convertToRobotCode(self):
        if self.TextBoxAction=='SetValue':
            return "| | Input Text | "+self.LocateValue+" | "+self.InputValues[0].convertToRobotCode()
    
class ActValidation(Action):
    Condition=""
    def __init__(self,Condition,FlowControl,StatusConverter):
        self.Condition=Condition
        self.FlowControl=FlowControl   
        self.StatusConverter=StatusConverter
    def convertToRobotCode(self):
        return

class ActInputValue(Action):
    Param=""
    StoreToVariable=""
    Value=""
    Active=True
    Description=""
    EnableRetryMechanism=False
    MaxNumberOfRetries=0
    RetryMechanismInterval=""
    Wait=0
    key=""
    id=""
    robotparam=""
    def __init__(self, Param,Value):
        self.Param=Param
        self.Value=Value
    def convertToRobotCode(self):
        return self.Value