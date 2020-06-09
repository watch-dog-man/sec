# Chapter 2 Notes

## Command in lec4

```sh
wget http://www.sometarget.tgt/.svn/wc.db 
#https://stable.modified-shop.org/.svn/
sqlite3 wc.db 'select local_relpath, ".svn/pristine/" || substr(checksum,7,2) || "/" || substr(checksum,7) || ".svn-base" as alpha from NODES;'
```

## URLs in lec4

* https://whois.domaintools.com/ 
* https://stable.modified-shop.org/.svn/wc.db 
* https://www.megacorpone.com/
* https://searchdns.netcraft.com/
* https://github.com/techgaun/github-dorks
* https://www.shodan.io/ 
* https://help.shodan.io/the-basics/search-query-fundamentals 
