import speedtest

test = speedtest.Speedtest()

# Make download test and convert to mb/s
down = test.download()
rsDown = round(down)
fDown = int(rsDown / 1e+6)

# Make upload test and convert to mb/s
upload = test.upload()
rsUp = round(upload)
fUp = int(rsUp / 1e+6)

# Show results
print(f"Your download speed is: {fDown} Mbps")
print(f"Your upload speed is: {fUp} Mbps")
