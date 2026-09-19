"""
@Author:xuyinglai
@Date:2026/7/25
@DESC:
"""


class Birds:
    def __init__(self, name, color, skill_description):
        self.name = name
        self.color = color
        self.skill_description = skill_description

    def fly(self):
        print(f"小鸟{self.name}会飞")

    def call(self):
        print(f"小鸟{self.name}会叫")

    def user_skill(self):
        print(f"{self.name}会技能")


class RedBirds(Birds):
    def __init__(self, name, color, skill_description):
        super.__init__()

    pass


class YellowBird(Birds):
    pass


class BlueBird(Birds):
    pass
