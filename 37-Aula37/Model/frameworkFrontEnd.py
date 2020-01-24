
class FrameworkFrontEnd:
    def __init__(self, FrameworkFrontEnd, FrontEnd_desc):
        self.id_FrontEnd = 0
        self.FrameworkFrontEnd = FrameworkFrontEnd
        self.FrontEnd_desc = FrontEnd_desc

    def __str__(self):
        return f'{self.id_FrontEnd};{self.FrameworkFrontEnd};{self.FrontEnd_desc}' 