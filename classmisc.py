#!/usr/bin/env python

class Activity(object):
    Active=True
    ActivityName=""
    EnableActionsVariablesDependenciesControl=False
    TargetApplication=""
    def __init__(self,Active,ActivityName):
        self.Active=Active
        self.ActivityName=ActivityName        
    def convertToRobotCode(self):
        return "| " + self.ActivityName+"\n"

class FlowControl(object):
    Active=True
    Condition=""
    FlowControlAction=""
    Value=""
    def __init__(self,Condition,FlowControlAction,Value):
#       self.Active=Active
        self.Condition=Condition
        self.FlowControlAction=FlowControlAction
        self.Value=Value
    def convertToRobotCode(self):
        return

class VariableString(object):
    Name=""
    ParentType=""
    InitialStringValue=""
    ParentType=""
    Value=""
    def __init__(self,Name,ParentType,InitialStringValue,Value):
        self.Name=Name
        self.ParentType=ParentType
        self.InitialStringValue=InitialStringValue
        self.Value=Value
    def convertToRobotCode(self):
        return self.Name + "=" +self.InitialStringValue
    
