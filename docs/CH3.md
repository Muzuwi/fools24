# Challenge 3

http://fools2024.online:26273/

# Sending the required stuff

echo -ne "GET /secret?p=0 HTTP/1.1\r\n\r\n" | nc fools2024.online 26273

# Payload that hits the size limit

echo -ne "GET /secret?p=0 HTTP/1.1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaaaaaaaaaaaaaaaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\r\n\r\n" | nc fools2024.online 26273

put null anywhere before the end - works

# Verification

- happens on the entire param string (after `?` character)
- param string = probably the flag

# Broken?

- ScanUntil seems broken? 400 branch is unreachable

doesn't work:
    line = b'GET /public\r?'
works:
    line = b'GET /public\0?'

- requests >0x800 bytes are immediately rejected, probably by the upper HTTP server
and it doesn't need spinning up bgb or whatever emulator then (response is immediate)

It's broken; scf never takes an effect.

Can exactly inject each component.

Minimized payload:
    time echo -ne "\r/public \r\n\r\n" | nc fools2024.online 26273
can skip method entirely
/public requires a space immediately after, /secret does not?


# LIMITS

- Total request size: 2048 bytes, w. trailing \r\n\r\n