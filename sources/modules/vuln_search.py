import re, sys, os, xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:13337')

# List of vulnerable functions
vulnerable_functions = ["alloca", "_alloca", "scanf", "wscanf", "sscanf", "swscanf", "vscanf", "vsscanf", "strlen", "wcslen", "strtok", "strtok_r", "wcstok", "strcat", "strncat", "wcscat", "wcsncat", "strcpy", "strncpy", "wcscpy", "wcsncpy", "memcpy", "wmemcpy", "stpcpy", "stpncpy", "wcpcpy", "wcpncpy", "memmove", "wmemmove", "memcmp", "wmemcmp", "mset", "wmemset", "gets", "vsprintf", "swprintf", "vswprintf", "snprintf", "vsnprintf", "realpath", "getwd", "wctomb", "wcrtomb", "wcstombs", "wcsrtombs", "wcsnrtombs", "strcpy", "strcpyA", "strcpyW", "wcscpy", "_tcscpy", "_mbscpy", "StrCpy", "StrCpyA", "StrCpyW", "lstrcpy", "lstrcpyA", "lstrcpyW", "_tccpy", "_mbccpy", "_ftcscpy", "strncpy", "wcsncpy", "_tcsncpy", "_mbsncpy", "_mbsnbcpy", "StrCpyN", "StrCpyNA", "StrCpyNW", "StrNCpy", "strcpynA", "StrNCpyA", "StrNCpyW", "lstrcpyn", "lstrcpynA", "lstrcpynW", "strcat", "strcatA", "strcatW", "wcscat", "_tcscat", "_mbscat", "StrCat", "StrCatA", "StrCatW", "lstrcat", "lstrcatA", "lstrcatW", "StrCatBuff", "StrCatBuffA", "StrCatBuffW", "StrCatChainW", "_tccat", "_mbccat", "_ftcscat", "strncat", "wcsncat", "_tcsncat", "_mbsncat", "_mbsnbcat", "StrCatN", "StrCatNA", "StrCatNW", "StrNCat", "StrNCatA", "StrNCatW", "lstrncat", "lstrcatnA", "lstrcatnW", "lstrcatn", "sprintfW", "sprintfA", "wsprintf", "wsprintfW", "wsprintfA", "sprintf", "swprintf", "_stprintf", "wvsprintf", "wvsprintfA", "wvsprintfW", "vsprintf", "_vstprintf", "vswprintf", "wnsprintf", "wnsprintfA", "wnsprintfW", "_snwprintf", "snprintf", "sntprintf", "_vsnprintf", "vsnprintf", "_vsnwprintf", "_vsntprintf", "wvnsprintf", "wvnsprintfA", "wvnsprintfW", "_snwprintf", "_snprintf", "_sntprintf", "nsprintf", "wvsprintf", "wvsprintfA", "wvsprintfW", "vsprintf", "_vstprintf", "vswprintf", "_vsnprintf", "_vsnwprintf", "_vsntprintf", "wvnsprintf", "wvnsprintfA", "wvnsprintfW", "strncpy", "wcsncpy", "_tcsncpy", "_mbsncpy", "_mbsnbcpy", "StrCpyN", "StrCpyNA", "StrCpyNW", "StrNCpy", "strcpynA", "StrNCpyA", "StrNCpyW", "lstrcpyn", "lstrcpynA", "lstrcpynW", "_fstrncpy", "strncat", "wcsncat", "_tcsncat", "_mbsncat", "_mbsnbcat", "StrCatN", "StrCatNA", "StrCatNW", "StrNCat", "StrNCatA", "StrNCatW", "lstrncat", "lstrcatnA", "lstrcatnW", "lstrcatn", "_fstrncat", "strtok", "_tcstok", "wcstok", "_mbstok", "makepath", "_tmakepath", "_makepath", "_wmakepath", "_splitpath", "_tsplitpath", "_wsplitpath", "scanf", "wscanf", "_tscanf", "sscanf", "swscanf", "_stscanf", "snscanf", "snwscanf", "_sntscanf", "_itoa", "_itow", "_i64toa", "_i64tow", "_ui64toa", "_ui64tot", "_ui64tow", "_ultoa", "_ultot", "_ultow", "gets", "_getts", "_gettws", "IsBadWritePtr", "IsBadHugeWritePtr", "IsBadReadPtr", "IsBadHugeReadPtr", "IsBadCodePtr", "IsBadStringPtr", "CharToOem", "CharToOemA", "CharToOemW", "OemToChar", "OemToCharA", "OemToCharW", "CharToOemBuffA", "CharToOemBuffW", "alloca", "_alloca", "strlen", "wcslen", "_mbslen", "_mbstrlen", "StrLen", "lstrlen", "memcpy", "RtlCopyMemory", "CopyMemory", "wmemcpy", "ChangeWindowMessageFilter"]

# Regular expression pattern to match stack buffer declarations
stack_declaration_pattern = re.compile(r"(char|unsigned char|int|unsigned int|short|unsigned short|long|unsigned long)\s+(\*\s*)?([a-zA-Z_]\w*)\s*\[(\d*)\];")

# Regular expression pattern to find heap buffer declaration
heap_declaration_pattern = re.compile(r"([a-zA-Z_]\w*)\s*=\s*.*(?:malloc|realloc|calloc|alloca)\s*\(\s*sizeof\s*\(\s*(.+?)\s*\)\s*\);")


def analyze_file(input):
    # Store data in buffer
    buffer = input
    
    # Find all vulnerable function occurrences in the buffer
    vulnerable_function_occurrences = {}
    for function_name in vulnerable_functions:
        pattern = r'\b{}\b'.format(re.escape(function_name))
        matches = re.finditer(pattern, buffer)
        line_numbers = [match.start() + buffer.count('\n', 0, match.start()) + 1 for match in matches]
        vulnerable_function_occurrences[function_name] = {"Count": len(line_numbers), "Line Numbers": line_numbers}
    
    # Find all stack buffer declarations
    stack_declarations = stack_declaration_pattern.findall(buffer)
    
    # Find all heap buffer declarations 
    heap_declarations = heap_declaration_pattern.findall(buffer)
    
    # Store the stack declarations in a dictionary
    stack_dict = {}
    for declaration in stack_declarations:
        stack_dict[declaration[2]] = {"Type": declaration[0], "Size": int(declaration[3]), "Arguments": declaration[1]}
    
    # Store the heap declarations in a dictionary
    heap_dict = {}
    for declaration in heap_declarations:
        heap_dict[declaration[0]] = {"Size": declaration[1]}
    
    return vulnerable_function_occurrences, stack_dict, heap_dict

def detect_loops(input):
    # Store data in buffer
    buffer = input

    # Regular expression patterns to match and extract exit conditions
    if_pattern = re.compile(r"\bif\s*\(((?:[^()]|\([^()]*?\))*)\)")
    while_pattern = re.compile(r"\bwhile\s*\(((?:[^()]|\([^()]*?\))*)\)")
    for_pattern = re.compile(r"\bfor\s*\([^;]*;[^;]*;\s*((?:[^()]|\([^()]*?\))*)\)")

    # Dictionary to store the loop information
    loop_dict = {}

    # Find all if statements and extract the exit condition
    if_matches = if_pattern.finditer(buffer)
    for match in if_matches:
        exit_cond = match.group(1)
        line_num = buffer.count('\n', 0, match.start()) + 1
        loop_dict[f"If statement at line {line_num}"] = {
            "Exit Condition": exit_cond
        }

    # Find all while loops and extract the exit condition
    while_matches = while_pattern.finditer(buffer)
    for match in while_matches:
        exit_cond = match.group(1)
        line_num = buffer.count('\n', 0, match.start()) + 1
        loop_dict[f"While loop at line {line_num}"] = {
            "Exit Condition": exit_cond
        }

    # Find all for loops and extract the exit condition
    for_matches = for_pattern.finditer(buffer)
    for match in for_matches:
        exit_cond = match.group(1)
        line_num = buffer.count('\n', 0, match.start()) + 1
        loop_dict[f"For loop at line {line_num}"] = {
            "Exit Condition": exit_cond
        }

    return loop_dict

def display_dicts(*dicts):
    for d in dicts:
        if d:
            for key, value in d.items():
                if isinstance(value, dict):
                    print(f"{key}:")
                    for k, v in value.items():
                        print(f"    {k}: {v}")
                else:
                    print(f"{key}: {value}")
            print("\n")

def dict_to_string(input_dict):
    result = ""
    for key, value in input_dict.items():
        result += f"{key}: {value}\n"
    return result

def vuln_hunt():

    # Store data in buffer
    source = proxy.rec_decomp()
    buffer = dict_to_string(source)

    # Analyze the file
    dicts1 = analyze_file(buffer)
    dicts2 = detect_loops(buffer)

    print("Vulnerability Scanner result:")
    display_dicts(dicts1[0], dicts1[1], dicts1[2])
    display_dicts(dicts2)
