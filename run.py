#!/usr/bin/env python
# coding: utf-8

import ctypes

from datetime import datetime
from pathlib import Path

home = Path.home()

zoom_videos = home / 'Documents' / 'zoom'
dropbox_dest = home / 'Dropbox' / 'podcast'


def mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def mbox_ok_cancel(title, text):
    resp = mbox(title, text, 1)
    if resp == 1:
        return 'ok'
    return 'cancel'


def file_exists(file):
    try:
        file.stat()
        return True
    except:
        return False


def folder_size(folder):
    size = sum(f.stat().st_size for f in folder.iterdir())
    size_mb = size / (1024 * 1024)
    return size_mb


def should_be_processed(last_folder):
    if file_exists(last_folder / 'processed'):
        print(f'folder "{last_folder.name}" already processed')
        return False

    audio = last_folder / 'Audio Record'

    if not file_exists(audio):
        print(f'folder "{last_folder.name}" contains no audio')
        return False

    size_mb = folder_size(audio)
    if size_mb <= 90:
        print(f'folder "{last_folder.name}" size too small: {size_mb:.2f} mb')

    return True


def get_guest_name(audio_records):
    names = []

    for r in audio_records.iterdir():
        speaker_name = r.name[len('audio'):-len('21994097274.m4a')]
        names.append(speaker_name)

    names.remove('AlexeyGrigorev')
    guest_name = names[0]
    return guest_name


def main():
    last_folder = sorted(zoom_videos.iterdir(), key=lambda f: -f.stat().st_ctime)[0]

    if not should_be_processed(last_folder):
        return

    audio_records = last_folder / 'Audio Record'

    dt = datetime.fromtimestamp(last_folder.stat().st_ctime)
    prefix = dt.strftime('%Y-%m-%d')
    guest_name = get_guest_name(audio_records)

    target_folder_name = f'{prefix}-{guest_name}'
    target_folder = dropbox_dest / target_folder_name

    #response = mbox_ok_cancel(
    #    title='Moving zoom recording',
    #    text=f'Moving "{last_folder.name}" to "{target_folder}". Proceed?'
    #)

    #if response != "ok":
    #    return

    audio_records.rename(target_folder)
    (last_folder / 'processed').touch()


if __name__ == '__main__':
    main()
