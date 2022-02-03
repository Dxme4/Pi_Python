import I2C_LCD_driver
import time

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Hello World!", 2)