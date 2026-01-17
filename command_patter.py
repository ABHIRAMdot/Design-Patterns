class Light:
    def on(self):
        print("Light ON")
    def off(self):
        print("Light OFF")


class Command:
    def execute(self):
        pass
    def undo(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light


    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LighOffCommand(Command):
    def __init__(self, light):
        self.light = light 

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()



class RemoteControl:
    def __init__(self):
        self.history = []

    def press(self, command):
        command.execute()
        self.history.append(command)
    
    def undo(self):
        if self.history:
            last = self.history.pop()
            last.undo()


light = Light()

on_cmd = LightOnCommand(light)
off_cmd = LighOffCommand(light)

remote = RemoteControl()

remote.press(on_cmd)
remote.press(off_cmd)


remote.undo()
remote.undo()