---
title: Python｜Pyftpsync を使ってローカルとリモートを同期する
description: 静的サイトジェネレーターで作成したサイトデータ Pyftpsync で同期する方法
summary: Pyftpsync の使用方法
categories: ["Programming"]
tags: ["macOS", "Python"]
date: 2020-04-05
lastmod: 2023-01-07
slug: 002-python-ftp-sync
---

静的サイトジェネレーターは静的ファイルを生成します。WordPress とは異なり、記事公開まで数ステップ必要です。

1. 記事を書く
2. ビルドして全サイトデータを生成（※）
3. レンタルサーバーにすべてのファイルをアップロード

だから、GitHub pages を使っている方もいらっしゃると思います。git push とともにデプロイされるのは楽ですからね。[Vercel](https://vercel.com/) を使うのもありでしょう。

でも、僕はすでに持っている独自ドメインや WordPress で使っているレンタルサーバーがあるのでこれらを流用したい。

そこで公開までさくっとやってくれるスクリプトを組みました。Pyftpsync を使い、[前回と同じく Automator を使ってアプリケーション化しています。](https://nnamm.work/blog/001-blog-writing-tool/)

![](./1.jpg)

## Pyftpsync とは

Martin Wendt さんがつくられている Python ライブラリで「**ローカルとリモートを rsync 風にやってくれるもの**」と僕は理解しています。

▶︎ [Pyftpsync](https://pyftpsync.readthedocs.io/en/latest/index.html)

ただし、既知の制限があります。最たるものは 2 つ。

1. 差分検知はファイルサイズと変更日から判断している
2. ローカルフォルダ内に個別のメタデータファイルをつくり、最後の同期時刻とサイズを保存することで差分を検出する

つまり Gridsome ではこうなります。

- static 配下の画像ファイルなど同一同名でも「差分あり」となる
- ビルドすると dist 配下のすべてのファイルが全削除＆再生成されるため、上記 2 の効果がない
- 結果、ほとんどのファイルがアップロード対象となる

当初の僕の希望である「**rsync コマンドのように差分だけがアップロードされればデプロイも短時間で済むじゃん**」は達成できません。

でもメリットもちゃんとあります。**手動でアップロードするよりだんぜん楽ということです。**

> 2023 年 1 月現在、SSG を Gridsome から Pelican に、さらに Hugo に移行しました。Gridsome の記述がありますが、Hugo で使っていません。本記事では Pyftpsync の使い方の紹介なので当日の記事のままとします。

![](./2.jpg)

## Pyftpsync の使い方

公式のとおりに作ればとてもカンタン。使いやすい設計です。以下は同期モードの例で、他にアップロードモードがあります。

```py
from ftpsync.ftp_target import FtpTarget
from ftpsync.targets import FsTarget
from ftpsync.synchronizers import BiDirSynchronizer


local = FsTarget("ローカルディレクトリパス")
remote = FtpTarget(
    "リモートディレクトリパス",
    "FTPサーバーアドレス",
    username="FTPアカウント",
    password="FTPパスワード",
    tls=True  # Trueの場合、FTPSが有効
)

# オプション設定例
opts = {
    "resolve": "local"  # コンフリクトした場合はローカルファイルを優先
}

# 同期の実行
sync = BiDirSynchronizer(local, remote, opts)
sync.run()
```

※デフォルトではコンソールにログ出力されますので何やっているかが分かります。

## おわりに

WordPress や note を使ってきて「公開までの仕組みがすべてつくられていること」ってすごいことだなと痛感しています。で、ここにきて SSG を使ったサイト運営ですよ。

**「手間かかることを楽しんでいる」感があります（笑）**

でも、その結果

- 楽するためにどうするか？
- 効率化するためできることはあるか？

という視点が磨かれてきましたし、なければつくってしまえ、という思考＆行動パターンになってきました。エンジニアに復帰した僕としては、これはとても望ましい成長と思っています。

ひとつひとつ作っていく感覚は楽しいです。

![](./3.jpg)

最近はコロナのせいで自宅に籠る時間ができました。だからこそ、思いっきり勉強したり、思いっきり怠惰をむさぼったり、これまでの生活スタイルを進化させられるんじゃないか、と僕は思います。

たとえば、当たり前と言われているものの反対をやってみて、人間としての幅を広げられたらいいんじゃないかな。

「**より良い未来のために、今できることをする**」です。

## 参考：sync_gridsome.py

```py
""" pyftpsyncライブラリを同期モードで使用し、Gridsomeでビルドしたデータ（dist/）をデプロイ先と同期する """

import configparser
import logging.handlers

from ftpsync.ftp_target import FtpTarget
from ftpsync.targets import FsTarget
from ftpsync.synchronizers import BiDirSynchronizer
from ftpsync.util import set_pyftpsync_logger


def sync_gridsome() -> None:
    """
    指定のローカルとリモートディレクトリを同期する
    """

    cfg = configparser.ConfigParser()
    cfg.read("config.ini")

    # ローカルとリモートの設定
    local = FsTarget(cfg["PATH"]["LOCAL"])
    user = cfg["FTPS"]["USER"]
    passwd = cfg["FTPS"]["PASSWORD"]
    remote = FtpTarget(
        cfg["PATH"]["REMOTE"],  # リモートディレクトリパス
        cfg["FTPS"]["SERVER"],  # FTPサーバ
        username=user,
        password=passwd,
        tls=True,  # FTPS有効
    )

    # オプション設定
    # ローカル優先／--deleteオプション有効／指定ディレクトリは同期除外
    # opts = {"resolve": "local", "delete": True, "force": True}
    opts = {"resolve": "local"}

    # 同期の実行
    sync = BiDirSynchronizer(local, remote, opts)
    sync.run()


if __name__ == "__main__":
    # ロガーの設定
    # pyftpsync.logにログを残す
    logger = logging.getLogger("sync.gridsome")
    log_path = "./pyftpsync.log"
    handler = logging.handlers.WatchedFileHandler(log_path)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    set_pyftpsync_logger(logger)

    # 同期
    sync_gridsome()
```

▶ 最新版は [GitHub](https://github.com/nnamm/gridsome_sync)
