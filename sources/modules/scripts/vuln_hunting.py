know_vulnerable = ["alloca", "_alloca", "scanf", "wscanf", "sscanf", "swscanf", "vscanf", "vsscanf", "strlen", "wcslen", "strtok", "strtok_r",
"wcstok", "strcat", "strncat", "wcscat", "wcsncat", "strcpy", "strncpy", "wcscpy", "wcsncpy", "memcpy", "wmemcpy", "stpcpy",
"stpncpy", "wcpcpy", "wcpncpy", "memmove", "wmemmove", "memcmp", "wmemcmp", "mset", "wmemset", "gets", "vsprintf", 
"swprintf", "vswprintf", "snprintf", "vsnprintf", "realpath", "getwd", "wctomb", "wcrtomb", "wcstombs", "wcsrtombs",
"wcsnrtombs", "strcpy", "strcpyA", "strcpyW", "wcscpy", "_tcscpy", "_mbscpy", "StrCpy", "StrCpyA", "StrCpyW", "lstrcpy",
"lstrcpyA", "lstrcpyW", "_tccpy", "mbccpy", "_ftcscpy", "strncpy", "wcsncpy", "_tcsncpy", "_mbsncpy", "_mbsnbcpy", 
"StrCpyN", "StrCpyNA", "StrCpyNW", "StrNCpy", "strcpynA", "StrNCpyA", "StrNCpyW", "lstrcpyn", "lstrcpynA", "lstrcpynW",
"strcat", "strcatA", "strcatW", "wcscat", "_tcscat", "_mbscat", "StrCat", "StrCatA", "StrCatW", "lstrcat", "lstrcatA",
"lstrcatW", "StrCatBuff", "StrCatBuffA", "StrCatBuffW", "StrCatChainW", "_tccat", "_mbccat", "_ftcscat", "strncat", 
"wcsncat", "_tcsncat", "_mbsncat", "_mbsnbcat", "StrCatN", "StrCatNA", "StrCatNW", "StrNCat", "StrNCatA", "StrNCatW", 
"lstrncat", "lstrcatnA", "lstrcatnW", "lstrcatn", "sprintfW", "sprintfA", "wsprintf", "wsprintfW", "wsprintfA", 
"sprintf", "swprintf", "_stprintf", "wvsprintf", "wvsprintfA", "wvsprintfW", "vsprintf", "_vstprintf", "vswprintf",
"wnsprintf", "wnsprintfA", "wnsprintfW", "_snwprintf", "snprintf", "sntprintf" "_vsnprintf", "vsnprintf", 
"_vsnwprintf", "_vsntprintf", "wvnsprintf", "wvnsprintfA", "wvnsprintfW", "_snwprintf", "_snprintf", "_sntprintf",
"nsprintf", "wvsprintf", "wvsprintfA", "wvsprintfW", "vsprintf", "_vstprintf", "vswprintf", "_vsnprintf", 
"_vsnwprintf", "_vsntprintf", "wvnsprintf", "wvnsprintfA", "wvnsprintfW", "strncpy", "wcsncpy", "_tcsncpy", 
"_mbsncpy", "_mbsnbcpy", "StrCpyN", "StrCpyNA", "StrCpyNW", "StrNCpy", "strcpynA", "StrNCpyA", "StrNCpyW", 
"lstrcpyn", "lstrcpynA", "lstrcpynW", "_fstrncpy","strncat", "wcsncat", "_tcsncat", "_mbsncat", "_mbsnbcat", 
"StrCatN", "StrCatNA", "StrCatNW", "StrNCat", "StrNCatA", "StrNCatW", "lstrncat", "lstrcatnA", "lstrcatnW",
"lstrcatn", "_fstrncat", "strtok", "_tcstok", "wcstok", "_mbstok", "makepath", "_tmakepath", "_makepath",
"_wmakepath,"  "_splitpath", "_tsplitpath", "_wsplitpath", "scanf", "wscanf", "_tscanf", "sscanf", "swscanf", 
"_stscanf", "snscanf", "snwscanf", "_sntscanf", "_itoa", "_itow", "_i64toa", "_i64tow", "_ui64toa", "_ui64tot", 
"_ui64tow", "ultoa", "_ultot", "_ultow", "gets", "_getts", "_gettws", "IsBadWritePtr", "IsBadHugeWritePtr", 
"IsBadReadPtr", "IsBadHugeReadPtr", "IsBadCodePtr", "IsBadStringPtr", "CharToOem", "CharToOemA", "CharToOemW",
"OemToChar", "OemToCharA", "OemToCharW", "CharToOemBuffA", "CharToOemBuffW",  "alloca",  "_alloca",  "strlen",  
"wcslen",  "_mbslen",  "_mbstrlen",  "StrLen",  "lstrlen",  "memcpy",  "RtlCopyMemory",  "CopyMemory",  "wmemcpy", 
"ChangeWindowMessageFilter"]


def get_functions():
	func_manager = currentProgram.getFunctionManager()
	all_functions = func_manager.getFunctionsNoStubs(True)

	for func in all_functions:
		vuln_check(func)
	return

def vuln_check(func):
	if func.getName() in know_vulnerable:
		callers = get_callers(func)
		if not callers:
			return
		else:
			for caller in callers:
				write_message(caller, func.getName())
	else:
		print("no vulnerable function found")
	return 

def get_callers(func):
	callers = func.getCallingFunctions(None)
	return callers 

def write_message(caller, func_name):
	print(f"[!] Vulnerable function: {func_name} is called by {caller}")
	return

get_functions()