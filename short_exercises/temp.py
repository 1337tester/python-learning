stringac = ("11",
"a = 1;",
"b = input();",
"",
"if a + b > 0 && a - b < 0:",
"    start()",
"elif a*b > 10 || a/b < 1:",
"    stop()",
"print set(list(a)) | set(list(b)) ",
"#Note do not change &&& or ||| or & or |",
"#Only change those '&&' which have space on both sides.",
"#Only change those '||' which have space on both sides.")

import re
n = int(input())

result = []
for a in range(1, n + 1):
    riadok = input()
    while ' && ' in riadok or ' || ' in riadok:
        riadok = re.sub(' \|\| ', " or ", riadok)
        riadok = re.sub(" && ", " and ", riadok)
    result.append(riadok)

for a in result:
    print(a)
