#!/bin/bash

echo ""
echo "OS :"
uname -a
lsb_release -a
echo ""


# Check installation
echo "Node version: "
node --version
echo ""
echo "NPM version: "
npm -version
echo ""
echo "Gulp version: "
gulp --version
echo ""
echo "Go version: "
go version
