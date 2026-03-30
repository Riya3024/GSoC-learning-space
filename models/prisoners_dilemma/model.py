from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import random


class PD_Agent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.move = random.choice(["C", "D"])

    def step(self):
        self.move = random.choice(["C", "D"])


class PD_Model(Model):
    def __init__(self, N=10, width=10, height=10):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        for i in range(self.num_agents):
            agent = PD_Agent(i, self)
            self.schedule.add(agent)
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))

    def step(self):
        self.schedule.step()
