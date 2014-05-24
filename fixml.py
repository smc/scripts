#!/usr/bin/python3

# This script replaces atomised chillus with their deatomised versions

import sys;

def replaceAanava(s): #{
	s = s.replace ("\u0D7A", "\u0D23\u0D4D\u200D").replace("\u0D7B","\u0D28\u0D4D\u200D").replace("\u0D7C", "\u0D30\u0D4D\u200D").replace("\u0D7D", "\u0D32\u0D4D\u200D").replace("\u0D7E", "\u0D33\u0D4D\u200D");
	return s;
#}

with sys.stdin as infile: #{
	for line in infile: #{
		sys.stdout.write(replaceAanava(line));
	#}
#}
