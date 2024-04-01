#!/usr/bin/env bash

rgbasm dumper.asm -o dumper.o
rgblink -o dumper.gb -n dumper.sym dumper.o 
rgbfix -v dumper.gb

