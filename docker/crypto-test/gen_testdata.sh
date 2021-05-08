#!/bin/sh
# Generate data for crypto tests

for size in 1024 ; do
	for side in us them ; do
		d=pki/${side}-rsa${size}
		mkdir -p $d
		openssl genrsa -out $d/private.pem $size
		openssl req \
			-x509 \
			-key $d/private.pem \
			-out $d/public.pem \
			-subj "/OU=test/CN=$side" \
			-days 36525
		openssl rsa \
			-in $d/private.pem \
			-out $d/rawpublic.pem \
			-outform PEM \
			-pubout
		echo "message from $side" > $d/msg.clear
		openssl rand 16 > $d/enc.key
		openssl enc \
			-rc4 \
			-nosalt \
			-in $d/msg.clear \
			-out $d/msg.enc \
			-K $(od -tx1 -An < $d/enc.key | tr -d ' ')
		base64 -w0 < $d/msg.enc > $d/msg.enc.b64
		openssl rsautl \
			-encrypt \
			-inkey $d/rawpublic.pem \
			-pubin \
			-in $d/enc.key \
			-out $d/enc.key.rsaenc
		base64 -w0 < $d/enc.key.rsaenc > $d/enc.key.rsaenc.b64
	done
done
