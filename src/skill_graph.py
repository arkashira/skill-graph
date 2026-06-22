import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Skill:
    name: str
    dependencies: List[str]

class SkillGraph:
    def __init__(self):
        self.skills = {}

    def add_skill(self, skill: Skill):
        self.skills[skill.name] = skill.dependencies

    def generate_graph(self, target_skill: str) -> Dict:
        graph = {}
        visited = set()

        def recursive_lookup(skill: str):
            if skill not in self.skills:
                return
            if skill in visited:
                return
            visited.add(skill)
            dependencies = self.skills.get(skill, [])
            graph[skill] = dependencies
            for dependency in dependencies:
                recursive_lookup(dependency)

        recursive_lookup(target_skill)
        return graph

    def api_endpoint(self, target_skill: str) -> str:
        graph = self.generate_graph(target_skill)
        return json.dumps(graph)
