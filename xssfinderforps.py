import requests, time, sys

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print('usage: xssfinderforps.py <url>')
    else:
        url = sys.argv[1]
        fuzz = 'FUZZ'
        found = False
        with open('wordlist.txt', 'r') as wordlist:
            
            for word in wordlist:
                fuzz_test = url.replace(fuzz, word)           
                resp = requests.get(fuzz_test)
                
                
                if resp.status_code == 200:
                    print('\033[92m' + fuzz_test + "  =  " + str(resp) + '\033[0m')
                    found = True
                    break
                else:
                    print(fuzz_test + "  =  " + str(resp))
                
                time.sleep(1)
                        

            
        if found == False:
            print('No results found.')