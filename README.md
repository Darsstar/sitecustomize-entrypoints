# sitecustomize-entrypoints

A very simple library that makes a python module called `sitecustomize`
available. Python's [site](https://docs.python.org/3/library/site.html)
module gives it, and `usercustomize`, special treatment by importing it after
it is done looking for and processing .pth files.

What this package does is that is finds all `sitecustomize` entry points and,
if they are callable, calls them.