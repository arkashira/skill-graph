import pytest
from skill_graph import Skill, Edge, SkillGraph

def test_skill_graph():
    graph = SkillGraph()
    skill1 = Skill(name='skill1', data_sources=['data_source1'])
    skill2 = Skill(name='skill2', data_sources=['data_source2'])
    edge = Edge(from_node='data_source1', to_node='skill1')
    graph.add_skill(skill1)
    graph.add_skill(skill2)
    graph.add_edge(edge)
    graph.add_data_source('data_source1')
    assert len(graph.get_nodes()) == 3
    assert len(graph.get_edges()) == 1

def test_skill_graph_load():
    graph = SkillGraph()
    data = {
        'skills': [
            {'name': 'skill1', 'data_sources': ['data_source1']},
            {'name': 'skill2', 'data_sources': ['data_source2']}
        ],
        'edges': [
            {'from_node': 'data_source1', 'to_node': 'skill1'}
        ]
    }
    graph.load(data)
    assert len(graph.get_nodes()) == 3
    assert len(graph.get_edges()) == 1

def test_skill_graph_visualize():
    graph = SkillGraph()
    skill1 = Skill(name='skill1', data_sources=['data_source1'])
    skill2 = Skill(name='skill2', data_sources=['data_source2'])
    edge = Edge(from_node='data_source1', to_node='skill1')
    graph.add_skill(skill1)
    graph.add_skill(skill2)
    graph.add_edge(edge)
    graph.add_data_source('data_source1')
    visualized_graph = graph.visualize()
    assert len(visualized_graph) == 3
    assert 'skill1' in visualized_graph
    assert 'skill2' in visualized_graph
    assert 'data_source1' in visualized_graph
