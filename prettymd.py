#!/usr/bin/env python

# The MIT License (MIT) Copyright (c) 2012 Michael-Keith Bernard
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
from StringIO import StringIO
from subprocess import Popen, PIPE

from mako.template import Template
from mako.runtime import Context

MARKDOWN_TEMPLATE = """<html>
  <head>
    <title>${title}</title>
    % if use_stylesheet:
    <link href="http://kevinburke.bitbucket.org/markdowncss/markdown.css" rel="stylesheet" />
    % endif
  </head>
  <body>
${content}
  </body>
</html>
"""

def run_cmd(cmd):
  res = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
  return (res.stdout.read(), res.stderr.read())

def main():
  parser = argparse.ArgumentParser(description="Markdownify Template")
  parser.add_argument("-f", "--file", required=True)
  parser.add_argument("-o", "--output", default=None)
  parser.add_argument("-t", "--title", default="No title")
  parser.add_argument("-n", "--no-style", action='store_false', default=True)
  args = parser.parse_args()

  content, _err = run_cmd("markdown %s" % args.file)

  buff = StringIO()
  ctx = Context(buff, title=args.title, use_stylesheet=args.no_style,
      content=content)
  template = Template(MARKDOWN_TEMPLATE)
  template.render_context(ctx)

  if args.output:
    with open(args.output, "wb") as f:
      f.write(buff.getvalue())
      f.flush()
  else:
    print buff.getvalue()

if __name__ == "__main__":
  main()
