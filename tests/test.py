from pytest import *



def Markdown_to_HTML_test():
    # full test
    # file.md -> html:str
    pass

def headers_test():
    # Test for headers (h1, h2, h3, etc.)
    # Markdown: # Header 1, ## Header 2, ### Header 3
    # HTML: <h1>Header 1</h1>, <h2>Header 2</h2>, <h3>Header 3</h3>
    pass

def paragraphs_test():
    # Test for paragraphs
    # Markdown: This is a paragraph.
    # HTML: <p>This is a paragraph.</p>
    pass

def blockquotes_test():
    # Test for blockquotes
    # Markdown: > This is a blockquote
    # HTML: <blockquote><p>This is a blockquote</p></blockquote>
    pass

def lists_test():
    # Test for both ordered and unordered lists
    # Markdown (unordered): * Item 1, * Item 2 or - Item 1, - Item 2
    # HTML (unordered): <ul><li>Item 1</li><li>Item 2</li></ul>
    # Markdown (ordered): 1. Item 1, 2. Item 2
    # HTML (ordered): <ol><li>Item 1</li><li>Item 2</li></ol>
    pass

def tables_test():
    # Test for tables (if supported)
    # Markdown: | Header | Header |\n|--------|--------|\n| Cell   | Cell   |
    # HTML: <table><thead><tr><th>Header</th><th>Header</th></tr></thead><tbody><tr><td>Cell</td><td>Cell</td></tr></tbody></table>
    pass

def code_blocks_test():
    # Test for inline code and code blocks
    # Markdown (inline): `code`
    # HTML (inline): <code>code</code>
    # Markdown (block): ```python\nprint("Hello")\n```
    # HTML (block): <pre><code class="language-python">print("Hello")</code></pre>
    pass

def horizontal_rule_test():
    # Test for horizontal rules
    # Markdown: --- or *** or ___
    # HTML: <hr>
    pass

def html_passthrough_test():
    # Test for HTML passthrough (if supported)
    # Markdown: <div>Raw HTML</div>
    # HTML: <div>Raw HTML</div>
    pass


def emphasis_test():
    # Test for italic text
    # Markdown: *italic* or _italic_
    # HTML: <em>italic</em>
    pass

def strong_emphasis_test():
    # Test for bold text
    # Markdown: **bold** or __bold__
    # HTML: <strong>bold</strong>
    pass

def links_test():
    # Test for hyperlinks
    # Markdown: [Link text](https://www.example.com)
    # HTML: <a href="https://www.example.com">Link text</a>
    pass

def images_test():
    # Test for image embedding
    # Markdown: ![Alt text](image.jpg)
    # HTML: <img src="image.jpg" alt="Alt text">
    pass

def line_breaks_test():
    # Test for line breaks
    # Markdown: End of line  (two spaces)
    # HTML: End of line<br>
    pass

def task_lists_test():
    # Test for task lists (if supported)
    # Markdown: - [ ] Task 1, - [x] Task 2
    # HTML: <ul><li><input type="checkbox"> Task 1</li><li><input type="checkbox" checked> Task 2</li></ul>
    pass

def strikethrough_test():
    # Test for strikethrough text (if supported)
    # Markdown: ~~strikethrough~~
    # HTML: <del>strikethrough</del>
    pass

def definition_lists_test():
    # Test for definition lists (if supported)
    # Markdown: Term\n: Definition
    # HTML: <dl><dt>Term</dt><dd>Definition</dd></dl>
    pass

def footnotes_test():
    # Test for footnotes (if supported)
    # Markdown: Here's a sentence with a footnote.[^1]\n\n[^1]: This is the footnote.
    # HTML: <p>Here's a sentence with a footnote.<sup id="fnref:1"><a href="#fn:1" class="footnote-ref">1</a></sup></p><div class="footnote"><hr><ol><li id="fn:1"><p>This is the footnote.&nbsp;<a href="#fnref:1" class="footnote-backref">↩</a></p></li></ol></div>
    pass

def abbreviations_test():
    # Test for abbreviations (if supported)
    # Markdown: The HTML specification\n*[HTML]: Hypertext Markup Language
    # HTML: The <abbr title="Hypertext Markup Language">HTML</abbr> specification
    pass

def nested_elements_test():
    # Test for proper nesting of elements (e.g., bold inside a list item)
    # Markdown: * List item with **bold** text
    # HTML: <ul><li>List item with <strong>bold</strong> text</li></ul>
    pass

def escaping_test():
    # Test for proper escaping of special characters
    # Markdown: \*Not italic\*
    # HTML: *Not italic*
    pass

def html_passthrough_test():
    # Test for HTML passthrough (if supported)
    # Markdown: <div>Raw HTML</div>
    # HTML: <div>Raw HTML</div>
    pass