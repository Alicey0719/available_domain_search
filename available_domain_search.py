import itertools
import whois
import time

def generate_domains(tld, length):
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789-._'
    domains = []

    # 指定した文字数の全ての組み合わせを生成
    for domain_tuple in itertools.product(characters, repeat=length):
        domain = ''.join(domain_tuple) + '.' + tld
        domains.append(domain)

    return domains

def check_domain_availability(domain):
    try:
        # whoisでドメインの情報を取得
        w = whois.whois(domain)
        # 取得できない場合はドメインが利用可能
        return w.status is None
    except Exception:
        # エラーが発生した場合はドメインが利用可能とみなす
        return True

def find_available_domains(tld, length):
    available_domains = []
    domains = generate_domains(tld, length)

    total_domains = len(domains)

    for index, domain in enumerate(domains):
        print(f'チェック中: {domain}')  # 現在チェックしているドメインを表示
        if check_domain_availability(domain):
            available_domains.append(domain)

        # 進捗を表示
        if (index + 1) % 10 == 0:  # 10ドメインごとに進捗を表示
            print(f'進捗: {index + 1}/{total_domains} ドメインをチェック中...')

        time.sleep(1)  # 1秒待機して、リクエストを分散させる

    return available_domains

# 使用例
if __name__ == '__main__':
    tld = 'cc'  # TLDを指定
    length = 3   # ドメイン名の文字数を指定
    available_domains = find_available_domains(tld, length)

    print(f'利用可能なドメイン ({tld}, {length}文字):')
    for domain in available_domains:
        print(domain)

