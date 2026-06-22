import pytest
from skill_graph import SkillGraph, Skill

def test_add_skill():
    graph = SkillGraph()
    skill = Skill("Python", ["Programming"])
    graph.add_skill(skill)
    assert graph.skills["Python"] == ["Programming"]

def test_generate_graph():
    graph = SkillGraph()
    graph.add_skill(Skill("Python", ["Programming"]))
    graph.add_skill(Skill("Programming", ["Algorithms", "Data Structures"]))
    result = graph.generate_graph("Python")
    assert result == {
        "Python": ["Programming"],
        "Programming": ["Algorithms", "Data Structures"]
    }

def test_api_endpoint():
    graph = SkillGraph()
    graph.add_skill(Skill("Python", ["Programming"]))
    graph.add_skill(Skill("Programming", ["Algorithms", "Data Structures"]))
    result = graph.api_endpoint("Python")
    expected = '{"Python": ["Programming"], "Programming": ["Algorithms", "Data Structures"]}'
    assert result == expected

def test_generate_graph_edge_case():
    graph = SkillGraph()
    graph.add_skill(Skill("Python", ["Programming"]))
    result = graph.generate_graph("Unknown Skill")
    assert result == {}
