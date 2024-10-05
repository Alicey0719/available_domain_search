import itertools
import whois
import asyncio
import time

async def check_domain_availability(domain):
    try:
        w = whois.whois(domain)
        return domain if w.status is None else None
    except Exception:
        return 'error'

async def main(tld, length):
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    domains = [''.join(domain_tuple) + '.' + tld for domain_tuple in itertools.product(characters, repeat=length)]

    tasks = []
    
    for domain in domains:
        tasks.append(check_domain_availability(domain))
    
    available_domains = await asyncio.gather(*tasks)

    # delete none
    return [domain for domain in available_domains if domain]

if __name__ == '__main__':
    tld = 'cc'   # TLD
    length = 2   # 検索したいドメインの文字数
    
    start_time = time.time()
    available_domains = asyncio.run(main(tld, length))
    
    print(f'利用可能なドメイン ({tld}, {length}文字):')
    for domain in available_domains:
        print(domain)
    
    print(f'処理時間: {time.time() - start_time:.2f}秒')
