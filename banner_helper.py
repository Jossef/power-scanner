__author__ = 'Jossef'
# Info scarped from http://www.computec.ch/projekte/httprecon/?s=database&t=head_existing&f=banner


known_banner_web_servers = {
    '0w/0.8c': '0w 0.8c',
    'webstar/2.0 id/33333': '4d webstar 2.0',
    'webstar/2.1.1 id/33333': '4d webstar 2.1.1',
    'webstar/3.0.2 id/878810': '4d webstar 3.0.2',
    'webstar/4.2(ssl) id/79106': '4d webstar 4.2',
    'webstar/4.5(ssl) id/878810': '4d webstar 4.5',
    '4d_webstar_s/5.3.1 (macos x)': '4d webstar 5.3.1',
    '4d_webstar_s/5.3.3 (macos x)': '4d webstar 5.3.3',
    '4d_webstar_s/5.4.0 (macos x)': '4d webstar 5.4.0',
    'aidex/1.1 (win32)': 'aidex mini-webserver 1.1',
    'naviserver/2.0 aolserver/2.3.3': 'aolserver 2.3.3',
    'aolserver/3.3.1+ad13': 'aolserver 3.3.1',
    'aolserver 3.4.2': 'aolserver 3.4.2',
    'aolserver/3.4.2 sp/1': 'aolserver 3.4.2',
    'aolserver/3.5.10': 'aolserver 3.4.2',
    'aolserver/3.5.0': 'aolserver 3.5.0',
    'aolserver/4.0.10': 'aolserver 4.0.10',
    'aolserver/4.0.10a': 'aolserver 4.0.10a',
    'aolserver/4.0.11a': 'aolserver 4.0.11a',
    'aolserver/4.5.0': 'aolserver 4.5.0',
    'abyss/2.0.0.20-x2-win32 abysslib/2.0.0.20': 'abyss 2.0.0.20 x2',
    'abyss/2.4.0.3-x2-win32 abysslib/2.4.0.3': 'abyss 2.4.0.3 x2',
    'abyss/2.5.0.0-x1-win32 abysslib/2.5.0.0': 'abyss 2.5.0.0 x1',
    'abyss/2.5.0.0-x2-linux abysslib/2.5.0.0': 'abyss 2.5.0.0 x2',
    'abyss/2.5.0.0-x2-macos x abysslib/2.5.0.0': 'abyss 2.5.0.0 x2',
    'abyss/2.5.0.0-x2-win32 abysslib/2.5.0.0': 'abyss 2.5.0.0 x2',
    'abyss/2.6.0.0-x2-linux abysslib/2.6.0.0': 'abyss 2.6.0.0 x2',
    'allegroserve/1.2.50': 'allegroserve 1.2.50',
    'anti-web v3.0.7 (fear and loathing on the www)': 'anti-web httpd 3.0.7',
    'antiweb/4.0beta13': 'anti-web httpd 4.0beta13',
    'apache/1.2.6': 'apache 1.2.6',
    'apache/1.3.12 (unix) php/3.0.14': 'apache 1.3.12',
    'apache/1.3.17 (win32)': 'apache 1.3.17',
    'apache/1.3.26 (linux/suse) mod_ssl/2.8.10 openssl/0.9.6g php/4.2.2': 'apache 1.3.26',
    'apache/1.3.26 (unitedlinux) mod_python/2.7.8 python/2.2.1 php/4.2.2': 'apache 1.3.26',
    'apache/1.3.26 (unix)': 'apache 1.3.26',
    'apache/1.3.26 (unix) debian gnu/linux php/4.1.2': 'apache 1.3.26',
    'apache/1.3.26 (unix) debian gnu/linux mod_ssl/2.8.9 openssl/0.9.6g': 'apache 1.3.26',
    'mit web server apache/1.3.26 mark/1.5 (unix) mod_ssl/2.8.9': 'apache 1.3.26',
    'apache/1.3.27 (linux/suse) mod_ssl/2.8.12 openssl/0.9.6i php/4.3.1': 'apache 1.3.27',
    'apache/1.3.27 (turbolinux) mod_throttle/3.1.2 mod_ruby/0.9.7 ruby/1.6.4': 'apache 1.3.27',
    'apache/1.3.27 (unix) (red-hat/linux)': 'apache 1.3.27',
    'apache/1.3.27 (unix) (red-hat/linux) mod_python/2.7.8 python/1.5.2': 'apache 1.3.27',
    'apache/1.3.27 (unix) (red-hat/linux) mod_ssl/2.8.12 openssl/0.9.6b': 'apache 1.3.27',
    'apache/1.3.27 (unix) php/4.3.1': 'apache 1.3.27',
    'apache/1.3.27 (unix) mod_perl/1.27': 'apache 1.3.27',
    'apache/1.3.27 (win32)': 'apache 1.3.27',
    'apache/1.3.28 (unix) mod_perl/1.27 php/4.3.3': 'apache 1.3.28',
    'apache/1.3.29 (debian gnu/linux) mod_perl/1.29': 'apache 1.3.29',
    'apache/1.3.29 (unix)': 'apache 1.3.29',
    'apache/1.3.31 (unix)': 'apache 1.3.31',
    'anu_webapp': 'apache 1.3.33',
    'apache/1.3.33 (darwin) php/5.2.1': 'apache 1.3.33',
    'apache/1.3.33 (darwin) mod_ssl/2.8.24 openssl/0.9.7l mod_jk/1.2.25': 'apache 1.3.33',
    'apache/1.3.33 (debian gnu/linux) php/4.3.10-20 mod_perl/1.29': 'apache 1.3.33',
    'apache/1.3.33 (debian gnu/linux) php/4.3.8-9 mod_ssl/2.8.22': 'apache 1.3.33',
    'apache/1.3.33 (debian gnu/linux) mod_gzip/1.3.26.1a php/4.3.10-22': 'apache 1.3.33',
    'apache/1.3.33 (debian gnu/linux) mod_python/2.7.10 python/2.3.4': 'apache 1.3.33',
    'apache/1.3.33 (openpkg/2.4) mod_gzip/1.3.26.1a php/4.3.11 mod_watch/3.17': 'apache 1.3.33',
    'apache/1.3.33 (unix) php/4.3.10 frontpage/5.0.2.2510': 'apache 1.3.33',
    'apache/1.3.33 (unix) mod_auth_passthrough/1.8 mod_bwlimited/1.4': 'apache 1.3.33',
    'apache/1.3.33 (unix) mod_fastcgi/2.4.2 mod_gzip/1.3.26.1a mod_ssl/2.8.22': 'apache 1.3.33',
    'apache/1.3.33 (unix) mod_perl/1.29': 'apache 1.3.33',
    'apache/1.3.33 (unix) mod_ssl/2.8.22 openssl/0.9.7d php/4.3.10': 'apache 1.3.33',
    'apache/1.3.34': 'apache 1.3.34',
    'apache/1.3.34 (debian) authmysql/4.3.9-2 mod_ssl/2.8.25 openssl/0.9.8c': 'apache 1.3.34',
    'apache/1.3.34 (debian) php/4.4.4-8+etch4': 'apache 1.3.34',
    'apache/1.3.34 (debian) php/5.2.0-8+etch7 mod_ssl/2.8.25 openssl/0.9.8c': 'apache 1.3.34',
    'apache/1.3.34 (unix) (gentoo) mod_fastcgi/2.4.2': 'apache 1.3.34',
    'apache/1.3.34 (unix) (gentoo) mod_perl/1.30': 'apache 1.3.34',
    'apache/1.3.34 (unix) (gentoo) mod_ssl/2.8.25 openssl/0.9.7e': 'apache 1.3.34',
    'apache/1.3.34 (unix) php/4.4.2 mod_perl/1.29 dav/1.0.3 mod_ssl/2.8.25': 'apache 1.3.34',
    'apache/1.3.34 (unix) mod_jk/1.2.15 mod_perl/1.29 mod_gzip/1.3.26.1a': 'apache 1.3.34',
    'apache/1.3.35 (unix)': 'apache 1.3.35',
    'apache/1.3.27 (unix) (red-hat/linux) mod_perl/1.26 php/4.3.3': 'apache 1.3.37',
    'apache/1.3.37 (unix) frontpage/5.0.2.2635 mod_ssl/2.8.28 openssl/0.9.7m': 'apache 1.3.37',
    'apache/1.3.37 (unix) php/4.3.11': 'apache 1.3.37',
    'apache/1.3.37 (unix) php/4.4.7 mod_throttle/3.1.2 frontpage/5.0.2.2635': 'apache 1.3.37',
    'apache/1.3.37 (unix) php/5.1.2': 'apache 1.3.37',
    'apache/1.3.37 (unix) php/5.2.0': 'apache 1.3.37',
    'apache/1.3.37 (unix) php/5.2.1': 'apache 1.3.37',
    'apache/1.3.37 (unix) php/5.2.3 mod_auth_passthrough/1.8': 'apache 1.3.37',
    'apache/1.3.37 (unix) mod_auth_passthrough/1.8 mod_log_bytes/1.2': 'apache 1.3.37',
    'apache/1.3.37 (unix) mod_perl/1.29': 'apache 1.3.37',
    'apache/1.3.37 (unix) mod_perl/1.30 mod_ssl/2.8.28 openssl/0.9.7e-p1': 'apache 1.3.37',
    'apache/1.3.37 (unix) mod_ssl/2.8.28 openssl/0.9.7d': 'apache 1.3.37',
    'apache/1.3.37 (unix) mod_ssl/2.8.28 openssl/0.9.8d': 'apache 1.3.37',
    'apache/1.3.37 (unix) mod_throttle/3.1.2 dav/1.0.3 mod_fastcgi/2.4.2': 'apache 1.3.37',
    'apache/1.3.37 ben-ssl/1.57 (unix) mod_gzip/1.3.26.1a mod_fastcgi/2.4.2': 'apache 1.3.37',
    'apache/1.3.37.fb1': 'apache 1.3.37',
    'apache/1.3.39 (unix) dav/1.0.3 mod_auth_passthrough/1.8': 'apache 1.3.39',
    'apache/1.3.39 (unix) php/4.4.7': 'apache 1.3.39',
    'apache/1.3.39 (unix) php/5.2.3 mod_bwlimited/1.4': 'apache 1.3.39',
    'apache/1.3.39 (unix) php/5.2.5 dav/1.0.3 mod_ssl/2.8.30 openssl/0.9.7c': 'apache 1.3.39',
    'apache/1.3.39 (unix) mod_auth_passthrough/1.8 mod_log_bytes/1.2': 'apache 1.3.39',
    'apache/1.3.39 (unix) mod_fastcgi/2.4.2 mod_auth_passthrough/1.8': 'apache 1.3.39',
    'apache/1.3.39 ben-ssl/1.57 (unix) mod_perl/1.30 frontpage/5.0.2.2624': 'apache 1.3.39',
    'apache/1.3.41 (unix) php/5.2.8': 'apache 1.3.41',
    'apache/2.0.45 (unix) mod_jk2/2.0.3-dev': 'apache 2.0.45',
    'apache/2.0.45 (unix) mod_perl/1.99_09-dev perl/v5.6.1 covalent_auth/2.3': 'apache 2.0.45',
    'apache/2.0.46 (centos)': 'apache 2.0.46',
    'apache/2.0.46 (red hat)': 'apache 2.0.46',
    'apache/2.0.46 (white box)': 'apache 2.0.46',
    'apache/2.0.48 (redhat 9/server4you)': 'apache 2.0.48',
    'apache/2.0.49 (linux/suse)': 'apache 2.0.49',
    'apache/2.0.49 (unix) php/4.3.9': 'apache 2.0.49',
    'apache/2.0.50 (linux/suse)': 'apache 2.0.50',
    'apache/2.0.50 (ydl)': 'apache 2.0.50',
    'apache/2.0.51 (fedora)': 'apache 2.0.51',
    'apache/2.0.52 (centos)': 'apache 2.0.52',
    'apache/2.0.52 (fedora)': 'apache 2.0.52',
    'apache/2.0.52 (red hat)': 'apache 2.0.52',
    'apache/2.0.52 (unix)': 'apache 2.0.52',
    'apache/2.0.52 (unix) dav/2 php/4.4.1': 'apache 2.0.52',
    'apache/2.0.52 (win32)': 'apache 2.0.52',
    'apache/2.0.52 (win32) mod_ssl/2.0.52 openssl/0.9.7e mod_auth_sspi/1.0.1': 'apache 2.0.52',
    'apache/2.0.53 (linux/suse)': 'apache 2.0.53',
    'apache/2.0.54 (debian gnu/linux) dav/2 svn/1.1.4': 'apache 2.0.54',
    'apache/2.0.54 (debian gnu/linux) php/4.3.10-18': 'apache 2.0.54',
    'apache/2.0.54 (debian gnu/linux) php/4.3.10-22 mod_ssl/2.0.54': 'apache 2.0.54',
    'apache/2.0.54 (debian gnu/linux) php/5.1.2': 'apache 2.0.54',
    'apache/2.0.54 (debian gnu/linux) mod_jk/1.2.14 php/5.2.4-0.dotdeb.0 with': 'apache 2.0.54',
    'apache/2.0.54 (debian gnu/linux) mod_ssl/2.0.54 openssl/0.9.7e php/4.4.6': 'apache 2.0.54',
    'apache/2.0.54 (fedora)': 'apache 2.0.54',
    'apache/2.0.54 (linux/suse)': 'apache 2.0.54',
    'apache/2.0.54 (netware) mod_jk/1.2.14': 'apache 2.0.54',
    'apache/2.0.54 (unix) php/4.4.7 mod_ssl/2.0.54 openssl/0.9.7e': 'apache 2.0.54',
    'apache/2.0.55': 'apache 2.0.55',
    'apache/2.0.55 (freebsd) php/5.2.3 with suhosin-patch': 'apache 2.0.55',
    'apache/2.0.55 (ubuntu) dav/2 php/4.4.2-1.1 mod_ssl/2.0.55 openssl/0.9.8b': 'apache 2.0.55',
    'apache/2.0.55 (ubuntu) php/5.1.2': 'apache 2.0.55',
    'apache/2.0.55 (unix) dav/2 mod_ssl/2.0.55 openssl/0.9.8a php/4.4.4': 'apache 2.0.55',
    'apache/2.0.55 (unix) mod_ssl/2.0.55 openssl/0.9.7i mod_jk/1.2.15': 'apache 2.0.55',
    'apache/2.0.55 (unix) mod_ssl/2.0.55 openssl/0.9.8a jrun/4.0': 'apache 2.0.55',
    'apache/2.0.58 (unix)': 'apache 2.0.58',
    'apache/2.0.58 (win32) php/5.1.4': 'apache 2.0.58',
    'apache/2.0.58 (win32) php/5.1.5': 'apache 2.0.58',
    'apache/2.0.59 (freebsd) dav/2 php/5.2.1 with suhosin-patch': 'apache 2.0.59',
    'apache/2.0.59 (freebsd) mod_fastcgi/2.4.2 php/4.4.4 with suhosin-patch': 'apache 2.0.59',
    'apache/2.0.59 (netware) mod_jk/1.2.15': 'apache 2.0.59',
    'apache/2.0.59 (unix) mod_ssl/2.0.59 openssl/0.9.7e mod_jk/1.2.15': 'apache 2.0.59',
    'apache/2.0.59 (unix) mod_ssl/2.0.59 openssl/0.9.8d mod_fastcgi/2.4.2': 'apache 2.0.59',
    'apache/2.0.63 (red hat)': 'apache 2.0.63',
    'apache/2.2.0 (freebsd) mod_ssl/2.2.0 openssl/0.9.7e-p1 dav/2 php/5.1.2': 'apache 2.2.0',
    'apache/2.2.11 (freebsd)': 'apache 2.2.11',
    'apache/2.2.2 (fedora)': 'apache 2.2.2',
    'apache/2.2.3 (centos)': 'apache 2.2.3',
    'apache/2.2.3 (debian) dav/2 svn/1.4.2 mod_python/3.2.10 python/2.4.4': 'apache 2.2.3',
    'apache/2.2.3 (debian) php/4.4.4-8+etch4': 'apache 2.2.3',
    'apache/2.2.3 (debian) php/5.2.0-8+etch7': 'apache 2.2.3',
    'apache/2.2.3 (debian) php/5.2.0-8+etch7 mod_ssl/2.2.3 openssl/0.9.8c': 'apache 2.2.3',
    'apache/2.2.3 (debian) php/5.2.0-8+etch7 mod_ssl/2.2.3 openssl/0.9.8e': 'apache 2.2.3',
    'apache/2.2.3 (debian) php/5.2.0-8+etch9': 'apache 2.2.3',
    'apache/2.2.3 (debian) mod_fastcgi/2.4.2 php/5.2.0-8+etch7 mod_ssl/2.2.3': 'apache 2.2.3',
    'apache/2.2.3 (debian) mod_jk/1.2.18 php/5.2.0-8+etch5~pu1 mod_ssl/2.2.3': 'apache 2.2.3',
    'apache/2.2.3 (debian) mod_jk/1.2.18 php/5.2.0-8+etch7': 'apache 2.2.3',
    'apache/2.2.3 (debian) mod_ssl/2.2.3 openssl/0.9.8c php/5.2.4': 'apache 2.2.3',
    'apache/2.2.3 (linux/suse)': 'apache 2.2.3',
    'apache/2.2.3 (mandriva linux/prefork-1mdv2007.0)': 'apache 2.2.3',
    'apache/2.2.3 (red hat)': 'apache 2.2.3',
    'apache/2.2.3 (unix) php/5.2.1': 'apache 2.2.3',
    'apache/2.2.4 (debian) php/4.4.4-9+lenny1 mod_ssl/2.2.4 openssl/0.9.8e': 'apache 2.2.4',
    'apache/2.2.4 (fedora)': 'apache 2.2.4',
    'apache/2.2.4 (fedora) mod_ssl/2.2.4 openssl/0.9.8b dav/2': 'apache 2.2.4',
    'apache/2.2.4 (freebsd)': 'apache 2.2.4',
    'apache/2.2.4 (unix) dav/2 php/5.2.1rc3-dev mod_ruby/1.2.5': 'apache 2.2.4',
    'apache/2.2.4 (unix) mod_ssl/2.2.4 openssl/0.9.7e dav/2 svn/1.4.2': 'apache 2.2.4',
    'apache/2.2.4 (win32)': 'apache 2.2.4',
    'apache/2.2.6 (debian) dav/2 php/4.4.4-9 mod_ssl/2.2.6 openssl/0.9.8g': 'apache 2.2.6',
    'apache/2.2.6 (debian) dav/2 svn/1.4.4 mod_python/3.3.1 python/2.4.4': 'apache 2.2.6',
    'apache/2.2.6 (debian) php/5.2.4-2 with suhosin-patch mod_ssl/2.2.6': 'apache 2.2.6',
    'apache/2.2.6 (freebsd) mod_ssl/2.2.6 openssl/0.9.8e dav/2': 'apache 2.2.6',
    'apache/2.2.6 (unix) mod_ssl/2.2.6 openssl/0.9.7a dav/2 mod_mono/1.2.4': 'apache 2.2.6',
    'apache/2.2.6 (unix) mod_ssl/2.2.6 openssl/0.9.7a mod_jk/1.2.25': 'apache 2.2.6',
    'apache/2.2.6 (unix) mod_ssl/2.2.6 openssl/0.9.8b dav/2 php/5.2.5 with': 'apache 2.2.6',
    'apache': 'apache 2.2.8',
    'apache/2.2.8 (freebsd) mod_ssl/2.2.8 openssl/0.9.8g dav/2 php/5.2.5': 'apache 2.2.8',
    'apache/2.2.8 (unix) mod_ssl/2.2.8 openssl/0.9.8g': 'apache 2.2.8',
    'apache/2.2.8 (unix)': 'apache 2.2.9',
    'apache/2.3.0-dev (unix)': 'apache 2.3.0',
    'araneida/0.84': 'araneida 0.84',
    '\'s webserver': 'ashleys webserver',
    'badblue/2.4': 'badblue 2.4',
    'badblue/2.5': 'badblue 2.5',
    'badblue/2.6': 'badblue 2.6',
    'badblue/2.7': 'badblue 2.7',
    'barracudaserver.com (posix)': 'barracudadrive 3.9.1',
    'basehttp/0.3 python/2.4.4': 'basehttpserver 0.3',
    'boa/0.92o': 'boa 0.92o',
    'boa/0.93.15': 'boa 0.93.15',
    'boa/0.94.14rc21': 'boa 0.94.14rc21',
    'cl-http/70.216 (lispworks': 'cl-http 70.216',
    'caudium/1.4.9 stable': 'caudium 1.4.9',
    'cherokee': 'cherokee 0.6.0',
    'cherokee/0.99': 'cherokee 0.99',
    'virata-emweb/r6_0_1': 'cisco vpn 3000 concentrator virata emweb r6.2.0',
    'virata-emweb/r6_2_0': 'cisco vpn 3000 concentrator virata emweb r6.2.0',
    'compaqhttpserver/5.2': 'compaq http server 5.2',
    'compaqhttpserver/5.7': 'compaq http server 5.7',
    'compaqhttpserver/5.91': 'compaq http server 5.91',
    'compaqhttpserver/5.94': 'compaq http server 5.94',
    'compaqhttpserver/9.9 hp system management homepage/2.1.7.168': 'compaq http server 9.9',
    'cougar/9.5.6001.6264': 'cougar 9.5.6001.6264',
    'goahead-webs': 'flexwatch fw-3440-b',
    'gatling/0.10': 'gatling 0.10',
    'gatling/0.9': 'gatling 0.9',
    'globalscape-secure server/3.3': 'globalscape secure server 3.3',
    'gws': 'google web server 2.1',
    'mfe': 'google web server 2.1',
    'sffe': 'google web server 2.1',
    'httpi/1.5.2 (demonic/aix)': 'httpi 1.5.2',
    'httpi/1.6.1 (demonic/aix)': 'httpi 1.6.1',
    'hiawatha v6.11': 'hiawatha 6.11',
    'hiawatha/6.2 mod_gwbasic/1.7.3 openxor/0.3.1a': 'hiawatha 6.2',
    'ibm_http_server/2.0.47.1 apache/2.0.47 (unix)': 'ibm http server 2.0.47.1',
    'ibm_http_server/6.0.2.19 apache/2.0.47 (unix)': 'ibm http server 6.0.2.19',
    'ibm_http_server/6.0.2.19 apache/2.0.47 (unix) dav/2': 'ibm http server 6.0.2.19',
    'ibm_http_server': 'ibm http server 6.1.0.19',
    'ipc@chip': 'ipc@chip 1.04',
    'icewarp/8.3': 'icewarp 8.3.0',
    'indy/9.00.10': 'indy idhttpserver 9.00.10',
    'jana-server/2.4.8.51': 'jana-server 2.4.8.51',
    'jetty/5.1.10 (linux/2.6.12 i386 java/1.5.0_05': 'jetty 5.1.10',
    'jetty/5.1.1 (linux/2.6.9-5.elsmp i386 java/1.5.0_09': 'jetty 5.1.1',
    'jetty(6.1.1)': 'jetty 6.1.1',
    'jigsaw/2.2.5': 'jigsaw 2.2.5',
    'jigsaw/2.2.6': 'jigsaw 2.2.6',
    'jigsaw/2.3.0-beta1': 'jigsaw 2.3.0-beta1',
    'kget': 'kget web interface 2.1.3',
    'klone/2.1.0rc1': 'klone 2.1.0rc1',
    'allegro-software-rompager/2.00': 'konica ip-421/7020 allegro rompager 2.00',
    'boa/0.94.13': 'linksys wvc54gc boa 0.94.13',
    'listmanagerweb/8.8c (based on tcl-webserver/3.4.2)': 'listmanagerweb 8.8c',
    'litespeed': 'litespeed web server 3.3',
    'domino-go-webserver/4.6.2.5': 'lotus domino go webserver 4.6.2.5',
    'mathopd/1.5p6': 'mathopd 1.5p6',
    'microsoft-iis/5.0': 'microsoft iis 5.0',
    'microsoft-iis/5.1': 'microsoft iis 5.1',
    'microsoft-iis/6.0': 'microsoft iis 6.0',
    'microsoft-iis/6.0.0': 'microsoft iis 6.0',
    'microsoft-iis/7.0': 'microsoft iis 7.0',
    'mongrel 1.0': 'mongrel 1.0',
    'aegis_nanoweb/2.2.10-dev (linux': 'nanoweb 2.2.10',
    'rapid logic/1.1': 'net2phone rapid logic 1.1',
    'thttpd/2.25b 29dec2003': 'netbotz 500 thttpd 2.25b',
    'netware-enterprise-web-server/5.1': 'netware enterprise web server 5.1',
    'zyxel-rompager/3.02': 'netgear rp114 3.26',
    'allegro-software-rompager/2.10': 'netopia router allegro rompager 2.10',
    'netscape-enterprise/2.01': 'netscape enterprise server 2.01',
    'netscape-enterprise/3.5.1': 'netscape enterprise server 3.5.1',
    'netscape-enterprise/3.5.1g': 'netscape enterprise server 3.5.1g',
    'netscape-enterprise/4.1': 'netscape enterprise server 4.1',
    'netscape-enterprise/6.0': 'netscape enterprise server 6.0',
    'netscape-fasttrack/3.02': 'netscape fasttrack 3.02a',
    'osu/3.12alpha': 'osu 3.12alpha',
    'osu/3.9': 'osu 3.9',
    'omnihttpd/2.06': 'omnihttpd 2.06',
    'omnihttpd/2.09': 'omnihttpd 2.09',
    'omnihttpd/2.10': 'omnihttpd 2.10',
    'opensa/1.0.1 / apache/1.3.23 (win32) php/4.1.1 dav/1.0.2': 'opensa 1.0.1',
    'opensa/1.0.3 / apache/1.3.26 (win32) mod_ssl/2.8.9 openssl/0.9.6g': 'opensa 1.0.3',
    'opensa/1.0.4 / apache/1.3.27 (win32) php/4.2.2 mod_gzip/1.3.19.1a': 'opensa 1.0.4',
    'opensa/1.0.5 / apache/1.3.27 (win32) (using ihtml/2.20.500)': 'opensa 1.0.5',
    'oracle-application-server-10g oracleas-web-cache-10g/10.1.2.0.0 (n': 'oracle application server 10g 10.1.2.0.0',
    'oracle-application-server-10g/10.1.2.0.0 oracle-http-server': 'oracle application server 10g 10.1.2.0.0',
    'oracle-application-server-10g/10.1.2.0.2 oracle-http-server': 'oracle application server 10g 10.1.2.0.2',
    'oracle-application-server-10g oracleas-web-cache-10g/10.1.2.2.0 (tn': 'oracle application server 10g 10.1.2.2.0',
    'oracle-application-server-10g/10.1.2.2.0 oracle-http-server': 'oracle application server 10g 10.1.2.2.0',
    'oracle-application-server-10g/10.1.3.0.0 oracle-http-server': 'oracle application server 10g 10.1.3.0.0',
    'oracle-application-server-10g/10.1.3.1.0 oracle-http-server': 'oracle application server 10g 10.1.3.1.0',
    'oracle-application-server-10g/9.0.4.0.0 oracle-http-server': 'oracle application server 10g 9.0.4.0.0',
    'oracle-application-server-10g/9.0.4.1.0 oracle-http-server': 'oracle application server 10g 9.0.4.1.0',
    'oracle-application-server-10g/9.0.4.2.0 oracle-http-server': 'oracle application server 10g 9.0.4.2.0',
    'oracle-application-server-10g/9.0.4.3.0 oracle-http-server': 'oracle application server 10g 9.0.4.3.0',
    'oracle9ias/9.0.2.3.0 oracle http server': 'oracle application server 9i 9.0.2.3.0',
    'oracle9ias/9.0.2 oracle http server': 'oracle application server 9i 9.0.2',
    'oracle9ias/9.0.3.1 oracle http server': 'oracle application server 9i 9.0.3.1',
    'orion/2.0.7': 'orion 2.0.7',
    'oversee webserver v1.3.18': 'oversee webserver 1.3.18',
    'httpd/1.00': 'packetshaper httpd 1.00',
    'wg_httpd/1.0(based boa/0.92q)': 'philips netcam 1.4.8 wg_httpd 1.0',
    'thttpd/2.20b 10oct00': 'qnap nas-4100 2.26.0517',
    'http server 1.0': 'qnap ts-411u 1.2.0.0531',
    'resin/3.0.23': 'resin 3.0.23',
    'resin/3.0.6': 'resin 3.0.6',
    'web-server/3.0': 'ricoh aficio 6002 3.53.3 web-server 3.0',
    'roxen/2.2.213': 'roxen 2.2.213',
    'roxen/4.5.111-release2': 'roxen 4.5.111',
    'roxen/4.5.145-rc2': 'roxen 4.5.145',
    'snap appliances, inc./3.1.603': 'snap appliance 3.1.603',
    'snap appliance, inc./3.4.803': 'snap appliance 3.4.803',
    'snap appliance, inc./3.4.805': 'snap appliance 3.4.805',
    'snap appliance, inc./4.0.830': 'snap appliance 4.0.830',
    'snap appliance, inc./4.0.854': 'snap appliance 4.0.854',
    'snap appliance, inc./4.0.860': 'snap appliance 4.0.860',
    'snapstream': 'snapstream digital video recorder',
    'netevi/1.09': 'sony snc-rz30 netevi 1.09',
    'netevi/2.05': 'sony snc-rz30 netevi 2.05',
    'netevi/2.05g': 'sony snc-rz30 netevi 2.05g',
    'netevi/2.06': 'sony snc-rz30 netevi 2.06',
    'netevi/2.13': 'sony snc-rz30 netevi 2.13',
    'netevi/2.14': 'sony snc-rz30 netevi 2.14',
    'netevi/2.24': 'sony snc-rz30 netevi 2.24',
    'netevi/3.01': 'sony snc-rz30 netevi 3.01',
    'netevi/3.02': 'sony snc-rz30 netevi 3.02',
    'netevi/3.03': 'sony snc-rz30 netevi 3.03',
    'netevi/3.10': 'sony snc-rz30 netevi 3.10',
    'netevi/3.10a': 'sony snc-rz30 netevi 3.10a',
    'netevi/3.14': 'sony snc-rz30 netevi 3.14',
    'netzoom/1.00': 'sony snc-z20 netzoom 1.00',
    'squid/2.5.stable5': 'squid 2.5.stable5',
    'squid/2.5.stable6': 'squid 2.5.stable6',
    'squid/2.5.stable9': 'squid 2.5.stable9',
    'squid/2.6.stable13': 'squid 2.6.stable13',
    'squid/2.6.stable4': 'squid 2.6.stable4',
    'squid/2.6.stable7': 'squid 2.6.stable7',
    'stweb/1.3.27 (unix) authmysql/3.1 mod_jk/1.1.0 php/3.0.18 php/4.2.3 with': 'stweb 1.3.27',
    'sun-java-system-web-server/6.1': 'sun java system web server 6.1',
    'sun-java-system-web-server/7.0': 'sun java system web server 7.0',
    'sun-one-web-server/6.1': 'sun one web server 6.1',
    'smssmtphttp': 'symantec mail security for smtp',
    'tcl-webserver/3.5.1 may 27, 2004': 'tclhttpd 3.5.1',
    'theserver/2.21l': 'theserver 2.21l',
    'userland frontier/9.0.1-winnt': 'userland frontier 9.0.1',
    'userland frontier/9.5-winnt': 'userland frontier 9.5',
    'realvnc/4.0': 'vnc server enterprise edition e4.2.5',
    'vswebserver/01.00 index/01.02.01': 'vs web server 01.00.00',
    'virtuoso/05.00.3021 (linux) i686-generic-linux-glibc23-32 vdb': 'virtuoso 5.0.3',
    'wdaemon/9.6.1': 'wdaemon 9.6.1',
    'webrick/1.3.1 (ruby/1.9.0/2006-07-13)': 'webrick 1.3.1',
    'wn/2.4.7': 'wn server 2.4.7',
    'allegro-software-rompager/3.06b1': 'xerox docuprint n4025 allegro rompager 3.06b1',
    'spyglass_microserver/2.01fc1': 'xerox phaser 6200',
    'yaws/1.65 yet another web server': 'yaws 1.65',
    'yaws/1.68 yet another web server': 'yaws 1.68',
    'yaws/1.72 yet another web server': 'yaws 1.72',
    'yaws/sys_6.0.5 yet another web server': 'yaws 6.0.5',
    'zeus/4.3': 'zeus 4.3',
    'zeus/4.41': 'zeus 4.41',
    'unknown/0.0 upnp/1.0 conexant-emweb/r6_1_0': 'zoom adsl',
    'zope/(zope 2.10.4-final, python 2.4.4, linux2) zserver/1.1 plone/3.0.1': 'zope 2.10.4',
    'zope/(zope 2.5.0 (binary release, python 2.1, linux2-x86), python 2.1.2,': 'zope 2.5.0',
    'zope/(zope 2.5.1 (source release, python 2.1, linux2), python 2.1.3,': 'zope 2.5.1',
    'zope/(zope 2.6.0 (binary release, python 2.1, linux2-x86), python 2.1.3,': 'zope 2.6.0',
    'zope/(zope 2.6.1 (source release, python 2.1, linux2), python 2.2.3,': 'zope 2.6.1',
    'zope/(zope 2.6.4 (source release, python 2.1, linux2), python 2.2.3,': 'zope 2.6.4',
    'zope/(zope 2.7.4-0, python 2.3.5, linux2) zserver/1.1': 'zope 2.7.4',
    'squid/2.5.stable12': 'zope 2.7.4',
    'zope/(zope 2.7.5-final, python 2.3.4, linux2) zserver/1.1 plone/2.0.5': 'zope 2.7.5',
    'zope/(zope 2.7.5-final, python 2.3.5, linux2) zserver/1.1': 'zope 2.7.5',
    'zope/(zope 2.7.6-final, python 2.3.5, linux2) zserver/1.1 plone/2.0.5': 'zope 2.7.6',
    'zope/(zope 2.7.6-final, python 2.4.0, linux2) zserver/1.1': 'zope 2.7.6',
    'zope/(zope 2.7.7-final, python 2.3.5, linux2) zserver/1.1 plone/2.0.5': 'zope 2.7.7',
    'zope/(zope 2.7.7-final, python 2.4.4, linux2) zserver/1.1': 'zope 2.7.7',
    'zope/(zope 2.7.8-final, python 2.3.5, linux2) zserver/1.1 plone/2.0.5': 'zope 2.7.8',
    'zope/(zope 2.7.9-final, python 2.3.5, linux2) zserver/1.1 plone/2.0.4': 'zope 2.7.9',
    'zope/(zope 2.8.0-a0, python 2.3.4, linux2) zserver/1.1 plone/2.0-rc3': 'zope 2.8.0',
    'zope/(zope 2.8.2-final, python 2.3.5, linux2) zserver/1.1 plone/unknown': 'zope 2.8.2',
    'zope/(zope 2.8.4-final, python 2.3.5, linux2) zserver/1.1 plone/unknown': 'zope 2.8.4',
    'zope/(zope 2.8.6-final, python 2.3.5, linux2) zserver/1.1 plone/unknown': 'zope 2.8.6',
    'zope/(zope 2.8.6-final, python 2.4.4, linux2) zserver/1.1 plone/unknown': 'zope 2.8.6',
    'zope/(zope 2.8.7-final, python 2.4.4, linux2) zserver/1.1 plone/unknown': 'zope 2.8.7',
    'zope/(zope 2.9.2-, python 2.4.3, linux2) zserver/1.1 plone/unknown': 'zope 2.9.2',
    'zope/(zope 2.9.3-, python 2.4.0, linux2) zserver/1.1': 'zope 2.9.3',
    'zope/(zope 2.9.3-, python 2.4.2, linux2) zserver/1.1 plone/2.5': 'zope 2.9.3',
    'zope/(zope 2.9.5-final, python 2.4.3, linux2) zserver/1.1 plone/2.5.1': 'zope 2.9.5',
    'zope/(zope 2.9.6-final, python 2.4.3, linux2) zserver/1.1 plone/2.5.1': 'zope 2.9.6',
    'zope/(zope 2.9.6-final, python 2.4.3, linux2) zserver/1.1 plone/2.5.2': 'zope 2.9.6',
    'zope/(zope 2.9.7-final, python 2.4.4, linux2) zserver/1.1': 'zope 2.9.7',
    'zope/(zope 2.9.8-final, python 2.4.4, linux2) zserver/1.1': 'zope 2.9.8',
    'rompager/4.07 upnp/1.0': 'zyxel zywall 10w rompager 4.07',
    'and-httpd/0.99.11': 'and-httpd 0.99.11',
    'bozohttpd/20060517': 'bozohttpd 20060517',
    'bozohttpd/20080303': 'bozohttpd 20080303',
    'dwhttpd/4.0.2a7a (inso': 'dwhttpd 4.0.2a7a',
    'dwhttpd/4.1a6 (inso': 'dwhttpd 4.1a6',
    'dwhttpd/4.2a7 (inso': 'dwhttpd 4.2a7',
    'emule': 'emule 0.48a',
    'ns-firecat/1.0.x': 'firecat 1.0.0 beta',
    'fnord/1.8a': 'fnord 1.8a',
    'lighttpd/1.4.13': 'lighttpd 1.4.13',
    'lighttpd/1.4.16': 'lighttpd 1.4.16',
    'lighttpd/1.4.18': 'lighttpd 1.4.18',
    'lighttpd/1.4.19': 'lighttpd 1.4.19',
    'lighttpd/1.4.22': 'lighttpd 1.4.22',
    'lighttpd/1.5.0': 'lighttpd 1.5.0',
    'nginx/0.5.19': 'nginx 0.5.19',
    'nginx/0.5.30': 'nginx 0.5.30',
    'nginx/0.5.31': 'nginx 0.5.31',
    'nginx/0.5.32': 'nginx 0.5.32',
    'nginx/0.5.33': 'nginx 0.5.33',
    'nginx/0.5.35': 'nginx 0.5.35',
    'nginx/0.6.13': 'nginx 0.6.13',
    'nginx/0.6.16': 'nginx 0.6.16',
    'nginx/0.6.20': 'nginx 0.6.20',
    'nginx/0.6.31': 'nginx 0.6.26',
    'nostromo 1.9.1': 'nostromo 1.9.1',
    'publicfile': 'publicfile',
    'thttpd/2.19-mx apr 25 2002': 'thttpd 2.19-mx',
    'thttpd/2.19-mx dec 2 2002': 'thttpd 2.19-mx',
    'thttpd/2.19-mx jan 24 2006': 'thttpd 2.19-mx',
    'thttpd/2.19-mx oct 20 2003': 'thttpd 2.19-mx',
    'thttpd/2.23beta1 26may2002': 'thttpd 2.23beta1',
    'thttpd/2.24 26oct2003': 'thttpd 2.24',
    'thttpd/2.26 ??apr2004': 'thttpd 2.26',
    'vqserver/1.9.56 the world\'s most friendly web server': 'vqserver 1.9.56',
    'webcamxp': 'webcamxp pro 2007 3.96.000 beta',
}

windows_hints = ['microsoft', 'windows', 'win32']
mac_os_hints = ['macos']
linux_hints = ['suse', 'linux', 'debian', 'solaris', 'red hat', 'unix', 'ubuntu', 'centos']

hosting_hints = ['host', 'hosting']

ftp_servers = {
    'crushftp': '*',
    'glftpd': 'unix',
    'goanywhere ': 'unix',
    'proftpd': '*',
    'pro-ftpd ': '*',
    'pure-ftpd': 'unix',
    'pureftpd': 'unix',
    'slimftpd ': 'windows',
    'slim-ftpd ': 'windows',
    'vsftpd ': 'unix',
    'wu-ftpd': 'unix',
    'wuftpd ': 'unix',
    'crushftp': '*',
    'alftp': 'windows',
    'cerberus ': 'windows',
    'completeftp': 'windows',
    'filezilla': '*',
    'logicaldoc': '*',
    'iis': 'windows',
    'naslite': 'unix',
    'syncplify': 'windows',
    'sysax': 'windows',
    'war ftp': 'windows',
    'ws ftp': 'windows',
    'ncftpd': 'unix',
}

smtp_servers = {
    'gws': 'google web services',
    'ncftpd': 'unix',
    'agorum': 'unix',
    'atmail': 'unix',
    'axigen': 'unix',
    'bongo': 'unix',
    'citadel': 'unix',
    'contactoffice': 'unix',
    'communigate': 'unix',
    'courier': 'unix',
    'critical path': 'unix',
    'imail': 'unix',
    'eudora': 'unix',
    'evo': 'unix',
    'exim': 'unix',
    'firstclass': 'unix',
    'gammadyne': 'unix',
    'gordano': 'unix',
    'haraka': 'unix',
    'hmailserver': 'unix',
    'ibm lotus domino': 'unix',
    'icewarp': 'unix',
    'ipswitch': 'unix',
    'ironport': 'unix',
    'james': 'unix',
    'kerio': 'unix',
    'magicmail': 'unix',
    'mailenable': 'unix',
    'mailtraq': 'unix',
    'mdaemon': 'windows',
    'mercury': 'unix',
    'meta1': 'unix',
    'microsoft': 'windows',
    'exchange': 'windows',
    'mmdf': 'unix',
    'momentum': 'unix',
    'groupwise': 'unix',
    'netmail': 'unix',
    'opensmtpd': 'unix',
    'openwave': 'unix',
    'open-xchange': 'unix',
    'beehive': 'unix',
    'oracle': 'unix',
    'port25': 'unix',
    'postfix': 'unix',
    'postmaster': 'unix',
    'qmail': 'unix',
    'qpsmtpd': 'unix',
    'scalix': 'unix',
    'sendmail': 'unix',
    'slmail pro': 'unix',
    'smail': 'unix',
    'sparkengine': 'unix',
    'smtp proxy': 'unix',
    'strongmail': 'unix',
    'sun java system': 'unix',
    'synovel collabsuite': 'unix',
    'wingate': 'windows',
    'xmail': 'unix',
    'xms': 'unix',
    'zarafa': 'unix',
    'zimbra': 'unix',
    'zmailer': 'unix',
}


class BannerHelper(object):
    @staticmethod
    def get_ftp_banner_info(banner):

        # Lower the banner's case in order to get case insensitive match
        banner = banner.lower()
        server = None
        operating_system = None

        if any(hint for hint, os in ftp_servers.iteritems() if hint in banner):
            server, operating_system = ((hint, os) for hint, os in ftp_servers.iteritems() if hint in banner).next()

        return server, operating_system


    @staticmethod
    def get_smtp_banner_info(banner):

        # Lower the banner's case in order to get case insensitive match
        banner = banner.lower()
        server = None
        operating_system = None

        if any(hint for hint, os in smtp_servers.iteritems() if hint in banner):
            server, operating_system = ((hint, os) for hint, os in smtp_servers.iteritems() if hint in banner).next()

        return server, operating_system


    @staticmethod
    def get_http_banner_info(banner):

        # Lower the banner's case in order to get case insensitive match
        banner = banner.lower()
        server = known_banner_web_servers.get(banner, None)
        operating_system = None

        # If we successfully matched a server
        if server:

            if any(item in banner for item in windows_hints):
                operating_system = 'windows'
            elif any(item in banner for item in linux_hints):
                distribution = (item in banner for item in linux_hints).next()
                operating_system = 'linux ({0})'.format(distribution)
            elif any(item in banner for item in mac_os_hints):
                operating_system = 'mac os'

        # Otherwise, let's try to guess using hints
        else:
            if any(item in banner for item in hosting_hints):
                operating_system = 'filtered (hosting protection)'
                server = banner

        return server, operating_system


known_ports = {
    1: 'tcp port service multiplexer (tcpmux)',
    2: 'compressnet management utility',
    3: 'compressnet compression process',
    5: 'remote job entry',
    7: 'echo',
    9: 'discard',
    11: 'active users (systat service)',
    13: 'daytime(rfc 867)',
    17: 'quote of the day',
    18: 'message send',
    19: 'character generator(chargen)',
    20: 'ftp data transfer',
    21: 'ftp',
    22: 'secure shell (ssh)',
    23: 'telnet',
    24: 'priv-mail',
    25: 'simple mail transfer(smtp)',
    26: 'encrypted smtp',
    27: 'nsw user system fe',
    29: 'msg icp',
    33: 'display support',
    35: 'any private printer server',
    37: 'time',
    39: 'resource location(rlp)',
    42: 'arpa host name server',
    43: 'whois',
    47: 'ni ftp',
    49: 'tacacs login host',
    50: 'remote mail checking',
    51: 'imp logical address maintenance',
    52: 'xns (xerox network systems) time',
    53: 'domain name system (dns)',
    54: 'xns (xerox network systems) clearinghouse',
    55: 'isi graphics language (isi-gl)',
    56: 'xns (xerox network systems) authentication',
    57: 'mail transfer(rfc 780)',
    58: 'xns (xerox network systems) mail',
    64: 'ci (travelport) (formerly covia) comms integrator',
    67: 'bootstrap(bootp) server',
    68: 'bootstrap(bootp) client',
    69: 'trivial file transfer(tftp)',
    70: 'gopher',
    71: 'netrjs',
    72: 'netrjs',
    73: 'netrjs',
    74: 'netrjs',
    77: 'any private remote job entry',
    79: 'finger',
    80: 'hypertext transfer(http)',
    88: 'kerberos',
    90: 'dnsix (dod network security for information exchange)',
    101: 'nic host name',
    102: 'iso-tsap (transport service access point) class 0',
    104: 'acr/nema digital imaging and communications in medicine (dicom)',
    105: 'ccso nameserver(qi/ph)',
    107: 'remote telnet service',
    108: 'sna gateway access server',
    109: 'post officev2 (pop2)',
    110: 'post officev3 (pop3)',
    111: 'onc rpc (sun rpc)',
    113: 'authentication service (auth)',
    115: 'simple file transfer(sftp)',
    117: 'uucp path service',
    118: 'sql (structured query language) services',
    119: 'network news transfer(nntp)',
    123: 'network time(ntp)',
    126: 'formerly unisys unitary login, renamed by unisys to nxedit.',
    135: 'dce endpoint resolution',
    137: 'netbios netbios name service',
    138: 'netbios netbios datagram service',
    139: 'netbios netbios session service',
    143: 'internet message access(imap)',
    152: 'background file transfer program (bftp)',
    153: 'sgmp, simple gateway monitoring',
    156: 'sql service',
    161: 'simple network management(snmp)',
    162: 'simple network managementtrap (snmptrap)',
    170: 'print-srv, network postscript',
    175: 'vmnet (ibm z/vm, z/os & z/vse - network job entry(nje))',
    177: 'x display manager control(xdmcp)',
    179: 'bgp (border gateway )',
    194: 'internet relay chat (irc)',
    199: 'smux, snmp unix multiplexer',
    201: 'appletalk routing maintenance',
    209: 'the quick mail transfer',
    210: 'ansi z39.50',
    213: 'internetwork packet exchange (ipx)',
    218: 'message posting(mpp)',
    220: 'internet message access(imap), version 3',
    259: 'esro, efficient short remote operations',
    264: 'bgmp, border gateway multicast',
    280: 'http-mgmt',
    308: 'novastor online backup',
    311: 'mac os x server admin (officially appleshare ip web administration)',
    318: 'pkix tsp, time stamp',
    319: 'precision timeevent messages',
    320: 'precision timegeneral messages',
    350: 'matip-type a, mapping of airline traffic over internet',
    351: 'matip-type b, mapping of airline traffic over internet',
    366: 'odmr, on-demand mail relay',
    369: 'rpc2portmap',
    370: 'codaauth2',
    371: 'clearcase albd',
    383: 'hp data alarm manager',
    384: 'a remote network server system',
    387: 'aurp, appletalk update-based routing [20]',
    389: 'lightweight directory access(ldap)',
    399: 'digital equipment corporation decnet (phase v+) over tcp/ip',
    401: 'ups uninterruptible power supply',
    427: 'service location(slp)',
    443: 'hypertext transferover tls/ssl (https)',
    444: 'snpp, simple network paging(rfc 1568)',
    445: 'microsoft-ds smb file sharing',
    464: 'kerberos change/set password',
    465: 'url rendezvous directory for ssm (cisco ), smtp over ssl',
    475: 'tcpnethaspsrv (aladdin knowledge systems hasp services)',
    497: 'dantz retrospect',
    500: 'internet security association and key management(isakmp)',
    504: 'citadel',
    514: 'syslog',
    515: 'line printer daemon',
    517: 'talk',
    518: 'ntalk',
    520: 'routing information(rip)',
    521: 'routing informationnext generation (ripng)',
    524: 'netware core(ncp)',
    525: 'timed, timeserver',
    530: 'rpc',
    532: 'netnews',
    533: 'netwall, for emergency broadcasts',
    540: 'uucp (unix-to-unix copy )',
    542: 'commerce (commerce applications)',
    543: 'klogin, kerberos login',
    544: 'kshell, kerberos remote shell',
    546: 'dhcpv6 client',
    547: 'dhcpv6 server',
    548: 'apple filing(afp) over tcp',
    550: 'new-rwho, new-who',
    554: 'real time streaming(rtsp)',
    556: 'remotefs, rfs, rfs_server',
    560: 'rmonitor, remote monitor',
    561: 'monitor',
    563: 'nntpover tls/ssl (nntps)',
    587: 'e-mail message submission (smtp)',
    591: 'filemaker 6.0 (and later) web sharing (http alternate, also see port 80)',
    593: 'http rpc - remote procedure call over hypertext transfer',
    604: 'tunnel profile',
    623: 'asf remote management and control(asf-rmcp)',
    631: 'internet printing(ipp)',
    635: 'rlz dbase',
    636: 'lightweight directory accessover tls/ssl (ldaps)',
    639: 'msdp, multicast source discovery',
    641: 'supportsoft nexus remote command (control/listening)',
    646: 'ldp, label distribution , a routing',
    647: 'dhcp failover',
    648: 'rrp (registry registrar)',
    651: 'ieee-mms',
    653: 'supportsoft nexus remote command (data)',
    654: 'media management system (mms) media management(mmp)',
    657: 'ibm rmc',
    660: 'mac os x server administration',
    666: 'doom, first online first-person shooter',
    674: 'acap (application configuration access )',
    688: 'realm-rusd (applianceware server appliance management )',
    691: 'ms exchange routing',
    694: 'linux-ha high availability heartbeat',
    695: 'ieee-mms-ssl (ieee media management system over ssl)',
    698: 'olsr (optimized link state routing)',
    700: 'epp (extensible provisioning)',
    701: 'lmp (link management(internet))',
    702: 'iris',
    706: 'secure internet live conferencing (silc)',
    711: 'cisco tag distribution',
    712: 'tbrpf',
    749: 'kerberos administration',
    750: 'kerberos-iv, kerberos version iv',
    753: 'reverse routing header (rrh)',
    754: 'tell send',
    800: 'mdbe daemon',
    808: 'microsoft net.tcp port sharing service',
    847: 'dhcp failover',
    848: 'group domain of interpretation (gdoi)',
    860: 'iscsi (rfc 3720)',
    861: 'owamp control (rfc 4656)',
    862: 'twamp control (rfc 5357)',
    873: 'rsync file synchronization',
    902: 'ideafarm-door',
    989: 'ftps(data): ftp over tls/ssl',
    990: 'ftps(control): ftp over tls/ssl',
    991: 'nas (netnews administration system)',
    992: 'telnetover tls/ssl',
    993: 'internet message accessover tls/ssl (imaps)',
    994: 'internet relay chat over tls/ssl (ircs)',
    995: 'post office3 over tls/ssl (pop3s)',
}


class PortHelper(object):
    @staticmethod
    def get_port_info(port):
        return known_ports.get(port, 'unknown')






