# ๐ฅ ๋ฉํฐ์บ ํผ์ค ์๊ณ ๋ฆฌ์ฆ ์คํฐ๋ ๐ฅ

<img width = "70%" src="https://user-images.githubusercontent.com/97590480/156875708-2d6bee9b-ce5c-4bbc-875a-5d6d5d85e51e.gif">

## โ ์ด๋ค ์คํฐ๋์ธ๊ฐ์?

์ ํฌ๋ IT๊ธฐ์ ์์ฌ์ ํ์ํ ์ฝ๋ฉ ํ์คํธ๋ฅผ ํ์ด์ฌ ์ธ์ด๋ฅผ ์ฌ์ฉํ์ฌ ์ฐ์ํ ์ฑ์ ์ผ๋ก ํต๊ณผํ๊ธฐ ์ํด ํ์ตํ๊ณ  ์๊ฒฌ์ ๋๋๋ ์๊ณ ๋ฆฌ์ฆ ์คํฐ๋์๋๋ค.
1. ์ฝ๋ฉ ํ์คํธ์ ์์ฃผ ๋์ค๋ ๊ฐ๋์ ๋ํ ํ์ต ๋ฐ ๋ฐฑ์ค or ํ๋ก๊ทธ๋๋จธ์ค์ ๋ฌธ์ ๋ค์ ํ๋ฉด์ ์ตํ๋๋ค.
2. ์ด๋์ ๋ ์ฝ๋ฉ ํ์คํธ์ ํ์ํ ๋ด์ฉ๋ค์ ํ์ตํ๋ค๋ฉด, ๊ธฐ์ถ๋ฌธ์  ์์ฃผ๋ก ๋ฌธ์ ํ์ด๋ฅผ ์งํํฉ๋๋ค.
3. ๊ธฐ์ถ๋ ๋ค ํ์ด๋ดค๋ค๋ฉด ๋ฐฑ์ค ๊ธฐ์ค ์ค๋ฒ ~ ๊ณจ๋ ๋ฌธ์ ๋ค์ ์ ๋ณํ์ฌ ํ์ด๋ด๋๋ค.

## โ ์ด๋ค ์์ผ๋ก ์งํ๋๋์?

1. 1์ฃผ์ผ์ ํ ๋ฌธ์ ๋ฅผ ์ ์ ํ์ฌ ๋ฌธ์ ๋ฅผ ํผ ๋ค, ๊นํ์ ์ฌ๋ฆฝ๋๋ค.
2. ๋งค์ฃผ ๋ชฉ์์ผ 6์์ ๋ง๋์ ์์ ์ด ํผ ๋ฌธ์ ์ ๋ํ ์ฝ๋ฉ ๋ฆฌ๋ทฐ๋ฅผ ์งํํ๊ณ  ํผ๋๋ฐฑ์ ์งํํฉ๋๋ค.
3. ์ ๋  12์๊น์ง(์ ์ด๋ ๋น์ผ ์ ์ฌ๊น์ง) ๋ ํผ์งํ ๋ฆฌ์ ์ฝ๋๋ฅผ ์๋ก๋ํด์ฃผ์์ผ ํฉ๋๋ค.

## โ ์ด๋ค ๊ท์น์ ์ง์ผ์ผ ํ๋์?

### โ ํ์ผ ์์ฑ ๋ฐ ์๋ก๋ ๊ท์น

1. ๋งค์ฃผ ์๋ก์ด ๋๋ ํ ๋ฆฌ๋ฅผ ๋ง๋ญ๋๋ค. ex) 1์ฃผ์ฐจ, 2์ฃผ์ฐจ..
2. ๋๋ ํ ๋ฆฌ ์์ ๋ฌธ์  ๋๋ ํ ๋ฆฌ๋ฅผ ๋ง๋ญ๋๋ค. ex) ๋ฐฑ์ค 1000๋ฒ ๋ฌธ์ ๋ผ๋ฉด BOJ_1000
3. ๋ฌธ์  ๋๋ ํ ๋ฆฌ ์์ ๊ฐ์ ํผ ๋ฌธ์ ๋ฅผ `BOJ_1000_ํ๊ธธ๋`์ ํ์์ผ๋ก ์๋ก๋ํฉ๋๋ค.
4. ์ต์ข์ ์ธ ๊ฒฝ๋ก๋ `1์ฃผ์ฐจ/BOJ_1000/BOJ_1000_ํ๊ธธ๋` ์๋๋ค.

### โ ๊นํ Push/Pull ๊ท์น

1. ๋ฌด์กฐ๊ฑด __pull__ ๋จผ์  ํด์ค๋๋ค. pull์ ํด์ ํด๋น ์ฃผ์ฐจ์ ๋๋ ํ ๋ฆฌ๊ฐ ์๊ธฐ์ง ์๋๋ค๋ฉด ๋ฐ๋ก ๋ง๋ค์ด์ฃผ์ธ์

```
$ git pull <remote ์ด๋ฆ> <๋ธ๋์น์ด๋ฆ>
$ git pull AlgorithmStudy master
```

2. ํ์ผ ์๋ก๋ ๊ท์น์ ๋ง๊ฒ pushํด์ฃผ์ธ์.
```
$ git add .
$ git commit -m "BOJ_1000_ํ๊ธธ๋"
$ git push <remote ์ด๋ฆ> master
```

3. ๋ง์ผ push๋ฅผ ํ๋ค๊ฐ __์ถฉ๋__ ์ด ์ผ์ด๋ฌ์ ๊ฒฝ์ฐ ์๋์ ์ฝ๋๋ฅผ ์๋ ฅํด์ฃผ์ธ์
```
$ git log --oneline
```
์๋ ฅ ํ ๋ด๊ฐ pushํ ์ปค๋ฐ ๋ฐ๋ก ์  ์ปค๋ฐ ์ฝ๋๋ฅผ ๋ณต์ฌํด์ค๋๋ค. ๊ทธ๋ฆฌ๊ณ  ๋ค์์ ์๋ ฅํด์ฃผ์ธ์
```
$ git reset --soft [๋ณต์ฌํ ์ปค๋ฐ ์ฝ๋]
```

1. ๋ง์ผ ๋ด๊ฐ ์ฌ๋ฆฐ ์ฝ๋์ ์์ /์ถ๊ฐ ๋ฑ์ ์ถ๊ฐ ์ปค๋ฐ์ pushํ  ๊ฒฝ์ฐ์ ์ปค๋ฐ ํ์์ ๋ค์๊ณผ ๊ฐ์ด ์์ฑํด์ฃผ์ธ์. ์์ ์ 2๋ฒ์งธ ํ  ๊ฒฝ์ฐ์ `fix2`๋ฅผ ๋ถ์ฌ์ฃผ์๋ฉด ๋ฉ๋๋ค.

```
git commit -m "BOJ_1000_ํ๊ธธ๋_fix"
git commit -m "BOJ_1000_ํ๊ธธ๋_add"
```

## ๐ ์๊ณ ๋ฆฌ์ฆ ์คํฐ๋ ๊ธฐ๋ก

### ๐ฑ ๋ฐฑ์ค

|๋ ์ง|๊ฐ๋|์๊ณ ๋ฆฌ์ฆ ๋ฌธ์ |๋ฌธ์ ๋ฒํธ|
|:---:|:---:|:---:|:---:|
|3.10|์์ถ๋ ฅ|๋ณ ์ฐ๊ธฐ, ๋ฌธ์์ด ๋ฐ๋ณต, ํฌ๋ก์ํฐ์ ์ํ๋ฒณ, ํฐ๋ฆฐ๋๋กฌ, ํฌ๋ก์ค์๋ ๋ง๋ค๊ธฐ|BOJ_10995, BOJ_2675, BOJ_2941, BOJ_8892, BOJ_2804|
|3.17|list, dictionary|๋๋ ์๋ฆฌ์ฌ๋ค, ํ๊ท ์ ๋๊ฒ ์ง, ๋๋ฌด ์กฐ๊ฐ, ๋ช๋ น ํ๋กฌํํธ, ์ธ๋ก ์ฝ๊ธฐ, ์์ข์ด, ์ง์ฌ๊ฐํ ๋ค ๊ฐ์ ํฉ์งํฉ์ ๋ฉด์  ๊ตฌํ๊ธฐ, ์ค๋์ฟ  ์ฒด์ , ๋ฃ๋ณด์ก, ๋ค์ด์ผ, ๋๋์ผ ํฌ์ผ๋ชฌ ๋ง์คํฐ ์ด๋ค์, 2021 ์นด์นด์ค ์ธํด ๊ธฐ์ถ|BOJ_2804, BOJ_2953, BOJ_4344, BOJ_2947, BOJ_1032, BOJ_10798, BOJ_2563, BOJ_2669, BOJ_9291, BOJ_1764, BOJ_5622, BOJ_1620, PRO_KAKAO2021|
|3.31|์ฌ๊ท, ์ ๋ ฌ, ๋ธ๋ฃจํธํฌ์ค, ๊ตฌํ, ๊ทธ๋ฆฌ๋|๋ณ ์ฐ๊ธฐ - 10, ๋์ด์ ์ ๋ ฌ, ํด์ฌ, ๋ฐฐ์ด ๋ณต์ํ๊ธฐ, ์๋์ง ๋๋งํฌ|BOJ_2447, BOJ_10814, BOJ_14501 BOJ_16967, BOJ_20115|
|4.7|๋์  ๊ณํ๋ฒ, ์คํ, ๊ทธ๋ฆฌ๋, ์ ๋ ฌ, ๋ธ๋ฃจํธํฌ์ค|ํฌ๋์ฃผ์์, ์คํ, ๋์ 0, ์ขํ ์ ๋ ฌํ๊ธฐ, ์ฐ๊ตฌ์|BOJ_2156, BOJ_10814, BOJ_11047, BOJ_11650|
|4.14|๋ค์ด๋๋ฏน ํ๋ก๊ทธ๋๋ฐ, ํธ๋ฆฌ, ๋ฐฑํธ๋ํน, ๋ธ๋ฃจํธํฌ์ค|1๋ก ๋ง๋ค๊ธฐ, ํธ๋ฆฌ ์ํ, ์คํํธ์ ๋งํฌ, ์นด๋ ๊ตฌ๋งคํ๊ธฐ|BOJ_1463, BOJ_1991, BOJ_11052, BOJ_14889|
|4.28|๋ค์ด๋๋ฏน ํ๋ก๊ทธ๋๋ฐ, ํธ๋ฆฌ, ๋ฐฑํธ๋ํน, ๋ธ๋ฃจํธํฌ์ค|์ฌ์ด ๊ณ๋จ ์, ๊ฐ์ฅ ๊ธด ๊ฐ์ํ๋ ๋ถ๋ถ ์์ด, ํธ๋ฆฌ์ ๋ถ๋ชจ ์ฐพ๊ธฐ|BOJ_10844, BOJ_11722, BOJ_11725, BOJ_15649|
|5.5|๊ทธ๋ฆฌ๋ ์๊ณ ๋ฆฌ์ฆ, ๊ตฌํ, ๋ค์ด๋๋ฏน ํ๋ก๊ทธ๋๋ฐ, ๋ธ๋ฃจํธํฌ์ค|ATM, ํต๊ณํ, 2xn ํ์ผ๋ง, ์นด์นด์ค 2021 ์ธํด์ฝ ๊ธฐ์ถ๋ฌธ์ |BOJ_2108, BOJ_11399, BOJ_11726, ํ๋ก๊ทธ๋๋จธ์ค|
|5.12|dfs, bfs, ๋ค์ด๋๋ฏน ํ๋ก๊ทธ๋๋ฐ, ์ํ|dfs/bfs, ์ด์น์, ๊ณ๋จ ์ค๋ฅด๊ธฐ, ํ๋๋ฐ ์์ด, ์นด์นด์ค 2020 ์ธํด์ฝ ๋ฌธ์  1|BOJ_1260, BOJ_2193, BOJ_2579, BOJ_9461|
|5.19|dfs, bfs, ๊ทธ๋ฆฌ๋ ์๊ณ ๋ฆฌ์ฆ, ๋ค์ด๋๋ฏน ํ๋ก๊ทธ๋๋ฐ, ๊ตฌํ|๋ฏธ๋ก ๋ง๋ค๊ธฐ, ์์ด๋ฒ๋ฆฐ ๊ดํธ, ์ด์๊ณ์ฐ, ๋จ์ด๋ค์ง๊ธฐ|BOJ_1347, BOJ_1541, BOJ_2644, BOJ_17413|
|5.26|ํ๋ก์ด๋-์์ฌ, ๊ตฌํ, ์๋ฎฌ๋ ์ด์, ๊ทธ๋ฆฌ๋ ์๊ณ ๋ฆฌ์ฆ, ์ ๋ ฌ|์ผ๋น๋ฒ ์ด์ปจ, ํ๋ณด ์ถ์ฒํ๊ธฐ, ๊ฑฐ๋ถ์ด, Yonsei TOTO,  ๋ก๋ด์ฒญ์๊ธฐ|BOJ_1389, BOJ_1713, BOJ_8911, BOJ_12018, BOJ_14503|
|6.16|๋ค์ด๋๋ฏน ํ๋ก๊ทธ๋๋ฐ, ํ, ๊ตฌํ, ์๋ฎฌ๋ ์ด์|01ํ์ผ, ํ๋ฆฐํฐ ํ, ๋ค๊ฐํ ๊ทธ๋ฆฌ๊ธฐ, ๋ก๋ด|BOJ_1904, BOJ_1966, BOJ_2641, BOJ_13567|
|6.23|๊ทธ๋ํ ํ์, ๋๋น ์ฐ์  ํ์, ๊น์ด ์ฐ์  ํ์, ๊ตฌํ, ์คํ, ์ฌ๊ท, ํ ์๋ฎฌ๋ ์ด์|์ ๊ธฐ๋ ๋ฐฐ์ถ, ๊ดํธ์ ๊ฐ, ํธ๋ญ, ์ ๊ณผ๊ฒฐ๊ณผ๋ฐ๊ธฐ|BOJ_1012, BOJ_2504, BOJ_13335, ์นด์นด์ค 2022 BLIND RECRUIMENT|
|6.30|๊ทธ๋ํ ํ์, ๋๋น ์ฐ์  ํ์, ๊น์ด ์ฐ์  ํ์|๋ฏธ๋กํ์, ์ฌ์ ๊ฐ์, ๋ก๋ด|BOJ_2178, BOJ_4963, BOJ_7576|
|7.7|๋์  ํ๋ก๊ทธ๋๋ฐ, ๊ทธ๋ํ ํ์, ๋๋น ์ฐ์  ํ์, ๊น์ด ์ฐ์  ํ์|๋๋ฌผ์, ๋์ดํธ์ ์ด๋, N๊ณผ M (12)|BOJ_1309, BOJ_7562, BOJ_15666|
|7.14|๊ทธ๋ํ ํ์,๊น์ด ์ฐ์  ํ์, ํ๋ก์ด๋-์์ฌ|๋จ์ง๋ฒํธ๋ถ์ด๊ธฐ, ํ๋ก์ด๋, ์๊ถ๋ํ, ํฌ๋ ์ธ์ธํ๋ฝ๊ธฐ|BOJ_2667,BOJ_11404, ์นด์นด์ค 2019 ๊ฒจ์ธ ์ธํ์ญ, ์นด์นด์ค 2022 BLIND RECRUIMENT|
|7.21|๋์  ํ๋ก๊ทธ๋๋ฐ, ๊ทธ๋ํ ํ์, ๊น์ด ์ฐ์  ํ์, ๊ตฌํ|๋์  1, ์ฐ๊ตฌ์, ์นํจ๋ฐฐ๋ฌ, ํ๋ ์ฆ4๋ธ๋ก|BOJ_2293, BOJ_14502, BOJ_15686, ์นด์นด์ค 2018 BLIND RECRUIMENT|
|7.28|๋์  ํ๋ก๊ทธ๋๋ฐ, ๊ทธ๋ํ ํ์, ๊น์ด ์ฐ์  ํ์, ๊ตฌํ|๋ฆฌ๋ชจ์ปจ, LCS, ๋ฐฉ๊ธ๊ทธ๊ณก|BOJ_1107, BOJ_9251, ์นด์นด์ค 2018 BLIND RECRUIMENT|
## ๐ ์ฐธ๊ณ ์ฌํญ

### ๐ ์๊ฒฉ ์ ์ฅ์ ๋ฑ๋กํ๊ธฐ

`git remote add <์๊ฒฉ์ ์ฅ์ ์ด๋ฆ> <์ฃผ์>` ํ์์ผ๋ก ์์ฑํฉ๋๋ค.

```bash
$ git remote add algorithmStudy https://github.com/Trailblazer-Yoo/Multicamp_Algorithm_Study.git
```

### ๐ ์๊ฒฉ ์ ์ฅ์ ์กฐํ


`git remote -v`๋ก ๋ฑ๋ก์ด ์ ๋๋์ง ํ์ธํด๋ด๋๋ค.
```
$ git remote -v
algorithmStudy https://github.com/Trailblazer-Yoo/Multicamp_Algorithm_Study.git (fetch)
algorithmStudy https://github.com/Trailblazer-Yoo/Multicamp_Algorithm_Study.git (push)