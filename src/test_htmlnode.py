import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", {"class": "container"})
        node2 = HTMLNode("div", {"class": "container"})
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = HTMLNode("div", {"class": "container"})
        node2 = HTMLNode("div", {"class": "row"})
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("div", "hello", [], {"class": "container"})
        self.assertEqual(
            "HTMLNode(tag=div, value=hello, children=[], props={'class': 'container'})", repr(node)
        )

if __name__ == "__main__":
    unittest.main()