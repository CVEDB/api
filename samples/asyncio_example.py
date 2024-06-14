#!/usr/bin/env python3

import asyncio
import multiprocessing
import functools
import cvedb
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


cvedb_api = cvedb.Cvedb(api_key="YOUR_API_KEY_HERE")

loop = asyncio.get_event_loop()
# pool = ProcessPoolExecutor(max_workers=multiprocessing.cpu_count())
pool = ThreadPoolExecutor(max_workers=multiprocessing.cpu_count())


async def get_collection():
    print('Get collections')
    # using default executor
    return await loop.run_in_executor(None, cvedb_api.collections)


async def search(query, **kwargs):
    # run using own executor
    print('Run search `%s`.' % query)
    ret = await loop.run_in_executor(pool, functools.partial(cvedb_api.search, query, **kwargs))
    print('Searching `%s` done.' % query)
    return ret


async def main():
    collection_names = await get_collection()
    queries = ["type:%s" % collection for collection in collection_names[:20]]
    futures = [asyncio.ensure_future(search(query, limit=10)) for query in queries]
    results = await asyncio.wait(futures)
    print(results)


loop.run_until_complete(main())
loop.close()
