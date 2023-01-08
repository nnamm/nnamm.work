---
title: iCloud Drive はあらゆるファイルが同期されるわけではない
description: iCloud Drive を開発用ファイルの保存場所にするには注意が必要です
summary: 開発における iCloud Drive の注意点
categories: ["Apple"]
tags: ["macOS"]
date: 2021-05-30
lastmod: 2023-01-08
slug: 007-be-careful-files-sync-by-icloud
---

データ管理についての備忘録です。最終的には記事タイトルのことに行き着いた、失敗から得た学びです。

僕は開発系のファイルを含めて、ざっくりした作業ディレクトリを作っています。Coding とか Photo とか Sandbox とか。それらを定期的に外部ストレージにバックアップしたり、GitHub で管理します。

ある日、データ管理について考えることがありました。

## 我、名案、閃キ

ふと思ったのです。

開発系ファイル一式を iCloud Drive（正確には macOS の Documents ディレクトリ）に移動したら 2 重で保存されていいじゃなーい！？

嬉々としてフォルダを移動したものの、完全同期されるまで 1 日じゃ終わりませんでした。

どうやら 1 万や 10 万といった大量ファイルの同期リクエストがなされると、ファイルサイズに関わらず、とてつもなく時間がかかるようです。調べてみると、これは Dropbox でも同様でした。

> venv や node_modules といったものまであったので、そりゃもう大量のファイルがありました・・・。通常は `.gitignore` に書いて除外しますもんね

## 「.」で始まるファイルがなくなってる

さて、同期もおわり iTerm でのぞいてみると「.git」や「.gitignore」、「.eslintrc.js」などがことごとくない！！

どうも iCloud Drive の仕様で、何でもかんでも同期されるわけじゃないようですね。Stack Overflow や Apple のサイトをみるに、そのことが書かれていました。

## 情報源

### 1. [iCloud Drive FAQ - Apple Support](https://support.apple.com/en-us/HT201104)

「What types of files can I store in iCloud Drive?」の項には、こう書かれています。

> You shouldn't store app folders, libraries, or .tmp files in iCloud Drive.

> 訳）アプリフォルダー、ライブラリ、または.tmp ファイルを iCloud ドライブに保存しないでください。

### 2. [github - Can Git and iCloud Drive be effectively used together? - Stack Overflow](https://stackoverflow.com/questions/35853139/can-git-and-icloud-drive-be-effectively-used-together/51253959#51253959)

`.git` は上記のアプリフォルダーとして扱われているとのこと。

### 3. [How to exclude a sub folder from iCloud drive in macOS Sierra? - Ask Different](https://apple.stackexchange.com/questions/254313/how-to-exclude-a-sub-folder-from-icloud-drive-in-macos-sierra/295929#295929)

こちらには具体的にどんなファイルが同期されないかがリストアップされていました。以下、Stack Overflow から拝借。2021年5月現在の情報です。

> **Filename:**<br>
is .DS_Store<br>
begins with (A Document Being Saved<br>
contains .nosync (in any case)<br>
is .ubd<br>
contains .weakpkg<br>
is tmp (in any case)<br>
is .tmp (in any case)<br>
is desktop.ini (in any case)<br>
begins with ~$<br>
is Microsoft User Data (in any case)<br>
is $RECYCLE.BIN (in any case)<br>
is iPhoto Library (in any case)<br>
is Dropbox (in any case)<br>
is OneDrive (in any case)<br>
is IDrive-Sync (in any case)<br>
is .dropbox (in any case)<br>
is .dropbox.attr (in any case)<br>
is icon\r (in any case)<br>
<br>
**Extension is (in any case):**<br>
tmp<br>
photoslibrary<br>
photolibrary<br>
aplibrary<br>
migratedaplibrary<br>
migratedphotolibrary<br>
migratedaperturelibrary

## おわりに

iCloud Drive はたいていの場合は普通のストレージとして使えますが、物理ストレージと同じではないってことですね。認識を改めないと。

現在、クラウドがあたりまえになっています。使いようによっては手間のかからないバックアップ手段ともなりますが、物理ストレージではありません。

僕の用途としては写真ファイルもありますから、物理的なバックアップはまだまだ必要だと思うのでした。
