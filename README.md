Python scripts
==============

> *little tasks, little python scripts.*

---

# Table of contents
1. [About] (#about)
2. [Demo] (#demo)
3. [Features] (#features)
4. [Installation] (#installation)
5. [Usage] (#usage)
6. [Development] (#development)
7. [Change log] (#change-log)
8. [License] (#license)
9. [Credits] (#credits)
10. [Authors] (#authors)

## About
-----

Some python scripts to do some tasks:

-	[acoes.py](https://github.com/ggrigon/python/blob/master/acoes.py): Command Line Tool that scrapes any brazilian stock price from [UOL website](http://cotacoes.economia.uol.com.br).
-	[cartola.py](https://github.com/ggrigon/python/blob/master/cartola.py): a bot to send Telegram messages about [Cartola-FC](http://globoesporte.globo.com/cartola-fc).

## Demo
----

See `acoes.py` in action:

<a href="./acoes.py"><img src="go.png" alt="Go" style="width: 50px; height: 50px"/></a>

See `cartola.py` in action:

<a href="./cartola.py"><img src="go.png" alt="Go" style="width: 50px; height: 50px"/></a>

## Features
--------

There are some pros in this repository:

-	Small repository;
-	Uncomplicated python code;
-	One script to one task;

Maybe we have more :)

## Installation
------------

### Requirements

The [acoes.py](https://github.com/ggrigon/python/blob/master/acoes.py) needs:

-	[python 2](https://www.python.org/downloads/);
-	[bs4](https://www.crummy.com/software/BeautifulSoup/#Download) (`pip install beautifulsoup4`);
-	[requests](http://docs.python-requests.org/en/master/user/install/) (`pip install requests`).

And [cartola.py](https://github.com/ggrigon/python/blob/master/cartola.py) needs:

-	[python 3](https://www.python.org/downloads/);
-	[python-telegram-bot](https://python-telegram-bot.org/) (`pip install python-telegram-bot`);
-	[subprocess](https://docs.python.org/3/library/subprocess.html) (It is a Python built in, it cames in Python standard library);
-	[logging](https://docs.python.org/3/library/logging.html) (It is a Python built in, it cames in Python standard library);

### Install

In four steps:

1.	Download this project ([here in a zip file](https://github.com/ggrigon/python/archive/master.zip));
2.	Unzip its folder in your local machine;
3.	Open the folder in a terminal (shell);
4.	Run any commands showed in next section.

## Usage
-----

Open the Terminal (shell) and, go to the project folder that contains the script to be executed.

### acoes.py

To run [acoes.py](https://github.com/ggrigon/python/blob/master/acoes.py):

1.	In the Terminal, type: `python acoes.py`
2.	When showing `Código da ação:` message, type the stock ticker to be searched *with quotes*, eg. `'petr3.sa'` or, `'vale5.sa'` or, `'CIEL3.SA'` or, `'EZTC3.SA'`.
3.	The script will search the stock on [UOL website](http://cotacoes.economia.uol.com.br) and return one of the two cases:
	1.	If not found the stock ticker, it returns this message: `Nenhum dado encontrato para esse código`.
	2.	Else, if found the stock ticker, the script scrapes web data and shows the stock price in the terminal like this:

```
Resultado da consulta:
---------------------
Data: 24 Oct. 2016
Horário: 18:09
---------------------
Ação: PETROBRAS ON
Code: petr3.sa
Isin: BRPETRACNOR9

Status:       alta
Último Valor: 19,38
Maior Valor:  19,72
Menor Valor:  19,07
Abertura:     19,52
Volume:       16.685.500

```

After all, the script closes itself, automatically.

### cartola.py

To run [cartola.py](https://github.com/ggrigon/python/blob/master/cartola.py):

*(blank)*

## Development
-----------

### Contribution

Its simple!

*Have you issues and questions?* Then go and write in [our Github Repository issue tracker](https://github.com/ggrigon/python/issues) and let's discuss it! :)

*And want you to develop some code?* So go and send it to [our Github Pull Request](https://github.com/ggrigon/python/pulls) to be checked and accepted!

### Tests

Nothing! We have not any test classes. :(

## Change log
----------

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).

**[0.4.0] - 2016-10-24**

*Added*

-	Included `Demo` section on `README.md` file.

*Changed*

-	Included changes in `Change log` section on `README.md` file.
-	Break big code-lines in `acoes.py` for readability.

*Fixed*

-	Deleted blank spaces in `acoes.py` file that bugging it.
-	Corrected portuguese grammar typos in `acoes.py` file.

**[0.3.0] - 2016-10-23**

*Added*

-	Included `README.md` file.

**[0.2.0] - 2016-10-19**

*Added*

-	Included `cartola.py` file.

**[0.1.0] - 2016-05-06**

*Added*

-	Included `acoes.py` file.

## License
-------

This project, named *Python*, is avaliable under the following license: [licence_name](http://www.example.org).

## Credits
-------

Acknowledgment to the following people and projects:

-	`acoes.py` based on *(blank)*.
-	`cartola.py` based on *(blank)*.
-	`README.md` file inspired by many projects in [Awesome-readme repository](https://github.com/matiassingers/awesome-readme), and in [PurpleBooth/README-Template.md](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2), and by Daniel Bader's [article](https://dbader.org/blog/write-a-great-readme-for-your-github-project).

Thanks to everyone!

## Authors
-------

This project is authored by:

-	**Name (nick)**: Guilherme (ggrigon)
	-	*Website*: [http://www.pequenasnotaveis.com.br/](http://www.pequenasnotaveis.com.br/)
	-	*Email*: [guilherme@rigon.info](mailto:guilherme@rigon.info)
	-	*Github*: [https://github.com/ggrigon](https://github.com/ggrigon)
	-	*Bitbucket*: *(blank)*
	-	*Twitter*: *(blank)*
	-	*Facebook*: *(blank)*
