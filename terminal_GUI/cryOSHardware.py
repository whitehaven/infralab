class cryOSTempSensor(object):
    def __init__(self, description, diagram_location, temp=0, test_mode=False):
        self.temp = temp
        self.description = description
        self.diagram_location = diagram_location
        self.test_mode = test_mode

    def __repr__(self):
        return 'cryOSTempSensor("' \
               + self.description \
               + '", diagram_location=' \
               + str(self.diagram_location) \
               + ', temp=' \
               + str(self.temp) \
               + ', test_mode=' \
               + str(self.test_mode) \
               + ')'

    def update_sensor(self):
        # TODO: connect to sensor code
        self.temp = 0


class cryOSHardwareSet(object):
    def __init__(self, temp_sensors=None, hardware_layout='double heatsink'):
        if not temp_sensors:
            self.temp_sensors = list()
        else:
            self.temp_sensors = temp_sensors
        self.last_refresh = None
        self.hardware_layout = hardware_layout

        if self.hardware_layout == 'double heatsink':
            self.diagram = ('  ||     ||  ',
                            '  ||     ||  ',
                            '  ||     ||  ',
                            '  =========  ',
                            ' +---------+ ',
                            ' +---------+ ',
                            '  | | | | |  ',
                            '    | | |    ',
                            '    | | |    ',
                            '      |      ',
                            '      |      '
                            )

    def __repr__(self):
        return 'cryOSHardwareSet(hardware_layout="' \
               + self.hardware_layout \
               + '", temp_sensors=' \
               + repr(self.temp_sensors) \
               + ')'

    def add_temp_sensor(self, description, diagram_location, test_mode=False):
        self.temp_sensors.append(
            cryOSTempSensor(description=description, diagram_location=diagram_location, test_mode=test_mode))

    def update_temp_sensors(self):
        for sensor in self.temp_sensors:
            sensor.update_sensor()


if __name__ == '__main__':
    test_temp_sensor = cryOSTempSensor('test', diagram_location=1, test_mode=True)

    print(repr(test_temp_sensor))

    test_cryOS_rig = cryOSHardwareSet()
    test_cryOS_rig.add_temp_sensor('test1', diagram_location=1, test_mode=True)
    test_cryOS_rig.add_temp_sensor('test2', diagram_location=2, test_mode=True)

    print(repr(test_cryOS_rig))
