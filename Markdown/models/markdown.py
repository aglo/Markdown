import houdini as h
from misaka import SmartyPants
from misaka import HtmlRenderer

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound

class BleepRenderer(HtmlRenderer, SmartyPants):
    def block_code(self, text, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % h.escape_html(text.strip())
        try:
            lexer = get_lexer_by_name(lang, stripall=True)
        except ClassNotFound:
            return '\n<pre><code>%s</code></pre>\n' % h.escape_html(text.strip())
        formatter = HtmlFormatter()
        return highlight(text, lexer, formatter)
