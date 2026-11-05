import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

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

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self): 
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_with_props(self):
        parent_node = ParentNode("div", [], {"class": "container"})
        self.assertEqual(parent_node.to_html(), '<div class="container"></div>')

    def test_to_html_with_children_and_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(parent_node.to_html(), '<div class="container"><span>child</span></div>')  
    
    def test_to_html_with_grandchildren_and_props(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span><b>grandchild</b></span></div>',
        )