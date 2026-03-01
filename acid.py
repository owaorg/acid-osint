import aiohttp,asyncio
from rich.console import Console
from rich.align import Align
import sys

pwaexho = Console()

#ДЕВ @pwaexho

def acid_write_banner():
    banner = rf'''[#00FA9A]    ___       ___       ___       ___   
   /\  \     /\  \     /\  \     /\  \  
  /::\  \   /::\  \   _\:\  \   /::\  \ 
 /::\:\__\ /:/\:\__\ /\/::\__\ /:/\:\__\
 \/\::/  / \:\ \/__/ \::/\/__/ \:\/:/  /
   /:/  /   \:\__\    \:\__\    \::/  / 
   \/__/     \/__/     \/__/     \/__/ 
   
   '''
    
    pwaexho.print(Align.center(banner))

def acid_helper():
    helper_acid_interface = """    [#00FA9A]Помощь     > -h / --help 
    Help       > -h / --help 

    Поиск      > python acid.py -search/-s < номер > 
    Search     > python acid.py -search/-s < number > 

    Поддержка только РУ номеров!
    Supporting only RU numbers"""

    pwaexho.print(Align.center(helper_acid_interface))

async def search_get_module(number, sem, url, session):
    async with sem:
        async with session.get(f"{url}{number}", timeout=5) as response:
            if response.status == 200:
                data = await response.json()

                if "voxlink" in url:
                    region = data.get("region", "")
                    operator = data.get("operator", "")

                    pwaexho.print("\n[#00FFFF]DEV: @pwaexho")
                    pwaexho.print("\n[#00FA9A]🧟‍♀️ ACID -> https://voxlink.org/num")
                    pwaexho.print(f"[#00FA9A]🏢 Оператор: {operator}\n📍 Регион: {region}")

                else:
                    pwaexho.print(data)

async def settigs_search(number):

    tasks = []
    sem = asyncio.Semaphore(5) #Поменяйте потоки если нужно
    sites = [
        "http://num.voxlink.ru/get/?num="
        #Добавьте свои сервисы
    ]

    async with aiohttp.ClientSession() as session:
        for url in sites:
            task = asyncio.create_task(search_get_module(number, sem, url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)

async def acid_main():
    acid_write_banner()

    if len(sys.argv) < 2:
        pwaexho.print("[#00FA9A]❌ Введите параметр для поиска!")
        pwaexho.print("[#00FA9A]Использование: python acid.py -s <номер> или -h для справки")
        return

    if sys.argv[1] in ["-h", "--help"]:
        acid_helper()
        return

    if sys.argv[1] in ["-s", "-search", "--search"]:
        if len(sys.argv) < 3:
            pwaexho.print("[#00FA9A]❌ Не указан номер телефона!")
            pwaexho.print("[#00FA9A]Использование: python acid.py -s <номер>")
            return
        
        number = sys.argv[2]
        await settigs_search(number)
        return

    pwaexho.print(f"[#00FA9A]❌ Неизвестная команда: {sys.argv[1]}")
    pwaexho.print("[#00FA9A]Используйте -h для списка команд")

if __name__ == "__main__":
    asyncio.run(acid_main())

