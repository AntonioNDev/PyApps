import re
import asyncio
import httpx


async def count_https_in_web():
   with open("websites.txt", "r", encoding='utf-8') as f:
      urls = [line.strip() for line in f.readlines()]

   async with httpx.AsyncClient() as client:
      tasks = (client.get(url) for url in urls)
      reqs = await asyncio.gather(*tasks)

   htmls = [req.text for req in reqs]

   count_https = 0
   count_http = 0

   for html in htmls:
      count_http += len(re.findall("http://", html))
      count_https += len(re.findall("https://", html))

   print(f'Finished parsing')
   print(f'{count_https=}')
   print(f'{count_http=}')
   print(f'{count_http/count_https}')

def main():
   asyncio.run(count_https_in_web())



if __name__ == "__main__":
   main()