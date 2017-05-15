#!/bin/bash
[[ ! -d cgi-bin ]] && mkdir cgi-bin && ln -s verifiweather.py cgi-bin
[[ ! -f index.html ]] && echo '<meta http-equiv="refresh" content="0; url=cgi-bin/verifiweather.py">' > index.html
echo "The app is available at http://<your IP>:8000/cgi-bin/verifiweather.py"
python -m CGIHTTPServer
