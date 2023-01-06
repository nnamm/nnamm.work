---
title: About
description: 自己紹介とサイトの説明
date: 2019-03-22
lastmod: 2023-01-06
summary: 自己紹介とサイトの説明
showAuthor: false
showDate: false
showDateUpdated: false
showPagination: false
sharingLinks: false
---

### Me

![](./about-0.jpg)

花村貴史 / Takashi Hanamura です。

- ソフトウェアエンジニア
- 空気感フォトグラファー
- 横浜育ち 38 年、脱サラ → 信州移住 2 年半、2018 年春から関西在住、翌年秋から夫婦生活スタート
- 関西に来てよかったことは京都が近くなったこと
- 2010 年から親指シフト使い

プライベートでは Golang/Python/C++ 周辺を楽しみ、オシゴトでは SAP に携わっているエンジニアです。週末フォトグラファーでもあります。

被写体は植物や水といった自然が多く、人を撮らせていただくことも。とくに撮られることに慣れてない方の笑顔や、空気感をすくい撮ることを得意としています。

詳しいプロフィールは僕のもうひとつのサイト、[PROFILE | Takashi Q. Hanamura Photography](https://nnamm.com/profile) に詳しく書いています。

### Site

- nnamm.work の work は作品のこと
- 技術的なネタや日々のことを書きためる場所
- 作品を紹介する Hub となる場所

を静的サイトジェネレーターを使って運営していきます。

### Static Site Generators

SSG はこれまで [Gridsome](https://gridsome.org/)、[Pelican](https://blog.getpelican.com/) と使ってきてました。Pelican では [Tailwind CSS](https://tailwindcss.com/) を利用したテーマを自作してウキウキしていたのですが、サイトのビルドに時間がかかるのがネック。

そこで速度重視の [Hugo](https://gohugo.io/) に移行することに。テーマは [Blowfish](https://github.com/nunocoracao/blowfish) をカスタムしています。実際にビルドは速いです。

SSG は SPA や WordPress とは違い、静的ファイルが生成されるだけだから非常にシンプルですね。
