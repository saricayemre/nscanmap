#!/usr/bin/python3
# -*- coding: utf-8 -*-

import nmap
import nmap3
import colorama
from colorama import Fore, Back, Style
import time

colorama.init(autoreset=True)                                 

def banner():  
                    
    print(Fore.RED+"""


    ╱╱╱╱╭━╮╱╭╮╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮╭━╮
    ╱╱╱╱┃┃╰╮┃┃┃╭━╮┃╱╱╱╱╱╱╱╱╱┃┃╰╯┃┃
    ╱╱╱╱┃╭╮╰╯┃┃╰━━┳━━┳━━┳━╮╱┃╭╮╭╮┣━━┳━━╮
    ╭━━╮┃┃╰╮┃┃╰━━╮┃╭━┫╭╮┃╭╮╮┃┃┃┃┃┃╭╮┃╭╮┃╭━━╮
    ╰━━╯┃┃╱┃┃┃┃╰━╯┃╰━┫╭╮┃┃┃┃┃┃┃┃┃┃╭╮┃╰╯┃╰━━╯
    ╱╱╱╱╰╯╱╰━╯╰━━━┻━━┻╯╰┻╯╰╯╰╯╰╯╰┻╯╰┫╭━╯
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯ 
\n""" + Fore.BLUE + """NScanMap v1. Copyright (c) 2020 @saricayemre\n""")

#Tarama Başlıyor Animasyonu

def tarama(ekran):
    
    time.sleep(1)
    print(ekran,end="")
    time.sleep(1)
    for i in range(3):
        print(Fore.BLUE+"•",end="")
        time.sleep(1)
    print("")
    
#İşletim Sistemi Tespit Etme Metodu

def OS_Tespit():
    ekran= Fore.BLUE+"  İşletim Sistemi Tespiti Taraması Başlıyor "
    tarama(ekran)
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")  
    list= []
    nm = nmap.PortScanner()
    sonuc = nm.scan(ip, arguments='-O')
    str_tcp=str(sonuc)
    list = str_tcp.split(", ")
    print("",list[10],"\n",list[16],"\n",list[35],"\n",list[36],"\n",list[38],"\n",list[37])
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")

#FIN Taraması Metodu

def FIN_Scan():
    ekran= Fore.BLUE+"  FIN Taraması Başlıyor "
    tarama(ekran)
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")
    list= []
    nmap = nmap3.NmapScanTechniques()
    sonuc = nmap.nmap_fin_scan(ip)
    str_fin=str(sonuc)
    list = str_fin.split(", ")
    for i in list:
        print(i)
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")
    
#Ping Taraması Metodu
    
def Ping_Scan():
    ekran= Fore.BLUE+"  Ping Taraması Başlıyor "
    tarama(ekran)
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")
    list= []
    nmap = nmap3.NmapScanTechniques()
    sonuc = nmap.nmap_ping_scan(ip)
    str_tcp=str(sonuc)
    list = str_tcp.split(", ")
    for i in list:
        print(i)
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")

#Idle Taraması Metodu

def Idle_Scan():
    ekran= Fore.BLUE+"  Idle Taraması Başlıyor "
    tarama(ekran)
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")
    list= []
    nmap = nmap3.NmapScanTechniques()
    sonuc = nmap.nmap_idle_scan(ip)
    str_idle=str(sonuc)
    list = str_idle.split(", ")
    for i in list:
        print(i)
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")

#no port scan taraması

def no_port_Scan():
    ekran= Fore.BLUE+"  No_PortScan Başlıyor "
    tarama(ekran)
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")
    list= []
    nm = nmap3.NmapHostDiscovery()
    sonuc = nm.nmap_no_portscan(ip)
    str_nport=str(sonuc)
    list = str_nport.split(", ")
    for i in list:
        print(i)
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")

#Arp Keşfi Taraması

def ARP_Discovery():
    ekran= Fore.BLUE+"  ARP Keşfi Taraması Başlıyor "
    tarama(ekran)
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")
    list= []
    nm = nmap3.NmapHostDiscovery()
    sonuc = nm.nmap_arp_discovery(ip)
    str_arp=str(sonuc)
    list = str_arp.split(", ")
    for i in list:
        print(i)
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")

#IP Protokol Taraması

def IP_Protocol():
    ekran= Fore.BLUE+"  IP Protokol Taraması Başlıyor "
    tarama(ekran)
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")  
    list= []
    nm = nmap.PortScanner()
    sonuc = nm.scan(ip, arguments='-sO')
    str_ip=str(sonuc)
    list = str_ip.split(", ")
    for i in list:
        print(i)
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")

#TCP Connect taraması
def TCP_Connect():
    ekran= Fore.BLUE+"  TCP Connect Taraması Başlıyor "
    tarama(ekran)
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")   
    list= []
    nm = nmap.PortScanner()
    sonuc = nm.scan(ip, arguments='-sT')
    str_tcp=str(sonuc)
    list = str_tcp.split(", ")
    for i in list:
        print(i)
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")

#UDP Taraması
def UDP_Connect():
    ekran= Fore.BLUE+"  TCP Connect Taraması Başlıyor "
    tarama(ekran)
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")     
    list= []
    nm = nmap.PortScanner()
    sonuc = nm.scan(ip, arguments='-sT')
    str_udp=str(sonuc)
    list = str_udp.split(", ")
    for i in list:
        print(i)
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")    

#TCP & UDP Taraması çağır

def Ek_Tarama():
    print(Fore.GREEN+"TCP Connect Taraması Yapmak İstiyor musunuz?")
    print(Fore.RED+"NOT: Tarama oldukça uzun sürecektir")
    secim = input("{ e/h } > ")
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")
    if(secim == 'e'):
        TCP_Connect()
    print(Fore.GREEN+"UDP Taraması Yapmak İstiyor musunuz?")
    print(Fore.RED+"NOT: Tarama oldukça uzun sürecektir")
    secim = input("{ e/h } > ")
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")
    if(secim == 'e'):
        UDP_Connect()
    else:
        ekran= Fore.BLUE+"  Tüm Taramalar Sonuçlanmıştır. Çıkış Yapılıyor "
        tarama(ekran)
        print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")  
              
#Main

def MAIN():  
       
    print(Fore.RED+"+"+Fore.RED+"-"*50+Fore.RED+"+")
    OS_Tespit()
    FIN_Scan()
    Ping_Scan()
    no_port_Scan()
    ARP_Discovery()
    IP_Protocol()
    Ek_Tarama()

banner()
ip=input(Fore.BLUE+"IP Adresi Giriniz! > "+Fore.RED+"")
MAIN()




    

