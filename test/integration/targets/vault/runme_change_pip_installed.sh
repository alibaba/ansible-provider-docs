#!/bin/bash

# start by removing pycrypto and cryptography

pip uninstall -y cryptography
pip uninstall -y pycrypto

./runme.sh

# now just pycrypto
pip install --no-cache-dir --user pycrypto

./runme.sh


# now just cryptography

pip uninstall -y pycrypto
pip install --no-cache-dir --user cryptography

./runme.sh

# now both

pip install --no-cache-dir --user pycrypto

./runme.sh
