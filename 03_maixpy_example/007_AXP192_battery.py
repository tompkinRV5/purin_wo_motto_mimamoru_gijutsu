## Copyright (c) 2019 aNoken
## https://anoken.jimdo.com/
## https://github.com/anoken/purin_wo_motto_mimamoru_gijutsu


import pmu,lcd
lcd.init()
lcd.clear()
axp = pmu.axp192()
axp.enableADCs(True)
while True:
    vbat = axp.getVbatVoltage()
    usb_vol = axp.getUSBVoltage()
    usb_cur = axp.getUSBInputCurrent()
    connext_vol = axp.getConnextVoltage()
    connext_input_current = axp.getConnextInputCurrent()
    bat_current= axp.getBatteryChargeCurrent()
    bat_dis_current = axp.getBatteryDischargeCurrent()
    bat_instant_watts = axp.getBatteryInstantWatts()
    temp = axp.getTemperature()

    lcd.draw_string(20,0,"vbat:"+str(vbat))
    lcd.draw_string(20,15,"usb_vol:"+str(usb_vol))
    lcd.draw_string(20,30,"usb_cur:"+str(usb_cur))
    lcd.draw_string(20,45,"connext_vol:"+str(connext_vol))
    lcd.draw_string(20,60,"connext_input_current:"+str(connext_input_current))
    lcd.draw_string(20,75,"bat_current:"+str(bat_current))
    lcd.draw_string(20,90,"bat_dis_current:"+str(bat_dis_current))
    lcd.draw_string(20,105,"bat_instant_watts:"+str(bat_instant_watts))
    lcd.draw_string(20,120,"temp:"+str(temp))


