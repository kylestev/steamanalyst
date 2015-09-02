# steamanalyst

This package provides a client interface for consuming data from [Steam Analyst's paid CS:GO API](http://csgo.steamanalyst.com/contact-us).

## Install

Via [PyPi](https://pypi.python.org/pypi)

``` bash
$ pip install steamanalyst
```

## Usage

### Local File Parsing

``` python
from steamanalyst import LocalAPIResultRetriever

file_name = './results.json'
results = LocalAPIResultRetriever(file_name).results()

for result in results:
    print result

```

### Remote API

Remote usage is very similar, however you will need to set an environment variable to authenticate with Steam Analyst's API. The environment variable is `STEAM_ANALYST_KEY`.

On a Unix/Linux system you can set an environment variable in a couple of ways, a simple way being: `$ export STEAM_ANALYST_KEY=yourapikeyhere`

``` python
from steamanalyst import SteamAnalystAPIResultRetriever

results = SteamAnalystAPIResultRetriever().results()

for result in results:
    print result
```

## Change log

Please see [CHANGELOG](CHANGELOG.md) for more information what has changed recently.

## Credits

- [Kyle Stevenson](https://github.com/kylestev)

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.

