# Challenge III

Build the modified gbhttp ROM by running:
```
./build-gbhttp.sh
```

Build the dumper payload by running:
```
./build-payload.sh
```
You have to extract the bytes from the dumper payload to insert into sendresp.py, I can't recall how I did this.

The solution exploit is implemented in `sendresp.py`.
This dumps memory sequentially from the GameBoy.
The dumper is actually broken, as it gets 255 bytes instead of 256 bytes.
So, first try finding a rough range for the flag and then dump the entire flag in one go.
Otherwise, you may corrupt the flag while dumping by missing a byte (happened to me once).

