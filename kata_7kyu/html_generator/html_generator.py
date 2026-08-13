class HTMLGen:
    def __getattr__(self, tag):
        return lambda text: f"<{tag}>{text}</{tag}>"

    def comment(self, text):
        return f"<!--{text}-->"

