import pytest
import project.graph_utils as gu


def test_get_graph_info_skos():
    nodes, edges, labels = gu.get_graph_info("skos")
    assert nodes == 144
    assert edges == 252


def test_get_graph_info_atom():
    nodes, edges, labels = gu.get_graph_info("atom")
    assert nodes == 291
    assert edges == 425


def test_two_cycles_save(tmp_path):
    path = tmp_path.joinpath("cycles.dot")
    # path = "tmp.dot"

    gu.save_two_cycles_in_pydot(path, 2, 2)

    actual = path.read_text()

    expected = """digraph  {
1;
2;
0;
3;
4;
1 -> 2  [key=0, label=a];
2 -> 0  [key=0, label=a];
0 -> 1  [key=0, label=a];
0 -> 3  [key=0, label=b];
3 -> 4  [key=0, label=b];
4 -> 0  [key=0, label=b];
}
"""

    assert actual == expected
