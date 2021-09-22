#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import signal
import socket
import sys
import threading
import time

import requests
import whois
from bs4 import BeautifulSoup
from rich.console import Console

if sys.version_info < (3, 7):
    sys.stdout.write("Sorry, info requires Python 3.7 or higher\n")
    sys.exit(1)
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
}
console = Console()
INFO_COOL_LOOKING = '''

 ██▓ ███▄    █   █████▒▒█████    ██████ ▓█████ ▄▄▄       ██▀███   ▄████▄   ██░ ██ 
▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒▒██    ▒ ▓█   ▀▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  ▓██░ ██▒
▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒░ ▓██▄   ▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ ▒██▀▀██░
░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░  ▒   ██▒▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒░▓█ ░██ 
░██░▒██░   ▓██░░▒█░   ░ ████▓▒░▒██████▒▒░▒████▒▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░░▓█▒░██▓
░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ▒ ░░▒░▒
 ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒    ▒ ░▒░ ░
 ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  ░  ░  ░     ░    ░   ▒     ░░   ░ ░         ░  ░░ ░
 ░           ░            ░ ░        ░     ░  ░     ░  ░   ░     ░ ░       ░  ░  ░
                                                                 ░                

    '''


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u',
                        '--url',
                        type=str,
                        help='This is the url to scan')
    return parser


def get_parsed_args(parser, args):

    args_parsed = parser.parse_args(args)
    return args_parsed


def Print(text):
    console.print("[#046566][" + time.strftime("%H:%M:%S") + "][/#046566] " +
                  text,
                  style="bold blue")


def strip_url(url):
    return url[8:]


def file_write(text, file):
    with open('reports/' + file, 'a+') as f:
        f.write(text)


def echo_del(file):
    os.system("cat reports/" + file + " >> reports/report.md")
    os.system("rm -f reports/" + file)


def quit(signum, frame):
    print(' Control-C Interrupt')
    #sys.exit()


def file_title(title, file):
    with open('reports/' + file, 'a+') as f:
        f.write(title)


def subdomain_scan(url):
    file_title("# Subdomain scan\n", "subdomain.md")
    temp = url
    with open('db/subdomain.txt', 'r') as f:
        #signal.signal(signal.SIGINT, quit)
        #signal.signal(signal.SIGTERM, quit)
        for line in f:
            line = line.strip('\n')
            line = line + '.'
            url = list(url)
            url.insert(8, line)
            url = "".join(url)
            try:
                r = requests.get(url=url, headers=headers)
                if (r.status_code == 200):
                    file_write(url + '\n', "subdomain.md")
                    console.print("[#046566][" + time.strftime("%H:%M:%S") +
                                  "][/#046566]" + " [+] " + url +
                                  " Found site",
                                  style="bold green")
            except requests.exceptions.SSLError as e:
                console.print("[#046566][" + time.strftime("%H:%M:%S") +
                              "][/#046566]" + " [!] " + url + " Not Found",
                              style="bold red")
            except KeyboardInterrupt as e:
                print(" KeyBoard Interrupt!")
                break
            finally:
                url = temp
    echo_del("subdomain.md")
    Print("[*] Subdomain scan successed!")


def whois_scan(url):
    #file_title("# Whois scan\n","whois.md")
    console.print("[bold yellow]Target:[/bold yellow]" + "[bold pink] " + url +
                  "[/bold pink]")
    url = strip_url(url)
    os.system("whois "+url+" >> reports/report.md")
    #echo_del("whois.md")
    Print("[*] Whois scan successed!")


def shodan_scan(url):
    file_title("# Shodan scan\n",'shodan.md')
    url = url[8:]
    ip = socket.gethostbyname(url)
    #os.system("echo '# Shodan scan' >> reports/report.md")
    os.system("shodan host " + ip + " >> reports/shodan.md")
    echo_del('shodan.md')
    Print("[*] Shodan scan successed!")


def sensi_scan(url):
    file_title("# Sensitive scan\n",'sensi.md')
    temp = url
    with open('db/dict.txt') as f:
        for line in f:
            line = line.strip('\n')
            url = url + line
            try:
                r = requests.get(url=url, headers=headers)
                if (r.status_code == 200):
                    file_write(url + '\n', "sensi.md")
                    console.print("[#046566][" + time.strftime("%H:%M:%S") +
                                  "][/#046566]" + ' [+] ' + url + " OK",
                                  style="bold green")
                elif (r.status_code == 400):
                    console.print("[#046566][" + time.strftime("%H:%M:%S") +
                                  "][/#046566]" + ' [!] ' + url +
                                  " Bad Request",
                                  style="bold red")

                else:
                    console.print("[#046566][" + time.strftime("%H:%M:%S") +
                                  "][/#046566]" + ' [!] ' + url +
                                  " Method not allowed",
                                  style="bold red")

            except requests.exceptions.SSLError as e:
                console.print("[#046566][" + time.strftime("%H:%M:%S") +
                              "][/#046566]" + ' [!] ' + url + " Not Found",
                              style="bold red")
            except KeyboardInterrupt as e:
                print(" KeyBoard Interrupt!")
                break
            finally:
                url = temp
    echo_del('sensi.md')
    Print("[*] Sensitive scan successed!")


'''
def whatweb_scan(url):
    os.system("echo '# Whatweb scan' >> reports/report.md")
    os.system("whatweb " + url + " >> reports/report.md")
    console.print("[*] Whatweb scan successed!",style="bold blue")
'''


def nmap_scan(url):
    url = strip_url(url)
    os.system("echo '# Nmap scan\n' >> reports/nmap.md")
    os.system("nmap -v -A " + url + " >> reports/nmap.md")
    os.system("cat reports/nmap.md >> reports/report.md")
    os.system("rm -f reports/nmap.md")
    Print("[*] Nmap scan successed!")


def dns_scan(url):
    url = strip_url(url)
    os.system("echo '# Dns scan\n' >> reports/dns.md")
    os.system("dnsmap " + url + " >> reports/dns.md")
    os.system("cat reports/dns.md >> reports/report.md")
    os.system("rm -f reports/dns.md")
    Print("[*] Dns scan successed!")


def wordpress_scan(url):
    temp_url = url + "/wp-login.php"
    file_title('# Wordpress scan\n',"wordpress.md")
    try:
        r = requests.get(temp_url, headers=headers)
        if r.status_code == 200:
            os.system(
                "wpscan --disable-tls-checks --url " + url +
                " --api-token k86bPX4fxJOZGWGR9fuBqRbfbUwTJPhoBYFoNFAqNAY" +
                " >> reports/wordpress.md")
    except requests.exceptions.SSLError as e:
        console.print("[#046566][" + time.strftime("%H:%M:%S") +
                      "][/#046566] " + "[!] This website is not wordpress!",
                      style="bold red")
    echo_del('wordpress.md')
    Print("[*] Wpscan successed")


def waf_scan(url):
    file_title('# Waf scan\n',"waf.md")
    try:
        r = requests.get(url, headers)
        if r.status_code == 200:
            os.system("wafw00f " + url + " >> reports/waf.md")
    except requests.exceptions.SSLError as e:
        console.print("[#046566][" + time.strftime("%H:%M:%S") +
                      "][/#046566] " + "[!] something wrong!",
                      style="bold red")
    echo_del('waf.md')
    Print("[*] Waf scan successed!")


def main():
    os.system("rm -f reports/report.md")
    console.print(
        "[bold yellow]Infosearch Version:[/bold yellow] [bold red]1.0[/bold red]           [bold green]Author: Nadine[/bold green]"
    )
    console.print(INFO_COOL_LOOKING, style="bold red")
    console.print("[#046566][" + time.strftime("%H:%M:%S") + "][/#046566] " +
                  "The report is located reports/report.md",
                  style='#046566')
    parser = get_parser()
    arg = get_parsed_args(parser, sys.argv[1:])
    if arg.url:
        url = arg.url
        threads = [
            threading.Thread(target=whois_scan, args=(url, )),
            threading.Thread(target=subdomain_scan, args=(url, )),
            threading.Thread(target=shodan_scan, args=(url, )),
            threading.Thread(target=sensi_scan, args=(url, )),
            threading.Thread(target=sensi_scan, args=(url, )),
            threading.Thread(target=nmap_scan, args=(url, )),
            threading.Thread(target=dns_scan, args=(url, )),
            threading.Thread(target=wordpress_scan, args=(url, )),
            threading.Thread(target=waf_scan, args=(url, ))
        ]
        try:
            for t in threads:
                t.start()
        except KeyboardInterrupt as e:
            Print("Exit")
            sys.exit(0)

if __name__ == '__main__':
    main()
