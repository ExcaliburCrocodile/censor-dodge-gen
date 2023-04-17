import requests
import threading
import random

space = ' '

def create_proxy(subdomain):
    random_num = str(random.randint(10000, 99999))
    full_domain = subdomain + random_num + ".elude.wiki"
    headers = {
        'authority': 'www.censordodge.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.censordodge.com',
        'referer': 'https://www.censordodge.com/',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'subDomain': subdomain + random_num,
        'rootDomain': 'elude.wiki',
    }
    response = requests.post(
        'https://www.censordodge.com/wp-content/plugins/one-click-proxy-setup/setup.php',
        headers=headers,
        data=data,
    )
    if response.status_code == 200:
        print(f"Proxy created: {full_domain}")
        with open("proxy.txt", "a") as f:
            f.write(full_domain + "\n")
    else:
        print(f"Proxy created: {full_domain}")

def main():
    subdomain = input("Enter subdomain: ")
    num_threads = int(input("Enter number of proxies to create: "))
    print(space)
    
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=create_proxy, args=(subdomain,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()
