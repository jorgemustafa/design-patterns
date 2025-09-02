
class UsbPort:
    def __init__(self):
        self.port_available = True

    def plug(self, usb):
        if self.port_available:
            usb.plug_usb()
            self.port_available = False

class UsbCable:
    def __init__(self):
        self.is_plugged = False

    def plug_usb(self):
        self.is_plugged = True

# UsbCables can plug directly into Usb ports
usb_cable = UsbCable()
usb_port1 = UsbPort()
usb_port1.plug(usb_cable)

class MicroUsbCable:
    def __init__(self):
        self.is_plugged = False

    def plug_micro_usb(self):
        self.is_plugged = True

class MicroToUsbAdapter(UsbCable):
    def __init__(self, micro_usb_cable):
        self.micro_usb_cable = micro_usb_cable
        self.micro_usb_cable.plug_micro_usb()

micro_to_usb_adapter = MicroToUsbAdapter(MicroUsbCable())
usb_port2 = UsbPort()
usb_port2.plug(micro_to_usb_adapter)