"""
<plugin key="AHU" name="AHU32bit" author="plmicia" version="0.2">
    <params>
        <param field="Address" label="IP Address" width="250px" required="true" default="192.168.2.91"/>
        <param field="Port" label="Port" width="50px" required="true" default="23"/>
        <param field="Mode6" label="Debug" width="75px">
            <options>
                <option label="True" value="Debug"/>
                <option label="False" value="Normal"  default="true" />
            </options>
        </param>
    </params>
</plugin>
"""
import Domoticz

class BasePlugin:
    nextConnect = 3
    oustandingPings = 0

    AHU32bitConn = None

    def __init__(self):
        return

    def onStart(self):
        Domoticz.Debug("onStart called")

        if Parameters["Mode6"] == "Debug":
            Domoticz.Debugging(1)
        Domoticz.Log("AHU32bit Telnet plugin start")

        if 1 not in Devices:
            Domoticz.Device(Name="T_Supply", Unit=1, TypeName="Temperature", Used=1).Create()
        if 2 not in Devices:
            Domoticz.Device(Name="T_Return", Unit=2, TypeName="Temperature", Used=1).Create()
        if 3 not in Devices:
            Domoticz.Device(Name="T_Gas", Unit=3, TypeName="Temperature", Used=1).Create()  
        if 4 not in Devices:
            Domoticz.Device(Name="T_Liquid", Unit=4, TypeName="Temperature", Used=1).Create()
        if 5 not in Devices:
            Domoticz.Device(Name="T_Room", Unit=5, TypeName="Temperature", Used=1).Create()
        if 6 not in Devices:
            Domoticz.Device(Name="T_Set_Command", Unit=6, TypeName="Temperature", Used=1).Create()
        if 7 not in Devices:
            Domoticz.Device(Name="T_Out", Unit=7, TypeName="Temperature", Used=1).Create()
        if 8 not in Devices:
            Domoticz.Device(Name="T_Cond", Unit=8, TypeName="Temperature", Used=1).Create()
        if 9 not in Devices:
            Domoticz.Device(Name="T_Disch", Unit=9, TypeName="Temperature", Used=1).Create()  
        if 10 not in Devices:
            Domoticz.Device(Name="T_Module", Unit=10, TypeName="Temperature", Used=1).Create()
        Options = { "Custom" : "1;Hz"} 
        if 11 not in Devices:
            Domoticz.Device(Name="actual_freq", Unit=11, TypeName="Custom", Used=1).Create() 
        if 12 not in Devices:
            Domoticz.Device(Name="actual_dc_voltage", Unit=12, TypeName="Voltage", Used=1).Create()
        if 13 not in Devices:
            Domoticz.Device(Name="actual_current", Unit=13, TypeName="Current (Single)", Subtype=1, Used=1).Create()
        Options = { "Custom" : "1;x"} 
        if 14 not in Devices:
            Domoticz.Device(Name="on_off_counter", Unit=14, TypeName="Custom", Used=1,Options=Options).Create()
        Options = { "Custom" : "1;h"} 
        if 15 not in Devices:
            Domoticz.Device(Name="operation_time", Unit=15, TypeName="Custom", Used=1,Options=Options).Create()
        if 16 not in Devices:
            Domoticz.Device(Name="power_consumed", Unit=16, TypeName="Usage", Used=1).Create()
        if 17 not in Devices:
            Domoticz.Device(Name="power_produced", Unit=17, TypeName="Usage", Used=1).Create()
        Options = { "Custom" : "1;x"} 
        if 18 not in Devices:
            Domoticz.Device(Name="COP_P", Unit=18, TypeName="Custom", Used=1,Options=Options).Create()
        if 19 not in Devices:
            Domoticz.Device(Name="energy_consumed", Unit=19, Type=0x71, Used=1).Create()
        if 20 not in Devices:
            Domoticz.Device(Name="energy_produced", Unit=20, Type=0x71, Used=1).Create() 
        Options = { "Custom" : "1;x"} 
        if 21 not in Devices:
            Domoticz.Device(Name="COP_E", Unit=21, TypeName="Custom", Used=1,Options=Options).Create() 
        Options = { "Custom" : "1;l/min"}     
        if 22 not in Devices:
            Domoticz.Device(Name="actual_flow", Unit=22, TypeName="Custom", Used=1,Options=Options).Create() 
        Options = { "Custom" : "1;flag"} 
        if 23 not in Devices:
            Domoticz.Device(Name="under_defrost_flag", Unit=23, TypeName="Custom", Used=1,Options=Options).Create()  
        Options = { "Custom" : "1;x"} 
        if 24 not in Devices:
            Domoticz.Device(Name="defrost_counter", Unit=24, TypeName="Custom", Used=1,Options=Options).Create()
        Options = { "Custom" : "1;Step"} 
        if 25 not in Devices:
            Domoticz.Device(Name="actual_EEV", Unit=25, TypeName="Custom", Used=1,Options=Options).Create()
        Options = { "Custom" : "1;rpm"} 
        if 26 not in Devices:
            Domoticz.Device(Name="actual_ODU_fan", Unit=26, TypeName="Custom", Used=1,Options=Options).Create()
        Options = { "Custom" : "1;times"}     
        if 27 not in Devices:
            Domoticz.Device(Name="state_BYTE_1", Unit=27, TypeName="Custom", Used=1).Create()   
        Options = { "Custom" : "1;times"}     
        if 28 not in Devices:
            Domoticz.Device(Name="state_BYTE_2", Unit=28, TypeName="Custom", Used=1).Create()   
        Options = { "Custom" : "1;times"}     
        if 29 not in Devices:
            Domoticz.Device(Name="state_BYTE_3", Unit=29, TypeName="Custom", Used=1).Create() 
        Options = { "Custom" : "1;Hz"}  
        if 30 not in Devices:
            Domoticz.Device(Name="Compressor_command", Unit=30, TypeName="Custom", Used=1,Options=Options).Create()
        Options = { "Custom" : "1;flag"}            
        if 31 not in Devices:
            Domoticz.Device(Name="Compressor_in_operation_flag", Unit=31, TypeName="Custom", Used=1).Create()  
        Options = { "Custom" : "1; "}  
        if 32 not in Devices:
            Domoticz.Device(Name="power_state", Unit=32, TypeName="Custom", Used=1).Create()
        Options = { "Custom" : "1; "}            
        if 33 not in Devices:
            Domoticz.Device(Name="Contorl_Mode", Unit=33, TypeName="Custom", Used=1).Create()  
        Options = { "Custom" : "1; "}            
        if 34 not in Devices:
            Domoticz.Device(Name="BASE_input_BYTE", Unit=34, TypeName="Custom", Used=1).Create()  
        Options = { "Custom" : "1; "}            
        if 35 not in Devices:
            Domoticz.Device(Name="IDU_Tx_0x31[3]", Unit=35, TypeName="Custom", Used=1).Create() 
        Options = { "Custom" : "1; "}            
        if 36 not in Devices:
            Domoticz.Device(Name="BASE_state_BYTE", Unit=36, TypeName="Custom", Used=1).Create()   
        Options = { "Custom" : "1; "}            
        if 37 not in Devices:
            Domoticz.Device(Name="IDU_Tx_0x31[14]", Unit=37, TypeName="Custom", Used=1).Create() 
        Options = { "Custom" : "1;x"}            
        if 38 not in Devices:
            Domoticz.Device(Name="on_off_counter", Unit=38, TypeName="Custom", Used=1,Options=Options).Create() 
        Options = { "Custom" : "1;h"}            
        if 39 not in Devices:
            Domoticz.Device(Name="operation_time", Unit=39, TypeName="Custom", Used=1,Options=Options).Create() 
        Options = { "Custom" : "1; "} 
        if 40 not in Devices:
            Domoticz.Device(Name="Compressor_P_term", Unit=40, TypeName="Custom", Used=1,Options=Options).Create() 
        if 41 not in Devices:
            Domoticz.Device(Name="Compressor_sum_error", Unit=41, TypeName="Custom", Used=1,Options=Options).Create() 
        if 42 not in Devices:
            Domoticz.Device(Name="Compressor_I_term", Unit=42, TypeName="Custom", Used=1,Options=Options).Create() 
        if 43 not in Devices:
            Domoticz.Device(Name="Compressor_PID_out", Unit=43, TypeName="Custom", Used=1,Options=Options).Create() 
        if 44 not in Devices:
            Domoticz.Device(Name="def_Compressor_kp", Unit=44, TypeName="Custom", Used=1,Options=Options).Create() 
        if 45 not in Devices:
            Domoticz.Device(Name="def_Compressor_ki", Unit=45, TypeName="Custom", Used=1,Options=Options).Create() 
        if 46 not in Devices:
            Domoticz.Device(Name="Compressor_error", Unit=46, TypeName="Custom", Used=1,Options=Options).Create()     
        if 47 not in Devices:
            Domoticz.Device(Name="Power", Unit=47, TypeName="Switch", Image=1, Used=1).Create()                    
            #devicecreated.append(deviceparam(13 ,0, "23"))  # default is 23 degree
        DumpConfigToLog()
#Devices(1)
        self.AHU32bitConn = Domoticz.Connection(Name="Telnet", Transport="TCP/IP", Protocol="Line", Address=Parameters["Address"], Port=Parameters["Port"])
        self.AHU32bitConn.Connect()
        Domoticz.Heartbeat(1)

    def onStop(self):
        Domoticz.Log("onStop called")

    def onConnect(self, Connection, Status, Description):
        Domoticz.Log("onConnect called")
        if Status == 0:
            self.isConnected = True
            Domoticz.Log("Connected successfully to: "+Parameters["Address"]+":"+Parameters["Port"])
            self.AHU32bitConn.Send('?AHU\n') 
            wait=5

        else:
            self.isConnected = False
            self.power_on = False
            Domoticz.Debug("Failed to connect ("+str(Status)+") to: "+Parameters["Address"]+":"+Parameters["Port"]+" with error: "+Description)
        return

    def onMessage(self, Connection, Data):
        Domoticz.Log("onMessage called")
        self.oustandingPings = self.oustandingPings - 1
        strData = Data.decode("utf-8", "ignore")
        Domoticz.Log("onMessage called with Data: '"+str(strData)+"'")
        if (strData[0:9]=="$AHU32bit"):
            splitData = strData.split(";")
            T_Supply = splitData[1]
            Domoticz.Log("T_Supply: '"+str(T_Supply)+"'")
            T_Return = splitData[2]
            Domoticz.Log("T_Return: '"+str(T_Return)+"'")
            T_Gas = splitData[3]
            Domoticz.Log("T_Gas: '"+str(T_Gas)+"'")
            T_Liquid = splitData[4]
            Domoticz.Log("T_Liquid: '"+str(T_Liquid)+"'")
            T_Room = splitData[5]
            Domoticz.Log("T_Room: '"+str(T_Room)+"'")   
            T_Set_Command = splitData[6]
            Domoticz.Log("T_Set_Command: '"+str(T_Set_Command)+"'")  
            T_Out = splitData[7]
            Domoticz.Log("T_Out: '"+str(T_Out)+"'") 
            T_Cond = splitData[8]
            Domoticz.Log("T_Cond: '"+str(T_Cond)+"'") 
            T_Disch = splitData[9]
            Domoticz.Log("T_Disch: '"+str(T_Disch)+"'")             
            T_Module = splitData[10]
            Domoticz.Log("T_Module: '"+str(T_Module)+"'") 
            actual_freq = splitData[11]
            Domoticz.Log("actual_freq: '"+str(actual_freq)+"'") 
            actual_dc_voltage = splitData[12]
            Domoticz.Log("actual_dc_voltage: '"+str(actual_dc_voltage)+"'") 
            actual_current = splitData[13]
            Domoticz.Log("actual_current: '"+str(actual_current)+"'") 
            on_off_counter = splitData[14]
            Domoticz.Log("on_off_counter: '"+str(on_off_counter)+"'") 
            operation_time = splitData[15]
            Domoticz.Log("operation_time: '"+str(operation_time)+"'") 
            power_consumed = splitData[16]
            Domoticz.Log("power_consumed: '"+str(power_consumed)+"'") 
            power_produced = splitData[17]
            Domoticz.Log("power_produced: '"+str(power_produced)+"'") 
            COP_P = splitData[18]
            Domoticz.Log("COP_P: '"+str(COP_P)+"'") 
            energy_consumed = splitData[19]
            Domoticz.Log("energy_consumed: '"+str(energy_consumed)+"'") 
            energy_produced = splitData[20]
            Domoticz.Log("energy_produced: '"+str(energy_produced)+"'") 
            COP_E = splitData[21]
            Domoticz.Log("COP_E: '"+str(COP_E)+"'") 
            actual_flow = splitData[22]
            Domoticz.Log("actual_flow: '"+str(actual_flow)+"'") 
            defrost_flag = splitData[23]
            Domoticz.Log("defrost_flag: '"+str(defrost_flag)+"'") 
            defrost_counter = splitData[24]
            Domoticz.Log("defrost_counter: '"+str(defrost_counter)+"'") 
            actual_EEV = splitData[25]
            Domoticz.Log("actual_EEV: '"+str(actual_EEV)+"'") 
            actual_ODU_fan = splitData[26]
            Domoticz.Log("actual_ODU_fan: '"+str(actual_ODU_fan)+"'") 
            state_BYTE_1 = splitData[27]
            Domoticz.Log("state_BYTE_1: '"+str(state_BYTE_1)+"'") 
            state_BYTE_2 = splitData[28]
            Domoticz.Log("state_BYTE_2: '"+str(state_BYTE_2)+"'") 
            state_BYTE_3 = splitData[29]
            Domoticz.Log("state_BYTE_3: '"+str(state_BYTE_3)+"'") 
            Compressor_command = splitData[30]
            Domoticz.Log("Compressor_command: '"+str(Compressor_command)+"'") 
            Compressor_in_operation_flag = splitData[31]
            Domoticz.Log("Compressor_in_operation_flag: '"+str(Compressor_in_operation_flag)+"'") 
            power_state = splitData[32]
            Domoticz.Log("power_state: '"+str(power_state)+"'") 
            Contorl_Mode = splitData[33]
            Domoticz.Log("Contorl_Mode: '"+str(Contorl_Mode)+"'")   
            BASE_input_BYTE = splitData[34]
            Domoticz.Log("BASE_input_BYTE: '"+str(BASE_input_BYTE)+"'")   
            IDU_Tx_0x31_3 = splitData[35]
            Domoticz.Log("IDU_Tx_0x31_3: '"+str(IDU_Tx_0x31_3)+"'")  
            BASE_state_BYTE = splitData[36]
            Domoticz.Log("BASE_state_BYTE: '"+str(BASE_state_BYTE)+"'")    
            IDU_Tx_0x31_14 = splitData[37]
            Domoticz.Log("IDU_Tx_0x31_14: '"+str(IDU_Tx_0x31_14)+"'")    
            on_off_counter = splitData[38]
            Domoticz.Log("on_off_counter: '"+str(on_off_counter)+"'")  
            operation_time = splitData[39]
            Domoticz.Log("operation_time: '"+str(operation_time)+"'") 
            Compressor_P_term = splitData[40]
            Domoticz.Log("Compressor_P_term: '"+str(Compressor_P_term)+"'") 
            Compressor_sum_error = splitData[41]
            Domoticz.Log("Compressor_sum_error: '"+str(Compressor_sum_error)+"'") 
            Compressor_I_term = splitData[42]
            Domoticz.Log("Compressor_I_term: '"+str(Compressor_I_term)+"'") 
            Compressor_PID_out = splitData[43]
            Domoticz.Log("Compressor_PID_out: '"+str(Compressor_PID_out)+"'") 
            def_Compressor_kp = splitData[44]
            Domoticz.Log("def_Compressor_kp: '"+str(def_Compressor_kp)+"'") 
            def_Compressor_ki = splitData[45]
            Domoticz.Log("def_Compressor_ki: '"+str(def_Compressor_ki)+"'") 
            Compressor_error = splitData[46]
            Domoticz.Log("Compressor_error: '"+str(Compressor_error)+"'") 

        Devices[1].Update(0,T_Supply)
        Devices[2].Update(0,T_Return)
        Devices[3].Update(0,T_Gas)
        Devices[4].Update(0,T_Liquid)
        Devices[5].Update(0,T_Room)
        Devices[6].Update(0,T_Set_Command)
        Devices[7].Update(0,T_Out)
        Devices[8].Update(0,T_Cond)
        Devices[9].Update(0,T_Disch)
        Devices[10].Update(0,T_Module)
        Devices[11].Update(0,actual_freq)
        Devices[12].Update(0,actual_dc_voltage)
        Devices[13].Update(0,actual_current) 
        Devices[14].Update(0,on_off_counter) 
        Devices[15].Update(0,operation_time)         
        Devices[16].Update(0,power_consumed) 
        Devices[17].Update(0,power_produced) 
        Devices[18].Update(0,COP_P)
        Devices[19].Update(0,energy_consumed)
        Devices[20].Update(0,energy_produced)
        Devices[21].Update(0,COP_E)
        Devices[22].Update(0,actual_flow)
        Devices[23].Update(0,defrost_flag)
        Devices[24].Update(0,defrost_counter)
        Devices[25].Update(0,actual_EEV)
        Devices[26].Update(0,actual_ODU_fan)   
        Devices[27].Update(0,state_BYTE_1)   
        Devices[28].Update(0,state_BYTE_2)   
        Devices[29].Update(0,state_BYTE_3)   
        Devices[30].Update(0,Compressor_command)  
        Devices[31].Update(0,Compressor_in_operation_flag)  
        Devices[32].Update(0,power_state)  
        Devices[33].Update(0,Contorl_Mode) 
        Devices[34].Update(0,BASE_input_BYTE) 
        Devices[35].Update(0,IDU_Tx_0x31_3) 
        Devices[36].Update(0,BASE_state_BYTE) 
        Devices[37].Update(0,IDU_Tx_0x31_14) 
        Devices[38].Update(0,on_off_counter) 
        Devices[39].Update(0,operation_time)
        Devices[40].Update(0,Compressor_P_term) 
        Devices[41].Update(0,Compressor_sum_error) 
        Devices[42].Update(0,Compressor_I_term) 
        Devices[43].Update(0,Compressor_PID_out)
        Devices[44].Update(0,def_Compressor_kp) 
        Devices[45].Update(0,def_Compressor_ki) 
        Devices[46].Update(0,Compressor_error)   
        return

    def onCommand(self, Unit, Command, Level, Hue):
        Domoticz.Debug("onCommand called for Unit " + str(Unit) + ": Parameter '" + str(Command) + "', Level: " + str(Level))
        action, sep, params = Command.partition(' ')
        action = action.capitalize()
        params = params.capitalize()
        if Unit == 47:
            if Command=='Off':
                Domoticz.Debug("Unit Power Off")
                self.AHU32bitConn.Send(Message='AHU_OFF'+'\n', Delay=0)
                self.power_on = False
            elif Command=='On':
                Domoticz.Debug("Unit Power On")
                self.AHU32bitConn.Send(Message='AHU_ON'+'\n', Delay=0)
                self.power_on = True
        #elif Unit == self.UNITS['input']:
        #    if (action == "Set"):
        #       if Level != "0":
        #            self.input_mode = self.selector_find(Level,1)
        #            self.AHU32bitConn.Send(Message=self.input_mode+'FN\r', Delay=0)
        #        else:
        #            self.power_on = False
#                    self.AHU32bitConn.Send(Message=api.cmd_PowerOff, Delay=0)


    def onNotification(self, Name, Subject, Text, Status, Priority, Sound, ImageFile):
        Domoticz.Log("Notification: " + Name + "," + Subject + "," + Text + "," + Status + "," + str(Priority) + "," + Sound + "," + ImageFile)

    def onDisconnect(self, Connection):
        Domoticz.Log("onDisconnect called")
        self.isConnected = False

    def onHeartbeat(self):
        if (self.isConnected == True):
            self.AHU32bitConn.Send(Message='#T_set'+Devices[13].sValue+'\n', Delay=0)
            if (self.oustandingPings > 3):
                Domoticz.Debug("Ping Timeout, Disconnect")
                self.AHU32bitConn.Disconnect()
                self.nextConnect = 0
            else:
                Domoticz.Debug("POWER STATUS Message Sent")
                self.oustandingPings = self.oustandingPings + 1
        else:
            self.oustandingPings = 0
            self.nextConnect = self.nextConnect - 1
            if (self.nextConnect <= 0):
                self.nextConnect = 3
                self.AHU32bitConn.Connect()
        return


global _plugin
_plugin = BasePlugin()

def onStart():
    global _plugin
    _plugin.onStart()

def onStop():
    global _plugin
    _plugin.onStop()

def onConnect(Connection, Status, Description):
    global _plugin
    _plugin.onConnect(Connection, Status, Description)

def onMessage(Connection, Data):
    global _plugin
    _plugin.onMessage(Connection, Data)

def onCommand(Unit, Command, Level, Hue):
    global _plugin
    _plugin.onCommand(Unit, Command, Level, Hue)

def onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile):
    global _plugin
    _plugin.onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile)

def onDisconnect(Connection):
    global _plugin
    _plugin.onDisconnect(Connection)

def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()

# Generic helper functions

def UpdateDevice(Unit, nValue, sValue, TimedOut):
    # Make sure that the Domoticz device still exists (they can be deleted) before updating it 
    if (Unit in Devices):
        if (Devices[Unit].nValue != nValue) or (Devices[Unit].sValue != sValue) or (Devices[Unit].TimedOut != TimedOut):
            Devices[Unit].Update(nValue=nValue, sValue=str(sValue), TimedOut=TimedOut)
            Domoticz.Log("Update "+str(nValue)+":'"+str(sValue)+"' ("+Devices[Unit].Name+")")
    return

def DumpConfigToLog():
    for x in Parameters:
        if Parameters[x] != "":
            Domoticz.Debug( "'" + x + "':'" + str(Parameters[x]) + "'")
    Domoticz.Debug("Device count: " + str(len(Devices)))
    for x in Devices:
        Domoticz.Debug("Device:           " + str(x) + " - " + str(Devices[x]))
        Domoticz.Debug("Device ID:       '" + str(Devices[x].ID) + "'")
        Domoticz.Debug("Device Name:     '" + Devices[x].Name + "'")
        Domoticz.Debug("Device nValue:    " + str(Devices[x].nValue))
        Domoticz.Debug("Device sValue:   '" + Devices[x].sValue + "'")
        Domoticz.Debug("Device LastLevel: " + str(Devices[x].LastLevel))
    return
