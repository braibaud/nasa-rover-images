import numpy as np
import pickle
import aiofiles
import aiohttp
import argparse as ap
import json
import os


def extract_elements_from_path(path: str) -> tuple:
    folder, file = os.path.split(
        p=os.path.abspath(
            path=path))

    file_name, file_ext = os.path.splitext(
        p=file)
    
    return folder, file_name, file_ext


async def fetch_json(session, url):
    async with session.get(url) as resp:
        assert resp.status == 200
        return await resp.json()


async def fetch_image(session, url, destination_path):
    async with session.get(url) as resp:
        assert resp.status == 200
        async with aiofiles.open(destination_path, mode='wb') as f:
            await f.write(await resp.read())


async def get_image(url, dest):
    async with aiohttp.ClientSession() as session:
        await fetch_image(session, url, dest)


def load_data(file_path):
    with open(file_path, 'rb') as fp:
        data = pickle.load(fp)
    return data


def save_data(file_path, data):
    with open(file_path, 'wb') as fp:
        pickle.dump(data, fp, protocol=pickle.HIGHEST_PROTOCOL)
    return file_path


def load_json(file_path):
    with open(file_path, 'r') as fp:
        data = json.load(fp)
    return data


def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf8') as fp:
        json.dump(
            obj=data,
            fp=fp,
            indent=4)
    return file_path
