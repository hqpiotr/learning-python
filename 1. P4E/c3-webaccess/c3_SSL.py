# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

source = urllib.request.urlopen(linkorfile, context=ctx).read().decode()
