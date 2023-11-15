# XSS Finder for PortSwigger

Script created for the PortSwigger lab "Reflected XSS into HTML context with most tags and attributes blocked"

This script performs brute-force on URLs to identify cross-site scripting vulnerabilities.

## Usage:
Clone this repository, then install requests with `pip3 install requests` or `python3 -m pip install requests`.

To use this script, place the words you want to test in a file named wordlist.txt in the same directory and use the word FUZZ in the lab URL. "FUZZ" will be replaced by the words from your wordlist for the bruteforce. Remember to keep URL encoded.

For example, if you want to test `<FUZZ>` (so that FUZZ is replaced by head, img, etc.), make it URL encoded as in the example:

```
python3 xssfinderforps.py https://lab-url/%3CFUZZ%3E
```