import nmap3
import art
from sty import fg, bg, ef, rs

host = '18.185.160.73'
separator = 80*'*'
# host = 'houseoftest.rocks'

nmap = nmap3.Nmap()
results = nmap.scan_top_ports(host)

# print(separator)
art.tprint('1337tester')

print(separator)
for member in results[host]:
    hostinfo = f"Host {member['host']}, protocol {member['protocol']}, portid {member['portid']}, state {member['state']}"
    print(fg.blue + hostinfo + fg.rs)
    service = f"    Service is {member['service']}"
    # print(fg.yellow + service + fg.rs)

print(separator)
os_results = nmap.nmap_os_detection(host)
for machine in os_results:
    os_machine = f"OS is {machine['name']}, accuracy is {machine['accuracy']}"
    print(fg.green + os_machine + fg.rs)

print(separator)
bruteforce = nmap.nmap_dns_brute_script(host)
for brute in bruteforce:
    bruteforced = f"Bruteforced {brute}"
    print(fg.magenta + bruteforced + fg.rs)













# foo = fg.red + 'This is red text!' + fg.rs
# bar = bg.blue + 'This has a blue background!' + bg.rs
# baz = ef.italic + 'This is italic text' + rs.italic
# qux = fg(201) + 'This is pink text using 8bit colors' + fg.rs
# qui = fg(255, 10, 10) + 'This is red text using 24bit colors.' + fg.rs
# print(foo, bar, baz, qux, qui, sep='\n')
