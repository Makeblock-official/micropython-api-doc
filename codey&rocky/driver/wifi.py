#we can call the functions like this
# w=makeblock_wlan()
# w.__wifi_enable()
# w.__wifi_add_mac(True)
# w.wifi_sta("Maker-office","hulurobot423")
# w.__wifi_ap_config("oooy","12345678")
# w.wifi_mode(3)
# w.__wifi_start()
#to set theESP32 wifi at ap+sta mode,it will connect company's router,
#and set itself a ap,named "oooy" + mac address

from codey_global_board import *
from global_object import wlan_o
import time

class wifi():
    # mode:0 for null, 1 for sta, 2 for ap,3 for apsta
    # you can also use const variable STA 、AP、STA_AP
    def __init__(self):
        self.w_en = False
        self.w_mode = wlan_o.get_mode()
        self.connecting_ssid = None
        self.connecting_pass = None
        self.STA = wlan_o.STA
        self.AP = wlan_o.AP
        self.APSTA = wlan_o.STA_AP
        
    def __wifi_enable(self):
        if wlan_o.enable() == True:
            self.w_en = True
            return True
        else:
            return False

    def __wifi_disenable(self):
        if wlan_o.deinit() == True:
            self.w_en = False
            return True
        else:
            return False

    def __wifi_add_mac(self, en):
        if self.w_en == True:
            wlan_o.apssid_add_mac(en)
        else:
            print_dbg("wifi is not enabled")
          
    def __wifi_mode_config(self, mode):
        if self.w_en == True:      
            if mode > wlan_o.STA_AP:
                mode = wlan_o.STA_AP
            if wlan_o.set_mode(mode) == True:
                self.w_mode = mode
                return True
            else:
                return False
        else:
            print_dbg("wifi is not enabled")
        
    @ property
    def wifi_mode(self):
        return self.w_mode

    
    def __wifi_ap_config(self, ssid, password):
        if self.w_en == True:
            wlan_o.set_ap(ssid, password)
        else:
            print_dbg("wifi is not enabled")
        
    @property
    def wifi_ap(self):
        pass
    
    def __wifi_sta_config(self, ssid, password):
        if self.w_en == True:
            wlan_o.set_sta(ssid, password)
        else:
            print_dbg("wifi is not enabled")

    @property
    def wifi_sta(self):
        pass


    def __wifi_sta_auto_connect(self, en):
        if self.w_en == True:
            wlan_o.set_auto_connect(True)
        else:
            print_dbg("wifi is not enabled")
  
    def __wifi_start(self):
        if self.w_en == True:
            wlan_o.start(self.w_mode)
        else:
            print_dbg("wifi is not enabled")
        
    def __wifi_stop(self):
        if self.w_en == True:
           wlan_o.stop()
        else:
            print_dbg("wifi is not enabled")

    def __wifi_connect(self):
        if self.w_en == True:
            if self.w_mode == wlan_o.STA or self.w_mode == wlan_o.STA_AP:
                swlan_o.connect()
            else:
                print_dbg("only sta or apsta mode have this func")
        else:
            print_dbg("wifi is not enabled")
        
    def __wifi_disconnect(self):
        if self.w_en == True:
            if self.w_mode == wlan_o.STA or self.w_mode == wlan_o.STA_AP:
                temp = wlan_o.disconnect()
            else:
                temp = None
                print_dbg("only sta or apsta mode have this func")
        else:
            temp = None
            print_dbg("wifi is not enabled")
        return temp
        
    def __wifi_scan(self):
        if self.w_en == True:
            if self.w_mode == wlan_o.STA or self.w_mode == wlan_o.STA_AP:
                wlan_o.scan()
            else:
                print_dbg("only sta or apsta mode have this func")
        else:
            print_dbg("wifi is not enabled")
        
    #ifx shoule be set to :0 or 1    
    def __wifi_get_mac(self, ifx):
        if self.w_en == True:
            if ifx > 1:
                ifx = 1
            elif ifx < 0:
                ifx = 0;
            
            return wlan_o.get_mac(ifx)
        else:
            print_dbg("wifi is not enabled")

    def __wifi_sta_is_conn(self):
        if self.w_en == True:
            return wlan_o.sta_is_conn()
        else:
            return False

    # only the two function below face to users
    def start(self, ssid, password, mode = wlan_o.STA):
        ssid = str(ssid)
        password = str(password)
        if self.STA == mode:
            self.__wifi_enable()
            if (ssid != self.connecting_ssid) or (password != self.connecting_pass):
                self.connecting_ssid = ssid
                self.connecting_pass = password
                self.__wifi_sta_config(ssid, password)
                self.__wifi_mode_config(wlan_o.STA)
                self.__wifi_start()
            else:
                if not self.__wifi_sta_is_conn():
                    self.__wifi_connect()

    def is_connected(self):
        # sleep below is necessary now
        time.sleep(0.05)
        temp =  self.__wifi_sta_is_conn()
        return bool(temp)
