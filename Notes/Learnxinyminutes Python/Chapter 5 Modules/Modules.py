"""
    Chapter 5
    Modules
"""

# A module is any .py file

# Example:
# math_utils.py
# characters.py
# inventory.py

# Let's say inside math_utils.py is
def add(x, y):
    return x + y

# You can use this to bring it into another file
import math_utils
print(math_utils.add(3, 4))

# Modules = namespaces
# Everything inside them is addressed as 
# module_name.object_name




# How python finds modules
# When you write
import foo
# Python searches in the following places IN THIS ORDER:
# 1) CWD
# 2) Any directories in PYTHONPATH
# 3) Site-packages (installed libs)
# 4) Standard Library


# Modules only need to be imported ONCE
# They are cached once used. 


# Different ways to import

# Import the Module
import math_utils
math_utils.add(2, 3)

# Import specific names
from math_utils import add
add(2,3)

# Import with Alias
import math_utils as m
m.add(2, 3)

# Import multiple names
from math_utils import add, subtract

# Import everything (Almost always a bad move)
from math_utils import *
# Usually a bad idea because you lose namespace safety. Funky things can happen





# Every module has a Name: __name__

# file: mymodule.py
print(__name__)     # Will print __main__ if run from the file it's in

# file: someotherfile.py
import mymodule
print(mymodule.print(__name__))     # will print mymodule because the function is from another file





# Packages (Directories that act like Modules)
# A directory is a package if it has an __init__.py file:
'''
myproject/
    __init__.py
    utils/
        __init__.py
        math.py
        io.py
    models/
        __init__.py
        person.py
'''

# Use it like
import myproject.utils.math
# or
from myproject.utils.math import add

# Relative imports (Used inside packages)
from .math import add
# . means "Import from the current package"
# .. means "Import from the parent package"





# The STL (Standard Library) is a MASSIVE toolbox
# Python ships with a ton of modules
# Browse all the built in ones at https://docs.python.org/3/py-modindex.html
'''
🔹 Text Processing Services

string – basic string helpers and constants. 
 

string.templatelib – support for template string literals (new 3.14 t-strings). 
 
+1

re – regular expressions. 
 

difflib – compute differences (diff/patch-style). 
 

textwrap – wrap/fill text into columns. 
 

unicodedata – Unicode character database. 
 

stringprep – string preparation for internet protocols. 
 

readline – GNU readline integration. 
 

rlcompleter – tab-completion with readline. 
 



🔹 Binary Data Services

struct – pack/unpack C-style binary data. 
 

codecs – codec registry and encoding/decoding base classes. 
 



🔹 Data Types

datetime – date/time types. 
 

zoneinfo – IANA timezone database support. 
 

calendar – calendar/weekday/month utilities. 
 

collections – extra container types (deque, Counter, etc.). 
 

collections.abc – abstract base classes for containers. 
 

heapq – heap (priority queue) operations. 
 

bisect – binary search and insertion into sorted lists. 
 

array – compact C-like numeric arrays. 
 

weakref – weak references to objects. 
 

types – helpers and names for dynamic type creation. 
 

copy – shallow/deep copying utilities. 
 

pprint – pretty-print Python data structures. 
 

reprlib – controlled / shortened repr() implementations. 
 

enum – enumeration types. 
 

graphlib – graph utilities (e.g., topological sort). 
 



🔹 Numeric & Mathematical Modules

numbers – numeric abstract base classes. 
 

math – standard math functions (sin, cos, sqrt…). 
 

cmath – math for complex numbers. 
 

decimal – decimal fixed/floating-point arithmetic. 
 

fractions – rational numbers (p/q). 
 

random – pseudo-random numbers. 
 

statistics – basic statistics (mean, median, stdev…). 
 



🔹 Functional Programming Helpers

itertools – iterator-building tools (chain, product, etc.). 
 

functools – higher-order functions (partial, lru_cache, etc.). 
 

operator – operators exposed as callable functions. 
 



🔹 File & Directory Access

pathlib – OO filesystem paths. 
 

os.path – traditional path utilities. 
 

stat – interpret stat() results / mode bits. 
 

filecmp – compare files/directories. 
 

tempfile – temp files and directories. 
 

glob – shell-style path patterns (*.txt). 
 

fnmatch – filename pattern matching. 
 

linecache – random access to lines in text files. 
 

shutil – high-level file ops (copy, move, rmtree…). 
 



🔹 Data Persistence

pickle – serialize/deserialize Python objects. 
 

copyreg – register custom pickling functions. 
 

shelve – simple persistent dict-like storage. 
 

marshal – internal object serialization (implementation detail). 
 

dbm – simple key/value “database” interfaces. 
 

sqlite3 – built-in SQLite DB-API 2.0 interface. 
 



🔹 Data Compression & Archiving

compression package – umbrella for compression modules. 
 
+1

compression.zstd – Zstandard compression support (new 3.14). 
 
+1

zlib – DEFLATE/gzip-style compression. 
 

gzip – read/write .gz files. 
 

bz2 – bzip2 compression. 
 

lzma – LZMA/XZ compression. 
 

zipfile – ZIP archive handling. 
 

tarfile – tar archive handling. 
 



🔹 File Formats

csv – CSV read/write. 
 

configparser – INI-style config files. 
 

tomllib – parse TOML files. 
 

netrc – .netrc credential files. 
 

plistlib – Apple .plist read/write. 
 



🔹 Cryptographic Services

hashlib – secure hashes (SHA, etc.). 
 

hmac – keyed hashing (HMAC). 
 

secrets – crypto-strong randoms for secrets. 
 



🔹 Generic OS Services

os – core OS interfaces (env, processes, paths). 
 

io – stream abstractions (files, buffers). 
 

time – time access/conversion. 
 

logging – logging framework. 
 

logging.config – configure logging. 
 

logging.handlers – extra logging handlers. 
 

platform – info about the OS/platform. 
 

errno – standard errno constants. 
 

ctypes – call C functions from shared libs. 
 



🔹 Command-line Interface Libraries

argparse – modern CLI argument parser. 
 

optparse – older CLI parser (superseded). 
 

getpass – secure password input. 
 

fileinput – loop over stdin and files as one. 
 

curses – terminal control (ncurses). 
 

curses.textpad – text widgets for curses. 
 

curses.ascii – ASCII helpers. 
 

curses.panel – panel stack extension for curses. 
 

cmd – build line-oriented command shells. 
 



🔹 Concurrent Execution

threading – threads with locks/queues. 
 

multiprocessing – process-based parallelism. 
 

multiprocessing.shared_memory – shared memory blocks between processes. 
 

concurrent package – higher-level concurrency framework. 
 

concurrent.futures – thread/process pools. 
 

concurrent.interpreters – subinterpreters in one process (3.14). 
 
+1

subprocess – spawn and manage child processes. 
 

sched – event scheduler. 
 

queue – thread-safe queues. 
 

contextvars – context-local variables. 
 

_thread – low-level thread API. 
 



🔹 Networking & IPC

asyncio – async I/O event loop. 
 

socket – BSD socket interface. 
 

ssl – TLS/SSL wrapping around sockets. 
 

select – I/O readiness multiplexing. 
 

selectors – higher-level I/O multiplexing. 
 

signal – signal handlers. 
 

mmap – memory-mapped file access. 
 



🔹 Internet Data Handling

email – full email/MIME package. 
 

json – JSON encode/decode. 
 

mailbox – mailbox file formats. 
 

mimetypes – map file extensions ↔ MIME types. 
 

base64 – Base16/32/64/85 encodings. 
 

binascii – binary↔ASCII conversion. 
 

quopri – MIME quoted-printable handling. 
 



🔹 Structured Markup & XML

html – HTML helpers. 
 

html.parser – basic HTML parser. 
 

html.entities – predefined HTML entities. 
 

XML modules: 
 

xml.etree.ElementTree – high-level XML tree API.

xml.dom – DOM API.

xml.dom.minidom – minimal DOM implementation.

xml.dom.pulldom – incremental DOM building.

xml.sax – SAX2 interface.

xml.sax.handler – SAX handler base classes.

xml.sax.saxutils – SAX utilities.

xml.sax.xmlreader – SAX parser interface.

xml.parsers.expat – Expat-based XML parser.



🔹 Internet Protocols & Support

webbrowser – launch/configure a web browser. 
 

wsgiref – WSGI utilities/reference server. 
 

urllib – URL helpers umbrella. 
 

urllib.request – open URLs.

urllib.response – response types.

urllib.parse – URL parsing/building.

urllib.error – URL-related exceptions.

urllib.robotparser – robots.txt parser.

http – base HTTP modules.

http.client – HTTP client.

ftplib – FTP client.

poplib – POP3 client.

imaplib – IMAP4 client.

smtplib – SMTP client.

uuid – RFC 9562 UUID objects.

socketserver – base classes for network servers.

http.server – simple HTTP server.

http.cookies – cookie handling (server-side).

http.cookiejar – cookie handling (client-side).

xmlrpc – XML-RPC support umbrella.

xmlrpc.client – XML-RPC client.

xmlrpc.server – XML-RPC servers.

ipaddress – IPv4/IPv6 manipulation.



🔹 Multimedia Services

wave – read/write WAV audio. 
 

colorsys – color space conversions. 
 



🔹 Internationalization

gettext – message translation (i18n). 
 

locale – locale settings & formatting. 
 



🔹 GUI with Tk

tkinter – main Tk GUI bindings. 
 

tkinter.colorchooser – color chooser dialog.

tkinter.font – font handling.

tkinter.messagebox – message dialogs.

tkinter.scrolledtext – scrolled text widget.

tkinter.dnd – drag-and-drop.

tkinter.ttk – themed widgets.

IDLE – bundled editor/IDE.

turtle – turtle graphics (teaching/visuals).



🔹 Development Tools

typing – type hints / static typing helpers. 
 

pydoc – generate/view docs.

Python Development Mode – dev-mode runtime behaviors.

doctest – test examples in docstrings.

unittest – unit testing framework.

unittest.mock – mocking for tests (plus its “getting started” doc entry).

test and test.support.* – CPython’s regression test suite and helpers.



🔹 Debugging & Profiling

bdb – debugger support framework. 
 

faulthandler – dump tracebacks on low-level faults.

pdb – interactive debugger.

timeit – micro-benchmarking small snippets.

trace – execution tracing.

tracemalloc – track memory allocations.

(Plus the “Python Profilers” doc section for cProfile/profile.)



🔹 Packaging & Distribution

ensurepip – bootstrap pip. 
 

venv – create venvs.

zipapp – build/run zip-based apps.



🔹 Python Runtime Services

sys – interpreter state & runtime info. 
 

sys.monitoring – execution event monitoring.

sysconfig – Python build/config info.

builtins – built-in functions, types, etc.

__main__ – top-level execution environment.

warnings – control warning filters.

dataclasses – auto-generate class boilerplate.

contextlib – context manager utilities (with).

abc – abstract base class helpers.

atexit – register exit hooks.

traceback – format/print tracebacks.

__future__ – enable future language features.

gc – garbage collector interface.

inspect – introspection of live objects.

annotationlib – annotation introspection utilities (new 3.14). 
 
+1

site – site-specific startup configuration.



🔹 Custom Python Interpreters

code – interactive interpreter base classes. 
 

codeop – compile Python code dynamically. 
 



🔹 Import System

zipimport – import from zip archives. 
 

pkgutil – helpers for extending packages.

modulefinder – find modules used by a script.

runpy – run modules as scripts.

importlib – core import implementation.

importlib.resources – access package resources.

importlib.resources.abc – resource ABCs.

importlib.metadata – read distribution/package metadata.



🔹 Language Services

ast – abstract syntax trees. 
 

symtable – compiler symbol tables.

token – token constants.

keyword – list/check of Python keywords.

tokenize – tokenization of Python source.

tabnanny – detect ambiguous indentation.

pyclbr – class browser helper.

py_compile – compile .py files.

compileall – byte-compile whole trees.

dis – bytecode disassembler.

pickletools – tools for examining pickles.



🔹 Windows-Specific

msvcrt – MSVC runtime helpers. 
 

winreg – Windows registry access.

winsound – play system sounds.



🔹 Unix-Specific

shlex – shell-style lexical analysis. 
 

posix – POSIX system calls.

pwd – password database.

grp – group database.

termios – POSIX terminal control.

tty – terminal control helpers.

pty – pseudo-terminals.

fcntl – fcntl/ioctl system calls.

resource – resource usage/limits.

syslog – syslog logging.



🔹 Superseded / Removed / CLI Docs

getopt – old C-style CLI parsing (superseded by argparse). 
 

    There are also doc sections for:

    “Modules command-line interface (CLI)”

    “Superseded Modules”

    “Removed Modules”

    “Security Considerations”
'''







# Installing external packages
# pip install PACKAGENAME
# pip install numpy





# Why Modules Matter
'''
Modules let you:

    split code logically

    avoid massive monolithic files

    avoid naming conflicts

    reuse code

    test components in isolation

    share code across projects

Python codebases with dozens or hundreds of files are common and normal.
'''





# Very rarely will you ever need to rerun an import (Maybe in interactive environments)
import importlib
importlib.reload(foo)

