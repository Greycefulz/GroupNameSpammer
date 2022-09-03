import requests
import random
import ctypes

ctypes.windll.kernel32.SetConsoleTitleA("Spam Name Spammer | github.com/greycefulz")

token = input("Enter Your Token: ")
id = input ("Enter Your Group ID: ")

names = ["", "", ""] #put random names here

proxy = {'http': 'PROXY-HERE'} #proxy isnt needed but you should use one in case of a ratelimit

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.7",
    "authorization": f"{token}",
    "referer": "https://discord.com/login",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36",
    "x-debug-options": "bugReporterEnabled",
    "x-discord-locale": "en-US",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNC4wLjUxMTIuMTAyIFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMDQuMC41MTEyLjEwMiIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxNDUxOTMsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
}

while True:
    name = random.choice(names)
    json = {
        "name": f"{name}"
        }
    requests.patch(f"https://discord.com/api/v9/channels/{id}", headers=headers, json=json, proxies=proxy)
