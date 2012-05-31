# Pretty Markdown

## Introduction

Pretty Markdown is a small Python script for making pretty stand-alone markdown
HTML pages. It wraps the page with the appropriate HTML tags and links with the
awesome [Markdown.css by Kevin
Burke](http://kevinburke.bitbucket.org/markdowncss/) stylesheet.

### Usage

Run `prettymd.py` with a markdown file to convert it into HTML wrapped in a
pretty template:

```
$ prettymd.py -f foo.markdown
```

By default, `prettymd.py` prints to stdout, but you can supply an output file on
the command-line as well:

```
$ prettymd.py -f foo.markdown -o bar.html
```

You can also supply a title for your pretty markdown page:

```
$ prettymd.py -f foo.markdown -o bar.html -t "Awesome Foobar!"
```

The pretty template uses [Markdown.css by Kevin
Burke](http://kevinburke.bitbucket.org/markdowncss/) by default. You can also
generate an output file without the stylesheet linked:

```
$ prettymd.py -f foo.markdown -o bar.html -t "Awesome Foobar!" -n
```
