import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode

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

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Bold text")
        self.assertEqual(node.to_html(), "<b>Bold text</b>")
    
    def test_leaf_to_html_i(self):
        node = LeafNode("i", "Italic text")
        self.assertEqual(node.to_html(), "<i>Italic text</i>")

    def test_leaf_to_html_u(self):
        node = LeafNode("u", "Underlined text")
        self.assertEqual(node.to_html(), "<u>Underlined text</u>")