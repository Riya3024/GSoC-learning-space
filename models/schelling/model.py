from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import SingleGrid
import random


class SchellingAgent(Agent):
    def __init__(self, unique_id, model, agent_type):
        super().__init__(unique_id, model)
        self.type = agent_type

    def step(self):
        similar = 0
        total = 0

        neighbors = self.model.grid.get_neighbors(
            self.pos, moore=True, include_center=False
        )

        for neighbor in neighbors:
            total += 1
            if neighbor.type == self.type:
                similar += 1

        if total > 0 and similar / total < self.model.homophily:
            self.model.grid.move_to_empty(self)


class SchellingModel(Model):
    def __init__(self, N=50, width=10, height=10, homophily=0.5):
        self.num_agents = N
        self.grid = SingleGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.homophily = homophily

        for i in range(self.num_agents):
            agent_type = random.choice([0, 1])
            agent = SchellingAgent(i, self, agent_type)
            self.schedule.add(agent)

            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))

    def step(self):
        self.schedule.step()
