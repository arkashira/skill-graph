import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Skill:
    name: str
    data_sources: List[str]

@dataclass
class Edge:
    from_node: str
    to_node: str

class SkillGraph:
    def __init__(self):
        self.skills: Dict[str, Skill] = {}
        self.edges: List[Edge] = []
        self.data_sources: Dict[str, Dict] = {}

    def add_skill(self, skill: Skill):
        self.skills[skill.name] = skill

    def add_edge(self, edge: Edge):
        self.edges.append(edge)

    def add_data_source(self, name: str):
        self.data_sources[name] = {'edges': []}

    def visualize(self):
        graph = {}
        for skill in self.skills.values():
            graph[skill.name] = {'data_sources': skill.data_sources, 'edges': []}
        for data_source in self.data_sources:
            graph[data_source] = self.data_sources[data_source]
        for edge in self.edges:
            if edge.from_node in graph:
                graph[edge.from_node]['edges'].append(edge.to_node)
        return graph

    def load(self, data: Dict):
        for skill_data in data['skills']:
            skill = Skill(name=skill_data['name'], data_sources=skill_data['data_sources'])
            self.add_skill(skill)
        for edge_data in data['edges']:
            edge = Edge(from_node=edge_data['from_node'], to_node=edge_data['to_node'])
            self.add_edge(edge)
            if edge.from_node not in self.data_sources:
                self.add_data_source(edge.from_node)

    def get_nodes(self):
        return list(self.skills.keys()) + list(self.data_sources.keys())

    def get_edges(self):
        return self.edges
