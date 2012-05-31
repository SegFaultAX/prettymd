#!/usr/bin/env python

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
  res = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
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
