from textnode import TextNode, TextType

print("hello world")

def main():
    example = TextNode("Durs are absolute dumbasses", TextType.LINK, "https://e621.net")
    print(example)

main()