from textnode import TextNode, TextType
from node_delimit import split_nodes_delimiter

def test_split_bold(self):
    node = TextNode("This is **bold** text", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertListEqual(
        [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ],
        new_nodes,
    )

def test_split_italic(self):
    node = TextNode("This is _italic_ text", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    self.assertListEqual(
        [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ],
        new_nodes,
    )

def test_split_code(self):
    node = TextNode("This is `code` text", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertListEqual(
        [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT),
        ],
        new_nodes,
    )

def test_split_missing_delimiter(self):
    node = TextNode("This has an unclosed `code block", TextType.TEXT)
    with self.assertRaises(Exception):
        split_nodes_delimiter([node], "`", TextType.CODE)