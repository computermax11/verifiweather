#!/bin/bash
[[ ! -f verifiweather/verifiweather.py ]] && echo "run from source directory" && exit 1
BPATH=$(pwd)
[[ ! -d cgi-bin ]] && mkdir cgi-bin 
[[ ! -h cgi-bin/verifiweather.py ]] && ln -s ${BPATH}/verifiweather/verifiweather.py ${BPATH}/cgi-bin
[[ ! -f index.html ]] && echo '<meta http-equiv="refresh" content="0; url=cgi-bin/verifiweather.py">' > index.html
echo "The app is available at http://<your IP>:8000/cgi-bin/verifiweather.py"
python -m CGIHTTPServer
